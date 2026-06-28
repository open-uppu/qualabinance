# 🔗 Cross-Link Map — How the Quant Finance Papers Connect

> **Purpose:** Show how canonical classics (1952-2018) connect to recent work (2019-2026) so you can navigate the literature as a **graph**, not isolated lists.
>
> **Built:** 2026-06-28 · **Owner:** Qualabinance / QuantResearcher
>
> **Companion files:**
> - [`_q1-ml-finance.md`](_q1-ml-finance.md) · [`_q1-portfolio-risk.md`](_q1-portfolio-risk.md) · [`_q1-econometrics.md`](_q1-econometrics.md) · [`_q1-2024-2026-frontier.md`](_q1-2024-2026-frontier.md)

---

## 🗺️ The 7 main research threads

```
┌─────────────────────────────────────────────────────────────────────────┐
│                                                                         │
│  ① Portfolio Theory & Asset Pricing ──────────────────── A1, A2, A5    │
│     Markowitz → CAPM → Fama-French → Gu/Kelly/Xiu → Neural Factors      │
│                                                                         │
│  ② Derivatives Pricing & Volatility Modeling ─────────── V1-V9, A4      │
│     BSM → GARCH → Stochastic Vol → Rough Bergomi → Foundation-Model Vol │
│                                                                         │
│  ③ Time-Series ML / DL Forecasting ──────────────────── T1-T8, F1-F4   │
│     LSTM/RNN → Transformer → TSFM (Chronos/TimesFM) → Foundation Models │
│                                                                         │
│  ④ Reinforcement Learning for Trading ────────────────── R1-R7, M1, M2  │
│     Almgren-Chriss → DDPG/PPO → FinRL → FinRL-X → Multi-Agent          │
│                                                                         │
│  ⑤ LLM in Finance ───────────────────────────────────── L1-L10, T8     │
│     FinBERT → FinGPT/BloombergGPT → DatedGPT → AI Economist Agent      │
│                                                                         │
│  ⑥ Microstructure & Market Impact ───────────────────── M1-M8           │
│     Kyle → Glosten-Milgrom → ABIDES → Square-Root Law → LOB DL         │
│                                                                         │
│  ⑦ Crypto / DeFi / Prediction Markets ───────────────── C1-C15         │
│     Bitcoin whitepaper → DEX AMM → Polymarket → On-Chain Micro         │
│                                                                         │
│  ⚠️ Backtest Methodology (cross-cutting guardrails) ─── B1, C12, C11   │
│     López de Prado (DSR) → Combinatorial Purged CV → Falsification Audit│
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## ① Portfolio Theory & Asset Pricing — the alpha thread

```
Markowitz 1952                  Sharpe 1964              Lintner/Mossin 1965/66
  "Portfolio Selection"    ──▶  CAPM                  ──▶  Independent CAPM
       │                           │                          derivations
       │                           ▼
       │                    Fama-French 1993
       │                    3-factor (MKT, SMB, HML)
       │                           │
       │                           ▼
       │                    Carhart 1997 (4-factor: MOM)
       │                           │
       │                           ▼
       │                    Hou-Xue-Zhang 2015 (q-factor)
       │                           │
       │                           ▼
       │                    Harvey-Liu-Zhu 2016 "...and the Cross-Section"
       │                    (factor zoo warning)
       │                           │
       │                           ▼
       │              ┌────────────┴────────────┐
       │              ▼                          ▼
       │        Gu-Kelly-Xiu 2020          A1 (2026) "Which Portfolios?"
       │        "Empirical Asset           (factor perf is
       │        Pricing via ML"            construction-dependent)
       │              │
       │              ▼
       │        A5 (2025) MLP vs G-K-X empirical
       │              │
       │              ▼
       │        A2 (2025) Consensus-Bottleneck
       │        (interpretable DL asset pricing)
       │              │
       │              ▼
       │        F4 (2026) From Index to Equity pre-training
       │
       └──▶ Black-Litterman 1992
                │
                ▼
            López de Prado 2016
            "Building Diversified Portfolios that
             Outperform Out of Sample" (HRP)
                │
                ▼
            Riskfolio-Lib / PyPortfolioOpt (open-source impl)
