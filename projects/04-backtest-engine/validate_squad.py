"""Validate the live daytrad squad (all9) with the rigorous engine.

Usage (from 04-backtest-engine dir, with .venv):
    .venv\\Scripts\\python.exe validate_squad.py [--assets gold,btc,eth] [--folds 4]

Outputs:
    reports/squad_validation_<date>.json  (machine-readable)
    reports/squad_validation_<date>.md    (Thai summary for the desk)

Method: one full-period run per asset with the REAL live signal function;
trades are then assigned to contiguous walk-forward folds by entry bar for
per-segment stability stats. Deflated Sharpe uses fold Sharpes as the trial
variance proxy (documented limitation; true trial count is larger).
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

from src.daytrad_adapter import SQUAD_PLAN, get_asset_spec, live_strategy_fn, load_bars
from src.engine import EngineConfig, RigorousEngine
from src.metrics import deflated_sharpe_ratio, fold_sharpes, sharpe_ratio, summarize_trades
from src.purged_cv import fold_index_for_bar, walk_forward_folds

WARMUP = 250


def validate_asset(plan: dict, n_folds: int) -> dict:
    symbol, tf, key = plan["symbol"], plan["tf"], plan["key"]
    df = load_bars(symbol, tf)
    spec = get_asset_spec(symbol)
    fn = live_strategy_fn(symbol, tf, key)
    cfg = EngineConfig(
        initial_balance=1000.0,
        risk_per_trade_pct=0.005,
        contract_size=float(spec["contract_size"]),
        spread=float(spec["typical_spread"]),
        min_lot=float(spec.get("min_lot", 0.01)),
        min_sl_dist=float(spec.get("min_sl_dist", 0.5)),
        max_open_positions=1,
        cooldown_bars=2 if tf == "M5" else 1,
        sl_before_tp=True,
    )
    res = RigorousEngine(cfg).run(df, fn, warmup_bars=WARMUP)
    trades = res["trades"]
    overall = summarize_trades(trades)
    folds = walk_forward_folds(len(df), n_folds, WARMUP)
    fidx = fold_index_for_bar(folds)
    fsharpes = fold_sharpes(trades, len(folds), fidx)
    valid_fs = [s for s in fsharpes if s is not None]
    trial_var = float(sum((s - sum(valid_fs) / len(valid_fs)) ** 2 for s in valid_fs) / len(valid_fs)) \
        if len(valid_fs) >= 2 else 0.0
    r_series = [t["r"] for t in trades]
    dsr = deflated_sharpe_ratio(r_series, n_trials=max(len(folds), 2),
                                trial_sharpe_variance=max(trial_var, 1e-6))
    fold_stats = []
    for k, (s, e) in enumerate(folds):
        ft = [t for t in trades if s <= t["entry_bar"] < e]
        fold_stats.append({"fold": k, "start": str(df["timestamp"].iloc[s]),
                           "end": str(df["timestamp"].iloc[min(e, len(df) - 1)]),
                           **summarize_trades(ft), "sharpe": fsharpes[k]})
    return {
        "asset": key, "symbol": symbol, "timeframe": tf, "strategy": plan["strategy"],
        "bars": len(df), "data_range": [str(df["timestamp"].iloc[0]), str(df["timestamp"].iloc[-1])],
        "config": {"spread": cfg.spread, "contract_size": cfg.contract_size,
                   "risk_pct": cfg.risk_per_trade_pct, "maxpos": cfg.max_open_positions,
                   "sl_before_tp": True, "entry": "next_bar_open", "spread_both_sides": True},
        "overall": overall,
        "sharpe_per_trade": sharpe_ratio(r_series),
        "deflated_sharpe": dsr,
        "folds": fold_stats,
        "return_pct": res["return_pct"],
        "rejected_min_sl": res["rejected_min_sl"],
    }


def verdict(r: dict) -> str:
    o = r["overall"]
    if o["trades"] < 20:
        return "SAMPLE_NOK (<20 trades)"
    exp = o["expectancy_r"] or 0.0
    dsr = (r["deflated_sharpe"] or {}).get("dsr")
    if exp > 0.05 and dsr is not None and dsr >= 0.90:
        return "PASS (edge + DSR>=0.90)"
    if exp > 0.0:
        return "WEAK (expectancy>0 but DSR<0.90)"
    return "FAIL (expectancy<=0)"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--assets", default="all", help="comma keys: gold,btc,eth,xag,xpt,gbp,eur,ukoil,xng")
    ap.add_argument("--folds", type=int, default=4)
    args = ap.parse_args()
    keys = None if args.assets == "all" else set(args.assets.split(","))
    plans = [p for p in SQUAD_PLAN if keys is None or p["key"] in keys]

    results = []
    for p in plans:
        print(f"[run] {p['key']} {p['symbol']} {p['tf']} ...", flush=True)
        r = validate_asset(p, args.folds)
        r["verdict"] = verdict(r)
        results.append(r)
        o = r["overall"]
        print(f"      trades={o['trades']} exp={o['expectancy_r']} PF={o['profit_factor']} "
              f"DSR={r['deflated_sharpe'].get('dsr')} -> {r['verdict']}", flush=True)

    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    out_dir = Path(__file__).resolve().parent / "reports"
    out_dir.mkdir(exist_ok=True)
    jpath = out_dir / f"squad_validation_{stamp}.json"
    jpath.write_text(json.dumps({"generated_utc": datetime.now(timezone.utc).isoformat(),
                                 "method": "rigorous engine: SL-before-TP, spread both sides, "
                                           "next-bar-open entry, live signal functions, "
                                           "walk-forward folds, deflated Sharpe",
                                 "results": results}, indent=2, ensure_ascii=False), encoding="utf-8")

    lines = ["# Squad Validation (rigorous engine) — " + stamp, "",
             "Engine: SL-before-TP | spread both sides | next-bar-open entry | live signal fn | no daily gates",
             "", "| Asset | TF | Trades | Win% | Exp(R) | PF | Sharpe | DSR | Verdict |",
             "|---|---|---|---|---|---|---|---|---|"]
    for r in results:
        o = r["overall"]
        wr = f"{o['win_rate']*100:.1f}" if o["win_rate"] is not None else "-"
        exp = f"{o['expectancy_r']:.3f}" if o["expectancy_r"] is not None else "-"
        pf = f"{o['profit_factor']:.2f}" if o["profit_factor"] is not None else "-"
        sr = f"{r['sharpe_per_trade']:.3f}" if r["sharpe_per_trade"] is not None else "-"
        dsr = f"{r['deflated_sharpe']['dsr']:.3f}" if r["deflated_sharpe"].get("dsr") is not None else "-"
        lines.append(f"| {r['symbol']} | {r['timeframe']} | {o['trades']} | {wr} | {exp} | {pf} | {sr} | {dsr} | {r['verdict']} |")
    mpath = out_dir / f"squad_validation_{stamp}.md"
    mpath.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"\nSaved: {jpath}\nSaved: {mpath}")


if __name__ == "__main__":
    main()