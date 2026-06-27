# 🔴 Risk Policy — Qualabinance

> **Hard rules for trading and platform operation. NO EXCEPTIONS without CEO approval.**

---

## 🎯 Why this exists

Real money + algorithmic execution = potential for catastrophic loss. These rules exist to:
- Prevent accidental financial ruin
- Enforce institutional-grade discipline
- Enable audit + post-mortem
- Comply with regulations across jurisdictions

---

## 🔴 Hard rules (NEVER VIOLATE without CEO approval)

### 1. ❌ No live trading in v0/v1
- v0/v1 = paper trading only
- Live trading requires explicit CEO approval per strategy
- Use testnet/sandbox where available (Binance testnet, Alpaca paper)

### 2. ❌ No API keys in code
- All secrets in `.env` files (gitignored)
- Use secret manager in production (AWS Secrets Manager, Vault)
- Run `detect-secrets` in CI (already in `.github/workflows/ci.yml`)
- Rotate keys every 90 days minimum

### 3. ❌ No leverage > 3x for crypto
- Default leverage cap = 1x (spot only)
- 2x requires written justification + CEO approval
- 3x maximum, requires daily review

### 4. ❌ No single position > 10% NAV
- Default position size cap = 5% NAV
- 10% requires justification + CEO approval
- Aggregate correlated positions counted together

### 5. ✅ Max daily loss = 2% NAV → kill switch
- Hit 2% loss in single day → automated kill
- All positions closed, no new orders for 24h
- Post-mortem required before re-activation

### 6. ✅ Max drawdown = 15% → strategy halted
- Strategy-level drawdown > 15% → halt
- Portfolio-level drawdown > 15% → halt all strategies
- Full review + CEO approval to re-enable

### 7. ✅ Heartbeat mandatory for sub-agents
- Every spawned sub-agent writes to `state/loop-engineering/run-log-YYYY-MM-DD.md` every 2 min
- Format: `HH:MM:SS GMT+7 | LOOP#N | TASK_ID | STATUS | DETAIL`
- 4+ min silent = PM kills + respawns

### 8. ✅ Paper-first
- Every new strategy must:
  1. Backtest (purged CV, deflated Sharpe)
  2. Paper trade 30+ days minimum
  3. Pass risk review
  4. Get CEO approval
- Then live trading with small capital ($1k initial)

---

## 📋 Operating procedures

### New strategy
1. Open issue → spec → code
2. Backtest with purged CV + deflated Sharpe
3. Run paper trade 30+ days
4. Risk review (VaR, ES, max DD)
5. CEO approval
6. Live with small capital + close monitoring

### New data source
1. Verify license (commercial OK?)
2. Verify methodology paper exists
3. Test pull (rate limits, errors)
4. Cache + integrate
5. Document in `knowledge/05-resources/data-providers/_with-papers.md`

### New broker
1. Paper trade 30+ days
2. Test all order types
3. Test error handling (network, rate limit)
4. Test reconciliation
5. CEO approval before live

### Incident response
1. **Detected anomaly** → kill switch immediate
2. **Assess damage** — what went wrong, what was exposed
3. **Contain** — revoke keys, disable integrations
4. **Eradicate** — fix root cause
5. **Recover** — re-enable with monitoring
6. **Post-mortem** — document in `docs/incidents/`

---

## 🛡️ Defense-in-depth

### Layer 1 — Strategy level
- Position size limit
- Per-strategy max DD
- Per-strategy max daily loss

### Layer 2 — Portfolio level
- Aggregate position limit
- Portfolio max DD
- Portfolio max daily loss

### Layer 3 — Account level
- Broker-level kill switch
- Margin call handling
- Liquidation buffer

### Layer 4 — Operational
- Heartbeat watcher (PM)
- Cost cap enforcement
- Secret scanner
- Dependency audit

---

## 📊 Metrics tracked

| Metric | Threshold | Action |
|---|---|---|
| Daily PnL | < -2% | Kill switch |
| Weekly PnL | < -5% | Halt new strategies |
| Monthly PnL | < -10% | Full review |
| Drawdown (peak to trough) | > 15% | Strategy halted |
| Sharpe ratio (rolling 60d) | < 0.5 | Review |
| Deflated Sharpe | < 1.0 | Likely overfit |
| Slippage (vs expected) | > 2x | Pause + investigate |
| Order rejection rate | > 5% | Pause + investigate |
| API error rate | > 1% | Investigate |

---

## 🔄 Review cadence

- **Daily**: PnL, risk metrics, anomaly check
- **Weekly**: Strategy performance review
- **Monthly**: Risk policy review (CEO + agent)
- **Quarterly**: Full audit + policy revision

---

## 🔗 References

- [`chinese-wall.md`](chinese-wall.md) — isolation from other companies
- [`compliance.md`](compliance.md) — regulatory considerations
- [`../companies/qualabinance.md`](../companies/qualabinance.md) — company profile

---

*Risk Policy v1.0 · 2026-06-28 · Authoritative — supersedes all prior versions*
