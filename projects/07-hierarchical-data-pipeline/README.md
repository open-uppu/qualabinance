# 📊 07 — Hierarchical Data Pipeline

> **L1-L5 hierarchical data ingestion for systematic strategies.**

## 🎯 Purpose

Implement the data pipeline as designed in [`../../knowledge/06-variable-framework/`](../../knowledge/06-variable-framework/):
- L1 Global (FRED, World Bank, IMF)
- L2 Continental (MSCI, BIS)
- L3 Country (FRED, OECD, BOT)
- L4 Market (yfinance, Binance, CRSP)
- L5 External (GPR, EPU, climate)

## 📚 Knowledge dependencies

- [`../../knowledge/06-variable-framework/`](../../knowledge/06-variable-framework/) — variable lists
- [`../../knowledge/05-resources/data-providers/_with-papers.md`](../../knowledge/05-resources/data-providers/_with-papers.md) — data source list

## 📁 Structure

```
07-hierarchical-data-pipeline/
├── README.md
├── SPEC.md
├── src/
│   ├── l1_global.py         # FRED, WB, IMF
│   ├── l2_continental.py    # MSCI, BIS
│   ├── l3_country.py        # FRED, OECD, BOT
│   ├── l4_market.py         # yfinance, Binance, …
│   ├── l5_external.py       # GPR, EPU, climate
│   ├── align.py             # Frequency alignment
│   ├── reduce.py            # PCA, factor extraction
│   └── store.py             # TimescaleDB / Parquet
└── tests/
```

## 🚀 Quick start

```bash
uv sync
uv run python src/l1_global.py --update
uv run python src/l4_market.py --assets AAPL,BTC-USD,EURUSD
uv run python src/align.py --frequency daily
```

## 🎯 Features

- [ ] All 5 levels implemented
- [ ] Frequency alignment (forward-fill, interpolation)
- [ ] Stationarity testing (ADF, KPSS)
- [ ] PCA dimensionality reduction
- [ ] Fama-French factor extraction
- [ ] Storage in Parquet / TimescaleDB
- [ ] Caching + rate-limit handling

## ⚠️ Considerations

- **API rate limits** — FRED 120 req/min, IMF similar
- **Data licensing** — check before commercial use
- **Survivorship bias** — include delisted assets
- **Vintages** — use ALFRED for point-in-time macro data

## 📚 Resources

- FRED API: https://fred.stlouisfed.org/docs/api/
- World Bank: https://datahelpdesk.worldbank.org/
- pandas-datareader for many sources

---

*Status: 🟡 scaffold.*
