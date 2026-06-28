"""
config.py — Central config for hierarchical data pipeline.

All series are defined here so:
  - Changing a ticker doesn't require code edits in multiple places
  - New series can be added by editing a YAML, not a Python file
  - Tests can mock the config to use offline fixtures

Design rules:
  - All API keys come from .env, NEVER hardcoded
  - Series have explicit frequency + level + source
  - Resample rules are explicit per series

Built: 2026-06-28 · Qualabinance v0.1.0
"""
from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Literal

from dotenv import load_dotenv
from loguru import logger
from pydantic import BaseModel, Field, field_validator

load_dotenv()  # pulls .env at repo root


# ============================================================
# Storage paths
# ============================================================
REPO_ROOT = Path(__file__).resolve().parents[3]
DATA_DIR = Path(os.getenv("QUALABINANCE_DATA_DIR", REPO_ROOT / "data"))
PARQUET_DIR = DATA_DIR / "parquet"
DUCKDB_PATH = DATA_DIR / "qualabinance.duckdb"

PARQUET_DIR.mkdir(parents=True, exist_ok=True)
DATA_DIR.mkdir(parents=True, exist_ok=True)


# ============================================================
# API keys (loaded from .env, NEVER logged)
# ============================================================
@dataclass(frozen=True)
class APIKeys:
    fred: str | None = os.getenv("FRED_API_KEY")
    coingecko_pro: str | None = os.getenv("COINGECKO_PRO_KEY")
    binance: str | None = os.getenv("BINANCE_API_KEY")
    binance_secret: str | None = os.getenv("BINANCE_API_SECRET")
    bot_thailand: str | None = os.getenv("BOT_API_KEY")
    quandl: str | None = os.getenv("QUANDL_KEY")

    def safe_repr(self) -> str:
        """Used in logs — masks all keys."""
        keys = {k: "***" if v else None for k, v in self.__dict__.items()}
        return f"APIKeys({keys})"


KEYS = APIKeys()
if not KEYS.fred:
    logger.warning(
        "FRED_API_KEY not set — L1/L3 US series will fail. "
        "Get free key at https://fred.stlouisfed.org/docs/api/api_key.html"
    )


# ============================================================
# Series specification
# ============================================================
Frequency = Literal["daily", "weekly", "monthly", "quarterly", "annual"]
Level = Literal["L1", "L2", "L3", "L4", "L5"]
AssetClass = Literal[
    "equity", "etf", "bond", "fx", "commodity", "crypto", "macro", "alt"
]


class Series(BaseModel):
    """One time-series to ingest."""

    id: str = Field(..., description="Unique slug e.g. 'fred_fedfunds'")
    level: Level
    asset_class: AssetClass
    source: str = Field(..., description="Provider key e.g. 'fred', 'yfinance'")
    code: str = Field(..., description="Native series code (FRED id, ticker, etc)")
    description: str = ""
    frequency: Frequency = "daily"
    transform: Literal["level", "log_return", "yoy_pct", "diff"] = "level"
    start_date: str | None = None
    country: str | None = None

    @field_validator("code")
    @classmethod
    def code_not_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("code cannot be empty")
        return v.strip()