```

**Connections worth chasing:**
- A5 (MLP vs G-K-X) → directly tests whether neural factor models beat linear factors on US large-cap → ties to **A1's portfolio-construction critique**
- A2 (Consensus-Bottleneck) → addresses the **interpretability problem** of G-K-X
- Harvey-Liu-Zhu (2016) → the foundational **"factor zoo" warning** → A1 (2026) extends it by showing **portfolio construction** also drives spurious results

---

## ② Derivatives Pricing & Volatility Modeling — the vol thread

```
Black-Scholes 1973             Merton 1976
  Closed-form log-normal  ──▶  Jump-diffusion
  option pricing                  │
       │                          │
       ▼                          ▼
Heston 1993             ┌─────────────────────┐
Stochastic vol          │ Empirical vol       │
(closed-form via        │ "smile" / "smirk"   │
characteristic fn)      │ motivates SV/jumps  │
       │                └─────────────────────┘
       ▼
GARCH family
  Engle 1982 (ARCH)
    → Bollerslev 1986 (GARCH)
        → Nelson 1991 (EGARCH)
            → Glosten-Jagannathan-Runkle 1993 (GJR)
                → Engle 2002 (DCC)
                    │
                    ▼
              V2 (2026) Multi-Scale MS-GARCH
              V7 (2026) Operator-level ARCH
              V9 (2025) DBN for stressed ES
                    │
                    ▼
              Realized vol (Andersen-Bollerslev 2003)
                    │
                    ▼
              V5 (2026) Bayesian DCC with shrinkage
              V6 (2026) Composite-likelihood fGNP
                    │
                    ▼
              Rough volatility (Gatheral 2014)
                    │
                    ▼
              A4 (2026) VIX options in Bergomi
              (state-of-the-art for vol-surface fitting)
                    │
                    ▼
              Foundation-model vol
              F3 (2025) TimesFM fine-tuned
              → statistically beats GARCH via DM + GW tests
                    │
                    ▼
              V1 (2026) HMM + heavy-tail emissions
              → regime-conditional VaR for fat-tail GARCH misspecification
```

**Connections worth chasing:**
- F3 (TimesFM for realized vol) → **direct empirical test** of whether DL beats econometric benchmarks → ties to **B1 (falsification audit)** — does the win survive placebo tests?
- V1 (HMM + Student-t) → **complements** F3: when DL fails (regime shift), regime-switching models catch it → the case for **ensembling** both
- A4 (Bergomi VIX options) → connects to **microstructure thread M-series** (VIX options are themselves an LOB)

---

## ③ Time-Series ML / DL Forecasting — the forecasting thread

```
RNN/LSTM era                  Transformer era           Foundation-model era
  Fischer-Krauss 2018    ──▶  Vaswani 2017            ──▶  Chronos (Amazon 2024)
  Deep momentum                "Attention is All            TimesFM (Google 2024)
                               You Need"                    Timer (2024)
                                    │                       Kronos 2025 (✅ F1)
                                    ▼                       FinGPT-era
                              N-BEATS, N-HiTS                │
                              TFT (Lim 2021)                 ▼
                                    │                 F1 Kronos for finance
                                    ▼                       │ (+93% RankIC vs TSFM,
                              T1 (2026) HANET                │  +87% vs best
                              Macro-aware mixed-             │  non-pretrained)
                              frequency attention            ▼
                              →+ risk-adj returns      F2 (2026) Chronos for finance
                              in turbulent regimes     → MV beats UV for
                                    │                 Magnificent-7 + UST
                                    ▼
                              T5 (2026) Empirical MNQ intraday
                              → GBM ≈ LSTM at minute-freq
                              (questions value of DL here)
                                    │
                                    ▼
                              T2 (2026) Transformer + shifted
                              augmentation for non-stationarity
