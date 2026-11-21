"""Research sweep: find profitable alternatives for the demo squad.

Experiments (rigorous engine, real daytrad signal functions):
- BTC/ETH: strategies A/C/D on M15 (current M5 scalper has proven negative edge)
- Gold: A/D on M15; M5 scalper with lower frequency (cooldown 4/6) and RR 3.0

Usage: .venv\\Scripts\\python.exe research_sweep.py
Output: reports/research_sweep_crypto_gold_<date>.json/.md
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

from src.daytrad_adapter import ensure_daytrad_importable, get_asset_spec, load_bars
from src.engine import EngineConfig, RigorousEngine
from src.metrics import deflated_sharpe_ratio, fold_sharpes, sharpe_ratio, summarize_trades
from src.purged_cv import fold_index_for_bar, walk_forward_folds

WARMUP = 250
N_FOLDS = 4


def run_one(label, symbol, tf, fn, cooldown, rr_override=None):
    ensure_daytrad_importable()
    if rr_override is not None:
        from config import config
        config.target_rr_ratio = rr_override
    df = load_bars(symbol, tf)
    spec = get_asset_spec(symbol)
    cfg = EngineConfig(
        initial_balance=1000.0, risk_per_trade_pct=0.005,
        contract_size=float(spec["contract_size"]), spread=float(spec["typical_spread"]),
        min_lot=float(spec.get("min_lot", 0.01)), min_sl_dist=float(spec.get("min_sl_dist", 0.5)),
        max_open_positions=1, cooldown_bars=cooldown, sl_before_tp=True,
    )
    res = RigorousEngine(cfg).run(df, fn, warmup_bars=WARMUP)
    trades = res["trades"]
    overall = summarize_trades(trades)
    folds = walk_forward_folds(len(df), N_FOLDS, WARMUP)
    fs = fold_sharpes(trades, len(folds), fold_index_for_bar(folds))
    valid = [s for s in fs if s is not None]
    var = float(sum((s - sum(valid) / len(valid)) ** 2 for s in valid) / len(valid)) if len(valid) >= 2 else 1e-6
    dsr = deflated_sharpe_ratio([t["r"] for t in trades], max(len(folds), 2), max(var, 1e-6))
    out = {"label": label, "symbol": symbol, "tf": tf, "cooldown": cooldown,
           "rr_override": rr_override, "overall": overall,
           "sharpe": sharpe_ratio([t["r"] for t in trades]),
           "dsr": dsr.get("dsr"), "fold_sharpes": fs,
           "fold_expectancy": []}
    for s, e in folds:
        ft = [t for t in trades if s <= t["entry_bar"] < e]
        out["fold_expectancy"].append(summarize_trades(ft)["expectancy_r"])
    return out


def main():
    ensure_daytrad_importable()
    from backtest import strategies as S

    def scalper(asset):
        return lambda w, i: S.strategy_m5_scalper(w, i, asset_type=asset)

    experiments = [
        ("BTC M15 A pullback", "BTCUSD", "M15", S.strategy_ema_pullback, 1, None),
        ("BTC M15 C BB", "BTCUSD", "M15", S.strategy_bb_reversion, 1, None),
        ("BTC M15 D MTF", "BTCUSD", "M15", S.strategy_mtf_momentum, 1, None),
        ("ETH M15 A pullback", "ETHUSD", "M15", S.strategy_ema_pullback, 1, None),
        ("ETH M15 C BB", "ETHUSD", "M15", S.strategy_bb_reversion, 1, None),
        ("ETH M15 D MTF", "ETHUSD", "M15", S.strategy_mtf_momentum, 1, None),
        ("GOLD M15 D MTF", "XAUUSD", "M15", S.strategy_mtf_momentum, 1, None),
        ("GOLD M15 A pullback", "XAUUSD", "M15", S.strategy_ema_pullback, 1, None),
        ("GOLD M5 F cd4", "XAUUSD", "M5", scalper("gold"), 4, None),
        ("GOLD M5 F cd6", "XAUUSD", "M5", scalper("gold"), 6, None),
        ("GOLD M5 F RR3", "XAUUSD", "M5", scalper("gold"), 2, 3.0),
    ]
    results = []
    for label, sym, tf, fn, cd, rr in experiments:
        print(f"[run] {label} ...", flush=True)
        r = run_one(label, sym, tf, fn, cd, rr)
        results.append(r)
        o = r["overall"]
        exp = f"{o['expectancy_r']:.3f}" if o["expectancy_r"] is not None else "-"
        pf = f"{o['profit_factor']:.2f}" if o["profit_factor"] is not None else "-"
        dsr = f"{r['dsr']:.3f}" if r["dsr"] is not None else "-"
        print(f"      n={o['trades']} exp={exp} PF={pf} DSR={dsr}", flush=True)

    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    out_dir = Path(__file__).resolve().parent / "reports"
    out_dir.mkdir(exist_ok=True)
    base = out_dir / f"research_sweep_crypto_gold_{stamp}"
    base.with_suffix(".json").write_text(json.dumps(
        {"generated_utc": datetime.now(timezone.utc).isoformat(), "results": results},
        indent=2, ensure_ascii=False), encoding="utf-8")
    lines = ["# Research sweep: crypto alternatives + gold tuning — " + stamp, "",
             "| Experiment | n | Win% | Exp(R) | PF | DSR | fold exp(R) |",
             "|---|---|---|---|---|---|---|"]
    for r in results:
        o = r["overall"]
        wr = f"{o['win_rate']*100:.1f}" if o["win_rate"] is not None else "-"
        exp = f"{o['expectancy_r']:.3f}" if o["expectancy_r"] is not None else "-"
        pf = f"{o['profit_factor']:.2f}" if o["profit_factor"] is not None else "-"
        dsr = f"{r['dsr']:.3f}" if r["dsr"] is not None else "-"
        fe = ", ".join(f"{x:.2f}" if x is not None else "-" for x in r["fold_expectancy"])
        lines.append(f"| {r['label']} | {o['trades']} | {wr} | {exp} | {pf} | {dsr} | {fe} |")
    base.with_suffix(".md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"\nSaved: {base}.json / .md")


if __name__ == "__main__":
    main()