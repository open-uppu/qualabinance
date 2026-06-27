# 🎯 03 — Options Pricer

> **Black-Scholes + interactive UI for pricing European options.**

## 🎯 Purpose

Implement Black-Scholes-Merton from scratch + interactive web UI:
- Price European calls/puts
- Compute Greeks (delta, gamma, theta, vega, rho)
- Visualize payoff diagrams
- Implied volatility solver

## 📚 Knowledge dependencies

- [`../../knowledge/02-finance/derivatives-pricing.md`](../../knowledge/02-finance/derivatives-pricing.md) (pending)
- [`../../knowledge/05-resources/papers/_q1-portfolio-risk.md`](../../knowledge/05-resources/papers/_q1-portfolio-risk.md) — canonical Black-Scholes 1973

## 📁 Structure

```
03-options-pricer/
├── README.md
├── SPEC.md
├── src/
│   ├── black_scholes.py    # BS closed-form pricing
│   ├── greeks.py           # Analytical Greeks
│   ├── binomial.py         # CRR binomial tree
│   ├── monte_carlo.py      # MC pricing
│   ├── implied_vol.py      # IV solver (Newton-Raphson)
│   └── ui.py               # Streamlit / Dash app
└── tests/
```

## 🚀 Quick start

```bash
uv sync
uv run streamlit run src/ui.py
```

## 🎯 Features

- [ ] Black-Scholes European call/put
- [ ] All 5 Greeks
- [ ] Binomial tree (American approximation)
- [ ] Monte Carlo with variance reduction
- [ ] Implied vol solver
- [ ] Payoff diagram
- [ ] Volatility smile visualizer

## 📐 Formulae

```python
# Black-Scholes call
d1 = (log(S/K) + (r + σ²/2)T) / (σ√T)
d2 = d1 - σ√T
C  = S·N(d1) - K·e^(-rT)·N(d2)
```

## 📚 Resources

- Hull, *Options, Futures, and Other Derivatives*, Ch. 15-17
- QuantLib-Python for cross-validation
- ORATS for real IV data

---

*Status: 🟡 scaffold.*
