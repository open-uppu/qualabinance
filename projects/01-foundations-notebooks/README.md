# 📓 01 — Foundations Notebooks

> **Math, statistics, and programming exercises in Jupyter.**

## 🎯 Purpose

Build the bedrock skills for quantitative finance through hands-on notebooks:
- Calculus / linear algebra exercises
- Probability + statistics fundamentals
- Time series basics
- NumPy / pandas / matplotlib fluency

## 📚 Knowledge dependencies

- [`../../knowledge/01-foundations/`](../../knowledge/01-foundations/)

## 📁 Structure

```
01-foundations-notebooks/
├── README.md
├── notebooks/
│   ├── 01-calculus.ipynb
│   ├── 02-linear-algebra.ipynb
│   ├── 03-probability.ipynb
│   ├── 04-statistics.ipynb
│   ├── 05-time-series-basics.ipynb
│   ├── 06-numpy-fluency.ipynb
│   ├── 07-pandas-fluency.ipynb
│   └── 08-visualization.ipynb
└── tests/
```

## 🚀 Quick start

```bash
uv sync
uv run jupyter lab notebooks/
```

## 🎓 Topics covered

### Math
- Derivative / integral by hand + sympy
- Eigenvalues, SVD, PCA
- Optimization (gradient descent, Newton's method)

### Statistics
- Descriptive stats
- Hypothesis testing (t-test, F-test, χ²)
- Confidence intervals
- Bootstrap
- Multiple testing corrections

### Time series
- ARIMA basics
- Stationarity (ADF, KPSS)
- Autocorrelation (ACF, PACF)

### Programming
- NumPy vectorization
- pandas indexing / groupby / merge
- matplotlib / seaborn / plotly

## 🎯 Done when

- [ ] All notebooks run without errors
- [ ] Exercises completed
- [ ] Tests pass

---

*Status: 🟡 scaffold — notebooks pending.*
