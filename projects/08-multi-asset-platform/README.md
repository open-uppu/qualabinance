# 🏛️ 08 — Multi-Asset Platform (Production)

> **Production-grade multi-asset quant platform — research → backtest → risk → execution.**

## 🎯 Purpose

The culmination project: integrate everything from #01-#07 into a production-ready platform:
- Multi-broker abstraction
- Risk gate (institutional)
- Live + paper execution
- Observability + audit log
- Multi-tenancy (multiple accounts)

## 📚 Knowledge dependencies

ALL knowledge layer + ALL prior projects.

## 📁 Structure

```
08-multi-asset-platform/
├── README.md
├── SPEC.md
├── ARCHITECTURE.md
├── src/
│   ├── core/                # Domain models
│   │   ├── instrument.py    # Stock, future, option, crypto, bond
│   │   ├── order.py
│   │   ├── portfolio.py
│   │   └── account.py
│   ├── brokers/             # Broker adapters
│   │   ├── base.py          # BrokerAdapter interface
│   │   ├── binance.py
│   │   ├── alpaca.py
│   │   ├── interactive_brokers.py
│   │   └── oanda.py
│   ├── data/                # Data providers
│   │   ├── base.py          # DataProvider interface
│   │   ├── yfinance.py
│   │   ├── polygon.py
│   │   └── fred.py
│   ├── risk/                # Risk management
│   │   ├── gate.py          # RiskGate (every order passes here)
│   │   ├── var.py
│   │   ├── es.py
│   │   ├── drawdown.py
│   │   └── kill_switch.py
│   ├── execution/           # Execution engine
│   │   ├── engine.py
│   │   ├── slippage.py
│   │   └── smart_router.py
│   ├── strategies/          # Strategy registry
│   ├── signals/             # Alpha signals
│   ├── backtest/            # Backtest harness
│   ├── observability/       # Tracing, metrics, logs
│   │   ├── tracing.py
│   │   ├── metrics.py
│   │   └── audit_log.py
│   └── api/                 # FastAPI / gRPC
├── tests/
├── deployment/
│   ├── docker/
│   ├── k8s/
│   └── terraform/
└── docs/
```

## 🚀 Quick start

```bash
uv sync
uv run qualabinance init
uv run qualabinance backtest momentum --symbol BTC-USD --period 2y
uv run qualabinance paper-trade momentum --broker binance --capital 10000
uv run qualabinance live-trade momentum --broker binance --capital 1000 --ceo-approval
```

## 🎯 Features (v0)

- [ ] Broker adapter abstraction
- [ ] Data provider abstraction
- [ ] Risk gate (VaR, drawdown, position limit)
- [ ] Kill switch (manual + auto)
- [ ] Paper trading (Binance testnet)
- [ ] Audit log (every order + state change)
- [ ] Prometheus metrics
- [ ] Grafana dashboard
- [ ] Multi-account

## ⚠️ Hard constraints (per risk policy)

1. ❌ No live trading without `--ceo-approval` flag
2. ❌ No API keys in code (`.env` + scanner)
3. ❌ Max leverage 3x for crypto
4. ❌ Max position 10% NAV per asset
5. ✅ Max daily loss 2% NAV → kill
6. ✅ Max drawdown 15% → halt

## 📚 Resources

- See [`../../docs/risk-policy.md`](../../docs/risk-policy.md)
- See [`../../docs/compliance.md`](../../docs/compliance.md)
- See [`../../knowledge/05-resources/github-projects/_github-with-papers.md`](../../knowledge/05-resources/github-projects/_github-with-papers.md) for inspiration (FinRL, QuantConnect Lean, …)

---

*Status: ⏸️ pending — start after #01-#07 progress.*