```

**Connections worth chasing:**
- T1 (HANET) + V1 (HMM-t) → both address **regime-shift fragility** of pure price-based DL → ties to **L1-L5 variable framework** (macro features as regime signals)
- T5 (LSTM ≈ GBM intraday) → **devils-advocate** paper — when does DL NOT help? Essential counterweight to F1/F2 foundation-model hype
- F1 (Kronos) + F3 (TimesFM fine-tuning) → both show pretraining helps, but **fine-tuning on financial data is essential** — directly contradicts "foundation model = zero-shot works everywhere" marketing

---

## ④ Reinforcement Learning for Trading — the execution thread

```
Optimal execution             RL era                    Modern RL infra
  Bertsimas-Lo 1998      ──▶  Moody-Saffell 2001     ──▶  FinRL (Yang et al. 2020)
  Almgren-Chriss 2000         (direct RL for              OpenAI Gym interface
                               trading)                   for finance
  (closed-form execution            │                     EIIE, PPO, A2C, DDPG
   schedules)                      ▼                            │
       │                    Deep RL (2015+)                     ▼
       │                    DDPG, PPO, SAC,              R7 (2026) FinRL-X
       │                    TD3, Rainbow                 AI-native modular
       │                           │                     end-to-end platform
       │                           ▼                           │
       │                    FinRL-Podracer 2021                ▼
       │                    (distributed RL)             R2 (2026) TT-DAC-PS
       │                    FinRL-Meta 2022             Twin-Target TD3 +
       │                    FinRL-DeepSeek 2024          policy smoothing
       │                           │                     → improves on
       │                           ▼                     Almgren-Chriss
       │                    R3 (2026) Multi-region
       │                    RL portfolio allocator
       │                    R4 (2026) Multi-pair crypto RL
       │                    R5 (2026) Exploratory RL for speculative
       │
       └──▶ Market simulators (needed for RL training)
            ABIDES (Byrd et al. 2020)
                 │
                 ▼
            R6 (2026) KineticSim
            (lightweight, real-time, open-source)
                 │
                 ▼
            M1 (2026) Inference-compute frontier
            (HFT-realistic LOB prediction)
```

**Connections worth chasing:**
- R6 (KineticSim) + R1 (FinRL-X) → together enable **RL training at scale without paying for ABIDES Cloud**
- R2 (TT-DAC-PS) + M2 (square-root law) → does RL-discovered execution still obey the square-root law? Empirical test would be very interesting
- R4 (crypto multi-pair RL) + C1 (cross-chain spillovers) → does RL learn to exploit attention-induced substitution?

---

## ⑤ LLM in Finance — the language thread

```
Static NLP                       FinBERT era              FinGPT / Bloomberg era
  Bag-of-words + TF-IDF   ──▶  FinBERT 2019          ──▶  BloombergGPT 2023
  Loughran-McDonald 2011       (financial-domain         FinGPT 2023
  financial sentiment          BERT)                     (open-source LLM)
       │                            │                          │
       ▼                            ▼                          ▼
  Classic sentiment          Embedding-based          Instruction-tuned
  scores (LM dictionary)     features fed to           financial LLMs
                             classifiers                (FinMA / PIXIU)
                                                          │
                                                          ▼
                                                  Time-aware debiasing
                                                  L7 (2026) DatedGPT ✅
                                                  (prevents look-ahead
                                                   bias in LLM pretraining)
                                                          │
                                                          ▼
                                                  LLM-as-feature-extractor
                                                  L5 (2026) Cross-stock semantic
                                                  L8 (2025) LLM factors in CN
                                                  L9 (2026) Segment disclosures
                                                          │
                                                          ▼
                                                  Agentic frameworks
                                                  L1 (2026) AI Economist
                                                  L2 (2026) CFO LLM study
                                                  R7 (2026) OOM-RL alignment
                                                          │
                                                          ▼
                                                  LLM-augmented evaluation
                                                  C12 (2026) Foresight Arena
                                                  (on-chain forecasting eval)
