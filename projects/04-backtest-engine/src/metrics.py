"""Performance metrics with statistical rigor (López de Prado school).

All trade-level metrics are computed in R-multiples (pnl / initial risk) so
results are comparable across assets and lot sizes.
"""

from __future__ import annotations

import math
from typing import Any, Dict, List, Sequence

import numpy as np
from scipy import stats

EULER_GAMMA = 0.5772156649015329


def summarize_trades(trades: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Core trade statistics from a list of engine trade dicts (need 'r')."""
    n = len(trades)
    if n == 0:
        return {"trades": 0, "win_rate": None, "expectancy_r": None,
                "profit_factor": None, "net_r": 0.0, "avg_win_r": None,
                "avg_loss_r": None, "max_drawdown_r": 0.0}
    r = np.array([t["r"] for t in trades], dtype=float)
    wins = r[r > 0]
    losses = r[r <= 0]
    gross_win = float(wins.sum()) if len(wins) else 0.0
    gross_loss = float(-losses.sum()) if len(losses) else 0.0
    equity = np.cumsum(r)
    peak = np.maximum.accumulate(np.concatenate([[0.0], equity]))[1:]
    dd = float(np.max(peak - equity)) if n else 0.0
    return {
        "trades": n,
        "win_rate": float(len(wins) / n),
        "expectancy_r": float(r.mean()),
        "profit_factor": (gross_win / gross_loss) if gross_loss > 0 else None,
        "net_r": float(r.sum()),
        "avg_win_r": float(wins.mean()) if len(wins) else None,
        "avg_loss_r": float(losses.mean()) if len(losses) else None,
        "max_drawdown_r": dd,
        "net_pnl_usd": float(sum(t.get("pnl_usd", 0.0) for t in trades)),
    }


def sharpe_ratio(returns: Sequence[float]) -> float | None:
    """Non-annualized Sharpe of a per-period return series (no rf)."""
    r = np.asarray(returns, dtype=float)
    if len(r) < 2 or r.std(ddof=1) == 0:
        return None
    return float(r.mean() / r.std(ddof=1))


def deflated_sharpe_ratio(
    returns: Sequence[float],
    n_trials: int,
    trial_sharpe_variance: float,
) -> Dict[str, Any]:
    """Bailey & López de Prado (2014) Deflated Sharpe Ratio.

    Returns the probability that the observed Sharpe exceeds the expected
    maximum Sharpe of `n_trials` independent zero-edge trials, after
    correcting for skew/kurtosis and sample length.

    `trial_sharpe_variance` = variance of Sharpe ratios across the trials
    that were tried (selection bias). If unknown, pass a conservative
    estimate (e.g. variance of walk-forward fold Sharpes).
    """
    r = np.asarray(returns, dtype=float)
    T = len(r)
    out: Dict[str, Any] = {"dsr": None, "sr_observed": None, "sr_threshold": None,
                           "n_trials": n_trials, "t": T}
    if T < 3 or n_trials < 1 or trial_sharpe_variance <= 0:
        return out
    sr = float(r.mean() / r.std(ddof=1))
    skew = float(stats.skew(r, bias=False))
    kurt = float(stats.kurtosis(r, fisher=False, bias=False))  # Pearson (3 = normal)
    z1 = stats.norm.ppf(1.0 - 1.0 / n_trials)
    z2 = stats.norm.ppf(1.0 - 1.0 / (n_trials * math.e))
    sr0 = math.sqrt(trial_sharpe_variance) * ((1.0 - EULER_GAMMA) * z1 + EULER_GAMMA * z2)
    denom = 1.0 - skew * sr + ((kurt - 1.0) / 4.0) * sr * sr
    if denom <= 0:
        return out
    dsr = float(stats.norm.cdf((sr - sr0) * math.sqrt(T - 1) / math.sqrt(denom)))
    out.update({"dsr": dsr, "sr_observed": sr, "sr_threshold": float(sr0),
                "skew": skew, "kurtosis": kurt})
    return out


def fold_sharpes(trades: List[Dict[str, Any]], n_folds: int,
                 fold_of_bar: Any) -> List[float | None]:
    """Per-fold Sharpe of trade R series; fold assigned by entry bar."""
    buckets: List[List[float]] = [[] for _ in range(n_folds)]
    for t in trades:
        k = fold_of_bar(t["entry_bar"])
        if k is not None and 0 <= k < n_folds:
            buckets[k].append(t["r"])
    return [sharpe_ratio(b) for b in buckets]