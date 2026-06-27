# 📊 06 — Portfolio Optimizer

> **Markowitz + Black-Litterman + Hierarchical Risk Parity.**

## 🎯 Purpose

Build a portfolio optimization library with multiple methods:
- Mean-Variance (Markowitz 1952)
- Black-Litterman (1992) — Bayesian
- Hierarchical Risk Parity (López de Prado 2016)
- Risk Parity (equal risk contribution)
- Maximum Diversification

## 📚 Knowledge dependencies

- [`../../knowledge/02-finance/portfolio-theory.md`](../../knowledge/02-finance/portfolio-theory.md) (pending)
- [`../../knowledge/05-resources/papers/_q1-portfolio-risk.md`](../../knowledge/05-resources/papers/_q1-portfolio-risk.md) — Markowitz 1952, Sharpe 1964, Black-Litterman 1992, López de Prado 2016

## 📁 Structure

```
06-portfolio-optimizer/
├── README.md
├── SPEC.md
├── src/
│   ├── markowitz.py         # Classic MVO
│   ├── black_litterman.py   # Bayesian
│   ├── hrp.py               # Hierarchical Risk Parity
│   ├── risk_parity.py       # Equal risk contribution
│   ├── constraints.py       # Long-only, leverage cap, etc.
│   └── compare.py           # Compare methods
└── tests/
```

## 🚀 Quick start

```bash
uv sync
uv run python src/markowitz.py --tickers AAPL,MSFT,GOOG,SPY,BND
uv run python src/hrp.py --tickers <same>
uv run python src/compare.py
```

## 🎯 Features

- [ ] Markowitz with constraints
- [ ] Black-Litterman with views
- [ ] Hierarchical Risk Parity
- [ ] Risk Parity
- [ ] Compare out-of-sample Sharpe / max DD
- [ ] Riskfolio-Lib wrapper

## ⚠️ Common pitfalls

1. **Covariance estimation error** — sample cov is noisy
   - Solution: shrinkage (Ledoit-Wolf), exponential weighting
2. **Expected returns estimation** — even noisier than cov
   - Solution: Black-Litterman, shrinkage, equal-weight as baseline
3. **Concentration** — unconstrained MVO puts 90% in 1 asset
   - Solution: max position constraint, HRP

## 📚 Resources

- Meucci, *Risk and Asset Allocation*
- López de Prado, *Advances in Financial Machine Learning*, Ch. 16-17
- riskfolio-lib: https://github.com/dcajasn/Riskfolio-Lib

---

*Status: 🟡 scaffold.*
