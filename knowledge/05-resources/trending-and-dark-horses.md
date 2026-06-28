# 🔥 Trending + 🐴 Dark Horses — What People Are Watching

> **What everyone is looking at right now (Jun 2026)** + **dark horses** (rising stars most haven't noticed yet).
>
> **Built:** 2026-06-28 · **Refresh:** weekly via `scripts/pull_github_trending.py` + manual curation
>
> **Signals used:**
> - HuggingFace `trendingScore` (24h velocity)
> - GitHub stars velocity (recent + per-day)
> - OpenAlex citation count (recent papers)
> - arXiv submission velocity
> - Manual curation (dark horses with high signal density)

---

## 🔥 SECTION 1: Trending Now (mass attention)

### 🤗 HuggingFace — Trending Models (24h velocity)

| Trend | Downloads | Likes | Model | What it is |
|---|---|---|---|---|
| 🏆 **2** | 2,038 | 32 | `DragonLLM/Llama-Open-Finance-8B` | Llama-3.1 fine-tune for finance Q&A. Open weights. |
| 1 | 68,297 | 69 | `nickmuchi/finbert-tone-finetuned-finance-topic-classification` | FinBERT variant, sentiment + topic classifier |
| 1 | 506 | 46 | `tarun7r/Finance-Llama-8B` | Another Llama finance fine-tune |
| 1 | 0 | 5 | `DragonLLM/Llama-Pro-Finance-70B` | 🆕 **Dark horse** — 70B params, hot launch |
| 1 | 1,962 | 6 | `mradermacher/DeepSeek-R1-Finance-Reasoning-14B-GGUF` | DeepSeek-R1 reasoning, finance-tuned, local |

### 🤗 HuggingFace — Trending Datasets

| Trend | Downloads | Dataset | Use case |
|---|---|---|---|
| 🏆 **3** | 141,643 | `defeatbeta/yahoo-finance-data` | Bulk OHLCV |
| 2 | 404 | `AfterQuery/FinanceQA` | Finance QA for RAG eval |
| 2 | 61 | `VedantPadwal/quantitative-finance-reasoning` | Quant reasoning (small but hot) |
| 1 | 4,311 | `PatronusAI/financebench` | Finance RAG benchmark |
| 1 | 984 | `Josephgflowers/Finance-Instruct-500k` | 500k instruction samples |
| 1 | 901 | `gretelai/synthetic_pii_finance_multilingual` | Compliance testing data |

### ⭐ GitHub — Hot Repos (created since 2026)

| ⭐ | Repo | Why hot |
|---|---|---|
| 🏆 **89,199** | [**TauricResearch/TradingAgents**](https://github.com/TauricResearch/TradingAgents) | 🐉 **#1 most-starred quant repo.** Multi-agent LLM trading framework. The de facto standard for LLM-trading. |
| **1,627** | [**akfamily/akquant**](https://github.com/akfamily/akquant) | ⚡ Rust+Python high-perf quant framework. akshare integration. |
| **1,176** | [**QuantaAlpha/QuantaAlpha**](https://github.com/QuantaAlpha/QuantaAlpha) | 🧬 LLM + evolutionary alpha factor mining. Self-evolving agent. |
| 1,477 | simonlin1212/TradingAgents-astock | **Chinese A-share fork** of TradingAgents |
| 813 | cookiy-ai/user-research-skill | Cookiy AI skill for AI agents (Claude, Codex, Cursor) |
| 437 | Po1yScripts/polymarket-arbitrage-trading-bot-pack | Polymarket + Kalshi arbitrage bot (5/15-min) |
| 184 | dwebagents/AgentPipe | Multi-threaded task execution |
| 161 | toddwyl/hl-quant | Heuristic-learning quant |
| 97 | Trata-Inc/trata-hedge-bench | Benchmark for hedge-fund reasoning |
| 97 | Lumina-Finance/lumina-finance | Self-hostable portfolio management |

### 📚 arXiv — Most-Cited Recent (last 90 days, top cites)

| Citations | Year | Paper | Why trending |
|---|---|---|---|
| 🏆 **131** | 2026 | **TimeLLM: Time Series Forecasting by Reprogramming Large Language Models** | LLM-as-time-series — bridging NLP and forecasting. |
| 35 | 2026 | Large Models for Time Series and Spatio-Temporal Data: A Survey and Outlook | Survey paper — reads like a roadmap. |
| 3 | 2025 | AI Agents in Finance and Fintech: A Scientific Review | Maps the agent-finance landscape. |
| 2 | 2026 | **Kronos: A Foundation Model for the Language of Financial Markets** | The TSFM for finance paper we tracked. |
| 2 | 2026 | (other Kronos-citing paper) | — |
| 0 | 2026 | **Prediction Arena: Benchmarking AI Models on Real-World Prediction Markets** | 🐴 Dark horse — AI vs prediction-market ground truth. |

---

## 🐴 SECTION 2: Dark Horses (under the radar)

> **Dark horse = high signal density + low mass awareness.** These will be on the trending list in 6-12 months if they keep growing.

### 🐴 1. **Prediction Arena** (arXiv 2026)
- **What:** Real benchmark of AI models on real prediction markets
- **Why dark:** Cited 0× but solves the actual eval problem
- **Why matters:** Last week every AI lab claimed their model could forecast — this paper actually tests it on Polymarket ground truth
- **Action:** Track when it gets cited by major labs

### 🐴 2. **QuantaAlpha** (GitHub 1,176⭐)
- **What:** LLM + evolutionary algorithms for alpha factor mining
- **Why dark:** Recent (created 2026-01), self-evolving agent paradigm
- **Why matters:** Most alpha research still manual. Auto-evolving factors is the next frontier.
- **Stack:** LLM intelligence + evolutionary strategies
- **Action:** Try `git clone https://github.com/QuantaAlpha/QuantaAlpha` and benchmark vs hand-crafted factors

### 🐴 3. **AKQuant** (GitHub 1,627⭐)
- **What:** Rust+Python quant framework with akshare (CN data) integration
- **Why dark:** Asian-market focused, smaller community vs Zipline/Lean
- **Why matters:** Most quant frameworks are US-centric. AKQuant has CN data native.
- **Action:** Use if you trade CN/HK/TW equities

### 🐴 4. **empiricalwiki** (GitHub 62⭐, Lambenthan)
- **What:** AI knowledge base for **empirical econ research** (Chinese)
- **Why dark:** Tiny star count but very dense signal
- **Why matters:** Based on Karpathy's LLM-Wiki. Covers 10 entity types: variables, datasets, models, mechanisms, hypotheses, identification, robustness, heterogeneity, tables, papers
- **Action:** If you do empirical research, study this design pattern

### 🐴 5. **VedantPadwal/quantitative-finance-reasoning** (HF trend=2)
- **What:** Small quant-reasoning dataset, only 61 dl but trend=2
- **Why dark:** Tiny + hot. The signal: someone is curating reasoning examples for quant.
- **Action:** Watch — if it grows, mirrors the FinGPT/FinMA trajectory

### 🐴 6. **trata-hedge-bench** (GitHub 97⭐)
- **What:** Benchmark for hedge-fund-style reasoning tasks
- **Why dark:** Small but high signal — first real hedge-fund eval
- **Why matters:** Most LLM evals are toy. Hedge-fund reasoning = complex, multi-step, adversarial.
- **Action:** Use as eval set for any quant agent you build

### 🐴 7. **AgentPipe** (GitHub 184⭐)
- **What:** Multi-threaded task execution framework
- **Why dark:** Recent, raw infra — but quant agents need exactly this
- **Why matters:** Most LLM agents run single-threaded. Multi-agent RL systems need parallel coordination.
- **Action:** Use as runtime for multi-agent trading systems

### 🐴 8. **B1 "Spurious Predictability in Financial ML"** (already in library)
- Already in `_q1-2024-2026-frontier.md` — **falsification audit** at workflow level
- Cited 0× currently but will explode when first major quant fund gets caught with overfit strategy

### 🐴 9. **NS-NTK** (GitHub 43⭐, imbue-bit)
- **What:** Official implementation of "Deep Learning under COnstraint"
- **Why dark:** Theory paper from active lab, small but growing
- **Why matters:** Constraint-aware DL = more interpretable, fewer spurious features
- **Action:** Read paper, evaluate on factor selection

### 🐴 10. **ShaneLiu04/Finance-DeepSeek** (GitHub 36⭐)
- **What:** DeepSeek-R1-Distill-Qwen-1.5B fine-tuned for finance QA (CN)
- **Why dark:** Tiny, but uses **reasoning distillation** (R1) — first CN quant to do this
- **Why matters:** Distilled reasoning models are the right size for production
- **Action:** Benchmark vs ProsusAI/finbert for sentiment tasks

---

## 📊 Pattern observations (Jun 2026)

### What's moving from edge → mainstream (next 6 months)
1. **Foundation models for finance** — Kronos, TimesFM, Chronos-finance. The "Chronos-for-X" pattern is winning. Expect **"Llama-for-X"** equivalents in finance soon.
2. **Multi-agent LLM trading** — TradingAgents (89k⭐) has hit escape velocity. Expect forks (CN A-share variant already exists).
3. **Prediction-market-based LLM eval** — Prediction Arena + Polymarket data = first real-world forecasting benchmark.
4. **Self-evolving alpha factors** — QuantaAlpha pattern (LLM + evolutionary search).
5. **Cross-chain microstructure** — Still academic, but on-chain perp DEXs (Hyperliquid, dYdX) are producing real data.

### What's over (saturated)
- ❌ "Yet another LSTM for stock prediction" — death by 2024
- ❌ Generic sentiment analysis with FinBERT — everyone's done it, alpha decayed
- ❌ Static factor zoo papers without ML — Gu-Kelly-Xiu won this round

### What's not yet mainstream but should be
- 🔮 HANET-style macro-aware DL (T1 2026) — most teams still use pure price DL
- 🔮 Spurious predictability audit (B1 2026) — every quant desk should run this, almost none do
- 🔮 DatedGPT for LLM debiasing (L7 2026) — critical for any LLM-in-the-loop system
- 🔮 Polymarket microstructure (C2 2026) — entirely new venue, ~0 competition

---

## 🔁 How to detect dark horses yourself

**Signals (sorted by reliability):**
1. **GitHub stars velocity** (stars/week) — most reliable for code
2. **HuggingFace trendingScore** (24h velocity) — for models
3. **arXiv citation velocity** (citations/week) — for papers, lagged 6-12 mo
4. **Niche community mentions** (Discord, Substack, X) — leads by 1-3 mo
5. **Author pedigree** — known researcher publishing in new area = high signal

**Heuristics:**
- New repo with >50⭐ in <30 days AND solves a real problem (not a wrapper)
- Paper with >5 cites in <60 days from peer-reviewed venue
- Model with >1000 downloads in <30 days AND open weights

**Red flags (don't be fooled):**
- 🚩 Repo with marketing hype but no code
- 🚩 "Revolutionary AI" without reproducibility
- 🚩 Claims of beating market with no live track record

---

## 🎯 Action items for QuantResearcher

Based on this scan, here's what to investigate next:

1. **Try QuantaAlpha** — benchmark vs hand-crafted factors on project-07 pipeline data
2. **Read Prediction Arena paper** in full — model eval methodology transferable to our backtest framework
3. **Track TradingAgents forks** — CN A-share variant is the most relevant for Thailand expansion
4. **Bookmark empiricalwiki** design pattern — apply to our knowledge library (entity-based, not file-based)
5. **Watch NS-NTK + B1 audit** — when they get cited by mainstream quant funds, deploy in our project-07

---

## 🔗 See also

- `arxiv-frontier-live.md` — all 219 last-30-day papers
- `huggingface-finance-catalog.md` — all 68 models + 79 datasets
- `kaggle-finance-catalog.md` — all 269 datasets
- `openalex-cross-disciplinary.md` — all 96 papers
- `papers/_q1-2024-2026-frontier.md` — curated 70+ frontier papers
- `papers/_cross-link-map.md` — how papers connect

---

**Built:** 2026-06-28 · **Mode:** 🔄 CONTINUOUS RESEARCH · **Refresh:** weekly