# 📋 Knowledge Layer — Master Index

> **Every file in `../`, with status + quick summary.**

**Last updated**: 2026-06-28
**Total files**: 6 research files (~270 verified entries) + scaffold

---

## 🗂️ File tree with status

```
knowledge/
├── README.md                          ← overview + reading paths ✅
├── 00-INDEX.md                        ← this file ✅
│
├── 01-foundations/
│   ├── README.md                      ⏳ pending
│   ├── mathematics.md                 ⏳ pending (calculus, linalg, ODE/PDE)
│   ├── statistics.md                  ⏳ pending (probability, hypothesis, regression)
│   ├── time-series.md                 ⏳ pending (ARIMA, GARCH, stationarity)
│   └── programming.md                 ⏳ pending (Python, C++, SQL, Git, libs)
│
├── 02-finance/
│   ├── README.md                      ⏳ pending
│   ├── portfolio-theory.md            ⏳ pending (MVO, CAPM, BL, HRP)
│   ├── derivatives-pricing.md         ⏳ pending (Black-Scholes, MC)
│   ├── volatility-modeling.md         ⏳ pending (GARCH family, SV)
│   ├── risk-management.md             ⏳ pending (VaR, ES, stress)
│   └── markets/
│       ├── _global-markets.md         ⏳ pending (taxonomy)
│       └── README.md                  ⏳ pending
│
├── 03-career-paths/
│   ├── README.md                      ⏳ pending
│   ├── quant-researcher.md            ⏳ pending
│   ├── quant-trader.md                ⏳ pending
│   ├── quant-developer.md             ⏳ pending
│   └── risk-quant.md                  ⏳ pending
│
├── 04-mindset/
│   ├── README.md                      ⏳ pending
│   └── quant-mindset.md               ⏳ pending
│
├── 05-resources/                      ← ⭐ POPULATED
│   ├── papers/
│   │   ├── _q1-ml-finance.md          ✅ 30 papers (ML/AI for finance)
│   │   ├── _q1-portfolio-risk.md      ✅ 82 entries (Portfolio + Risk + Derivatives)
│   │   ├── _q1-econometrics.md        ✅ 35 papers (Time series + microstructure)
│   │   ├── _q1-2024-2026-frontier.md  ✅ 70+ papers (foundation models, agents, Polymarket, …) [NEW 2026-06-28]
│   │   └── _cross-link-map.md         ✅ 7 threads × canon→modern→frontier + reading paths [NEW 2026-06-28]
│   ├── github-projects/
│   │   ├── _github-with-papers.md     ✅ 40+ repos (FinRL, FinGPT, QuantLib, …)
│   │   └── _paper-with-code.md        ✅ paper-with-code index [NEW 2026-06-28]
│   ├── books/
│   │   └── _canonical.md              ✅ 34 books (Hull, Shreve, López de Prado, …)
│   ├── data-providers/
│   │   ├── _with-papers.md            ✅ 50+ providers (FRED, CRSP, Kaiko, …)
│   │   └── treemap-primary-mapping.md ✅ Treemap cells → primary API + reproducibility [NEW 2026-06-28]
│   └── _additional-sources.md         ✅ 150+ sources across 11 categories (newsletters, podcasts, central banks, …) [NEW 2026-06-28] 
│
└── 06-variable-framework/
    ├── README.md                      ⏳ pending
    ├── L1-global.md                   ⏳ pending (GDP, VIX, Fed rate, DXY)
    ├── L2-continental.md              ⏳ pending (MSCI regional, …)
    ├── L3-country.md                  ⏳ pending (CPI, GDP, policy rate, FX)
    ├── L4-market.md                   ⏳ pending (equity/bond/FX/comm/deriv/crypto)
    ├── L5-external.md                 ⏳ pending (geopolitical, climate, EPU)
    └── cross-cutting.md               ⏳ pending (PCA, stationarity, freq)
```

---

│   ├── huggingface-finance-catalog.md ✅ Live API: 68 finance models + 79 datasets [NEW 2026-06-28]
│   ├── kaggle-finance-catalog.md      ✅ Live API: 269 finance datasets [NEW 2026-06-28]
│   ├── arxiv-frontier-live.md         ✅ Live re-fetchable: 219 q-fin papers last 30 days [NEW 2026-06-28]
│   ├── openalex-cross-disciplinary.md ✅ Live re-fetchable: 96 papers cross-disciplinary (econ+CS+finance) [NEW 2026-06-28]
│   ├── _multi-source-catalog.md       ✅ NYT/FT/Reddit/Social/OpenAlex/CrossRef + charts [NEW 2026-06-28]
│   └── _additional-sources.md         ✅ 150+ sources across 11 categories (newsletters, podcasts, central banks, …) [NEW 2026-06-28]
│
├── 06-variable-framework/             ← ⭐ POPULATED (2 files: README + L1-L5 series codes)
├── scripts/                            ← 🆕 Maintenance scripts [NEW 2026-06-28]
│   ├── pull_arxiv.py                   Auto-refresh arXiv frontier
│   ├── pull_huggingface.py             Auto-refresh HF catalog
│   ├── pull_kaggle.py                  Auto-refresh Kaggle catalog
│   └── pull_openalex.py                Auto-refresh OpenAlex catalog
├── maintenance-loop.sh                 ← 🆕 Bash wrapper for scheduled refresh [NEW 2026-06-28]
├── LIBRARY.md                          ← 🆕 Single entry point [NEW 2026-06-28]
├── TOPIC-INDEX.md                      ← 🆕 Reverse lookup by query [NEW 2026-06-28]
└── QUICK-REFERENCE.md                  ← 🆕 10 quick-ref cards [NEW 2026-06-28]

## 📊 Population status

| Status | Count |
|---|---|
| ✅ Populated (verified content) | 16 |
| 🟡 Scaffold (placeholder + .gitkeep) | ~22 |
| ⏳ Pending | ~22 |
| **Total planned** | ~60 |

**Bootstrap completion**: 16/60 = **~27%** — knowledge skeleton + populated research layer + 2024-2026 frontier + cross-link map + 4 live API catalogs (HF/Kaggle/arXiv/OpenAlex) + auto-refresh scripts + library entry-point + topic index + quick-reference cards done, domain explanations pending.

---

## 🎯 Next 10 priorities (in order)

1. ⏳ `01-foundations/programming.md` — Python + libs catalog
2. ⏳ `01-foundations/statistics.md` — Probability + hypothesis testing
3. ⏳ `02-finance/markets/_global-markets.md` — Asset class taxonomy
4. ⏳ `02-finance/portfolio-theory.md` — MVO + CAPM + BL + HRP
5. ⏳ `02-finance/derivatives-pricing.md` — Black-Scholes + MC
6. ⏳ `06-variable-framework/README.md` — L1-L5 master
7. ⏳ `06-variable-framework/L4-market.md` — most important for trading
8. ⏳ `04-mindset/quant-mindset.md` — what makes a good quant
9. ⏳ `03-career-paths/quant-researcher.md` — role description
10. ⏳ `01-foundations/time-series.md` — ARIMA, GARCH, stationarity

---

## 🔗 Cross-links

- Top-level: [`../README.md`](../README.md)
- Company profile: [`../companies/qualabinance.md`](../companies/qualabinance.md)
- Agent spec: [`../agents/quant-researcher.md`](../agents/quant-researcher.md)
- Risk policy: [`../docs/risk-policy.md`](../docs/risk-policy.md)
- Compliance: [`../docs/compliance.md`](../docs/compliance.md)

---

*Maintained by: CEO-Profile loop · Bootstrap v0.1.0 · 2026-06-28*