```

**Connections worth chasing:**
- L7 (DatedGPT) + B1 (spurious predictability) → the **LLM version of backtest overfitting** is LLM lookahead. DatedGPT debiases pretraining, but you still need B1's falsification audit on LLM features
- L3 (audit LLM BTC bias) → ties to **C1 (cross-chain spillovers)** — does LLM bias toward BTC explain why cross-chain diversification underperforms?
- L10 (Foresight Arena) → ties to **C2-C7 (Polymarket)** — same prediction-market venue used for both training and evaluation

---

## ⑥ Microstructure & Market Impact — the execution thread

```
Theory era                       Empirical era             DL/LLM era
  Kyle 1985                ──▶  Hasbrouck 1993         ──▶  DeepLOB (Zhang 2019)
  (informed trader              (VAR for price              (CNN on LOB images)
   model)                       impact)
  Glosten-Milgrom 1985           │                           │
  (bid-ask spread)               ▼                           ▼
       │                   Almgren-Chriss 2000        T5 (2026) GBM ≈ LSTM
       ▼                   (optimal execution)        on MNQ intraday
  Harris 1986                                              │
  Trading & Exchanges                                       ▼
  (the textbook)                                      M1 (2026) Inference-
       │                                               compute frontier
       ▼                                               (latency-efficient LOB)
  Cont 2001                                            M3 (2026) Long-memory
  (empirical properties                               trade signs +
   of returns)                                         square-root law
       │                                                    │
       ▼                                                    ▼
  Bouchaud et al. 2010                            M2 (2026) Square-root law
  (Trades, Quotes & Prices)                       confirmed on US large-cap
  → square-root law
       │
       ▼
  M4 (2026) Hierarchical GNN
  for commodity calendar spreads
       │
       ▼
  M7 (2026) Axiomatic Market Making
  M8 (2026) Informedness vs profitability trade-off
       │
       ▼
  DEX microstructure (NEW)
  C6 (2026) Hyperliquid market impact + adverse selection
  C2 (2026) Polymarket microstructure
  (8 stylized facts of a decentralized PM)
```

**Connections worth chasing:**
- M2 (square-root law US equity) + Almgren-Chriss (2000) → when execution algorithms obey square-root law, they're **near-optimal** → R2 (TT-DAC-PS) could test this empirically
- M7 (Axiomatic MM) + M8 (Informedness-PnL trade-off) → the **theory + empirics** of market making — ties to **R-series** (RL agents as market makers in simulation)
- C2 (Polymarket microstructure) → Polling on the **8 stylized facts** — does Polymarket behave more like equities (Kyle λ) or FX (depth profile)?

---

## ⑦ Crypto / DeFi / Prediction Markets — the frontier thread

```
Crypto theory                   DeFi era                  Prediction markets
  Nakamoto 2008            ──▶  Uniswap 2018           ──▶  Polymarket 2020+
  Bitcoin whitepaper              (x*y=k AMM)                  │
       │                          │                           ▼
       ▼                          ▼                      C2 (2026) Polymarket
  Buterin 2013              Curve 2020                    8 stylized facts
  Ethereum whitepaper        (stableswap)            ──▶  C3-C5 (2026)
       │                          │                   Leveraged event perps
       ▼                          ▼                          │
  ERC-20 / ERC-721          Aave / Compound                   ▼
  (tokens + NFTs)           (lending)                  C6-C7 (2026) Information
       │                          │                   leakage on PMs
       ▼                          ▼                          │
  Yield farming              C11 (2026) Liquid             ▼
  (Compound COMP 2020)       Restaking risk         C12 (2026) Foresight Arena
       │                          │                 (AI agents compete on PM)
       ▼                          ▼                          │
  Governance tokens          C14 (2026) DeFi           ▼
  (Maker DAO, 2020)          → TradFi spillover    C13 (2026) SoK RWA
       │                          │                 (tokenized Treasuries,
       ▼                          ▼                  real estate, commodities)
  C9 (2026) Crypto            Stablecoin era
  pricing with hidden         C15 (2026) Stablecoins
  factors                     in retail payments
       │
       ▼
  C10 (2025) Funding mechanics
  of crypto perps
       │
       ▼
  C8 (2025) 480M MC simulations
  of HODL strategy
       │
       ▼
  C1 (2026) Cross-Chain
  negative spillovers
  (ETH/SOL/BSC/ARB/AVAX)
