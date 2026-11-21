"""Rigorous bar-by-bar backtest engine.

Fixes the optimistic biases found in daytrad's legacy M5 engine:
1. SL is checked BEFORE TP within a bar (pessimistic when both touch).
2. Spread is charged on BOTH entry and exit (half-spread each side).
3. Entry fills at the NEXT bar open after the signal bar close
   (no same-bar close look-ahead).
4. No daily profit/loss gates by default — matches live squad running
   with --no-loss-cutoff. Gates can be enabled explicitly.

Signal functions are daytrad-compatible: fn(window_df, idx) -> dict with
keys action (BUY/SELL/HOLD), sl, tp, reason. The window is df.iloc[:idx+1]
(expanding, past-only), identical to the legacy sweep harness so results
are directly comparable.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Dict, List, Optional

import pandas as pd


@dataclass
class EngineConfig:
    initial_balance: float = 1000.0
    risk_per_trade_pct: float = 0.005
    contract_size: float = 100.0
    spread: float = 0.20          # full spread in price units
    min_lot: float = 0.01
    max_lot: float = 5.0
    min_sl_dist: float = 1.0      # reject signals with SL closer than this
    max_open_positions: int = 1   # live config default
    cooldown_bars: int = 1        # min bars between entries
    sl_before_tp: bool = True
    daily_target_pct: Optional[float] = None   # None = off (live no-loss-cutoff)
    daily_max_loss_pct: Optional[float] = None


class RigorousEngine:
    def __init__(self, cfg: EngineConfig):
        self.cfg = cfg

    def run(
        self,
        df: pd.DataFrame,
        signal_fn: Callable[[pd.DataFrame, int], Dict[str, Any]],
        warmup_bars: int = 250,
        trade_start: Optional[int] = None,
        trade_end: Optional[int] = None,
    ) -> Dict[str, Any]:
        cfg = self.cfg
        n = len(df)
        ts = trade_start if trade_start is not None else warmup_bars
        te = trade_end if trade_end is not None else n
        half = cfg.spread / 2.0

        balance = cfg.initial_balance
        trades: List[Dict[str, Any]] = []
        positions: List[Dict[str, Any]] = []
        pending: Optional[Dict[str, Any]] = None
        last_entry_bar = -10**9
        rejected_min_sl = 0
        day_key = ""
        day_pnl = 0.0
        day_locked = False

        opens = df["open"].to_numpy(dtype=float)
        highs = df["high"].to_numpy(dtype=float)
        lows = df["low"].to_numpy(dtype=float)
        closes = df["close"].to_numpy(dtype=float)
        times = df["timestamp"].tolist()

        for i in range(warmup_bars, n):
            # day roll / optional gates
            d = str(times[i])[:10]
            if d != day_key:
                day_key, day_pnl, day_locked = d, 0.0, False

            # 1) fill pending signal at THIS bar open (signal from i-1 close)
            if pending is not None and i < te:
                sig = pending
                pending = None
                blocked = day_locked or len(positions) >= cfg.max_open_positions \
                    or (i - last_entry_bar) < cfg.cooldown_bars
                if not blocked:
                    side = sig["action"]
                    entry = opens[i] + half if side == "BUY" else opens[i] - half
                    sl, tp = float(sig["sl"]), float(sig["tp"])
                    risk_dist = abs(entry - sl)
                    if risk_dist > 0:
                        risk_usd = balance * cfg.risk_per_trade_pct
                        lots = risk_usd / (risk_dist * cfg.contract_size)
                        lots = max(cfg.min_lot, min(cfg.max_lot, lots))
                        positions.append({
                            "side": side, "entry_fill": entry, "sl": sl, "tp": tp,
                            "lots": lots, "entry_bar": i, "entry_time": str(times[i]),
                            "risk_dist": risk_dist, "reason": sig.get("reason", ""),
                        })
                        last_entry_bar = i

            # 2) manage open positions on this bar (SL first = pessimistic)
            still_open: List[Dict[str, Any]] = []
            for pos in positions:
                buy = pos["side"] == "BUY"
                sl_hit = lows[i] <= pos["sl"] if buy else highs[i] >= pos["sl"]
                tp_hit = highs[i] >= pos["tp"] if buy else lows[i] <= pos["tp"]
                exit_price = None
                reason = None
                if cfg.sl_before_tp:
                    if sl_hit:
                        exit_price, reason = pos["sl"], "SL_HIT"
                    elif tp_hit:
                        exit_price, reason = pos["tp"], "TP_HIT"
                else:
                    if tp_hit:
                        exit_price, reason = pos["tp"], "TP_HIT"
                    elif sl_hit:
                        exit_price, reason = pos["sl"], "SL_HIT"
                if exit_price is None:
                    still_open.append(pos)
                    continue
                exit_fill = exit_price - half if buy else exit_price + half
                direction = 1.0 if buy else -1.0
                pnl = (exit_fill - pos["entry_fill"]) * direction * pos["lots"] * cfg.contract_size
                r = (exit_fill - pos["entry_fill"]) * direction / pos["risk_dist"]
                balance += pnl
                day_pnl += pnl
                trades.append({
                    "entry_bar": pos["entry_bar"], "exit_bar": i,
                    "entry_time": pos["entry_time"], "exit_time": str(times[i]),
                    "side": pos["side"], "entry_fill": pos["entry_fill"],
                    "exit_fill": exit_fill, "sl": pos["sl"], "tp": pos["tp"],
                    "lots": pos["lots"], "pnl_usd": pnl, "r": r,
                    "exit_reason": reason, "reason": pos["reason"],
                    "bars_held": i - pos["entry_bar"],
                    "actual_risk_pct": pos["risk_dist"] * pos["lots"] * cfg.contract_size / max(balance - pnl, 1e-9),
                })
                if cfg.daily_target_pct is not None and day_pnl >= cfg.initial_balance * cfg.daily_target_pct:
                    day_locked = True
                if cfg.daily_max_loss_pct is not None and day_pnl <= -cfg.initial_balance * cfg.daily_max_loss_pct:
                    day_locked = True
            positions = still_open

            # 3) evaluate signal at THIS bar close -> pending for next bar
            if i + 1 < te and not day_locked and len(positions) < cfg.max_open_positions \
                    and (i - last_entry_bar) >= cfg.cooldown_bars:
                sig = signal_fn(df.iloc[: i + 1], i)
                action = sig.get("action", "HOLD")
                if action in ("BUY", "SELL") and sig.get("sl") and sig.get("tp"):
                    sl_dist = abs(closes[i] - float(sig["sl"]))
                    valid_side = (float(sig["sl"]) < closes[i] < float(sig["tp"])) if action == "BUY" \
                        else (float(sig["tp"]) < closes[i] < float(sig["sl"]))
                    if sl_dist < cfg.min_sl_dist or not valid_side:
                        rejected_min_sl += 1
                    else:
                        pending = sig

        # force-close leftovers at last close (mark as EOD, spread charged)
        if positions:
            last = n - 1
            for pos in positions:
                buy = pos["side"] == "BUY"
                exit_fill = closes[last] - half if buy else closes[last] + half
                direction = 1.0 if buy else -1.0
                pnl = (exit_fill - pos["entry_fill"]) * direction * pos["lots"] * cfg.contract_size
                r = (exit_fill - pos["entry_fill"]) * direction / pos["risk_dist"]
                balance += pnl
                trades.append({
                    "entry_bar": pos["entry_bar"], "exit_bar": last,
                    "entry_time": pos["entry_time"], "exit_time": str(times[last]),
                    "side": pos["side"], "entry_fill": pos["entry_fill"],
                    "exit_fill": exit_fill, "sl": pos["sl"], "tp": pos["tp"],
                    "lots": pos["lots"], "pnl_usd": pnl, "r": r,
                    "exit_reason": "EOD", "reason": pos["reason"],
                    "bars_held": last - pos["entry_bar"],
                    "actual_risk_pct": None,
                })

        return {
            "trades": trades,
            "final_balance": balance,
            "return_pct": (balance / cfg.initial_balance - 1.0) * 100.0,
            "rejected_min_sl": rejected_min_sl,
            "bars": n,
            "warmup_bars": warmup_bars,
        }