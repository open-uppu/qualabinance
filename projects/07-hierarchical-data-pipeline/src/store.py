"""
store.py — DuckDB-backed analytical store with Parquet snapshots.

Why DuckDB:
  - Single-file (easy version control with git LFS or DVC)
  - SQL interface for cross-series joins
  - Fast columnar reads for ML pipelines
  - Plays nicely with pandas/polars

Layout:
  data/
    qualabinance.duckdb            # main analytical DB
    parquet/
      raw/{source}_{code}.parquet   # raw pulls (immutable)
      aligned/wide_daily.parquet    # wide daily aligned panel
"""
from __future__ import annotations

from datetime import datetime, timezone

import duckdb
import pandas as pd
from loguru import logger

from config import DUCKDB_PATH, PARQUET_DIR


def get_con() -> duckdb.DuckDBPyConnection:
    """Open (and lazily create) the main DuckDB connection."""
    return duckdb.connect(str(DUCKDB_PATH))


def save_raw(series_id: str, df: pd.DataFrame) -> Path:
    """Persist raw pull to Parquet (one file per series, immutable)."""
    out_dir = PARQUET_DIR / "raw"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{series_id}.parquet"
    df.to_parquet(out_path, index=True)
    logger.info(f"saved raw {series_id}: {len(df)} rows → {out_path}")
    return out_path


def load_raw(series_id: str) -> pd.DataFrame:
    """Load previously-pulled raw data (for offline re-runs)."""
    path = PARQUET_DIR / "raw" / f"{series_id}.parquet"
    if not path.exists():
        raise FileNotFoundError(path)
    return pd.read_parquet(path)


def upsert_series(con: duckdb.DuckDBPyConnection, series_id: str,
                  df: pd.DataFrame, level: str, asset_class: str,
                  source: str, frequency: str, transform: str) -> None:
    """Replace the rows for this series_id in the master `series_observations` table."""
    con.execute("""
        CREATE TABLE IF NOT EXISTS series_observations (
            series_id   VARCHAR,
            level       VARCHAR,
            asset_class VARCHAR,
            source      VARCHAR,
            frequency   VARCHAR,
            transform   VARCHAR,
            obs_date    TIMESTAMP,
            value       DOUBLE,
            fetched_at  TIMESTAMP,
            PRIMARY KEY (series_id, obs_date)
        )
    """)
    prepped = df.reset_index().rename(columns={"index": "obs_date", "value": "value"})
    if "date" in prepped.columns and "obs_date" not in prepped.columns:
        prepped = prepped.rename(columns={"date": "obs_date"})
    prepped["series_id"] = series_id
    prepped["level"] = level
    prepped["asset_class"] = asset_class
    prepped["source"] = source
    prepped["frequency"] = frequency
    prepped["transform"] = transform
    prepped = prepped[[
        "series_id", "level", "asset_class", "source", "frequency",
        "transform", "obs_date", "value", "fetched_at"
    ]]

    con.execute(
        "DELETE FROM series_observations WHERE series_id = ?",
        [series_id],
    )
    con.register("df_tmp", prepped)
    con.execute("INSERT INTO series_observations SELECT * FROM df_tmp")
    con.unregister("df_tmp")
    logger.info(f"upserted {series_id}: {len(prepped)} rows into DuckDB")


def save_aligned(df: pd.DataFrame, name: str = "wide_daily") -> Path:
    """Save the wide daily aligned panel."""
    out_dir = PARQUET_DIR / "aligned"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{name}.parquet"
    df.to_parquet(out_path)
    logger.info(f"saved aligned panel: {df.shape} → {out_path}")
    return out_path


def coverage_report(con: duckdb.DuckDBPyConnection) -> pd.DataFrame:
    """Return a tidy coverage report per series."""
    return con.execute("""
        SELECT
            series_id,
            level,
            asset_class,
            frequency,
            MIN(obs_date) AS first_obs,
            MAX(obs_date) AS last_obs,
            COUNT(*) AS n_obs,
            COUNT(value) AS n_valid,
            ROUND(COUNT(value)::DOUBLE / COUNT(*), 4) AS valid_ratio
        FROM series_observations
        GROUP BY series_id, level, asset_class, frequency
        ORDER BY level, series_id
    """).df()


# Re-export Path so callers don't have to import it
from pathlib import Path  # noqa: E402
