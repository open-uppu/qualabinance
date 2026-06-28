# 🏛️ Qualabinance Knowledge Library

> **Single entry point** — find any topic in ≤ 2 clicks from here.
>
> **Mode:** 🔄 **CONTINUOUS RESEARCH** (active librarian) — pull new papers / models / datasets / sources continuously, organize into library, commit regularly. Never stop.
>
> **Built:** 2026-06-28 · **Coverage:** 22 files / 13 populated · ~8,900 lines · 200+ papers, 50+ books, 40+ repos, 150+ sources

---

## 🚀 I want to find… (jump table)

| Looking for… | Go to |
|---|---|
| 📄 **A specific paper** | [§3 Paper index](#3-papers-220--entries) |
| 📚 **A book / textbook** | [§4 Book index](#4-books-34-entries) |
| 💻 **A GitHub repo** | [§5 Repo index](#5-github-repos-40--entries) |
| 🤗 **A HuggingFace model** | [§6 HF models](#6-huggingface-models-15--live) |
| 📊 **A Kaggle dataset** | [§7 Kaggle datasets](#7-kaggle-datasets-20--live) |
| 📦 **A data provider / API** | [§8 Data providers](#8-data-providers--apis-50--live) |
| 📰 **A news / podcast / blog source** | [§9 Additional sources](#9-additional-sources-300--curated) |
| 📈 **Series code to pull a macro variable** | [§10 Series codes](#10-series-codes-l1-l5-32-live) |
| 🔗 **How papers connect** | [§11 Cross-link map](#11-cross-link-map-7-threads) |
| 🆕 **Latest 30-day frontier papers** | [§12 Live arXiv](#12-live-arxiv-frontier-re-fetchable) |
| 🏗️ **Foundations of quant** | [§13 Topic foundations](#13-topic-foundations-scaffold) |

---

## 📂 1. Folder structure (current)

```
knowledge/
├── LIBRARY.md                         ← 🆕 you are here (single entry point)
├── README.md                          ← overview
├── 00-INDEX.md                        ← file-tree with status
│
├── 01-foundations/                    ← scaffold (placeholder for math/stats/programming/time-series)
├── 02-finance/                        ← scaffold (portfolio / derivatives / vol / risk)
│   └── markets/_global-markets.md     ← asset class taxonomy (populated)
│
├── 05-resources/                      ← ⭐ POPULATED (13 files)
│   ├── papers/                        ← 5 files (4 curated lists + 1 cross-link map)
│   ├── github-projects/               ← 2 files (40+ repos + paper-with-code index)
│   ├── books/                         ← 1 file (34 textbooks, 4 phases)
│   ├── data-providers/                ← 2 files (50+ providers + treemap mapping)
│   ├── huggingface-finance-catalog.md ← HF live API (15+ models, 20+ datasets)
│   ├── kaggle-finance-catalog.md      ← Kaggle live API (20+ datasets)
│   ├── arxiv-frontier-live.md         ← arXiv live (31 papers last 30 days)
│   ├── _multi-source-catalog.md       ← NYT/Reddit/OpenAlex/CrossRef + charts
│   └── _additional-sources.md         ← 150+ newsletters/podcasts/CBs/competitions
│
└── 06-variable-framework/             ← ⭐ POPULATED (2 files: README + L1-L5 series codes)
```

---

## 2. Topic heat-map

```
📈 ASSET CLASSES ──────────────────────────────────────────────────────────
   Equities (US/TH/EU/CN/JP/HK)        → 02-finance/markets/_global-markets.md
   ETFs                                → 02-finance/markets/_global-markets.md
   Bonds / Fixed income                → 02-finance/markets/_global-markets.md + _with-papers.md
   FX                                  → 02-finance/markets/_global-markets.md
   Commodities                         → 02-finance/markets/_global-markets.md
   Crypto (spot + perp)                → 02-finance/markets/_global-markets.md + _multi-source-catalog.md
   Options / Derivatives               → 02-finance/markets/_global-markets.md
   Prediction markets (Polymarket)     → papers/_q1-2024-2026-frontier.md (C-section)
   Tokenized RWAs                      → papers/_q1-2024-2026-frontier.md (C13)

📊 METHODOLOGY ────────────────────────────────────────────────────────────
   Portfolio theory                    → papers/_q1-portfolio-risk.md (Markowitz/CAPM/FF/...)
   Asset pricing                       → papers/_q1-portfolio-risk.md + papers/_q1-2024-2026-frontier.md (A-section)
   Derivatives pricing                 → papers/_q1-portfolio-risk.md (BSM/Heston/Vašíček)
   Volatility modeling (GARCH family)  → papers/_q1-econometrics.md (GARCH sec)
   Stochastic vol                      → papers/_q1-econometrics.md (SV sec) + A4 (Bergomi 2026)
   Realized volatility                 → papers/_q1-econometrics.md (RV sec) + F3 (TimesFM 2025)
   Risk (VaR / ES / coherent)          → papers/_q1-portfolio-risk.md (Artzner/Rockafellar)
   Backtest methodology / debiasing    → papers/_cross-link-map.md ⚠️ + B1 (Spurious 2026)

🧠 ML / AI ────────────────────────────────────────────────────────────────
   Time-series DL (LSTM/Transformer)   → papers/_q1-ml-finance.md (sec 2) + T-series in frontier
   Foundation models (Kronos/Chronos)  → papers/_q1-2024-2026-frontier.md (F-section) ⭐ HOT 2025-2026
   Reinforcement learning              → papers/_q1-ml-finance.md (sec 3) + R-series in frontier
   LLM in finance                      → papers/_q1-ml-finance.md (sec 4) + L-series in frontier
   FinBERT / FinGPT / BloombergGPT     → papers/_q1-ml-finance.md (#19-22)
   Time-aware debiasing                → L7 (DatedGPT 2026) ⭐ CRITICAL

📡 MICROSTRUCTURE ──────────────────────────────────────────────────────────
   Market impact (square-root law)     → papers/_q1-econometrics.md (Microstructure sec) + M2 (2026)
   Optimal execution (Almgren-Chriss)  → papers/_q1-econometrics.md (Execution sec) + R2 (TT-DAC-PS)
   Limit order book modeling           → papers/_q1-econometrics.md (LOB sec) + M1 (Inference-Compute 2026)
   On-chain microstructure             → C-series in frontier + BlockDB HuggingFace
   DEX microstructure (Hyperliquid)    → M6 (2026) in frontier

🌍 MACRO / VARIABLE FRAMEWORK ──────────────────────────────────────────────
   L1 Global macro/financial/risk      → 06-variable-framework/L1-L5-series-codes.md
   L2 Continental                      → L1-L5-series-codes.md + yfinance tickers
   L3 Country (TH focus)               → L1-L5-series-codes.md (Thailand table) + treemap-primary-mapping.md
   L4 Per-instrument                   → L1-L5-series-codes.md + project-07 pipeline (32 series live)
   L5 Exogenous (GPR/EPU/GSCPI)        → L1-L5-series-codes.md + treemap mapping
   Macro-aware DL (HANET)              → T1 (2026) in frontier ⭐ NEW 2026

🛠️ INFRASTRUCTURE ─────────────────────────────────────────────────────────
   Backtest engines                    → github-projects/_github-with-papers.md (OpenBB/Lean/Zipline/...)
   ML quant platforms (Qlib/FinRL)     → github-projects + _paper-with-code.md
   Live data APIs (free + paid)        → data-providers/_with-papers.md + treemap-primary-mapping.md
   Project 07 pipeline (Qualabinance)  → projects/07-hierarchical-data-pipeline/ (32 series, 11 tests pass)
   Cron / refresh scripts              → arxiv-frontier-live.md + multi-source-catalog.md

🎓 LEARNING PATHS ─────────────────────────────────────────────────────────
   Quant Researcher path               → papers/_cross-link-map.md (Path A)
   Quant Developer path                → books/_canonical.md (Phase 3) + github-projects
   Quant Trader path                   → books/_canonical.md (Phase 4) + _additional-sources.md
   Risk Quant path                     → papers/_q1-portfolio-risk.md (C10-C11) + BIS Quarterly
   Crypto Quant path                   → papers/_q1-2024-2026-frontier.md (C-section) + multi-source
   Thailand-specific path              → L1-L5-series-codes.md (TH table) + BOT API + ThaiBMA + SETSMART
   LLM-in-trading path                 → papers/_cross-link-map.md (Path D)
```

---

## 3. Papers (220+ entries)

### Curated static lists
| File | Count | Coverage |
|---|---|---|
| `_q1-portfolio-risk.md` | 82 | Markowitz → CAPM → Fama-French → BSM → GARCH → Artzner → LdP |
| `_q1-2024-2026-frontier.md` | 70+ | Kronos / Chronos / FinRL-X / DatedGPT / HANET / Polymarket |
| `_q1-econometrics.md` | 35 | GARCH family / SV / RV / microstructure / cointegration / heavy tails |
| `_q1-ml-finance.md` | 30 | LSTM / Transformer / RL / FinBERT / FinGPT / DeepLOB |

### Live re-fetchable
| File | Cadence | Notes |
|---|---|---|
| `arxiv-frontier-live.md` | weekly | 31 papers last 30 days, Python cron script included |

### Cross-cutting
| File | Purpose |
|---|---|
| `_cross-link-map.md` | How papers connect — 7 threads × canon→modern→frontier + 4 reading paths |

### Search hints
- "predictability / factor zoo / spurious" → `_cross-link-map.md` ⚠️ section + B1 (2026)
- "Polymarket / Hyperliquid / DEX" → frontier C-section + M6
- "GARCH / SV / Bergomi" → econometrics GARCH-section + frontier V1-V9
- "transformer / LSTM / TSFM" → ml-finance sec 2 + frontier F1-F4
- "RL / FinRL / execution" → ml-finance sec 3 + frontier R1-R7
- "LLM / FinBERT / DatedGPT" → ml-finance sec 4 + frontier L1-L10

---

## 4. Books (34 entries)

**File:** `05-resources/books/_canonical.md`

- **Phase 1 (Math foundations):** Strang (Lin Alg), Ross (Probability), Shreve (Stochastic Calc)
- **Phase 2 (Finance core):** Hull (Options/Futures), Bodie-Kane-Marcus (Investments)
- **Phase 3 (Quant methods):** López de Prado (*Advances in Financial ML*), Chan (Algo Trading)
- **Phase 4 (Specialization):** Wilmott, Gatheral (Vol surface), Andersen (Realized Vol)

Each book has: ISBN-13 (verified), edition, difficulty tag (U/G/P/R), reading time, companion code (if any), seminal papers cited.

---

## 5. GitHub repos (40+ entries)

**Files:**
- `github-projects/_github-with-papers.md` — 40+ repos, sorted by category + stars
- `github-projects/_paper-with-code.md` — paper-with-code index

**Top picks by category:**

| Category | Top repo | Stars |
|---|---|---|
| Unified data terminal | OpenBB / OpenBBTerminal | ~70k |
| Multi-asset algo engine | QuantConnect Lean | ~20k |
| Classic backtester | Zipline | ~20k |
| RL for trading | FinRL | (active) |
| Portfolio optimization | riskfolio-lib | (active) |
| AI quant platform | Qlib (Microsoft) | (active) |
| Derivatives pricing | QuantLib | (active) |
| Market simulator | ABIDES | (active) |
| Crypto framework | Freqtrade | (active) |
| Financial LLM | FinGPT / BloombergGPT | (active) |

---

## 6. HuggingFace models (15+ live)

**File:** `05-resources/huggingface-finance-catalog.md`

| Tier | Model |
|---|---|
| **🏆 Most downloaded** | `nickmuchi/finbert-tone-finetuned-finance-topic-classification` (65,889 dl) |
| **Best FinLLM (small)** | `DragonLLM/Llama-Open-Finance-8B` (2,038 dl, Llama-3.1 base) |
| **Best FinLLM (reasoning)** | `mradermacher/DeepSeek-R1-Finance-Reasoning-14B-GGUF` |
| **Best RL agent** | `Adilbai/stock-trading-rl-agent` (159 likes) |
| **Best LoRA** | `mrzlab630/lora-alpaca-trading-candles` |

Re-fetch: `curl -sL "https://huggingface.co/api/models?search=finance&limit=50" | jq '.[].id'`

---

## 7. Kaggle datasets (20+ live)

**File:** `05-resources/kaggle-finance-catalog.md`

| Tier | Dataset | Size |
|---|---|---|
| **🏆 Bulk US equities** | `9000+ Tickers of Stock Market Data (Full History)` | 1.9 GB |
| **🏆 Crypto sentiment** | `Bitcoin tweets - 16M tweets` | 1.7 GB |
| **Multi-index daily** | `World Stock Prices (Daily Updating)` | 12 MB |
| **Long-history benchmark** | `S&P 500 Daily Prices 1986-2018` | 41 KB |
| **Sentiment + market aligned** | `Financial News Sentiment vs Market 2020 - Present` | 1 MB |
| **Commodity futures** | `NYMEX Crude Oil Futures Dataset (CL Contract)` | 1.1 MB |
| **Chinese A-share** | `qinchen1986/a_stock_kline_mainboard_next_return_2025` (HF) | — |

---

## 8. Data providers / APIs (50+ live)

**Files:**
- `05-resources/data-providers/_with-papers.md` — 50+ providers + methodology papers
- `05-resources/data-providers/treemap-primary-mapping.md` — Treemap cells → primary API + reproducibility

**By asset class:**

| Asset class | Free API | Paid API | Notes |
|---|---|---|---|
| Macro (US) | FRED (free) | — | 11 series in project-07 |
| Macro (Global) | World Bank + IMF (free) | BIS ($3k/yr) | 4 series in project-07 |
| Equity (US) | yfinance (free) | Polygon ($29/mo), CRSP (academic) | 10 tickers in project-07 |
| Equity (Thailand) | yfinance `^SET.BK` (free, delayed) | SETSMART (paid) | 1 ticker in project-07 |
| Bonds (US) | FRED yields (free) | ICE BofA (paid) | Daily OAS via FRED |
| FX | FRED (free, daily) | Dukascopy (free, tick) | 6 pairs in project-07 |
| Commodity | FRED WTI/Gold (free) | EIA (free), Kaiko | 2 in project-07 |
| Crypto | Binance + CoinGecko + ccxt (free) | Glassnode ($29/mo), Kaiko | 1 in project-07 |
| Alt data | GPR/EPU/GSCPI CSV (free) | GDELT, RavenPack | Manual CSV drop in project-07 |

---

## 9. Additional sources (300+ curated)

**File:** `05-resources/_additional-sources.md`

**Live API catalogs:**
- `huggingface-finance-catalog.md` (HF live)
- `kaggle-finance-catalog.md` (Kaggle live)
- `arxiv-frontier-live.md` (arXiv live)
- `_multi-source-catalog.md` (NYT/Reddit/OpenAlex/CrossRef/social/streaming/charts)

**Curated catalogs (need keys or subscription):**
- Newsletters (15): Quantocracy, AQR Insights, Robeco Quant, Man Institute, …
- Podcasts (10): Top Traders Unplugged, Flirting with Models, Odd Lots, …
- YouTube (15): MIT OCW, Simons, 3Blue1Brown, Sentdex, …
- Communities (14): r/quant, r/algotrading, Wilmot, Discord servers, …
- Central banks (18): FRED, ECB, BIS, BOT, EDGAR, CFTC COT, SET, …
- Industry reports (22): GS, JPM, MS, DB, Citi GPS, BlackRock, Bridgewater, …
- Competitions (15): Numerai, WorldQuant BRAIN, Jane Street, Optiver, …
- Tools/SaaS (35): OpenBB, QuantConnect, FinRL-X, Vectorbt, Glassnode, …
- Pre-print servers (12): arXiv, SSRN, RePEc, NBER, OpenReview, …
- University courses (25): MIT 18.404, Stanford ICME, Oxford, Cambridge, CQF, EPAT, …

---

## 10. Series codes L1-L5 (32 live)

**File:** `06-variable-framework/L1-L5-series-codes.md`

| Level | Count | Top series |
|---|---|---|
| L1 Global | 9 | FEDFUNDS, DTWEXBGS, VIXCLS, T10Y2Y, BAMLH0A0HYM2, DCOILWTICO, LBMA/GOLD_USD_PM |
| L2 Continental | 6 | ^GSPC, ^IXIC, ^N225, ^STOXX, EEM, ^SET.BK |
| L3 Country (TH focus) | 8 | wb_th_gdp, wb_th_cpi, fred_thb_usd, BOT_RATE (manual) |
| L4 Per-instrument | 5 | AAPL, MSFT, BTC-USD, ETH-USD, BTC/USDT (Binance) |
| L5 External | 3+1 | GPR, EPU, GSCPI (manual CSV), Fear & Greed (API) |

**All wired in project-07 pipeline** — pullable via `make refresh` (with API keys in `.env`).

---

## 11. Cross-link map (7 threads)

**File:** `05-resources/papers/_cross-link-map.md`

| Thread | Path |
|---|---|
| ① Portfolio / Asset pricing | Markowitz → CAPM → Fama-French → G-K-X → Neural factors |
| ② Derivatives / Vol | BSM → GARCH → SV → Rough Bergomi → Foundation-model vol |
| ③ Time-series ML | LSTM → Transformer → TSFM → Kronos |
| ④ RL trading | Almgren-Chriss → FinRL → FinRL-X |
| ⑤ LLM in finance | FinBERT → BloombergGPT → DatedGPT → AI Economist |
| ⑥ Microstructure | Kyle → Square-root law → LOB DL → Hyperliquid |
| ⑦ Crypto / DeFi / PM | BTC whitepaper → DEX AMM → Polymarket → RWA |
| ⚠️ Backtest guardrail | DSR → CPCV → Falsification audit (B1 2026) |

Includes **4 reading paths** (alpha / execution / crypto / LLM) with day-counts.

---

## 12. Live arXiv frontier (re-fetchable)

**File:** `05-resources/arxiv-frontier-live.md`

- 31 papers submitted in last 30 days across q-fin.ST/TR/GN/PR/RM
- Includes Python cron script for weekly refresh
- Priority rule: multi-author + recent + well-known lab → add to static list

---

## 13. Topic foundations (scaffold)

| Topic | File | Status |
|---|---|---|
| Mathematics | `01-foundations/README.md` (placeholder) | ⏳ pending |
| Statistics | `01-foundations/README.md` (placeholder) | ⏳ pending |
| Programming | `01-foundations/README.md` (placeholder) | ⏳ pending |
| Time-series | `01-foundations/README.md` (placeholder) | ⏳ pending |
| Portfolio theory | `02-finance/README.md` (placeholder) | ⏳ pending |
| Derivatives pricing | `02-finance/README.md` (placeholder) | ⏳ pending |
| Vol modeling | `02-finance/README.md` (placeholder) | ⏳ pending |
| Risk management | `02-finance/README.md` (placeholder) | ⏳ pending |
| Asset class taxonomy | `02-finance/markets/_global-markets.md` | ✅ populated |
| Career paths | `03-career-paths/` (scaffold) | ⏳ pending |
| Quant mindset | `04-mindset/` (scaffold) | ⏳ pending |
| L1-L5 framework | `06-variable-framework/README.md` + `L1-L5-series-codes.md` | ✅ populated |

**Note:** When domain explanations are needed, point to a specific paper/repo/book rather than these scaffolds — they are intentional placeholders.

---

## 🔁 Maintenance mode

While in **CONTINUOUS RESEARCH** mode:
- 🔄 Pull new papers / models / datasets / sources regularly (see `maintenance-loop.sh`)
- 🔄 Re-organize as new info comes in
- ✅ Commit each incremental addition
- ✅ Use library to answer questions
- ✅ When pointing user to info, cite file + section
- ✅ When asked for something not in library, search actively first

**Refresh cadence:**
- arXiv: weekly (auto-pull newest 50)
- HuggingFace: bi-weekly (top downloads)
- Kaggle: monthly (trending datasets)
- Multi-source: monthly (OpenAlex papers, new sources)

---

## 📊 Library stats (2026-06-28)

| Metric | Value |
|---|---|
| Total files | 26 (.md + .sh) |
| Populated | 16 |
| Total lines | ~9,400 |
| Papers | 300+ (arxiv live + curated) |
| arXiv frontier | 219 (live, 30-day window) |
| OpenAlex cross-disciplinary | 96 (live, since 2023) |
| Books | 34 |
| GitHub repos | 40+ |
| HF models | 68 (live) |
| HF datasets | 79 (live) |
| Kaggle datasets | 269 (live) |
| Data providers | 50+ |
| Cross-link threads | 7 |
| Additional sources | 300+ |
| Series codes (live in pipeline) | 32 |
| Tests passing | 11/11 |
| **Auto-refresh scripts** | **4 (pull_arxiv/hf/kaggle/openalex)** |

---

**Built:** 2026-06-28 · **Status:** 🔄 CONTINUOUS RESEARCH (active) · **Custodian:** Qualabinance / QuantResearcher
