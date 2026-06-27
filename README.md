# 🧪⚡ Qualabinance

> **Multi-asset quantitative finance platform — research, backtest, risk, and live trading across all tradeable assets.**

[![GitHub](https://img.shields.io/badge/github-open--uppu%2Fqualabinance-blue)](https://github.com/open-uppu/qualabinance)
[![Status](https://img.shields.io/badge/status-MVP%20scaffold-yellow)]()
[![License](https://img.shields.io/badge/license-TBD-lightgrey)]()
[![Python](https://img.shields.io/badge/python-3.12%2B-blue)]()
[![Manager](https://img.shields.io/badge/uv-Astral-purple)]()

> ⚠️ **Trademark note**: The name "Qualabinance" is a portmanteau of *Quant + Lab + Alpha + Binance*. This is a personal R&D / open-source project — **not affiliated with, endorsed by, or sponsored by Binance Holdings Ltd.** See [`docs/trademark.md`](docs/trademark.md) for safe-use guidance.

---

## 🎯 Mission

Build a **production-grade, multi-asset quant platform** that:

1. **Researches** alpha across equities, ETFs, futures, options, FX, commodities, crypto, prediction markets, and tokenized RWAs
2. **Backtests** strategies with proper methodology (purged CV, deflated Sharpe, combinatorial purged CV)
3. **Manages risk** institutionally (VaR, ES, drawdown caps, kill-switches)
4. **Executes** orders across broker adapters with paper-first safety
5. **Observes** every decision (signals → risk gate → order → fill → PnL trace)

---

## 🌐 Asset Class Coverage

| Class | Examples | Data | Live Trading |
|---|---|---|---|
| 📈 Equities | SET, NYSE, NASDAQ, HKEX, TSE | yfinance, Polygon, CRSP | IB, Alpaca |
| 📊 ETFs | SPY, QQQ, KXI, TDEX | same as equities | same |
| 🏛️ Bonds | Gov, Corp, T-bills | FRED, OpenBond, Refinitiv | IB |
| 📜 Futures | ES, NQ, CL, GC, SET50 | CME, Quandl | IB, NinjaTrader |
| 🎯 Options | Equity, Index, Weekly | CBOE, ORATS, Deribit | IB, Deribit |
| ₿ Crypto Spot | BTC, ETH, alts | Binance, Kaiko, Glassnode | Binance, OKX |
| ⚡ Crypto Derivatives | Perp, Futures, Options | Deribit, Binance | Deribit, Binance |
| 💱 FX | Majors, EM | OANDA, BIS | OANDA, IB |
| 🛢️ Commodities | Oil, Gold, Agri | CME, Quandl | IB |
| 🏠 REITs | REIT funds | yfinance | IB |
| 🎰 Prediction | Polymarket, Kalshi | on-chain | on-chain |
| 🪙 Tokenized RWAs | Onchain treasuries | MakerDAO, Paxos | on-chain |

---

## 📁 Repo Structure

```
qualabinance/
├── README.md                          ← you are here
├── companies/
│   └── qualabinance.md                ← company profile + risk policy
├── agents/
│   └── quant-researcher.md            ← agent spec (15 fields + heartbeat)
├── knowledge/                         ← ⭐ curated research from Q1 sources
│   ├── README.md
│   ├── 00-INDEX.md                    ← master index
│   ├── 01-foundations/                ← math, stats, programming
│   ├── 02-finance/                    ← portfolio, derivatives, vol, risk
│   ├── 03-career-paths/               ← QR / QT / QD / Risk Quant
│   ├── 04-mindset/                    ← quant mindset
│   ├── 05-resources/                  ← papers, repos, books, data
│   │   ├── papers/                    ← Q1 papers (ML, portfolio, econ)
│   │   ├── github-projects/           ← GitHub repos with companion papers
│   │   ├── books/                     ← canonical textbooks
│   │   └── data-providers/            ← data APIs with methodology
│   └── 06-variable-framework/         ← L1-L5 hierarchical variables
├── projects/                          ← implementation projects
│   ├── 01-foundations-notebooks/
│   ├── 02-stock-analysis/
│   ├── 03-options-pricer/
│   ├── 04-backtest-engine/
│   ├── 05-garch-volatility/
│   ├── 06-portfolio-optimizer/
│   ├── 07-hierarchical-data-pipeline/
│   └── 08-multi-asset-platform/       ← production platform (final)
├── docs/
│   ├── trademark.md
│   ├── risk-policy.md
│   ├── compliance.md
│   └── chinese-wall.md
├── workflows/
├── state/loop-engineering/
├── .github/workflows/ci.yml
├── pyproject.toml
└── .gitignore
```

---

## 🔴 Hard Rules (Risk Policy)

> See [`docs/risk-policy.md`](docs/risk-policy.md) for full details.

1. ❌ **No live trading** in v0/v1 — paper trading only
2. ❌ **No API keys in code** — `.env` + secret scanner + gitignore
3. ❌ **No leverage > 3x** for crypto by default
4. ❌ **No single position > 10%** NAV by default (override requires justification)
5. ✅ **Max daily loss = 2% NAV** → kill switch triggers
6. ✅ **Max drawdown = 15%** → strategy halted, review required
7. ✅ **Heartbeat mandatory** every 2 min for any spawned sub-agent
8. ✅ **Paper-first** — every strategy must backtest + paper trade before live

---

## 🚀 Quick Start

```bash
# Clone
git clone https://github.com/open-uppu/qualabinance.git
cd qualabinance

# Install (using uv)
uv sync

# Start with notebook (foundations)
uv run jupyter lab projects/01-foundations-notebooks/
```

---

## 📊 Loop Status

See [`state/loop-engineering/STATE.md`](state/loop-engineering/STATE.md) for live project state.

| Loop | Target | Status |
|---|---|---|
| #1 | Foundations notebooks + global market taxonomy | 🔵 scaffold |
| #2 | Stock analysis w/ yfinance + dashboard | ⏸️ pending |
| #3 | Black-Scholes options pricer | ⏸️ pending |
| #4 | Backtest engine (vectorized) | ⏸️ pending |
| #5 | GARCH volatility | ⏸️ pending |
| #6 | Portfolio optimizer (Markowitz + BL + HRP) | ⏸️ pending |
| #7 | Hierarchical L1-L5 data pipeline | ⏸️ pending |
| #8 | Multi-asset platform (production) | ⏸️ pending |

---

## 🧬 Knowledge Highlights

- 📄 **147 Q1 / accepted papers** across ML-finance, portfolio/risk, econometrics
- 💻 **40+ GitHub repos** with companion papers (FinRL, FinGPT, QuantLib, pyfolio, ABIDES, …)
- 📚 **34 canonical textbooks** with ISBNs + reading paths
- 🔌 **50+ data providers** with methodology papers (FRED, CRSP, Kaiko, LOBSTER, …)
- 🌍 **12 asset classes** with execution venues
- 📊 **5-level hierarchical variable framework** (Global → Continental → Country → Market → External)

---

## 👤 Owner

- **CEO** of `open-uppu` org (also: Bank · Software House · DungWai · omyxia)
- **Company #5**: Qualabinance (independent, separate Chinese wall)

---

## 📜 License

TBD — open-source (Apache-2.0 or MIT) when productionized.

---

## 🙏 Acknowledgments

Built on the shoulders of:
- **Marcos López de Prado** — *Advances in Financial Machine Learning*
- **John Hull** — *Options, Futures, and Other Derivatives*
- **Steven Shreve** — *Stochastic Calculus for Finance*
- **Quantitative Finance community** — open-source ecosystem

---

*Last updated: 2026-06-28 — bootstrap complete, knowledge layer loaded, awaiting live data + execution engine.*
