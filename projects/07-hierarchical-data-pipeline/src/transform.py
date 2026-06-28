"""
transform.py — Apply per-series transform + stationarity handling.

Per the framework's L1-L5 series codes doc:
  - log_return   → log(P_t) - log(P_{t-1})        [prices, FX, indices]
  - yoy_pct      → (P_t / P_{t-252}) - 1          [CPI, GDP for daily data]
  - diff         → P_t - P_{t-1}                   [yields, spreads]
  - level        → pass through                     [rates, VIX, EPU]
"""
from __future__ import annotations

import numpy as np
import pandas as pd


def apply_transform(df: pd.DataFrame, method: str) -> pd.DataFrame:
    """Apply the requested transform, preserving the index and provenance."""
    if method == "level":
        return df

    value_col = "value"
    if value_col not in df.columns:
        raise ValueError(f"Expected 'value' column, got: {df.columns.tolist()}")

    series = df[value_col].astype(float)
    if method == "log_return":
        transformed = np.log(series).diff()
    elif method == "yoy_pct":
        # For daily data, ~252 trading days; for monthly data, 12.
        # Use a heuristic: if the median gap <= 2 days, use 252; else 12.
        gap_days = series.index.to_series().diff().dt.days.median()
        lag = 252 if (pd.isna(gap_days) or gap_days <= 2) else 12
        transformed = series.pct_change(periods=lag)
    elif method == "diff":
        transformed = series.diff()
    else:
        raise ValueError(f"Unknown transform: {method}")

    out = df.copy()
    out[value_col] = transformed
    out["transform"] = method
    return out.dropna(subset=[value_col])


def add_stationarity_flag(df: pd.DataFrame, value_col: str = "value") -> pd.DataFrame:
    """Run ADF test on `value_col` and add columns: adf_stat, adf_pvalue, is_stationary."""
    try:
        from statsmodels.tsa.stattools import adfuller
        cleaned = df[value_col].dropna()
        if len(cleaned) < 30:
            return df.assign(adf_pvalue=None, is_stationary=None)
        result = adfuller(cleaned, autolag="AIC")
        stat, pvalue, *_ = result
        df = df.copy()
        df["adf_stat"] = stat
        df["adf_pvalue"] = pvalue
        df["is_stationary"] = pvalue < 0.05
        return df
    except Exception as e:  # noqa: BLE001
        return df.assign(adf_error=str(e))
