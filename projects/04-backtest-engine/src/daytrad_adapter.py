"""Adapter: reuse daytrad's REAL strategy functions + local CSV bar data.

CEO-approved cross-project collaboration (2026-11-21): qualabinance research
may read daytrad code/data to validate the live squad. This adapter only
READS daytrad; it never modifies daytrad files or touches live trading.

Fidelity notes:
- Signal functions are imported untouched from daytrad/backtest/strategies.py
  so we validate exactly what the live specialists run.
- CSV timestamps are kept AS-IS (file clock = Asia/Bangkok UTC+7), identical
  to the legacy sweep harness, so results are directly comparable.
- Partial last bar (seconds != 0) is dropped; duplicate timestamps removed.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import Any, Callable, Dict, List, Tuple

import pandas as pd

_HERE = Path(__file__).resolve()
DAYTRAD_ROOT = Path(os.environ.get("DAYTRAD_ROOT", _HERE.parents[4] / "daytrad"))

# asset key -> (canonical symbol, timeframe, strategy label, wrapper factory)
SQUAD_PLAN: List[Dict[str, str]] = [
    {"key": "gold", "symbol": "XAUUSD", "tf": "M5", "strategy": "F: M5 Scalper (gold)"},
    {"key": "btc", "symbol": "BTCUSD", "tf": "M5", "strategy": "F: M5 Scalper (btc)"},
    {"key": "eth", "symbol": "ETHUSD", "tf": "M5", "strategy": "F: M5 Scalper (eth)"},
    {"key": "xag", "symbol": "XAGUSD", "tf": "M15", "strategy": "C: BB Reversion"},
    {"key": "xpt", "symbol": "XPTUSD", "tf": "M15", "strategy": "E: Agentic Confluence"},
    {"key": "gbp", "symbol": "GBPUSD", "tf": "M15", "strategy": "A: EMA Pullback"},
    {"key": "eur", "symbol": "EURUSD", "tf": "M15", "strategy": "D: MTF Momentum"},
    {"key": "ukoil", "symbol": "UKOIL", "tf": "M15", "strategy": "C: BB Reversion"},
    {"key": "xng", "symbol": "XNGUSD", "tf": "M15", "strategy": "A: EMA Pullback"},
]


def ensure_daytrad_importable() -> None:
    root = str(DAYTRAD_ROOT)
    if not Path(root).is_dir():
        raise FileNotFoundError(f"daytrad repo not found at {root} (set DAYTRAD_ROOT)")
    if root not in sys.path:
        sys.path.insert(0, root)


def load_bars(symbol: str, timeframe: str) -> pd.DataFrame:
    """Load daytrad CSV cache; clean duplicates + partial last bar."""
    path = DAYTRAD_ROOT / "data" / f"{symbol.lower()}_{timeframe.lower()}.csv"
    if not path.exists():
        raise FileNotFoundError(f"no local bars: {path}")
    df = pd.read_csv(path)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.sort_values("timestamp").drop_duplicates(subset="timestamp", keep="last")
    # drop partial final bar (seconds != 0) per research/factors-data.md
    if len(df) and df["timestamp"].iloc[-1].second != 0:
        df = df.iloc[:-1]
    return df.reset_index(drop=True)


def get_asset_spec(symbol: str) -> Dict[str, Any]:
    ensure_daytrad_importable()
    from backtest.data_loader import ASSET_SPECS
    return ASSET_SPECS[symbol]


def live_strategy_fn(symbol: str, tf: str, key: str) -> Callable[[pd.DataFrame, int], Dict[str, Any]]:
    """Return the exact signal function the live specialist uses."""
    ensure_daytrad_importable()
    from backtest import strategies as S

    if tf == "M5":
        asset_type = {"gold": "gold", "btc": "btc", "eth": "eth"}[key]

        def fn(window: pd.DataFrame, idx: int) -> Dict[str, Any]:
            return S.strategy_m5_scalper(window, idx, asset_type=asset_type)
        return fn

    m15_map = {
        "xag": S.strategy_bb_reversion,
        "xpt": S.strategy_agentic_confluence,
        "gbp": S.strategy_ema_pullback,
        "eur": S.strategy_mtf_momentum,
        "ukoil": S.strategy_bb_reversion,
        "xng": S.strategy_ema_pullback,
    }
    return m15_map[key]