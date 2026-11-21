"""Validate the CADENCE PACER — the mechanism that actually fires most live entries.

Live pacer (base_agent.step): when flat and >=300s since last entry, enter in
the direction of price vs HTF EMA200, SL = max(1.3*ATR, min_sl_dist),
TP = RR(2.5) * SL. Approximated here with the M5 window EMA200 (live falls
back to it when HTF < 200 bars) — documented approximation.

Usage: .venv\\Scripts\\python.exe pacer_validation.py
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

from src.daytrad_adapter import ensure_daytrad_importable, get_asset_spec, load_bars
from src.engine import EngineConfig, RigorousEngine
from src.metrics import deflated_sharpe_ratio, sharpe_ratio, summarize_trades
from src.purged_cv import fold_index_for_bar, walk_forward_folds
from src.metrics import fold_sharpes

WARMUP = 250


def pacer_fn(min_sl: float, rr: float = 2.5):
    ensure_daytrad_importable()
    from core.indicators import compute_all_indicators

    def fn(window, idx):
        if len(window) < 210:
            return {"action": "HOLD"}
        df = compute_all_indicators(window.tail(250))
        row = df.iloc[-1]
        close = float(row["close"])
        ema200 = float(row["ema_200"])
        atr = float(row["atr_14"])
        sl_dist = max(1.3 * atr, min_sl)
        if close >= ema200:
            return {"action": "BUY", "sl": close - sl_dist, "tp": close + rr * sl_dist,
                    "reason": "PACER macro bullish"}
        return {"action": "SELL", "sl": close + sl_dist, "tp": close - rr * sl_dist,
                "reason": "PACER macro bearish"}
    return fn


def main():
    results = []
    for key, sym, min_sl in [("gold", "XAUUSD", 1.0), ("btc", "BTCUSD", 25.0), ("eth", "ETHUSD", 2.0)]:
        print(f"[run] PACER {sym} M5 ...", flush=True)
        df = load_bars(sym, "M5")
        spec = get_asset_spec(sym)
        cfg = EngineConfig(
            initial_balance=1000.0, risk_per_trade_pct=0.005,
            contract_size=float(spec["contract_size"]), spread=float(spec["typical_spread"]),
            min_lot=0.01, min_sl_dist=float(spec.get("min_sl_dist", 0.5)),
            max_open_positions=1, cooldown_bars=1, sl_before_tp=True,
        )
        res = RigorousEngine(cfg).run(df, pacer_fn(min_sl), warmup_bars=WARMUP)
        trades = res["trades"]
        o = summarize_trades(trades)
        folds = walk_forward_folds(len(df), 4, WARMUP)
        fs = fold_sharpes(trades, len(folds), fold_index_for_bar(folds))
        valid = [s for s in fs if s is not None]
        var = float(sum((s - sum(valid) / len(valid)) ** 2 for s in valid) / len(valid)) if len(valid) >= 2 else 1e-6
        dsr = deflated_sharpe_ratio([t["r"] for t in trades], 4, max(var, 1e-6))
        fe = []
        for s, e in folds:
            ft = [t for t in trades if s <= t["entry_bar"] < e]
            fe.append(summarize_trades(ft)["expectancy_r"])
        r = {"asset": key, "symbol": sym, "overall": o,
             "sharpe": sharpe_ratio([t["r"] for t in trades]),
             "dsr": dsr.get("dsr"), "fold_sharpes": fs, "fold_expectancy": fe}
        results.append(r)
        exp = f"{o['expectancy_r']:.3f}" if o["expectancy_r"] is not None else "-"
        pf = f"{o['profit_factor']:.2f}" if o["profit_factor"] is not None else "-"
        print(f"      n={o['trades']} exp={exp} PF={pf} DSR={r['dsr']:.3f} folds={[round(x,3) if x is not None else None for x in fe]}", flush=True)

    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    out = Path(__file__).resolve().parent / "reports" / f"pacer_validation_{stamp}.json"
    out.write_text(json.dumps({"generated_utc": datetime.now(timezone.utc).isoformat(),
                               "note": "pacer approximated with M5-window EMA200; live uses HTF M15 EMA200 when >=200 bars",
                               "results": results}, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Saved: {out}")


if __name__ == "__main__":
    main()