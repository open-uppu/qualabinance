"""
align.py — Frequency alignment across heterogeneous series.

Critical rule (see knowledge/06-variable-framework/L1-L5-series-codes.md):
  - Macro features (monthly/quarterly) must be forward-filled to daily WITHOUT
    leaking the publication date. We stamp each value with its `publication_lag`
    before filling.

Output: a single wide DataFrame indexed by daily UTC dates, with one column per
series, ready for ML feature engineering.
"""
from __future__ import annotations

from datetime import timedelta

import numpy as np
import pandas as pd
from loguru import logger

# Reasonable publication lags: how many days AFTER period-end before data is known.
PUBLICATION_LAG = {
    "annual": 120,       # ~4 months after year-end
    "quarterly": 60,     # ~2 months after quarter-end
    "monthly": 30,       # ~1 month after month-end
    "weekly": 7,         # ~1 week after week-end
    "daily": 1,          # next-day
}


def reindex_to_daily(
    df: pd.DataFrame,
    frequency: str,
    start: str = "2000-01-01",
    end: str | None = None,
) -> pd.DataFrame:
    """Reindex a sparse series onto a daily calendar.

    The key trick: shift each observation back by `publication_lag` days BEFORE
    reindexing — so when we forward-fill, we use only what was actually known.
    """
    if df.empty:
        return df

    # Apply publication lag to avoid look-ahead
    lag_days = PUBLICATION_LAG.get(frequency, 1)
    df = df.copy()
    df.index = df.index - timedelta(days=lag_days)

    if end is None:
        end = pd.Timestamp.utcnow().strftime("%Y-%m-%d")
    daily_index = pd.date_range(start=start, end=end, tz="UTC", freq="D")

    return df.reindex(daily_index).ffill()


def align_all(
    series_dict: dict[str, pd.DataFrame],
    frequencies: dict[str, str],
    start: str = "2000-01-01",
) -> pd.DataFrame:
    """Align a dict of {series_id: dataframe} into a single wide daily table.

    Parameters
    ----------
    series_dict : {series_id: df_with_value_col}
    frequencies : {series_id: source_frequency_str}
    start : earliest date to keep
    """
    aligned = {}
    for sid, df in series_dict.items():
        freq = frequencies.get(sid, "daily")
        try:
            daily = reindex_to_daily(df, freq, start=start)
            aligned[sid] = daily["value"]
            logger.debug(f"aligned {sid} ({freq} → daily): {len(daily)} rows, "
                         f"{daily['value'].notna().sum()} non-null")
        except Exception as e:  # noqa: BLE001
            logger.warning(f"failed to align {sid}: {e}")

    wide = pd.DataFrame(aligned)
    # Trim pre-start rows
    wide = wide.loc[start:]
    # Count coverage per column
    coverage = wide.notna().mean().sort_values(ascending=False)
    logger.info(f"alignment done — {len(wide)} days, "
                f"{len(wide.columns)} series, "
                f"median coverage: {coverage.median():.1%}")
    return wide
