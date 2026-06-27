# 📚 Knowledge Layer — Qualabinance

> **Curated research base for the Qualabinance quant platform.**

This folder contains **hand-curated, source-verified research** that informs every project in `../projects/`. Treat it as the **ground truth** for:
- What Q1 / accepted papers say about a topic
- Which GitHub repos implement those papers
- Which canonical textbooks cover the math
- Which data providers have published methodology
- How the hierarchical L1-L5 variable framework works

---

## 🗂️ Index

### 📌 Top-level entry points

- 📋 **[`00-INDEX.md`](00-INDEX.md)** — Master index (every file linked + status)
- 🎯 **[`../README.md`](../README.md)** — Project overview

### 📖 Domain folders

| # | Folder | Purpose | Status |
|---|---|---|---|
| 1 | [`01-foundations/`](01-foundations/) | Math + stats + programming foundations | 🟡 scaffold |
| 2 | [`02-finance/`](02-finance/) | Portfolio + derivatives + vol + risk + markets | 🟡 scaffold |
| 3 | [`03-career-paths/`](03-career-paths/) | QR / QT / QD / Risk Quant roles | ⏳ pending |
| 4 | [`04-mindset/`](04-mindset/) | Quant mindset (skepticism, prob thinking, comms) | ⏳ pending |
| 5 | [`05-resources/`](05-resources/) | Papers, repos, books, data providers | ✅ populated |
| 6 | [`06-variable-framework/`](06-variable-framework/) | L1-L5 hierarchical variables | 🟡 scaffold |

---

## 🎓 Reading paths

### Path A — "Become a Quant Researcher"
1. `01-foundations/` (math + stats + programming)
2. `02-finance/portfolio/` + `02-finance/risk/`
3. `05-resources/papers/_q1-portfolio-risk.md` (foundational)
4. `05-resources/papers/_q1-ml-finance.md` (modern)
5. `05-resources/books/_canonical.md` → Phase 1-3
6. `06-variable-framework/` (master the L1-L5 data pipeline)

### Path B — "Become a Quant Developer"
1. `01-foundations/programming.md`
2. `02-finance/markets/_global-markets.md`
3. `05-resources/github-projects/_github-with-papers.md` (what to build on)
4. `05-resources/data-providers/_with-papers.md` (data plumbing)
5. `05-resources/papers/_q1-portfolio-risk.md` (Black-Scholes, GARCH)
6. `../projects/04-backtest-engine/` (build something real)

### Path C — "Become a Quant Trader"
1. `02-finance/markets/_global-markets.md` (what you can trade)
2. `02-finance/derivatives/` + `volatility/`
3. `05-resources/papers/_q1-econometrics.md` (microstructure)
4. `05-resources/books/_canonical.md` → Hull + Natenberg + Kaufman
5. `04-mindset/` (probabilistic thinking, risk first)
6. `../projects/04-backtest-engine/` (validate before deploying)

---

## 📊 Curated content (current state)

| Resource | Count | File |
|---|---|---|
| Q1 / accepted papers (ML/AI) | 30 | [`05-resources/papers/_q1-ml-finance.md`](05-resources/papers/_q1-ml-finance.md) |
| Q1 / accepted papers (Portfolio/Risk/Derivatives) | 82 | [`05-resources/papers/_q1-portfolio-risk.md`](05-resources/papers/_q1-portfolio-risk.md) |
| Q1 / accepted papers (Econometrics/Microstructure) | 35 | [`05-resources/papers/_q1-econometrics.md`](05-resources/papers/_q1-econometrics.md) |
| GitHub repos with companion papers | 40+ | [`05-resources/github-projects/_github-with-papers.md`](05-resources/github-projects/_github-with-papers.md) |
| Canonical textbooks | 34 | [`05-resources/books/_canonical.md`](05-resources/books/_canonical.md) |
| Data providers with methodology papers | 50+ | [`05-resources/data-providers/_with-papers.md`](05-resources/data-providers/_with-papers.md) |

**Total**: ~270 verified entries

---

## 🔄 Maintenance

When new research is added:
1. Use the same naming convention: `_q1-<topic>.md` or `<topic>.md`
2. Add entry to `00-INDEX.md`
3. Update count table above
4. Update reading path if major addition
5. Reference it from relevant project SPEC.md

---

*Last updated: 2026-06-28 — knowledge layer bootstrap.*
