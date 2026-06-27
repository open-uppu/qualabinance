# 🎯 Qualabinance — Loop Engineering State

> **Durable state for the Qualabinance quant platform.**

**Last updated**: 2026-06-28 00:55 GMT+7
**Status**: Bootstrap complete, awaiting first loop activation

---

## 🧬 Overview

This file is the **durable state** for Qualabinance development. It follows the CEO-Profile loop engineering pattern:
- **STATE.md** = durable state (this file)
- **run-log-YYYY-MM-DD.md** = event log
- **heartbeat-watcher.sh** = PM enforcement

---

## 📊 Loop status

| Loop | Target | Status | Cost | Notes |
|---|---|---|---|---|
| L1 | Bootstrap (rename + knowledge + projects scaffold) | ✅ done | $0.00 | 28 files created |
| L2 | Foundations notebooks (#01) | ⏸️ pending | — | Awaiting activation |
| L3 | Stock analysis (#02) | ⏸️ pending | — | Awaiting activation |
| L4 | Options pricer (#03) | ⏸️ pending | — | Awaiting activation |
| L5 | Backtest engine (#04) | ⏸️ pending | — | Awaiting activation |
| L6 | GARCH volatility (#05) | ⏸️ pending | — | Awaiting activation |
| L7 | Portfolio optimizer (#06) | ⏸️ pending | — | Awaiting activation |
| L8 | Hierarchical data pipeline (#07) | ⏸️ pending | — | Awaiting activation |
| L9 | Multi-asset platform (#08) | ⏸️ pending | — | Final project |

---

## 💰 Cost tracking

| Item | Budget | Used | Remaining |
|---|---|---|---|
| **Per-loop cap** | $5.00 | $0.00 | $5.00 |
| **Weekly cap** | $50.00 | $0.00 | $50.00 |
| **Alert at 80%** | $40.00 | — | — |
| **Stop at 100%** | $50.00 | — | — |

---

## 📦 Artifacts shipped (L1)

### Knowledge layer
- 6 research files (~270 verified entries)
- 6 domain overview READMEs (foundation scaffold)

### Projects layer
- 8 project scaffolds with README + structure
- projects/README.md (master index)

### Company + Agent
- companies/qualabinance.md (profile + risk policy)
- agents/quant-researcher.md (15 fields + heartbeat)

### Documentation
- docs/trademark.md (Binance wordmark note)
- docs/risk-policy.md (hard rules)
- docs/compliance.md (multi-jurisdiction)
- docs/chinese-wall.md (isolation from other 4 companies)

### Config
- .gitignore (Python + secrets + data)
- pyproject.toml (uv workspace)
- .github/workflows/ci.yml (CI scaffold)

**Total**: ~28 files, ~600KB

---

## 🎯 Next 5 priorities

1. **Activate L2** — Foundations notebooks (#01)
   - 8 notebooks (calculus, linalg, prob, stats, time-series, numpy, pandas, viz)
   - Estimated time: 2-3 hours of work
2. **Activate L3** — Stock analysis (#02)
   - yfinance fetcher + Plotly dashboard
   - Estimated time: 3-4 hours
3. **Activate L4** — Options pricer (#03)
   - Black-Scholes + Greeks + Streamlit UI
   - Estimated time: 2-3 hours
4. **Activate L5** — Backtest engine (#04)
   - Vectorized + purged CV + deflated Sharpe
   - Estimated time: 4-6 hours
5. **Re-verify research papers** — 23 papers in `_q1-ml-finance.md` need re-verification (rate-limited during initial research)

---

## 🚨 Risks

| Risk | Mitigation |
|---|---|
| Live trading accidents | paper-first, CEO approval for live |
| API key leak | .env + scanner + gitignore |
| Data provider license | check license per provider |
| Overfitting | deflated Sharpe, purged CV |
| Look-ahead bias | walk-forward validation |
| Survivorship bias | include delisted assets |

---

## 🔗 Cross-references

- [`../../companies/qualabinance.md`](../../companies/qualabinance.md) — company profile
- [`../../agents/quant-researcher.md`](../../agents/quant-researcher.md) — agent spec
- [`../../docs/risk-policy.md`](../../docs/risk-policy.md) — hard rules
- [`../../docs/chinese-wall.md`](../../docs/chinese-wall.md) — isolation
- `run-log-2026-06-28.md` — today's events

---

*Maintained by: CEO-Profile loop · v0.1.0 · 2026-06-28*
