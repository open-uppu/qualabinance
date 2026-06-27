# 📐 Foundations — Math, Stats, Programming

> **The bedrock of quantitative finance. Everything else builds on this.**

## 🎯 What you need to know

### 📐 Mathematics
- **Calculus**: Derivatives, integrals, multivariable, optimization
- **Linear algebra**: Matrices, eigenvalues, SVD, PCA
- **ODE/PDE**: Stochastic calculus (Itô's lemma, SDEs)
- **Probability**: Distributions, expectation, conditional expectation
- **Statistics**: Estimation, hypothesis testing, regression
- **Time series**: Stationarity, ARIMA, GARCH, cointegration

### 📊 Statistics
- Descriptive vs inferential
- Frequentist vs Bayesian
- Hypothesis testing (t-test, F-test, chi-square)
- Multiple testing corrections (Bonferroni, BHY)
- Confidence intervals, p-values
- Bootstrap, Monte Carlo

### 💻 Programming
- **Python** (primary): numpy, pandas, scipy, scikit-learn, statsmodels, arch
- **SQL**: PostgreSQL, TimescaleDB (for tick data)
- **C++/Rust**: For HFT / latency-critical paths
- **Git**: Branching, PRs, CI/CD
- **Data structures + algorithms**: Big-O, hash tables, trees

---

## 📚 Recommended resources

### Books
- See [`../05-resources/books/_canonical.md`](../05-resources/books/_canonical.md) → Phase 1 (Math Foundations)
  - Hamilton — Time Series Analysis
  - Williams — Probability with Martingales
  - Shreve — Stochastic Calculus for Finance I & II
  - Björk — Arbitrage Theory in Continuous Time

### Courses
- Coursera: "Financial Engineering" (Columbia)
- MIT OCW: 18.404J (Topics in Theoretical CS / Math)
- QuantStart: https://www.quantstart.com/

### Papers
- See [`../05-resources/papers/_q1-econometrics.md`](../05-resources/papers/_q1-econometrics.md) for foundational econometrics papers

---

## 🧰 Tooling

### Python ecosystem
```python
# Core
import numpy as np
import pandas as pd
import scipy

# Stats
import statsmodels.api as sm
from arch import arch_model           # GARCH
import pmdarima as pmd              # ARIMA auto

# ML
import sklearn
import torch
import lightgbm as lgb

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
```

### Setup
```bash
# Using uv (recommended)
uv sync

# Activate venv
source .venv/bin/activate

# Start Jupyter
uv run jupyter lab
```

---

## 🎓 Beginner checklist

- [ ] Derivative of `f(x) = e^x * sin(x)` by hand
- [ ] Compute eigenvalues of 3x3 matrix
- [ ] Solve simple SDE: `dS = μS dt + σS dW`
- [ ] Fit ARIMA(1,1,1) to a stock return series
- [ ] Fit GARCH(1,1) to a volatility series
- [ ] Compute VaR of a portfolio (parametric + MC)
- [ ] Backtest a moving-average strategy without look-ahead bias
- [ ] Read 5 papers from `../05-resources/papers/`

---

*Status: 🟡 scaffold — detailed content pending.*
