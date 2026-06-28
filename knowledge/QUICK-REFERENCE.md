# ⚡ Quick Reference Cards — 1-Page Topic Summaries

> **TL;DR ต่อหัวข้อ** — เนื้อหาหนาแน่นที่สุดเท่าที่จะยังอ่านรู้เรื่องใน 1 หน้า
>
> **Built:** 2026-06-28 · **Mode:** 🟢 LIBRARY

---

## 📑 Card index

1. [Foundation Models for Finance (2025-2026)](#1-foundation-models-for-finance-2025-2026) ⭐ HOT
2. [LLM in Trading — what works, what doesn't](#2-llm-in-trading)
3. [GARCH family — decision tree](#3-garch-family)
4. [Macro-aware DL (HANET) — when to use](#4-macro-aware-dl)
5. [Backtest guardrails — the 3 must-do checks](#5-backtest-guardrails)
6. [Live data stack — free + reliable](#6-live-data-stack)
7. [Project 07 pipeline — quick reference](#7-project-07-pipeline)
8. [Thailand-specific stack](#8-thailand-specific)
9. [Polymarket / prediction markets](#9-polymarket)
10. [Crypto on-chain data stack](#10-crypto-on-chain)

---

## 1. Foundation Models for Finance (2025-2026) ⭐ HOT

**What it is:** Pretrained transformer models on massive financial corpora, fine-tunable for specific tasks.

| Model | Source | Status | Use for |
|---|---|---|---|
| **Kronos** ✅ | arXiv 2508.02739 (2025-08) | Open code: github.com/shiyu-coder/Kronos | K-line / candlestick pretraining. +93% RankIC vs TSFM, +87% vs best baseline. |
| **Chronos-2** | Amazon (2024) | Open code | Time-series pretraining, multivariate |
| **TimesFM** | Google (2024) | Open code | Zero-shot + fine-tune. Fine-tuned beats GARCH on realized vol via DM+GW tests. |
| **FinGPT** | open-source | Active | Financial LLM, lighter than BloombergGPT |
| **BloombergGPT** | Bloomberg (2023) | Closed weights | The original financial LLM, 50B params |
| **DragonLLM/Llama-Open-Finance-8B** | HF | Open weights | Llama-3.1 fine-tuned for finance Q&A |
| **FinMA** | PIXIU (2023) | Open code | Multi-task instruction-tuned financial LLM |

**Critical lesson from frontier papers:**
- Pretraining helps but **fine-tuning on target data is essential** (F3 TimesFM paper)
- F1 Kronos: **K-line tokenizer preserves price dynamics + trade activity** — key innovation
- Use Chronos/TimesFM as **feature extractors**, not as oracle predictions

**When to use:**
- ✅ Large cross-asset universe (multi-market)
- ✅ Cold-start for new symbol with little history
- ✅ As feature in larger model
- ❌ Daily high-frequency trading (overkill, latency hurts)
- ❌ Single ticker with 20y history (LGBM often matches DL)

**Sources:**
- `papers/_q1-2024-2026-frontier.md` F1-F4
- `papers/_cross-link-map.md` Thread ③
- `huggingface-finance-catalog.md` (model IDs)

---

## 2. LLM in Trading

**Two roles for LLM in trading:**

### Role A: LLM-as-feature-extractor ✅ recommended
- Extract sentiment, entities, topics from news/filings/SEC docs
- Use embeddings or scores as inputs to classical models (LGBM, logistic)
- **Works well** when:
  - You have lots of unstructured text (10-K, earnings calls, news)
  - Classical NLP features are weak
- **Canonical models:** FinBERT (sentiment), FinMA (multi-task)

### Role B: LLM-as-oracle ❌ risky
- Ask LLM directly "should I buy AAPL?"
- **Why it fails:** LLMs trained on web text have:
  - Recency bias (L4 ChatGPT-as-Time-Capsule paper, 2026)
  - Asset-specific preferences (L3 audit-LLM-BTC-bias paper, 2026)
  - Look-ahead bias if not debiased (L7 DatedGPT, 2026)
- **Mitigation:** DatedGPT (L7) + B1 falsification audit

**Best practices (2024-2026 frontier):**
1. Use DatedGPT-style time-aware pretraining (L7)
2. Don't trade directly on LLM output — extract features
3. Audit for bias (L3 audit-LLM)
4. Always run B1 spurious-predictability audit
5. Combine LLM features with classical + macro (HANET T1)

**Sources:**
- `papers/_q1-2024-2026-frontier.md` L1-L10
- `papers/_cross-link-map.md` Thread ⑤
- `huggingface-finance-catalog.md` (FinBERT/Llama-Finance models)

---

## 3. GARCH family — decision tree

```
What are you modeling?
│
├─ Single series, daily returns, normal-ish
│   └─ Use: GARCH(1,1) with Student-t innovations (baseline)
│
├─ Single series, fat tails, regime shifts
│   └─ Use: GJR-GARCH (leverage effect) OR
│           Markov Switching GARCH (V2 2026 frontier)
│
├─ Single series, heavy tails
│   └─ Use: GARCH + Student-t or skewed-t innovations
│           OR V4 tempered skew t (2026 frontier)
│
├─ Multi-asset correlation over time
│   └─ Use: DCC (Engle 2002) baseline
│           OR V5 Bayesian DCC with shrinkage (2026 frontier)
│
├─ Volatility forecasting only (no need for parametric family)
│   └─ Use: Realized vol (Andersen-Bollerslev) +
│           HAR model (simple, beats GARCH out-of-sample often)
│           OR Fine-tuned TimesFM (F3 2025 frontier, beats GARCH)
│
├─ Regime-conditional VaR
│   └─ Use: V1 HMM + heavy-tail emissions (2026 frontier)
│
└─ Need interpretability + ML power
    └─ Use: HAR + neural net (Neural-HAR), or VQ-VAE factors (T8 2026)
```

**When to NOT use GARCH:**
- ❌ Intraday high-frequency (use realized vol)
- ❌ Long-horizon multi-year vol forecasting (use ML)
- ❌ When you have macro features (HANET T1 beats pure GARCH in stress)

**Sources:**
- `papers/_q1-econometrics.md` GARCH section
- `papers/_q1-2024-2026-frontier.md` V1-V9
- `papers/_cross-link-map.md` Thread ②

---

## 4. Macro-aware DL (HANET)

**Problem:** Pure price-based DL (LSTM/Transformer) collapses in turbulent regimes because it has no signal that "regime changed".

**Solution (HANET 2026-05):**
- Hierarchical LSTM + cross-attention between **daily returns** and **monthly macro windows**
- Macro context = FRED L1 series (GDP, CPI, Fed Funds) + VIX + spreads
- Attention learns **which historical regimes are most relevant** for current forecast

**When it wins:** turbulent periods (regime shift, crisis)
**When it ties:** calm bull markets (DL+macro ≈ DL alone)

**Implementation:**
```python
# 1. Pull L1 series from FRED via project-07 pipeline
# 2. Resample to daily (with publication-lag forward-fill)
# 3. Build hierarchical structure: [daily_returns, monthly_macro]
# 4. Cross-attention: low-freq macro ←→ high-freq returns
# 5. Ablation: shuffling macro contexts kills the gain
```

**Ablation proves the gain is genuine**, not just adding features.

**Sources:**
- `papers/_q1-2024-2026-frontier.md` T1
- `06-variable-framework/L1-L5-series-codes.md` (L1 macro series)
- `projects/07-hierarchical-data-pipeline/` (L1 pull + align)

---

## 5. Backtest guardrails — the 3 must-do checks

### Check 1: Deflated Sharpe Ratio (López de Prado 2014)
- Adjusts Sharpe for **multiple testing** (you tried 100 strategies)
- `deflated_sharpe = sharpe × sqrt((1 - γ₃ × sharpe + (γ₄ - 1)/4 × sharpe²) / (T-1))`
- Where γ₃, γ₄ are skew/kurtosis, T is #trials
- Implementations: `mlfinlab`, `quantstats`

### Check 2: Combinatorial Purged Cross-Validation (López de Prado 2018)
- Standard K-fold CV leaks info across time → overfit
- CPCV uses **purged** (drops labels around fold boundary) + **embargo** (extra gap)
- Multiple backtest paths from combinations of folds
- Implementation: `mlfinlab`, `vectorbt`

### Check 3: Spurious Predictability Audit (B1, 2026-04) ⭐ NEW
- Tests **complete workflow** against synthetic placebo environments:
  - Zero-predictability reference (random walk)
  - Microstructure placebo (matching vol but no signal)
- Workflows that pass placebo get **falsified**
- Quantifies **selection-induced inflation** via effective multiplicity

**Rule:** No strategy goes to live trading without all 3 checks passing.

**Sources:**
- `papers/_cross-link-map.md` ⚠️ thread
- `papers/_q1-2024-2026-frontier.md` B1
- `papers/_q1-portfolio-risk.md` C12

---

## 6. Live data stack — free + reliable

**Starter stack (free, all API-accessible, all in project-07):**

| Layer | Source | Series | Code |
|---|---|---|---|
| Macro US | FRED | FEDFUNDS, VIXCLS, DGS10, T10Y2Y, BAML spreads | `fredapi` |
| Macro global | World Bank | GDP, CPI per country | `wbgapi` |
| Equity OHLCV | yfinance | S&P, NASDAQ, AAPL, MSFT | `yfinance` |
| Thailand equity | yfinance | ^SET.BK | `yfinance` |
| FX | FRED | DEXTHUS, DEXUSEU, etc. | `fredapi` |
| Commodity | FRED / EIA | WTI, Gold | `fredapi` |
| Crypto | ccxt | BTC/USDT, ETH/USDT | `ccxt` |
| Crypto aggregate | CoinGecko | Total mcap, dominance | `pycoingecko` |
| Alt data | Manual CSV | GPR, EPU, GSCPI | drop in `data/parquet/raw/` |

**Authentication:** all keys in `.env` (free)
**Storage:** DuckDB (analytical) + Parquet (snapshots)
**Refresh:** `make refresh` (all series) or per-level (`make refresh-L1`)

**Scale-up path (when ready for paid):**
| Need | Paid option |
|---|---|
| Tick-level US | Polygon ($29/mo) or Databento ($50/mo) |
| On-chain premium | Glassnode ($29/mo) |
| Real-time crypto perp | ccxt + Binance WebSocket (free) |
| Sell-side news | FT Lex API ($10k+/yr) |

**Sources:**
- `projects/07-hierarchical-data-pipeline/` (working code)
- `data-providers/treemap-primary-mapping.md` (per cell)
- `06-variable-framework/L1-L5-series-codes.md` (per series)
- `data-providers/_with-papers.md` (50+ providers)

---

## 7. Project 07 pipeline — quick reference

**Path:** `projects/07-hierarchical-data-pipeline/`

```bash
# Install
cd qualabinance
uv venv && source .venv/bin/activate
uv pip install -e ".[data-pipeline,dev]"

# Configure
cp projects/07-hierarchical-data-pipeline/.env.example .env
# Add FRED_API_KEY (free) and any others you have

# Test (offline, no API)
cd projects/07-hierarchical-data-pipeline
make test
# → 11/11 passing

# Pull data
make refresh          # all 32 series
make refresh-L1       # only L1 (macro + global)
make refresh-L3-TH    # only Thailand country-level

# Build wide daily panel
make align            # → data/parquet/aligned/wide_daily.parquet

# Inspect
make coverage         # per-series coverage report
```

**What you get:**
- `data/qualabinance.duckdb` — main analytical DB
- `data/parquet/raw/{series_id}.parquet` — immutable raw snapshots (one per series)
- `data/parquet/aligned/wide_daily.parquet` — ML-ready wide daily panel

**Key design rules baked in:**
- **No look-ahead bias** — publication-lag applied before forward-fill (`align.py`)
- **Provenance everywhere** — `source` + `fetched_at` on every row
- **Config-driven** — add a series = add to `config.DEFAULT_SERIES`
- **Testable offline** — synthetic fixtures, no API needed

**Next loops (planned):**
- 7.1 Thailand connectors (BOT/ThaiBMA/SETSMART)
- 7.2 PCA / factor extraction
- 7.3 Cron + heartbeat
- 7.4 Data validation alerts
- 7.5 First feature panel consumer

---

## 8. Thailand-specific

**Equity universe:**
- SET (Thailand main board) — free delayed via yfinance `^SET.BK`, paid real-time via SETSMART
- mai (Market for Alternative Investment) — small caps
- ETFs: TDEX, K-SET50, 1DIV

**Macro:**
- BOT (Bank of Thailand) API Portal — free registration → `https://apiportal.bot.or.th/`
- BOT policy rate — `BOT_RATE` series in L3
- NESDC (National Economic and Social Development Council) — GDP quarterly
- MOC (Ministry of Commerce) — CPI, trade balance

**Bonds:**
- ThaiBMA — daily yield curve, requires free registration
- Government bonds (LB bonds), corporate bonds

**FX:**
- THB/USD via FRED `DEXTHUS` (free daily)
- Cross-rates via ThaiBMA or BOT

**Special considerations:**
- SET trades 10:00-16:30 ICT (no pre-market, no after-hours)
- SET settlement T+2
- Foreign ownership limits on some equities
- WHT (withholding tax) on dividends — factor into after-tax returns

**Sources:**
- `06-variable-framework/L1-L5-series-codes.md` (L3 TH table)
- `_multi-source-catalog.md` (BOT/ThaiBMA/SETSMART/NESDC/MOC)
- `_additional-sources.md` (Thailand-specific news)

---

## 9. Polymarket / prediction markets

**What it is:** On-chain event-contract venue (largest: Polymarket). Binary outcome contracts on real-world events (elections, sports, economics).

**Why quants care:**
- 30B+ events / 52 days = rich tick-level data
- Real-time market-implied probability
- Often > 50% alpha vs traditional polls (per C2 paper)
- New venue for systematic strategies (event-perp, cross-market arb)

**Critical caveat from C2 (2026-04):**
- Polymarket **public order-book feed** disagrees with on-chain ground truth ~59% of the time
- Feed-inferred trade direction: **only ~59% match on-chain** (vs ~80% Lee-Ready on Nasdaq)
- **Rule:** for microstructure research on Polymarket, **always source trade direction from on-chain OrderFilled events**, not from public feed

**Use cases:**
- ✅ Real-time probability signals (vs poll aggregates)
- ✅ Cross-market arb (Polymarket vs traditional bookmaker)
- ✅ Event-perp strategies (R2-style execution)
- ✅ Information leakage research (C6-C7 papers)
- ❌ Direct trading without on-chain data (you'll be misinformed)

**Data access:**
- Polymarket API: `https://docs.polymarket.com/`
- Subgraph: The Graph protocol (`https://thegraph.com/`)
- Dune Analytics has pre-built queries

**Sources:**
- `papers/_q1-2024-2026-frontier.md` C2-C7
- `papers/_cross-link-map.md` Thread ⑦
- `_multi-source-catalog.md` (Polymarket/Dune/The Graph)

---

## 10. Crypto on-chain data stack

**What you need (free, all accessible):**

| Need | Source | API/Library |
|---|---|---|
| Price OHLCV | Binance/Coinbase | ccxt |
| Aggregate market cap | CoinGecko | pycoingecko |
| On-chain transactions | Etherscan / BlockDB HF | etherscan-python, HF dataset |
| On-chain blocks | BlockDB HF | HF dataset |
| Token transfers | BlockDB HF | HF dataset |
| DEX liquidity | BlockDB HF, Dune | HF dataset, dune.com SQL |
| DeFi TVL | DefiLlama | defillama.com (free) |
| Funding rates | Coinglass | free + paid |
| Sentiment | Crypto Twitter | HF dataset (aaurelions), Stocktwits |
| Liquidation events | Coinglass | free |

**For QuantResearcher use:**
```python
import ccxt
binance = ccxt.binance()
btc_ohlcv = binance.fetch_ohlcv("BTC/USDT", "1d", limit=1000)

import requests
r = requests.get("https://api.coingecko.com/api/v3/global").json()
total_mcap = r["data"]["total_market_cap"]["usd"]

# On-chain via HF
from datasets import load_dataset
blocks = load_dataset("BlockDB/Raw-Blocks-Ethereum-And-EVM-Cryptocurrency-Data")
```

**Already wired in project-07:**
- `ccxt_binance_btc` (L4) — via CcxtSrc
- `altme_fng` (L5) — via CoinGeckoSrc (Fear & Greed)

**To add:**
- `ccxt_binance_eth`, `ccxt_binance_sol` — extend config.py
- on-chain ETH — needs Etherscan key or BlockDB
- DefiLlama TVL — new source class

**Sources:**
- `06-variable-framework/L1-L5-series-codes.md` (L4 crypto)
- `_multi-source-catalog.md` (crypto infra)
- `huggingface-finance-catalog.md` (BlockDB datasets)
- `projects/07-hierarchical-data-pipeline/src/ingest.py` (CcxtSrc, CoinGeckoSrc)

---

## 🚨 When to leave library mode

If you ask me something **not in any card above**, I will:
1. Search the library first (`TOPIC-INDEX.md`)
2. If not found, flag as **gap** + propose a research plan
3. You say "research [gap]" → exit library mode → fill it

If you ask me something **in a card above**, I will:
1. Point to the card
2. Cite the underlying file
3. Answer from existing content (no new research)

**Library mode is on. Ready to look up, not to explore.**

---

**Built:** 2026-06-28 · **Mode:** 🟢 LIBRARY (passive) · **Custodian:** Qualabinance / QuantResearcher
