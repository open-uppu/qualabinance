"""
cli.py — Entry points for the data pipeline.

Examples:
    uv run python -m src.cli --level L1 --refresh
    uv run python -m src.cli --series fred_fedfunds,yahoo_sp500 --refresh
    uv run python -m src.cli --align --output wide
    uv run python -m src.cli --coverage
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Ensure src/ is on the path so `import config` works when invoked as a script.
sys.path.insert(0, str(Path(__file__).resolve().parent))

from loguru import logger

import config
from align import align_all
import ingest
from store import coverage_report, get_con, save_aligned, save_raw, upsert_series
from transform import apply_transform


def cmd_refresh(args: argparse.Namespace) -> None:
    """Pull selected series, transform, persist raw + DuckDB."""
    series_pool = config.get_series(args.level) if args.level else config.DEFAULT_SERIES
    if args.series:
        wanted = set(args.series.split(","))
        series_pool = [s for s in series_pool if s.id in wanted]

    con = get_con()
    for s in series_pool:
        try:
            logger.info(f"→ pulling {s.id} ({s.source}/{s.code})")
            src = ingest.get_source(s.source)
            df = src.fetch(s)
            df = apply_transform(df, s.transform)

            save_raw(s.id, df)
            upsert_series(
                con,
                series_id=s.id,
                df=df,
                level=s.level,
                asset_class=s.asset_class,
                source=s.source,
                frequency=s.frequency,
                transform=s.transform,
            )
        except Exception as e:  # noqa: BLE001
            logger.error(f"✗ {s.id}: {e}")

    logger.info("refresh complete")


def cmd_align(args: argparse.Namespace) -> None:
    """Read all series_observations from DuckDB and build a wide daily panel."""
    con = get_con()
    series_dict: dict[str, object] = {}
    frequencies: dict[str, str] = {}
    rows = con.execute("""
        SELECT series_id, frequency, value, obs_date
        FROM series_observations
        ORDER BY series_id, obs_date
    """).fetchall()
    # group by series_id
    by_id: dict[str, dict] = {}
    for sid, freq, val, ts in rows:
        if sid not in by_id:
            by_id[sid] = {"freq": freq, "rows": []}
        by_id[sid]["rows"].append((ts, val))
    import pandas as pd  # noqa: PLC0415
    for sid, payload in by_id.items():
        df = pd.DataFrame(payload["rows"], columns=["obs_date", "value"]).set_index("obs_date")
        df.index = pd.to_datetime(df.index).tz_localize("UTC")
        series_dict[sid] = df
        frequencies[sid] = payload["freq"]

    wide = align_all(series_dict, frequencies, start=args.start)
    save_aligned(wide, name=args.output)


def cmd_coverage(args: argparse.Namespace) -> None:
    """Print coverage report."""
    con = get_con()
    rep = coverage_report(con)
    print(rep.to_string(index=False))


def main() -> None:
    parser = argparse.ArgumentParser(description="Qualabinance data pipeline")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_ref = sub.add_parser("refresh", help="Pull + transform + persist")
    p_ref.add_argument("--level", choices=["L1", "L2", "L3", "L4", "L5"])
    p_ref.add_argument("--series", help="Comma-separated series ids")
    p_ref.set_defaults(func=cmd_refresh)

    p_ali = sub.add_parser("align", help="Build wide daily aligned panel")
    p_ali.add_argument("--start", default="2000-01-01")
    p_ali.add_argument("--output", default="wide_daily")
    p_ali.set_defaults(func=cmd_align)

    p_cov = sub.add_parser("coverage", help="Per-series coverage report")
    p_cov.set_defaults(func=cmd_coverage)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
