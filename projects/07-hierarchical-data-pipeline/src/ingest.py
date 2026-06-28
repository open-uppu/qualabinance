"""
ingest.py — Pull a single series from its source.

Each ``Source`` class implements a ``fetch(series)`` returning a tidy DataFrame:

    index = pd.DatetimeIndex (UTC)
    columns = [value, source, fetched_at]

The catalog knows the source; the Source knows how to talk to it.
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from datetime import datetime, timezone
from typing import Any

import pandas as pd
from loguru import logger
from tenacity import retry, stop_after_attempt, wait_exponential

from config import KEYS, Series


def _stamp(df: pd.DataFrame, source_name: str) -> pd.DataFrame:
    """Add provenance columns to every pulled DataFrame."""
    df = df.copy()
    df["source"] = source_name
    df["fetched_at"] = datetime.now(timezone.utc)
    return df


# ============================================================
# Abstract base
# ============================================================
class Source(ABC):
    name: str

    @abstractmethod
    def fetch(self, series: Series) -> pd.DataFrame:
        """Return DataFrame with `value` column + DatetimeIndex (UTC)."""
        raise NotImplementedError


# ============================================================
# FRED
# ============================================================
class FREDSrc(Source):
    name = "fred"

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(min=2, max=30))
    def fetch(self, series: Series) -> pd.DataFrame:
        if not KEYS.fred:
            raise RuntimeError("FRED_API_KEY missing in .env")

        from fredapi import Fred
        fred = Fred(api_key=KEYS.fred)
        s = fred.get_series(series.code)
        df = pd.DataFrame({"value": s})
        df.index = pd.to_datetime(df.index).tz_localize("UTC")
        df.index.name = "date"
        return _stamp(df, self.name).sort_index()


# ============================================================
# World Bank
# ============================================================
class WorldBankSrc(Source):
    name = "worldbank"

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(min=2, max=30))
    def fetch(self, series: Series) -> pd.DataFrame:
        import wbgapi as wb
        # Code can be either indicator (annual) or indicator:country
        # e.g. "NY.GDP.MKTP.KD.ZG" + country filter
        kwargs: dict[str, Any] = {
            "indicator": series.code,
            "mrv": 30,           # most recent 30 years
        }
        if series.country:
            kwargs["country"] = series.country
        else:
            kwargs["country"] = "all"
        df = wb.data.DataFrame(**kwargs)
        # wbgapi returns countries as rows, years as columns
        df = df.T  # years as rows
        df.index = pd.to_datetime(df.index, format="%Y").tz_localize("UTC")
        df.index.name = "date"
        df.columns = ["value"]
        df["value"] = pd.to_numeric(df["value"], errors="coerce")
        return _stamp(df, self.name).sort_index().dropna()


# ============================================================
# yfinance
# ============================================================
class YFinanceSrc(Source):
    name = "yfinance"

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(min=2, max=30))
    def fetch(self, series: Series) -> pd.DataFrame:
        import yfinance as yf
        ticker = yf.Ticker(series.code)
        # 'max' goes back to issue date; cap to 1990+ for sane sizes
        hist = ticker.history(period="max", auto_adjust=True)
        if hist.empty:
            raise RuntimeError(f"yfinance returned empty data for {series.code}")
        df = pd.DataFrame({"value": hist["Close"]})
        # yfinance returns tz-aware Eastern Time — convert to UTC
        if df.index.tz is None:
            df.index = df.index.tz_localize("UTC")
        else:
            df.index = df.index.tz_convert("UTC")
        df.index.name = "date"
        return _stamp(df, self.name).sort_index()


# ============================================================
# ccxt (Binance + other crypto exchanges)
# ============================================================
class CcxtSrc(Source):
    name = "binance"

    def __init__(self, exchange_id: str = "binance") -> None:
        self.exchange_id = exchange_id
        self.name = exchange_id

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(min=2, max=30))
    def fetch(self, series: Series) -> pd.DataFrame:
        import ccxt
        ex = getattr(ccxt, self.exchange_id)({"enableRateLimit": True})
        symbol = series.code  # e.g. "BTC/USDT"
        # Fetch daily OHLCV (limit 1000 per call, loop for longer history)
        since_ms = int(pd.Timestamp("2015-01-01", tz="UTC").timestamp() * 1000)
        all_rows: list[list[Any]] = []
        while True:
            rows = ex.fetch_ohlcv(symbol, timeframe="1d", since=since_ms, limit=1000)
            if not rows:
                break
            all_rows.extend(rows)
            since_ms = rows[-1][0] + 86_400_000  # next day
            if len(rows) < 1000:
                break
        if not all_rows:
            raise RuntimeError(f"ccxt empty for {symbol}")
        df = pd.DataFrame(all_rows, columns=["ts", "open", "high", "low", "close", "vol"])
        df["date"] = pd.to_datetime(df["ts"], unit="ms", utc=True)
        df = df.set_index("date")[["close"]].rename(columns={"close": "value"})
        return _stamp(df, self.name).sort_index()


# ============================================================
# Manual CSV (for GPR, EPU, GSCPI — downloaded manually)
# ============================================================
class ManualCSVSource(Source):
    """Manual download — user places CSV at PARQUET_DIR/raw/{code}.csv.

    Expected CSV format:
        date,value
        2020-01-01,42.3
        2020-02-01,38.7
    """

    name = "manual_csv"

    def fetch(self, series: Series) -> pd.DataFrame:
        from config import PARQUET_DIR
        path = PARQUET_DIR / "raw" / f"{series.code}.csv"
        if not path.exists():
            raise FileNotFoundError(
                f"Manual CSV missing: {path}\n"
                f"Download for {series.id} and save to this path."
            )
        df = pd.read_csv(path, parse_dates=["date"])
        df["date"] = pd.to_datetime(df["date"]).dt.tz_localize("UTC")
        df = df.set_index("date")[["value"]]
        return _stamp(df, self.name).sort_index()


# ============================================================
# CoinGecko (Fear & Greed)
# ============================================================
class CoinGeckoSrc(Source):
    name = "coingecko"

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(min=2, max=30))
    def fetch(self, series: Series) -> pd.DataFrame:
        import requests
        if series.code == "fear_and_greed":
            url = "https://api.alternative.me/fng/?limit=0&format=json"
            r = requests.get(url, timeout=30)
            r.raise_for_status()
            data = r.json()["data"]
            df = pd.DataFrame(data)
            df["date"] = pd.to_datetime(df["timestamp"].astype(int), unit="s", utc=True)
            df = df.rename(columns={"value": "value"})[["date", "value"]]
            df["value"] = pd.to_numeric(df["value"], errors="coerce")
            df = df.set_index("date").sort_index()
            return _stamp(df, self.name)
        raise NotImplementedError(f"CoinGecko code {series.code} not wired")


# ============================================================
# Source registry
# ============================================================
SOURCE_REGISTRY: dict[str, type[Source] | Source] = {
    "fred": FREDSrc,
    "worldbank": WorldBankSrc,
    "yfinance": YFinanceSrc,
    "binance": CcxtSrc,           # class — instantiated per-fetch with exchange_id
    "manual_csv": ManualCSVSource,
    "coingecko": CoinGeckoSrc,
}


def get_source(source_name: str) -> Source:
    """Return an instance of the requested source."""
    cls_or_inst = SOURCE_REGISTRY[source_name]
    if isinstance(cls_or_inst, type):
        return cls_or_inst()
    return cls_or_inst
