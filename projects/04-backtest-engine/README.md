# 🧪 04 — Backtest Engine

> **Vectorized backtester with proper statistical rigor.**

## 🎯 Purpose

Build a proper backtest framework that avoids the classic pitfalls:
- Look-ahead bias (use purged CV)
- Selection bias (use deflated Sharpe ratio)
- Overfitting (limit strategy complexity)
- Survivorship bias (include delisted stocks)

## 📚 Knowledge dependencies

- [`../../knowledge/02-finance/portfolio-theory.md`](../../knowledge/02-finance/portfolio-theory.md) (pending)
- [`../../knowledge/05-resources/papers/_q1-portfolio-risk.md`](../../knowledge/05-resources/papers/_q1-portfolio-risk.md) — Bailey-López de Prado deflated Sharpe

## 📁 Structure

```
04-backtest-engine/
├── README.md
├── SPEC.md
├── src/
│   ├── engine.py           # Main backtest loop
│   ├── strategies/         # Mean-reversion, momentum, etc.
│   ├── metrics.py          # Sharpe, Sortino, max DD, deflated Sharpe
│   ├── purged_cv.py        # Purged k-fold CV (López de Prado)
│   └── reports.py          # QuantStats integration
└── tests/
```

## 🚀 Quick start

```bash
uv sync
uv run python -m src.engine --strategy momentum --symbol BTC-USD --period 2y
```

## 🎯 Features

- [ ] Vectorized event-driven backtest
- [ ] Slippage + commission model
- [ ] Sharpe / Sortino / Calmar
- [ ] Max drawdown + underwater curve
- [ ] Deflated Sharpe ratio (Bailey-López de Prado)
- [ ] Purged k-fold CV
- [ ] Combinatorial purged CV (CPCV)
- [ ] QuantStats HTML report

## ⚠️ Methodology (CRITICAL)

1. **Never** use future data in features (forward-looking bias)
2. **Always** include transaction costs
3. **Always** compute deflated Sharpe (multiple-testing correction)
4. **Always** walk-forward validate, don't just train/test split
5. **Always** question results — if Sharpe > 2, you almost certainly have a bug

## 📚 Resources

- vectorbt (existing framework to learn from)
- López de Prado, *Advances in Financial Machine Learning*, Ch. 11-12
- QuantStats for reports

---

*Status: 🟡 scaffold.*
