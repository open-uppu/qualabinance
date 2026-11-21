"""Unit tests for the rigorous engine + metrics + purged CV."""

import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.engine import EngineConfig, RigorousEngine
from src.metrics import deflated_sharpe_ratio, summarize_trades
from src.purged_cv import purged_kfold_indices, walk_forward_folds


def make_df(rows):
    return pd.DataFrame(rows, columns=["timestamp", "open", "high", "low", "close", "volume"])


def flat_df(n=60, price=100.0):
    ts = pd.date_range("2026-01-01", periods=n, freq="5min")
    return make_df([[t, price, price + 0.5, price - 0.5, price, 1] for t in ts])


def always_buy(window, idx):
    c = float(window["close"].iloc[-1])
    return {"action": "BUY", "sl": c - 2.0, "tp": c + 4.0, "reason": "test"}


class TestEngine:
    def test_sl_before_tp_when_both_hit(self):
        # bar 30 touches both SL and TP -> pessimistic engine must take SL
        df = flat_df(60)
        df.loc[30, "high"] = 200.0
        df.loc[30, "low"] = 50.0
        cfg = EngineConfig(spread=0.0, min_sl_dist=0.5, cooldown_bars=1000)
        res = RigorousEngine(cfg).run(df, always_buy, warmup_bars=29, trade_end=31)
        assert len(res["trades"]) == 1
        assert res["trades"][0]["exit_reason"] == "SL_HIT"
        assert res["trades"][0]["r"] < 0

    def test_spread_charged_both_sides(self):
        # TP hit: gross move = 4.0, spread 0.2 -> net R = (4 - 0.2) / (2 + 0.1)
        df = flat_df(60)
        df.loc[31, "high"] = 104.5  # entry at bar30 open=100+0.1, tp=102 (signal close 100 -? )
        cfg = EngineConfig(spread=0.2, min_sl_dist=0.5, cooldown_bars=1000)
        res = RigorousEngine(cfg).run(df, always_buy, warmup_bars=29, trade_end=32)
        t = res["trades"][0]
        # signal at bar29 close=100 -> sl=98, tp=104; entry bar30 open 100+0.1=100.1
        assert t["entry_fill"] == pytest.approx(100.1)
        assert t["exit_reason"] == "TP_HIT"
        assert t["exit_fill"] == pytest.approx(104.0 - 0.1)
        expected_r = (103.9 - 100.1) / (100.1 - 98.0)
        assert t["r"] == pytest.approx(expected_r)

    def test_entry_at_next_bar_open_not_signal_close(self):
        df = flat_df(60)
        df.loc[30, "open"] = 101.0  # gap up after signal bar29 close=100
        cfg = EngineConfig(spread=0.0, min_sl_dist=0.5, cooldown_bars=1000)
        res = RigorousEngine(cfg).run(df, always_buy, warmup_bars=29, trade_end=31)
        assert res["trades"][0]["entry_fill"] == pytest.approx(101.0)

    def test_no_lookahead_signal_window(self):
        seen = []

        def spy(window, idx):
            seen.append(len(window))
            return {"action": "HOLD"}

        df = flat_df(50)
        RigorousEngine(EngineConfig()).run(df, spy, warmup_bars=30)
        assert seen == list(range(31, 50))  # window ends at current bar, never future

    def test_min_sl_rejection(self):
        def tight(window, idx):
            c = float(window["close"].iloc[-1])
            return {"action": "BUY", "sl": c - 0.1, "tp": c + 0.2, "reason": "tight"}

        cfg = EngineConfig(min_sl_dist=1.0)
        res = RigorousEngine(cfg).run(flat_df(60), tight, warmup_bars=30)
        assert res["trades"] == []
        assert res["rejected_min_sl"] > 0


class TestMetrics:
    def test_summarize_basic(self):
        trades = [{"r": 2.0, "pnl_usd": 20}, {"r": -1.0, "pnl_usd": -10}, {"r": -1.0, "pnl_usd": -10}]
        s = summarize_trades(trades)
        assert s["trades"] == 3
        assert s["win_rate"] == pytest.approx(1 / 3)
        assert s["expectancy_r"] == pytest.approx(0.0)
        assert s["profit_factor"] == pytest.approx(1.0)
        assert s["max_drawdown_r"] == pytest.approx(2.0)

    def test_dsr_zero_edge_near_half_or_below(self):
        rng = np.random.default_rng(7)
        r = rng.normal(0.0, 1.0, 500)
        out = deflated_sharpe_ratio(r, n_trials=10, trial_sharpe_variance=0.02)
        assert out["dsr"] is not None and out["dsr"] < 0.9

    def test_dsr_strong_edge_high(self):
        rng = np.random.default_rng(7)
        r = rng.normal(0.3, 1.0, 500)
        out = deflated_sharpe_ratio(r, n_trials=2, trial_sharpe_variance=0.001)
        assert out["dsr"] > 0.95

    def test_dsr_more_trials_lower(self):
        rng = np.random.default_rng(7)
        r = rng.normal(0.1, 1.0, 300)
        d1 = deflated_sharpe_ratio(r, 2, 0.01)["dsr"]
        d2 = deflated_sharpe_ratio(r, 100, 0.01)["dsr"]
        assert d2 < d1


class TestPurgedCV:
    def test_walk_forward_contiguous_cover(self):
        folds = walk_forward_folds(1000, 4, 250)
        assert folds[0][0] == 250 and folds[-1][1] == 1000
        for a, b in zip(folds, folds[1:]):
            assert a[1] == b[0]

    def test_purged_kfold_no_overlap(self):
        for train, test in purged_kfold_indices(100, 5, purge_bars=5, embargo_bars=2):
            assert len(np.intersect1d(train, test)) == 0
            # purge: no train sample within 5 bars before test start
            assert not np.any((train >= test.min() - 5) & (train < test.min()))