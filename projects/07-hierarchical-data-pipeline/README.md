# 📊 07 — Hierarchical Data Pipeline

> **L1-L5 hierarchical data ingestion for systematic strategies.**
> Status: ✅ **working skeleton** (32 series configured, 11/11 tests pass, live yfinance pull verified)

## 🎯 Purpose

Implement the data pipeline as designed in [`../../knowledge/06-variable-framework/`](../../knowledge/06-variable-framework/):

- **L1 Global** (FRED, World Bank, IMF)
- **L2 Continental** (yfinance: S&P500, Nikkei, STOXX, MSCI EM, SET)
- **L3 Country** (FRED, World Bank, BOT — focus on TH / US / CN / JP / EU / UK)
- **L4 Market** (yfinance OHLCV, Binance via ccxt, CoinGecko)
- **L5 External** (GPR, EPU, GSCPI, Fear & Greed)

📚 **Series catalogue:** [`../../knowledge/06-variable-framework/L1-L5-series-codes.md`](../../knowledge/06-variable-framework/L1-L5-series-codes.md)
📚 **Treemap → primary mapping:** [`../../knowledge/05-resources/data-providers/treemap-primary-mapping.md`](../../knowledge/05-resources/data-providers/treemap-primary-mapping.md)

---

## 📁 Structure

```
07-hierarchical-data-pipeline/
├── README.md                    ← you are here
├── SPEC.md                      ← detailed spec
├── Makefile                     ← convenience targets
├── .env.example                 ← API keys template (copy to repo .env)
├── src/
│   ├── __init__.py
│   ├── config.py                ← Series catalogue + API keys + paths
│   ├── ingest.py                ← Source classes (FRED, WB, yfinance, ccxt, manual_csv, coingecko)
│   ├── transform.py             ← log_return / yoy_pct / diff / level + ADF stationarity
│   ├── align.py                 ← Frequency alignment with publication-lag (no look-ahead)
│   ├── store.py                 ← DuckDB writer + Parquet snapshots
│   └── cli.py                   ← `python -m src.cli {refresh,align,coverage}`
├── tests/
│   ├── __init__.py
│   └── test_pipeline.py         ← 11 unit tests (offline, no API)
└── data/                        ← gitignored: DuckDB + Parquet
    ├── qualabinance.duckdb
    └── parquet/
        ├── raw/{series_id}.parquet
        └── aligned/wide_daily.parquet
```

---

## 🚀 Quick start

```bash
# 1. Install data-pipeline extras
cd qualabinance
uv venv
source .venv/bin/activate
uv pip install -e ".[data-pipeline,dev]"

# 2. Copy env template, fill in keys
cp projects/07-hierarchical-data-pipeline/.env.example .env
# Edit .env and add at minimum: FRED_API_KEY (free at fred.stlouisfed.org)

# 3. Run tests (offline, no API needed)
cd projects/07-hierarchical-data-pipeline
make test

# 4. Pull data
make refresh          # all 32 series
make refresh-L1       # only L1 (macro + global)
make refresh-L3-TH    # only Thailand country-level

# 5. Build wide daily aligned panel
make align

# 6. Inspect coverage
make coverage
```

---

## 🧩 Design principles

1. **Config-driven** — every series lives in `config.DEFAULT_SERIES`. New series = add one line, no code change.
2. **Provenance everywhere** — every pull stamps `source` and `fetched_at`. Every save records the snapshot date.
3. **No look-ahead bias** — `align.py` shifts macro observations back by `publication_lag` days BEFORE forward-fill (rule: `monthly=30d, quarterly=60d, weekly=7d, daily=1d`).
4. **Tests offline** — `tests/test_pipeline.py` runs against synthetic fixtures, so CI doesn't hit external APIs.
5. **Reproducible** — `make refresh && make align` rebuilds the entire pipeline from scratch.

---

## 📊 What's wired today

| Source | Status | Series count |
|---|---|---|
| FRED | ✅ live | 11 (FEDFUNDS, VIXCLS, DGS10, BAML spreads, etc) |
| World Bank | ✅ live | 4 (global GDP, US/TH GDP, TH CPI) |
| yfinance | ✅ live verified (24k+ S&P rows) | 10 (S&P, NASDAQ, Nikkei, STOXX, EEM, SET, AAPL, MSFT, BTC, ETH) |
| ccxt (Binance) | ✅ wired (tested via code) | 1 (BTC/USDT) |
| Manual CSV | ✅ wired (user drops CSV in `data/parquet/raw/`) | 3 (GPR, EPU, GSCPI) |
| CoinGecko | ✅ wired (Fear & Greed) | 1 |

---

## 🎯 Features checklist

- [x] Config-driven series catalogue (32 series across L1-L5)
- [x] FRED + World Bank + yfinance + ccxt + manual + coingecko connectors
- [x] Frequency alignment with publication-lag rule
- [x] Stationarity testing (ADF)
- [x] DuckDB analytical store
- [x] Parquet snapshots (raw + aligned)
- [x] CLI: `refresh` / `align` / `coverage`
- [x] Offline tests (11/11 passing)
- [x] Makefile for common ops
- [x] .env.example for secrets
- [ ] PCA / factor extraction (`reduce.py`) — pending
- [ ] Cron / scheduled refresh — pending
- [ ] Thailand-specific (BOT API, ThaiBMA, SETSMART) connectors — pending
- [ ] Live data validation (alert if value moves > 10%) — pending

---

## 🔁 Next loops

| # | Target | Status |
|---|---|---|
| 7.1 | PCA / factor extraction module | ⏸️ pending |
| 7.2 | Thailand connectors (BOT, ThaiBMA, SETSMART) | ⏸️ pending |
| 7.3 | Cron + heartbeat watcher (daily refresh) | ⏸️ pending |
| 7.4 | Data validation alerts (CI Sanity check) | ⏸️ pending |
| 7.5 | First feature panel for `projects/02-stock-analysis/` | ⏸️ pending |

---

## 🛡️ Compliance

- Bank data isolation enforced: no `bank.md` data ever touches this pipeline.
- All API keys loaded from `.env` (gitignored).
- `safe_repr()` masks keys in logs.
- Raw pulls immutable (Parquet snapshot per series).

---

**Built:** 2026-06-28 · **Version:** v0.1.0 · **Owner:** Qualabinance / QuantResearcher
