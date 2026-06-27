# 🧪⚡ Qualabinance — Company Profile

> **Multi-asset quantitative finance platform — research, backtest, risk, and live trading.**

| Field | Value |
|---|---|
| **Org** | `open-uppu` (GitHub) |
| **Repo** | `open-uppu/qualabinance` |
| **Company ID** | 5 |
| **Status** | MVP scaffold (2026-06-28) |
| **Owner** | CEO |
| **Department** | Platform Engineering (Quant Research & Execution) |
| **Chinese wall** | 🔒 Isolated from Bank, Software House, DungWai, omyxia |

---

## 🎯 Mission

Build a **production-grade, multi-asset quantitative finance platform** covering research → backtest → risk → execution across every tradeable asset class.

---

## 📐 Scope

### In scope
- Research & alpha generation (factors, signals, ML/RL)
- Backtesting (vectorized, event-driven)
- Risk management (institutional-grade)
- Paper trading & live execution (multi-broker)
- Portfolio optimization (MVO, Black-Litterman, HRP, Risk Parity)
- Market data ingestion (L1-L5 hierarchical framework)
- Dashboard & observability

### Out of scope
- ❌ Custody / wallet management (use existing brokers)
- ❌ Compliance-as-a-Service (use broker-native)
- ❌ Social trading / copy-trading
- ❌ Retail-facing UI (this is a platform, not a product)

---

## 🏛️ Governance

### Decision rights
- **CEO**: approves all live trading, position limit overrides, broker integrations
- **Quant Researcher agent**: research, backtest, paper-trade (autonomous)
- **Risk gate**: every order must pass `RiskGate.check(order)` before reaching broker
- **PM (CEO-Profile)**: monitors loops, enforces heartbeat, manages cost caps

### Risk tiers
- **Tier 1 — Paper**: unlimited, full logging required
- **Tier 2 — Live small** (<$1k): auto-approved, daily PnL review
- **Tier 3 — Live medium** ($1k-$50k): PM review weekly
- **Tier 4 — Live large** (>$50k): CEO approval per strategy

---

## 🔴 Hard Rules

> See [`../docs/risk-policy.md`](../docs/risk-policy.md) for full details.

1. ❌ No live trading in v0/v1
2. ❌ No API keys in code (`.env` + scanner)
3. ❌ No leverage > 3x for crypto
4. ❌ No single position > 10% NAV (override = CEO)
5. ✅ Max daily loss = 2% NAV → kill-switch
6. ✅ Max drawdown = 15% → strategy halted
7. ✅ Heartbeat 2min for any sub-agent
8. ✅ Paper-first — backtest + paper trade before live

---

## 🧬 Architecture Principles

1. **Abstraction first** — Broker / Data / Instrument interfaces
2. **Risk before everything** — `RiskGate` is unconditional
3. **Observability always** — every decision traceable (signal → risk → order → fill)
4. **Paper-first always** — live trading is opt-in per strategy
5. **Multi-tenancy** — multiple accounts/portfolios in one platform
6. **Fail-safe defaults** — when uncertain, don't trade
7. **Immutable audit log** — every order, every state change

---

## 📚 Knowledge Assets

- 📄 147 Q1 / accepted academic papers (curated)
- 💻 40+ GitHub repos with companion papers
- 📚 34 canonical textbooks (ISBNs verified)
- 🔌 50+ data providers with methodology papers
- 🌐 12 asset classes + multi-asset strategies
- 📊 L1-L5 hierarchical variable framework

---

## 🌏 Target Markets (priority)

| Phase | Asset Class | Data Source | Broker |
|---|---|---|---|
| v0 | Crypto spot + perps | Binance, Kaiko | Binance |
| v0 | US equities | Polygon, yfinance | Alpaca (paper) |
| v1 | Thai equities + futures | SET Smart, TFEX | IB / KGI (paper) |
| v2 | Options (US + crypto) | Deribit, ORATS | IB, Deribit |
| v3 | FX | OANDA | OANDA |
| v4 | Bonds | OpenBond, FRED | IB |
| v5 | Tokenized RWAs | on-chain | on-chain |

---

## 🔗 Cross-company rules

- ✅ Bank secrets stay in `bank.md`
- ✅ Software House secrets stay in `software.md`
- ✅ DungWai secrets stay in `dungwai.md`
- ✅ omyxia specs stay in `omyxia.md`
- ✅ **Qualabinance secrets stay in `qualabinance.md`** (this file)
- ❌ No cross-pollination of code/data/team without explicit CEO OK
- ❌ No bank data in quant strategies (compliance + COI)

---

## 📋 Operating Manual

1. New strategy = open an issue → spec → backtest → paper → review → live
2. New data source = verify license + methodology paper
3. New broker = dry-run + paper trade 30 days minimum
4. Any deviation from hard rules = CEO approval required

---

*Owner: CEO · Last updated: 2026-06-28 · Bootstrap v0.1.0*
