# 📈 05 — GARCH Volatility

> **GARCH-family volatility forecasting + comparison with realized vol.**

## 🎯 Purpose

Build and compare volatility models:
- GARCH(1,1) — baseline
- EGARCH — leverage effect
- GJR-GARCH — asymmetry
- DCC-GARCH — multivariate
- Compare with realized volatility (RV)
- ML extensions (LSTM-Vol)

## 📚 Knowledge dependencies

- [`../../knowledge/02-finance/volatility-modeling.md`](../../knowledge/02-finance/volatility-modeling.md) (pending)
- [`../../knowledge/05-resources/papers/_q1-econometrics.md`](../../knowledge/05-resources/papers/_q1-econometrics.md) — Bollerslev 1986, Nelson 1991, GJR 1993

## 📁 Structure

```
05-garch-volatility/
├── README.md
├── SPEC.md
├── src/
│   ├── garch_baseline.py    # arch library GARCH(1,1)
│   ├── egarch.py            # Nelson E-GARCH
│   ├── gjr.py               # GJR-GARCH
│   ├── dcc.py               # DCC multivariate
│   ├── realized_vol.py      # Andersen-Bollerslev RV
│   ├── ml_vol.py            # LSTM-Vol, NNET-Vol
│   └── compare.py           # Out-of-sample comparison
└── tests/
```

## 🚀 Quick start

```bash
uv sync
uv run python src/garch_baseline.py --symbol BTC-USD --period 2y
uv run python src/compare.py
```

## 🎯 Features

- [ ] Fit GARCH(1,1) on returns
- [ ] Fit EGARCH(1,1) (leverage)
- [ ] Fit GJR-GARCH(1,1) (asymmetry)
- [ ] Compute realized vol (5-min RV)
- [ ] Out-of-sample vol forecast
- [ ] ML comparison (LSTM-Vol)
- [ ] Diebold-Mariano test (which model wins?)

## 📐 GARCH(1,1) recap

```
σ²_t = ω + α·r²_{t-1} + β·σ²_{t-1}
```

## 📚 Resources

- Bollerslev (1986) — original GARCH
- arch library: https://pypi.org/project/arch/
- Andersen & Bollerslev (1998) — realized volatility

---

*Status: 🟡 scaffold.*
