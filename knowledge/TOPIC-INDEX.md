# 🔍 Topic Index — Find by Query

> **Reverse lookup:** enter a query → get file + section.
> Use [`LIBRARY.md`](LIBRARY.md) for top-down browsing, this file for bottom-up search.

**Built:** 2026-06-28 · **Mode:** 🟢 LIBRARY

---

## How to use

Each entry has **query keywords** (top) and **pointers** (bottom). Match your query against keywords, jump to pointers.

Categories:
- [A] Asset classes
- [B] Methodology
- [C] ML/AI
- [D] Microstructure
- [E] Macro / variables
- [F] Infrastructure / data
- [G] Backtest / risk
- [H] Career / learning

---

## [A] Asset classes

| Query | Pointers |
|---|---|
| US stock / equity / NYSE / NASDAQ | `02-finance/markets/_global-markets.md` (Equities table) · `05-resources/data-providers/_with-papers.md` (Polygon/CRSP) · `06-variable-framework/L1-L5-series-codes.md` (L4: AAPL/MSFT) |
| Thai stock / SET / Bangkok | `_global-markets.md` (Thailand row) · `L1-L5-series-codes.md` (L2: ^SET.BK + L3: wb_th_*) · `_multi-source-catalog.md` (SETSMART/ThaiBMA) |
| Bond / fixed income / yield | `_global-markets.md` (Bonds/ETFs) · `papers/_q1-portfolio-risk.md` (Vasicek/Cox-Ingersoll-Ross) · `_with-papers.md` (FRED yields/BIS) |
| Forex / FX / currency | `_global-markets.md` (Forex) · `L1-L5-series-codes.md` (L3 FX: DEXTHUS etc.) · `papers/_q1-econometrics.md` (FX section) |
| Commodity / oil / gold | `_global-markets.md` (Commodities) · `L1-L5-series-codes.md` (L1: DCOILWTICO, LBMA/GOLD) · `data-providers/_with-papers.md` (EIA/WGC) |
| Crypto / bitcoin / ethereum / DeFi | `_global-markets.md` (Crypto) · `papers/_q1-2024-2026-frontier.md` (C-section: Polymarket/Cross-chain/RWA) · `L1-L5-series-codes.md` (L4: BTC-USD, ETH-USD) |
| Options / derivatives / futures | `_global-markets.md` (Options/Futures) · `papers/_q1-portfolio-risk.md` (BSM/Heston) · `_multi-source-catalog.md` (Deribit/CBOE) |
| Prediction market / Polymarket / event contract | `papers/_q1-2024-2026-frontier.md` (C2 Polymarket 8 stylized facts, C3-C7 event-linked perps) |
| RWA / tokenization / on-chain treasury | `papers/_q1-2024-2026-frontier.md` (C13 SoK RWA) · `_multi-source-catalog.md` (MakerDAO/Paxos) |

---

## [B] Methodology

| Query | Pointers |
|---|---|
| Portfolio theory / MVO / efficient frontier | `papers/_q1-portfolio-risk.md` (C1 Markowitz, C2 Sharpe CAPM, C9 Fama-French) · `books/_canonical.md` (Bodie-Kane-Marcus) |
| CAPM / alpha / beta / asset pricing | `papers/_q1-portfolio-risk.md` (C2-C9 CAPM + FF) · `papers/_q1-2024-2026-frontier.md` (A-section: factor zoo, portfolio construction) |
| Black-Scholes / option pricing / BSM | `papers/_q1-portfolio-risk.md` (C5 BSM, C6 Merton, C7 jump-diffusion) · `books/_canonical.md` (Hull) |
| GARCH / volatility clustering | `papers/_q1-econometrics.md` (GARCH family: Engle 1982, Bollerslev 1986, GJR, DCC) · `papers/_q1-2024-2026-frontier.md` (V1-V9: HMM-t, MS-GARCH, TimesFM vol) |
| VaR / Expected Shortfall / coherent risk | `papers/_q1-portfolio-risk.md` (C10 Artzner coherent, C11 Rockafellar CVaR) · `papers/_q1-2024-2026-frontier.md` (V1 HMM-conditional VaR) |
| Realized volatility / RV / HAR | `papers/_q1-econometrics.md` (RV section: Andersen-Bollerslev) · `papers/_q1-2024-2026-frontier.md` (F3 TimesFM for RV) |
| Stochastic vol / Heston / Bergomi / rough vol | `papers/_q1-econometrics.md` (SV section) · `papers/_q1-2024-2026-frontier.md` (A4 VIX options in Bergomi) |
| Cointegration / pair trading / statistical arbitrage | `papers/_q1-econometrics.md` (Cointegration section: Engle-Granger, Johansen) |
| Heavy tails / fat tails / stylized facts | `papers/_q1-econometrics.md` (Heavy tails section) · `papers/_q1-2024-2026-frontier.md` (V4 tempered skew t) |
| Factor model / factor zoo / factor investing | `papers/_q1-portfolio-risk.md` (Fama-French, Hou-Xue-Zhang q-factor) · `papers/_q1-2024-2026-frontier.md` (A1 construction-dependent, A2 interpretable) |