```

**Connections worth chasing:**
- C1 (cross-chain spillovers) + C9 (crypto hidden factors) → does the negative spillover come from a shared latent factor (Fed policy? BTC dominance?) or true attention-induced substitution?
- C2 (Polymarket microstructure) + C12 (Foresight Arena) → **Polymarket data trains AI agents** which then compete on the same venue → reflexive dynamics worth studying (ties to **L6 AI Trading & Bubbles**)
- C13 (RWA SoK) → directly relevant to **treemap cells** (real estate, bonds, gold all have tokenization paths) → ties to **`treemap-primary-mapping.md`**

---

## ⚠️ Backtest Methodology — the guardrail thread (cross-cutting)

```
Deflated Sharpe              Combinatorial Purged CV      Falsification Audit
  López de Prado 2014  ──▶  López de Prado 2018    ──▶  B1 (2026) Spurious
  (multiple-testing            (CPCV for ML               Predictability
   correction for SR)           backtests)                 (workflow-level audit
       │                         │                          against placebo)
       │                         │                          │
       ▼                         ▼                          ▼
  Walk-forward efficiency    Embargo + purging          Detects selection-
  Bailey et al. 2014          gaps in CV folds           induced inflation
       │                         │                          │
       ▼                         ▼                          ▼
  Probabilistic SR           López de Prado             B2 (2026) Counterfactual
  (PSR)                      "Advances in Financial       measurement for DEX
                             Machine Learning" 2018        execution
                             (the textbook)
                                  │
                                  ▼
                             MLFinLab (Hudson-Thames)
                             open-source impl
                                  │
                                  ▼
                             DatedGPT L7 (2026)
                             (LLM look-ahead debiasing)
