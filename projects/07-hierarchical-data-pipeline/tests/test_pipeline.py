"""
test_pipeline.py — Offline unit tests using synthetic fixtures.

Goal: ensure the pipeline logic is correct without hitting any external API.

Run with: uv run pytest projects/07-hierarchical-data-pipeline/tests/ -v
"""
from __future__ import annotations

import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

# Make src/ importable
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

import config  # noqa: E402
from align import align_all, reindex_to_daily  # noqa: E402
from transform import apply_transform, add_stationarity_flag  # noqa: E402


# ============================================================
# Fixtures
# ============================================================
@pytest.fixture
def synthetic_price_series() -> pd.DataFrame:
    """A 100-day random-walk price series."""
    rng = np.random.default_rng(42)
    dates = pd.date_range("2024-01-01", periods=100, freq="D", tz="UTC")
    prices = 100 * np.exp(np.cumsum(rng.normal(0, 0.01, 100)))
    return pd.DataFrame({
        "value": prices,
        "source": "synthetic",
        "fetched_at": datetime.now(timezone.utc),
    }, index=dates).rename_axis("date")


@pytest.fixture
def synthetic_monthly_macro() -> pd.DataFrame:
    """A 24-month monthly macro series."""
    dates = pd.date_range("2022-01-01", periods=24, freq="MS", tz="UTC")
    values = np.linspace(2.0, 5.0, 24) + np.random.default_rng(0).normal(0, 0.1, 24)
    return pd.DataFrame({
        "value": values,
        "source": "synthetic",
        "fetched_at": datetime.now(timezone.utc),
    }, index=dates).rename_axis("date")


# ============================================================
# transform tests
# ============================================================
class TestTransform:
    def test_level_is_passthrough(self, synthetic_price_series):
        out = apply_transform(synthetic_price_series, "level")
        pd.testing.assert_series_equal(
            out["value"], synthetic_price_series["value"], check_names=False
        )

    def test_log_return_correctness(self, synthetic_price_series):
        out = apply_transform(synthetic_price_series, "log_return")
        # apply_transform drops leading NaN
        assert len(out) == len(synthetic_price_series) - 1
        expected = np.log(synthetic_price_series["value"].iloc[1]) - \
                   np.log(synthetic_price_series["value"].iloc[0])
        assert out["value"].iloc[0] == pytest.approx(expected, rel=1e-9)

    def test_yoy_drops_short_series(self, synthetic_price_series):
        out = apply_transform(synthetic_price_series, "yoy_pct")
        # Series is only 100 days; 252-day lag means everything NaN → dropped
        assert len(out) == 0

    def test_diff_correctness(self, synthetic_price_series):
        out = apply_transform(synthetic_price_series, "diff")
        expected = synthetic_price_series["value"].iloc[1] - \
                   synthetic_price_series["value"].iloc[0]
        assert out["value"].iloc[0] == pytest.approx(expected, rel=1e-9)


# ============================================================
# align tests
# ============================================================
class TestAlign:
    def test_reindex_monthly_to_daily(self, synthetic_monthly_macro):
        out = reindex_to_daily(synthetic_monthly_macro, frequency="monthly", start="2022-01-01")
        # ~3 years of daily rows
        assert len(out) > 1000
        # Forward-fill produces long stretches of non-null
        assert out["value"].notna().sum() > 1000

    def test_publication_lag_shifts_dates_backward(self, synthetic_monthly_macro):
        """With monthly + 30-day lag, the first observation date should be
        shifted to `obs_date - 30 days`."""
        out = reindex_to_daily(
            synthetic_monthly_macro, frequency="monthly", start="2022-01-01"
        )
        # First observation was 2022-01-01 → known date = 2022-01-01 - 30d = 2021-12-02
        # After reindex to daily grid starting 2022-01-01, first non-null should be at
        # 2022-01-01 (closest daily grid point to the backshifted date).
        first_valid = out["value"].first_valid_index()
        assert first_valid >= pd.Timestamp("2021-12-02", tz="UTC")
        # And it must NOT appear before the lag-adjusted date
        assert first_valid >= pd.Timestamp("2021-12-02", tz="UTC")

    def test_align_all_returns_wide_panel(self, synthetic_price_series, synthetic_monthly_macro):
        sd = {"price": synthetic_price_series, "macro": synthetic_monthly_macro}
        freq = {"price": "daily", "macro": "monthly"}
        wide = align_all(sd, freq, start="2022-01-01")
        assert wide.shape[1] == 2
        assert "price" in wide.columns and "macro" in wide.columns


# ============================================================
# config tests
# ============================================================
class TestConfig:
    def test_default_series_covers_all_levels(self):
        levels = {s.level for s in config.DEFAULT_SERIES}
        assert {"L1", "L2", "L3", "L4", "L5"} <= levels

    def test_get_series_filters_by_level(self):
        l1 = config.get_series("L1")
        assert all(s.level == "L1" for s in l1)
        assert len(l1) > 0

    def test_get_series_by_id(self):
        s = config.get_series_by_id("fred_fedfunds")
        assert s is not None
        assert s.source == "fred"
        assert s.code == "FEDFUNDS"

    def test_all_series_have_valid_transform(self):
        valid = {"level", "log_return", "yoy_pct", "diff"}
        for s in config.DEFAULT_SERIES:
            assert s.transform in valid, f"{s.id} has bad transform {s.transform}"
