# 📐 SPEC — Hierarchical Data Pipeline (Project 07)

> **Detailed implementation contract** for Project 07. README is the user view; this is the engineering view.

---

## 1. Goals

1. Pull **32 series** across 5 levels (L1-L5) from **6 source types** (FRED, World Bank, yfinance, ccxt, manual CSV, CoinGecko)
2. Store raw pulls **immutably** as Parquet (one file per series)
3. Track provenance: `source`, `fetched_at` per row
4. Build a **wide daily aligned panel** with publication-lag-aware forward-fill (no look-ahead)
5. Make everything **reproducible** via `make refresh && make align`
6. Make everything **testable** offline via synthetic fixtures (no API needed for CI)

---

## 2. Non-goals

- ❌ Real-time streaming (cron-scheduled batch only)
- ❌ Order execution (separate project)
- ❌ ML model training (consumes the panel; lives in `projects/02-stock-analysis/`)
- ❌ Proprietary data (Bloomberg/Refinitiv) — free + open sources only

---

## 3. Architecture

```
┌───────────────────────────────────────────────────────────────┐
│ Series catalogue (config.py)                                  │
│  32 Series objects, each with: id, level, source, code,       │
│  frequency, transform, country                                │
└─────────────────────────┬─────────────────────────────────────┘
                          │
                          ▼
┌───────────────────────────────────────────────────────────────┐
│ Source registry (ingest.py)                                   │
│  Map source-name → Source class. Each Source.fetch(series)    │
│  returns: pd.DataFrame with 'value' col + DatetimeIndex UTC   │
└─────────────────────────┬─────────────────────────────────────┘
                          │
                          ▼
┌───────────────────────────────────────────────────────────────┐
│ Transform (transform.py)                                      │
│  Apply series.transform ∈ {level, log_return, yoy_pct, diff}  │
│  Optional: ADF stationarity flag                              │
└─────────────────────────┬─────────────────────────────────────┘
                          │
            ┌─────────────┴──────────────┐
            ▼                            ▼
┌──────────────────────┐    ┌──────────────────────────┐
│ Parquet raw snapshot │    │ DuckDB upsert            │
│ (immutable per pull) │    │ (one table, replace per  │
│ data/parquet/raw/    │    │ series_id)               │
└──────────────────────┘    └─────────────┬────────────┘
                                          │
                                          ▼
                          ┌──────────────────────────┐
                          │ align.py                 │
                          │ - shift by publication_lag│
                          │ - reindex to daily grid  │
                          │ - forward-fill           │
                          │ Output: wide_daily panel│
                          └──────────────────────────┘
                                          │
                                          ▼
                          ┌──────────────────────────┐
                          │ data/parquet/aligned/    │
                          │ wide_daily.parquet       │
                          │ (ML-ready feature panel) │
                          └──────────────────────────┘
```

---

## 4. Contract — Series

```python
class Series(BaseModel):
    id: str              # unique slug, e.g. "fred_fedfunds"
    level: Literal["L1","L2","L3","L4","L5"]
    asset_class: Literal["equity","etf","bond","fx","commodity","crypto","macro","alt"]
    source: str          # one of: fred, worldbank, yfinance, binance, manual_csv, coingecko
    code: str            # native series code (FRED id, ticker, ...)
    description: str
    frequency: Literal["daily","weekly","monthly","quarterly","annual"]
    transform: Literal["level","log_return","yoy_pct","diff"]
    start_date: str | None
    country: str | None  # ISO-2 for L3 (TH, US, CN, JP, EU, UK, ...)
```

**Invariants:**
- `id` is unique across the catalogue.
- `transform ∈ {"log_return", "yoy_pct"}` is only valid for `asset_class ∈ {"equity", "fx", "commodity", "etf", "crypto"}`.
- `transform == "yoy_pct"` requires ≥ 252 daily observations or ≥ 12 monthly.

---

## 5. Contract — Source

```python
class Source(ABC):
    name: str
    def fetch(self, series: Series) -> pd.DataFrame:
        """Returns:
        - pd.DataFrame with DatetimeIndex (UTC, tz-aware) named 'date'
        - columns: 'value' (float), 'source' (str), 'fetched_at' (datetime)
        - sorted ascending by index
        """
```

**Invariants:**
- `value` is numeric (NaN allowed but discouraged)
- All datetime-aware, UTC, sorted ascending
- Retries with exponential backoff (3 attempts, 2-30s)
- Raises `RuntimeError` on unrecoverable failure

---

## 6. Contract — Transform

| Input `transform` | Output |
|---|---|
| `level` | unchanged |
| `log_return` | `log(P_t) - log(P_{t-1})`, drop leading NaN |
| `yoy_pct` | `(P_t / P_{t-N}) - 1` where N=252 (daily) or 12 (monthly+), drop leading NaN |
| `diff` | `P_t - P_{t-1}`, drop leading NaN |

`add_stationarity_flag(df)` adds: `adf_stat`, `adf_pvalue`, `is_stationary` (p < 0.05).

---

## 7. Contract — Align

For each series, apply `publication_lag` (in days):

| frequency | publication_lag |
|---|---|
| annual | 120 |
| quarterly | 60 |
| monthly | 30 |
| weekly | 7 |
| daily | 1 |

**Steps:**
1. Shift index back by `publication_lag` (so `obs_date` becomes `obs_date - lag`)
2. Reindex to daily UTC grid
3. Forward-fill

**Output:** wide DataFrame, index = daily UTC dates, columns = series_ids.

---

## 8. Contract — Store

| Layer | Format | Mutable? |
|---|---|---|
| Raw | Parquet, one file per series | ❌ (immutable per snapshot) |
| Aligned | Parquet, one file per panel | ✅ (rebuilt each `align` run) |
| Metadata | DuckDB single table `series_observations` | ✅ (replace per series) |

---

## 9. CLI

```bash
python -m src.cli refresh [--level L1|L2|L3|L4|L5] [--series id1,id2,...]
python -m src.cli align [--start YYYY-MM-DD] [--output NAME]
python -m src.cli coverage
```

---

## 10. Testing strategy

- **Unit tests:** synthetic fixtures (no API), 11 tests covering transform / align / config / stationarity
- **Integration tests:** (manual) pull 1 series from each source type, verify shape + date range
- **Coverage target:** ≥ 80% on `transform.py`, `align.py`, `config.py`

---

## 11. Compliance

- No `bank.md` data ever enters this pipeline (Chinese wall).
- API keys loaded from `.env` only.
- All pulls logged with provenance (`source`, `fetched_at`).
- `safe_repr()` masks keys in any logging.

---

**Built:** 2026-06-28 · **Version:** v0.1.0