```

**Connections worth chasing:**
- **B1 must be applied to every paper in this corpus** — most ML-trading papers from 2020-2024 would not survive its audit. The **Spurious Predictability** paper is the **citation to weaponize** in any peer-review challenge.
- B1 + F1 (Kronos) → does Kronos's +93% RankIC survive B1's falsification? The paper doesn't run the test.
- L7 (DatedGPT) → the **LLM-specific version** of B1's audit — needed for any strategy that uses LLM features

---

## 🎯 Reading paths (suggested)

### Path A — "I want to build alpha"
1. **Foundations**: Markowitz → CAPM → Fama-French (1 day)
2. **Methodology**: López de Prado DSR + CPCV + MLFinLab (2 days)
3. **Modern**: Gu-Kelly-Xiu → A5 MLP → A2 Consensus-Bottleneck (1 day)
4. **Cutting edge**: F1 Kronos → F3 TimesFM for vol (1 day)
5. **Guardrail**: B1 Spurious Predictability audit (½ day)
6. **Apply**: build a Kronos-style factor on the project-07 pipeline output

### Path B — "I want to do execution / HFT"
1. **Theory**: Harris → Kyle → Glosten-Milgrom → Almgren-Chriss (3 days)
2. **Empirical**: Bouchaud square-root law → Cont empirical properties (2 days)
3. **Modern RL**: FinRL → R2 TT-DAC-PS → M1 inference-compute frontier (2 days)
4. **Infra**: ABIDES → R6 KineticSim (½ day)
5. **DEX microstructure**: C6 Hyperliquid → M8 informedness-PnL (1 day)
6. **Apply**: simulate on project-07 Binance OHLCV

### Path C — "I want to do crypto / DeFi / prediction markets"
1. **Crypto foundations**: Nakamoto → Buterin → Uniswap AMM math (2 days)
2. **Modern**: C9 hidden factors → C1 cross-chain spillovers (1 day)
3. **Prediction markets**: C2 Polymarket 8 facts → C6-C7 information leakage (1 day)
4. **RWA**: C13 SoK tokenization (½ day)
5. **On-chain risk**: C11 restaking risk → C14 DeFi-TradFi spillover (½ day)
6. **Apply**: integrate ccxt + CoinGecko into project-07, build BTC/ETH signal

### Path D — "I want to use LLMs in trading"
1. **Foundation**: Vaswani attention → BERT → FinBERT (1 day)
2. **LLM era**: BloombergGPT → FinGPT → FinMA/PIXIU (1 day)
3. **Debiasing**: L7 DatedGPT + B1 falsification audit (½ day)
4. **Features**: L5 cross-stock semantic → L8 CN futures factors (1 day)
5. **Agents**: L1 AI Economist → R7 OOM-RL alignment (1 day)
6. **Apply**: extract LLM sentiment from EDGAR 10-K filings, feed as L1-L5 macro features

---

## 📊 Paper age distribution (across all 5 lists)

| Era | Count | Share | Note |
|---|---|---|---|
| Pre-2000 (canon) | 12 | ~6% | foundational — must read |
| 2000-2014 (modern classics) | 35 | ~17% | empirical + theoretical |
| 2015-2020 (ML wave) | 50 | ~25% | factor zoo, deep RL, neural asset pricing |
| 2021-2023 (post-COVID) | 25 | ~13% | transformers + crypto boom |
| **2024-2026 (frontier)** | **77** | **~38%** | foundation models, agents, prediction markets |

> **Trend:** the 2024-2026 cohort is now the **largest single bucket** — keep this file updated quarterly. Cron schedule: `make refresh-papers` (TBD).

---

## 🛠️ How to use this map

1. Pick a **thread** (①–⑦ + ⚠️) that matches your project
2. Read the **canon → modern → frontier** papers in order
3. When a paper claims a result, follow the **connections** to the guardrail thread ⚠️ — does it survive B1's audit?
4. When you write a paper or strategy, cite the **full chain** (canon → your contribution)
5. When you build code, link the implementation repo to **at least one paper** in the thread (reproducibility)

---

## 🔁 Maintenance

- **Re-fetch arXiv quarterly** (every 90 days) to catch new submissions in q-fin.ST, q-fin.TR, q-fin.GN, q-fin.PR, q-fin.RM
- **Re-fetch CFArX / SSRN** for non-arXiv papers (Damodaran, Asness, etc.)
- **Cross-check** against [_paper-with-code.md](../github-projects/_paper-with-code.md) — if a frontier paper has no public code, lower its priority
- **Mark as 🟢/🟡/🟠** by citation count via Google Scholar (re-verify annually)

**Re-fetch command:**
```python
import requests
r = requests.get(
    "https://export.arxiv.org/api/query",
    params={
        "search_query": "cat:q-fin.ST+OR+cat:q-fin.TR+OR+cat:q-fin.GN+OR+cat:q-fin.PR+OR+cat:q-fin.RM",
        "max_results": 100,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    },
    headers={"User-Agent": "qualabinance-research/0.1"},
)
print(r.text[:2000])
```

---

**Built:** 2026-06-28 · **Curator:** QuantResearcher · **Last verified:** 2026-06-28 via arXiv API