---

## [C] ML / AI

| Query | Pointers |
|---|---|
| LSTM / RNN / time-series deep learning | `papers/_q1-ml-finance.md` (#8 Deep Momentum Networks, #11 Hybrid DL multi-step) |
| Transformer / attention / NLP for finance | `papers/_q1-ml-finance.md` (#12 RSR/TGCN, #13 Stock embedding) · `papers/_q1-2024-2026-frontier.md` (T1-T8: HANET, shifted aug, etc.) |
| Foundation model / TSFM / pretraining | `papers/_q1-2024-2026-frontier.md` (F1 Kronos ⭐, F2 Chronos-finance, F3 TimesFM vol) · `papers/_cross-link-map.md` (Thread ③) |
| Reinforcement learning / RL / agent / PPO / DDPG | `papers/_q1-ml-finance.md` (#14-18: FinRL, PPO, Adversarial RL) · `papers/_q1-2024-2026-frontier.md` (R1 FinRL-X ⭐, R2 TT-DAC-PS, R3-R7) |
| LLM / large language model / ChatGPT / GPT | `papers/_q1-ml-finance.md` (#19-22: BloombergGPT, FinGPT, FinBERT, FinMA) · `papers/_q1-2024-2026-frontier.md` (L1-L10: DatedGPT, AI Economist, audit LLM bias) |
| FinBERT / sentiment / NLP | `papers/_q1-ml-finance.md` (#21 FinBERT) · `huggingface-finance-catalog.md` (top model: nickmuchi/finbert-tone) |
| FinGPT / open-source financial LLM | `papers/_q1-ml-finance.md` (#20 FinGPT) · `github-projects/_github-with-papers.md` (FinGPT repo) |
| Sentiment / FinBERT / news alpha | `huggingface-finance-catalog.md` (top model) · `kaggle-finance-catalog.md` (Bitcoin tweets, Financial News Sentiment) · `_multi-source-catalog.md` (NYT API, FT API) |
| Graph neural network / GNN | `papers/_q1-2024-2026-frontier.md` (M4 Hierarchical GNN for calendar spreads, T8 VQ-VAE factors) |
| Spurious / overfitting / debiasing / look-ahead | `papers/_cross-link-map.md` ⚠️ thread · `papers/_q1-2024-2026-frontier.md` (B1 Spurious Predictability, L7 DatedGPT) · `papers/_q1-portfolio-risk.md` (C12 Deflated Sharpe) |
| Interpretability / explainability / SHAP | `papers/_q1-2024-2026-frontier.md` (A2 Consensus-Bottleneck interpretable) · `papers/_q1-ml-finance.md` (#6 Harvey 2017 "Limits of Knowledge") |

---

## [D] Microstructure

| Query | Pointers |
|---|---|
| Market impact / square-root law | `papers/_q1-econometrics.md` (Microstructure sec: Bouchaud square-root) · `papers/_q1-2024-2026-frontier.md` (M2 US large-cap confirmation, M3 trade-sign long-memory) |
| Optimal execution / Almgren-Chriss | `papers/_q1-econometrics.md` (Optimal execution sec) · `papers/_q1-2024-2026-frontier.md` (R2 TT-DAC-PS) |
| Limit order book / LOB / order flow | `papers/_q1-econometrics.md` (LOB sec) · `papers/_q1-ml-finance.md` (#26-28 DeepLOB, SVM-LOB) · `papers/_q1-2024-2026-frontier.md` (M1 inference-compute frontier) |
| Bid-ask spread / Kyle / Glosten-Milgrom | `papers/_q1-econometrics.md` (Microstructure sec) |
| Informed trading / PIN / adverse selection | `papers/_q1-econometrics.md` (Order flow sec) · `papers/_q1-2024-2026-frontier.md` (M6 Hyperliquid adverse selection, M8 informedness-PnL) |
| HFT / latency / market making | `papers/_q1-2024-2026-frontier.md` (M1 inference-compute, M7 axiomatic MM, M8 informedness) |
| Flash crash / systemic events | `papers/_q1-econometrics.md` (Flash crash sec) |
| On-chain microstructure / DEX / AMM | `papers/_q1-2024-2026-frontier.md` (C1 cross-chain spillovers, C2 Polymarket, M6 Hyperliquid, B2 counterfactual DEX) |

---

## [E] Macro / variables

| Query | Pointers |
|---|---|
| Global macro / Fed / FOMC / rates | `06-variable-framework/L1-L5-series-codes.md` (L1: FEDFUNDS, DGS10, T10Y2Y) · `data-providers/treemap-primary-mapping.md` (FRED section) |
| Global financial conditions / DXY | `L1-L5-series-codes.md` (L1: DTWEXBGS, NFCI) |
| Country macro / Thailand / BOT | `L1-L5-series-codes.md` (L3 Thailand table) · `_multi-source-catalog.md` (BOT API, NESDC, MOC) |
| Inflation / CPI / unemployment | `L1-L5-series-codes.md` (L3: CPIAUCSL, CPILFESL, UNRATE) · `data-providers/_with-papers.md` (BLS, FRED) |
| Yield curve / 10Y-2Y / slope | `L1-L5-series-codes.md` (L1: T10Y2Y) · `data-providers/_with-papers.md` (FRED yields) |
| Credit spread / IG / HY | `L1-L5-series-codes.md` (L1: BAMLH0A0HYM2, BAMLC0A0CM) |
| VIX / volatility index / fear | `L1-L5-series-codes.md` (L1: VIXCLS) · `data-providers/_with-papers.md` (CBOE) |
| Geopolitical risk / GPR / EPU | `L1-L5-series-codes.md` (L5: GPR, US_EPU) · `data-providers/_with-papers.md` (policyuncertainty.com, matteoiacoviello.com) |
| Supply chain / GSCPI | `L1-L5-series-codes.md` (L5: nyfed_gscpi) · `data-providers/_with-papers.md` (NY Fed) |
| Climate / ESG / carbon | `_with-papers.md` (climate section) · `_additional-sources.md` (NOAA, MSCI ESG) |
| Macro-aware model / mixed-frequency / HANET | `papers/_q1-2024-2026-frontier.md` (T1 HANET ⭐, 55 futures) |
| Macro regime / Markov switching | `papers/_q1-2024-2026-frontier.md` (T6 HMM+RL allocation, V1 HMM+heavy-tail) |

---

## [F] Infrastructure / data

| Query | Pointers |
|---|---|
| Data provider / API / vendor | `data-providers/_with-papers.md` (50+ providers) · `data-providers/treemap-primary-mapping.md` (per Treemap cell) · `L1-L5-series-codes.md` (per series) |
| FRED API / free macro data | `data-providers/treemap-primary-mapping.md` (FRED section) · `projects/07-hierarchical-data-pipeline/` (live) |
| yfinance / Yahoo Finance | `L1-L5-series-codes.md` (L2/L4 source: yfinance) · `huggingface-finance-catalog.md` (defeatbeta/yahoo-finance-data) |
| Binance API / crypto OHLCV | `L1-L5-series-codes.md` (L4: ccxt_binance_btc) · `projects/07-hierarchical-data-pipeline/src/ingest.py` (CcxtSrc) |
| CoinGecko / Fear & Greed | `L1-L5-series-codes.md` (L5: altme_fng) · `data-providers/_with-papers.md` (CoinGecko) |
| HuggingFace / model hub | `huggingface-finance-catalog.md` (live) · `_multi-source-catalog.md` (HF section) |
| Kaggle / dataset hub | `kaggle-finance-catalog.md` (live) · `_multi-source-catalog.md` (Kaggle section) |
| arXiv / paper server | `arxiv-frontier-live.md` (live) · `papers/_cross-link-map.md` (7 threads) · `_multi-source-catalog.md` (arXiv section) |
| OpenAlex / Semantic Scholar / CrossRef | `_multi-source-catalog.md` (alternative APIs) |
| Polygon / Databento / tick data | `data-providers/_with-papers.md` · `_multi-source-catalog.md` (real-time streams) |
| On-chain data / Dune / Nansen / Glassnode | `huggingface-finance-catalog.md` (BlockDB datasets) · `_multi-source-catalog.md` (Dune/Nansen/Glassnode) · `papers/_q1-2024-2026-frontier.md` (C1 cross-chain) |
| Backtest engine / Zipline / Lean / Backtrader | `github-projects/_github-with-papers.md` (Backtesting Frameworks) |
| Quant platform / OpenBB / Qlib / FinRL-X | `github-projects/_github-with-papers.md` · `papers/_q1-2024-2026-frontier.md` (R1 FinRL-X) |
| Pipeline / ETL / DuckDB / Parquet | `projects/07-hierarchical-data-pipeline/` (32 series, 11 tests pass) |
| Visualization / charting / Plotly / TradingView | `_multi-source-catalog.md` (Charting section) |

---

## [G] Backtest / risk

| Query | Pointers |
|---|---|
| Backtest overfitting / multiple testing | `papers/_q1-portfolio-risk.md` (C12 Deflated Sharpe) · `papers/_cross-link-map.md` ⚠️ thread · `papers/_q1-2024-2026-frontier.md` (B1 Spurious Predictability 2026) |
| Walk-forward / cross-validation / purged CV | `papers/_q1-portfolio-risk.md` (C12 + Combinatorial Purged CV) · `papers/_cross-link-map.md` (⚠️ chain) |
| Sharpe ratio / information ratio / Sortino | `papers/_q1-portfolio-risk.md` (C12 + related) |
| Drawdown / max DD / Calmar | `books/_canonical.md` (QuantStats reference) |
| Risk management / position sizing / Kelly | `books/_canonical.md` (Tharp) · `papers/_q1-portfolio-risk.md` (C10-C11 coherent risk) |
| Stress test / scenario analysis | `papers/_q1-portfolio-risk.md` (coherent measures) · `data-providers/_with-papers.md` (BIS stress scenarios) |
| Kill-switch / circuit breaker / risk gate | (not yet covered — flag as gap) |

---

## [H] Career / learning

| Query | Pointers |
|---|---|
| Quant researcher role | `03-career-paths/quant-researcher.md` (scaffold) · `papers/_cross-link-map.md` (Path A reading) |
| Quant developer role | `03-career-paths/quant-developer.md` (scaffold) · `github-projects/_github-with-papers.md` · `books/_canonical.md` (Phase 3) |
| Quant trader role | `03-career-paths/quant-trader.md` (scaffold) · `books/_canonical.md` (Phase 4) · `_additional-sources.md` (podcasts) |
| Risk quant role | `03-career-paths/risk-quant.md` (scaffold) · `papers/_q1-portfolio-risk.md` (C10-C11) |
| Roadmap / reading order | `books/_canonical.md` (4 reading paths) · `papers/_cross-link-map.md` (4 reading paths) · `_additional-sources.md` (university courses) |
| Textbooks / canonical reads | `books/_canonical.md` (34 books, ISBN-verified, 4 phases) |
| Interview prep / quant interview | (not yet covered — flag as gap) |
| Salary / compensation | (not yet covered — flag as gap) |
| Job boards | `_additional-sources.md` (LinkedIn/QuantNet/eFinancialCareers) |

---

## 🚨 Known gaps (flag when asked)

These topics are **not yet** in the library. If asked, say so honestly + propose a research plan:

- ❌ Kill-switch / circuit-breaker risk infrastructure
- ❌ Quant interview prep (brainteasers, probability puzzles)
- ❌ Tax-aware investing / after-tax returns
- ❌ ESG / impact investing methodology
- ❌ High-frequency trading (full latency optimization)
- ❌ Distributed RL for finance (Horovod, Ray)
- ❌ Quantum computing for finance (Qiskit Finance)
- ❌ Insurance / actuarial (LTC, mortality tables)
- ❌ Wealth management / robo-advisor

If you want to fill any of these, say "research [gap]" and exit library mode.

---

**Built:** 2026-06-28 · **Mode:** 🟢 LIBRARY (passive) · **Custodian:** Qualabinance / QuantResearcher
