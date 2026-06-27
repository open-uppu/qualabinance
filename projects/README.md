# 🚀 Projects — Qualabinance

> **Eight implementation projects, ordered by dependency.**

Each project is **independent but builds on the knowledge layer** in [`../knowledge/`](../knowledge/). Start with #01 and work your way up — or jump around if you know what you want.

---

## 📊 Project overview

| # | Project | Purpose | Status | Difficulty |
|---|---|---|---|---|
| 01 | [foundations-notebooks](01-foundations-notebooks/) | Math + stats exercises in Jupyter | 🟡 scaffold | Beginner |
| 02 | [stock-analysis](02-stock-analysis/) | yfinance + MA + vol + dashboard | ⏳ pending | Beginner |
| 03 | [options-pricer](03-options-pricer/) | Black-Scholes + interactive UI | ⏳ pending | Intermediate |
| 04 | [backtest-engine](04-backtest-engine/) | Vectorized backtester with risk metrics | ⏳ pending | Intermediate |
| 05 | [garch-volatility](05-garch-volatility/) | GARCH volatility forecasting | ⏳ pending | Intermediate |
| 06 | [portfolio-optimizer](06-portfolio-optimizer/) | MVO + Black-Litterman + HRP | ⏳ pending | Intermediate |
| 07 | [hierarchical-data-pipeline](07-hierarchical-data-pipeline/) | L1-L5 data ingestion | ⏳ pending | Advanced |
| 08 | [multi-asset-platform](08-multi-asset-platform/) | Production multi-asset platform | ⏳ pending | Expert |

---

## 🎯 Recommended learning path

```
#01 Foundations  →  #02 Stock  →  #03 Options  →  #04 Backtest
                                                  ↓
#08 Platform  ←  #07 Data Pipeline  ←  #06 Portfolio
        ↑                                ↑
        └──── #05 GARCH (vol model) ────┘
```

- **Phase 1** (#01-#02): Build intuition with Jupyter + free data
- **Phase 2** (#03-#05): Pricing, backtest, volatility modeling
- **Phase 3** (#06-#07): Portfolio + data infrastructure
- **Phase 4** (#08): Production-ready multi-asset platform

---

## 📁 Common structure (each project)

```
projects/<name>/
├── README.md           ← what + why + how to run
├── SPEC.md             ← detailed spec (math, data, API)
├── notebooks/          ← exploratory work
├── src/                ← production code
├── tests/              ← unit + integration tests
├── data/               ← gitignored, local data
└── pyproject.toml      ← if standalone
```

---

## 🔗 Knowledge dependencies

Each project references the knowledge layer for theory:

| Project | References |
|---|---|
| #01 | `../knowledge/01-foundations/` |
| #02 | `../knowledge/01-foundations/`, `../knowledge/05-resources/data-providers/_with-papers.md` |
| #03 | `../knowledge/02-finance/derivatives-pricing.md`, `../knowledge/05-resources/papers/_q1-portfolio-risk.md` |
| #04 | `../knowledge/02-finance/portfolio-theory.md`, `../knowledge/05-resources/papers/_q1-portfolio-risk.md` |
| #05 | `../knowledge/02-finance/volatility-modeling.md`, `../knowledge/05-resources/papers/_q1-econometrics.md` |
| #06 | `../knowledge/02-finance/portfolio-theory.md` |
| #07 | `../knowledge/06-variable-framework/` |
| #08 | ALL of the above |

---

## 🚦 Status legend

- 🟡 scaffold — folder + README created, code pending
- 🔵 in-progress — being actively built
- ✅ done — tested + documented
- ⏸️ blocked — waiting on something
- ❌ deprecated — superseded

---

*See [`../state/loop-engineering/STATE.md`](../state/loop-engineering/STATE.md) for live progress.*
