# ⚙️ Workflows — Qualabinance

> **Standardized procedures for recurring tasks.**

---

## 📋 Workflows

| Workflow | Purpose | Trigger |
|---|---|---|
| [daily-research-update](daily-research-update.md) | Update knowledge layer with new papers/repos | Daily at 06:00 GMT+7 |
| [market-data-refresh](market-data-refresh.md) | Refresh L1-L5 data pipeline | Hourly during market hours |
| [risk-metrics-check](risk-metrics-check.md) | Check all risk thresholds | Every 15 min during trading |
| [weekly-backtest-review](weekly-backtest-review.md) | Review all active strategies | Sunday 22:00 GMT+7 |
| [monthly-strategy-audit](monthly-strategy-audit.md) | Full strategy audit | 1st of month |

---

## 🎯 Workflow conventions

- Each workflow is a markdown file with:
  - **Trigger** — when does it run
  - **Inputs** — what data needed
  - **Steps** — ordered procedure
  - **Outputs** — artifacts produced
  - **Failure handling** — what if it breaks

- Workflows can be:
  - **Manual** — run on demand
  - **Scheduled** — cron job
  - **Event-driven** — triggered by condition

---

## 🔗 Related

- [`../state/loop-engineering/STATE.md`](../state/loop-engineering/STATE.md) — loop state
- [`../docs/risk-policy.md`](../docs/risk-policy.md) — risk rules

---

*Workflow index v0.1.0 · 2026-06-28*