# ============================================================
# Default series catalogue (the L1-L5 starter set)
# ============================================================
DEFAULT_SERIES: list[Series] = [
    # ─────────────── L1: GLOBAL ───────────────
    Series(id="fred_fedfunds", level="L1", asset_class="macro", source="fred",
           code="FEDFUNDS", frequency="monthly", transform="level",
           description="Effective Federal Funds Rate (US policy rate proxy)"),
    Series(id="fred_dxy_broad", level="L1", asset_class="macro", source="fred",
           code="DTWEXBGS", frequency="daily", transform="log_return",
           description="Trade-Weighted USD Index (Broad)"),
    Series(id="fred_vix", level="L1", asset_class="macro", source="fred",
           code="VIXCLS", frequency="daily", transform="level",
           description="CBOE Volatility Index (VIX)"),
    Series(id="fred_t10y2y", level="L1", asset_class="macro", source="fred",
           code="T10Y2Y", frequency="daily", transform="level",
           description="10Y-2Y Treasury Spread (yield curve slope)"),
    Series(id="fred_ig_spread", level="L1", asset_class="macro", source="fred",
           code="BAMLC0A0CM", frequency="daily", transform="level",
           description="ICE BofA US Corporate IG OAS"),
    Series(id="fred_hy_spread", level="L1", asset_class="macro", source="fred",
           code="BAMLH0A0HYM2", frequency="daily", transform="level",
           description="ICE BofA US High Yield OAS"),
    Series(id="fred_wti", level="L1", asset_class="commodity", source="fred",
           code="DCOILWTICO", frequency="daily", transform="log_return",
           description="WTI Crude Oil Spot"),
    Series(id="fred_gold_pm", level="L1", asset_class="commodity", source="fred",
           code="LBMA/GOLD_USD_PM", frequency="daily", transform="log_return",
           description="LBMA Gold Price PM Fix USD"),
    Series(id="wb_global_gdp_growth", level="L1", asset_class="macro",
           source="worldbank", code="NY.GDP.MKTP.KD.ZG", frequency="annual",
           transform="level",
           description="Global GDP growth (annual %)"),

    # ─────────────── L2: CONTINENTAL ───────────────
    Series(id="yahoo_sp500", level="L2", asset_class="equity", source="yfinance",
           code="^GSPC", frequency="daily", transform="log_return",
           description="S&P 500 Index"),
    Series(id="yahoo_nasdaq", level="L2", asset_class="equity", source="yfinance",
           code="^IXIC", frequency="daily", transform="log_return",
           description="NASDAQ Composite"),
    Series(id="yahoo_nikkei", level="L2", asset_class="equity", source="yfinance",
           code="^N225", frequency="daily", transform="log_return",
           description="Nikkei 225 (Japan)"),
    Series(id="yahoo_stoxx", level="L2", asset_class="equity", source="yfinance",
           code="^STOXX", frequency="daily", transform="log_return",
           description="STOXX Europe 600"),
    Series(id="yahoo_eem", level="L2", asset_class="etf", source="yfinance",
           code="EEM", frequency="daily", transform="log_return",
           description="iShares MSCI Emerging Markets ETF"),
    Series(id="yahoo_set", level="L2", asset_class="equity", source="yfinance",
           code="^SET.BK", frequency="daily", transform="log_return",
           description="Stock Exchange of Thailand Index"),

    # ─────────────── L3: COUNTRY ───────────────
    Series(id="fred_us_gdp", level="L3", asset_class="macro", source="fred",
           code="GDPC1", country="US", frequency="quarterly",
           transform="yoy_pct", description="US Real GDP"),
    Series(id="fred_us_cpi", level="L3", asset_class="macro", source="fred",
           code="CPIAUCSL", country="US", frequency="monthly",
           transform="yoy_pct", description="US CPI All Urban"),
    Series(id="fred_us_unrate", level="L3", asset_class="macro", source="fred",
           code="UNRATE", country="US", frequency="monthly", transform="level",
           description="US Unemployment Rate"),
    Series(id="fred_us_nfci", level="L3", asset_class="macro", source="fred",
           code="NFCI", country="US", frequency="weekly", transform="level",
           description="Chicago Fed National Financial Conditions Index"),
    Series(id="fred_us_debt", level="L3", asset_class="macro", source="fred",
           code="GFDEBTN", country="US", frequency="monthly", transform="level",
           description="US Federal Debt Total Public"),
    Series(id="wb_th_gdp", level="L3", asset_class="macro", source="worldbank",
           code="NY.GDP.MKTP.KD.ZG", country="TH", frequency="annual",
           transform="level", description="Thailand GDP growth"),
    Series(id="wb_th_cpi", level="L3", asset_class="macro", source="worldbank",
           code="FP.CPI.TOTL.ZG", country="TH", frequency="annual",
           transform="level", description="Thailand CPI inflation"),
    Series(id="fred_thb_usd", level="L3", asset_class="fx", source="fred",
           code="DEXTHUS", country="TH", frequency="daily",
           transform="log_return", description="THB/USD exchange rate"),

    # ─────────────── L4: MARKET (per instrument) ───────────────
    Series(id="yahoo_aapl", level="L4", asset_class="equity", source="yfinance",
           code="AAPL", frequency="daily", transform="log_return",
           country="US", description="Apple Inc"),
    Series(id="yahoo_msft", level="L4", asset_class="equity", source="yfinance",
           code="MSFT", frequency="daily", transform="log_return",
           country="US", description="Microsoft Corp"),
    Series(id="yahoo_btc_usd", level="L4", asset_class="crypto",
           source="yfinance", code="BTC-USD", frequency="daily",
           transform="log_return", description="Bitcoin / USD"),
    Series(id="yahoo_eth_usd", level="L4", asset_class="crypto",
           source="yfinance", code="ETH-USD", frequency="daily",
           transform="log_return", description="Ethereum / USD"),
    Series(id="ccxt_binance_btc", level="L4", asset_class="crypto",
           source="binance", code="BTC/USDT", frequency="daily",
           transform="log_return", description="BTC/USDT via Binance"),

    # ─────────────── L5: EXTERNAL ───────────────
    Series(id="gpr_index", level="L5", asset_class="alt", source="manual_csv",
           code="matteoiacoviello_gpr_daily", frequency="daily",
           transform="level",
           description="Geopolitical Risk Index (Caldara & Iacoviello)"),
    Series(id="us_epu", level="L5", asset_class="alt", source="manual_csv",
           code="policyuncertainty_us_epu", frequency="monthly",
           transform="level",
           description="US Economic Policy Uncertainty Index"),
    Series(id="fred_gscpi", level="L5", asset_class="alt", source="manual_csv",
           code="nyfed_gscpi", frequency="monthly", transform="level",
           description="Global Supply Chain Pressure Index"),
    Series(id="altme_fng", level="L5", asset_class="alt", source="coingecko",
           code="fear_and_greed", frequency="daily", transform="level",
           description="Crypto Fear & Greed Index"),
]


def get_series(level: Level | None = None) -> list[Series]:
    """Return all series, optionally filtered by level."""
    if level is None:
        return DEFAULT_SERIES
    return [s for s in DEFAULT_SERIES if s.level == level]


def get_series_by_id(series_id: str) -> Series | None:
    for s in DEFAULT_SERIES:
        if s.id == series_id:
            return s
    return None
