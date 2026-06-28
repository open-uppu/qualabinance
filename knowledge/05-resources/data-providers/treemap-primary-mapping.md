# 🗺️ Treemap "All the World's Money" → Primary Data Mapping

> **Purpose:** Reproduce every cell of the [Global Money Treemap](#-treemap-cells) using **authoritative, API-accessible primary sources** — not third-party blog aggregations. Every row links to (a) the dataset, (b) the field, (c) the Python/REST call, (d) the latest value.
>
> **Built:** 2026-06-28 · **Status:** living doc · **Owner:** Qualabinance / QuantResearcher

---

## 🎯 Why this exists

The Treemap in our Qualabinance dashboard showed asset-class sizes (Real Estate $393T, Equities $128T, Bonds $97T, Gold ~$22T, Crypto ~$3T, M2 ~$123T). The numbers came from secondary sources (Visual Capitalist, blog aggregations).

For a **production quant pipeline**, every number must be:
1. **Reproducible** — pulled by code, not copy-pasted
2. **Versioned** — dated snapshot, not "as of last week"
3. **Primary** — straight from the issuing institution
4. **Auditable** — citation + DOI/URL + access date

This document maps **each Treemap cell → primary dataset + access method**.

---

## 🗺️ Treemap cells

```
📊 TREEMAP CELLS (2025 Q2 snapshot)
├── 🏠 Real Estate           $393.3T   → Savills / Fed Z.1
├── 📈 Equities (global)     $127.9T   → WFE / World Federation of Exchanges
├── 🏦 Broad Money (M2)      $123.0T   → BIS / FRED M2SL
├── 💵 Bonds (investable)    $96.6T    → BIS Debt Securities Statistics
├── 🥇 Gold                  ~$22.0T   → World Gold Council
├── 🪙 Money + Silver (M0)   ~$2.0T    → BIS / central banks (banknotes)
└── ₿ Crypto                 $2.6T     → CoinGecko (free) / Glassnode (paid)
```

---

## 📋 Cell-by-cell primary mapping

### 🏠 Real Estate — $393.3T

| Field | Value (2025) | Primary Source | API/Dataset | Code |
|---|---|---|---|---|
| Global residential | ~$287T | **Savills Research** (cited by WEF/Oxford) | Manual PDF/Excel | [1] |
| Global commercial | ~$58T | **Savills Research** | Manual PDF/Excel | [1] |
| Global agricultural land | ~$48T | **Savills Research** | Manual PDF/Excel | [1] |
| US household real estate | ~$48T | **FRED Z.1 / OFR** | `BOGZ1FL075035503Q` (owner-occupied real estate) | FRED |

**Reproducibility:**
```python
# US slice via FRED (free, API)
from fredapi import Fred
fred = Fred(api_key=FRED_KEY)
us_real_estate = fred.get_series("BOGZ1FL075035503Q")  # quarterly, $ billions
```

**Limitation:** Savills updates the global figure only **annually** (mid-year report). Quarterly tracking via Z.1 gives US only; global aggregation lags 6–12 months.

**Cited source:** Savills — *World Residential, Commercial, Agricultural Land Report 2025* (private publication, ~$2,500 report)

---

### 📈 Equities — $127.9T

| Field | Value (2025) | Primary Source | API/Dataset | Code |
|---|---|---|---|---|
| Global market cap | $127.9T | **World Federation of Exchanges (WFE)** | Monthly stats (free CSV) | [2] |
| US share | $54T (64% of WFE) | **WFE** / NYSE + NASDAQ combined | WFE H1 2025 stats | [2] |
| Thailand share | ~$0.5T | **SET (Stock Exchange of Thailand)** | Daily `set.or.th` data | SETSMART |

**Reproducibility:**
```python
import pandas as pd
# WFE publishes "Monthly Market Highlights" CSV — no API, but free download
url = "https://www.world-exchanges.org/our-work/statistics"
wfe = pd.read_csv("wfe_monthly_2025-06.csv")  # manual download

# Alternative for US equities via FRED (Wilshire 5000 proxy)
wilshire_mcap = fred.get_series("WILL5000INDFC")  # full-cap Wilshire, $ billions
```

**Limitation:** WFE publishes **monthly aggregates** (not tick-level). For tick-level US data use Polygon.io ($29/mo). Thailand tick data via SETSMART is **paid** (~THB 50,000/yr).

**Cited source:** WFE — *Monthly Market Highlights, June 2025* (free CSV at world-exchanges.org)

---

### 🏦 Broad Money (M2) — $123.0T

| Field | Value (2025) | Primary Source | API/Dataset | Code |
|---|---|---|---|---|
| US M2 | ~$21.8T | **FRED** | `M2SL` (weekly, free API) | FRED |
| China M2 | ~$45T | **PBoC** (free, EN-translated) | Monthly bulk Excel | [3] |
| Eurozone M2 | ~$16T | **ECB** | `BSI.M.U2.Y.V.M20.X.1.U2.2300.Z01.E` (SDMX) | ECB SDMX |
| Japan M2 | ~$7T | **BoJ** | Monthly bulk CSV | [3] |
| Global aggregate | ~$123T | **BIS Total Credit Statistics** + central-bank aggregation | BIS (paid deep, free preview) | [3] |

**Reproducibility:**
```python
# US M2 (FRED, free, weekly)
us_m2 = fred.get_series("M2SL")  # billions USD, 1959-present

# Global M2 via World Bank (free, annual)
from pandas_datareader import wb
global_m2_panel = wb.download(indicator='FM.LBL.BMNY.GD.ZS', country='all', start=2020)
```

**Limitation:** BIS aggregate requires **paid subscription** ($3,000/yr). Free alternative = sum FRED `M2SL` + ECB SDMX + PBoC download = rebuild at zero cost but with manual labor.

**Cited source:** BIS — *Debt Securities Statistics, June 2025* (free quarterly aggregate, paid series-level)

---

### 💵 Bonds (investable) — $96.6T

| Field | Value (2025) | Primary Source | API/Dataset | Code |
|---|---|---|---|---|
| Global debt securities | $96.6T | **BIS Debt Securities Statistics** | Quarterly SDMX | BIS |
| US Treasuries outstanding | ~$27T | **FRED / TreasuryDirect** | `GFDEBTN` (monthly, free) | FRED |
| US IG Corp bonds | ~$10T | **FRED / SIFMA** | `BAMLC0A0CM` (ICE BofA IG OAS) | FRED |
| Thailand gov bonds | ~THB 13T (~$0.4T) | **ThaiBMA** | Daily CSV (free registration) | ThaiBMA |

**Reproducibility:**
```python
# US debt / FRED
us_total_debt = fred.get_series("GFDEBTN")        # total public debt, monthly
ig_credit_spread = fred.get_series("BAMLC0A0CM")  # IG OAS, daily
hy_credit_spread = fred.get_series("BAMLH0A0HYM2") # HY OAS, daily
treasury_10y = fred.get_series("DGS10")            # 10-year yield, daily

# BIS debt securities (Python sdmx)
import sdmx
client = sdmx.Client('BIS')
ds = client.data('DSRP', key='.USD+CNY+EUR+GBP+JPY.A.M.N.T.I.X.?', params={'startPeriod': '2020'})
```

**Limitation:** BIS series-level is **paid** (~$3,000/yr). SIFMA aggregates are **free quarterly**. Daily IG/HY OAS via FRED is **free** but ICE BofA licensed.

**Cited source:** BIS — *Debt Securities Statistics, June 2025* + SIFMA *US Capital Markets Fact Book 2025*

---

### 🥇 Gold — ~$22T

| Field | Value (2025) | Primary Source | API/Dataset | Code |
|---|---|---|---|---|
| Above-ground stock | ~216,000 tonnes | **World Gold Council (WGC)** | Quarterly "Gold Demand Trends" | [4] |
| Spot price (for valuation) | ~$3,300/oz (Jun 2026) | **LBMA** | Daily fix AM/PM (free) | LBMA |
| Total value at spot | $22.0T | computed: tonnes × oz/tonne × spot | see code | — |

**Reproducibility:**
```python
# LBMA Gold Price (FRED free)
gold_price = fred.get_series("LBMA/GOLD_USD_PM")  # London PM fix, daily, USD

# WGC tonnage via quarterly PDF (free, manual)
# OR via Quandl/Nasdaq Data Link "WGC/GOLD_DEMAND"
import nasdaqdatalink
gold_demand = nasdaqdatalink.get("WGC/GOLD_DEMAND")  # free with key
```

**Limitation:** WGC bulk data is **free but PDF/manual**. Nasdaq Data Link WGC feed is **free with API key**. LBMA fix is **free via FRED**.

**Cited source:** World Gold Council — *Gold Demand Trends Q2 2025* + LBMA daily fix

---

### 🪙 Physical Currency (M0) — ~$2T

| Field | Value (2025) | Primary Source | API/Dataset | Code |
|---|---|---|---|---|
| US banknotes in circulation | $2.3T | **FRED** | `MBCURRCIR` (weekly) | FRED |
| Global banknotes | ~$8T (cash in circulation) | **BIS Red Book** | Annual PDF | BIS |
| Silver above-ground | ~$0.2T | **Silver Institute / USGS** | Annual report | USGS |

**Reproducibility:**
```python
us_notes = fred.get_series("MBCURRCIR")  # billions USD, weekly, free
```

**Limitation:** BIS Red Book is **free PDF but not API**. Global M0 figure is **annual, lagged 18 months**.

**Cited source:** BIS — *Red Book: Statistics on Payment, Clearing and Settlement Systems, 2024*

---

### ₿ Crypto — $2.6T

| Field | Value (2025) | Primary Source | API/Dataset | Code |
|---|---|---|---|---|
| Total market cap | $2.6T | **CoinGecko** | `/global` endpoint (free, no key) | [5] |
| BTC dominance | ~52% | **CoinGecko** | `/global` (free) | [5] |
| Total crypto volume 24h | ~$80B | **CoinGecko** | `/global` (free) | [5] |
| BTC ETF flows | daily | **Coinglass / Farside Investors** | Daily CSV (free) | [6] |
| On-chain BTC supply | 19.8M | **Blockchain.com** | Free REST | Blockchain |
| On-chain ETH supply | 120.4M | **Etherscan** | Free REST | Etherscan |

**Reproducibility:**
```python
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
global_data = cg.get_global()["data"]
total_mcap = global_data["total_market_cap"]["usd"]
btc_dominance = global_data["market_cap_percentage"]["btc"]

# Or via CoinGecko free public API (no key)
import requests
r = requests.get("https://api.coingecko.com/api/v3/global").json()
```

**Limitation:** CoinGecko free tier has **10–30 calls/min** rate limit. For production, use **paid Pro tier ($129/mo)** or self-host via **CoinPaprika** (cheaper) or run your own Ethereum node for on-chain.

**Cited source:** CoinGecko — *Global Crypto Market Data, June 2025*

---

## 📊 Summary table — starter stack

| Asset Class | Free API? | Paid Alternative | Tick-level? | Latency |
|---|---|---|---|---|
| Real Estate | ❌ (PDF only) | Savills ($2.5k/yr) | ❌ | annual |
| Equities | ✅ (WFE monthly + yfinance daily) | Polygon ($29/mo), SETSMART | ✅ (paid) | daily–tick |
| M2 | ✅ (FRED + ECB + WB) | BIS aggregate ($3k/yr) | ❌ | weekly–monthly |
| Bonds | ✅ (FRED yields, SIFMA qtr) | BIS series ($3k/yr), ICE | ✅ (paid) | daily |
| Gold | ✅ (LBMA via FRED, WGC PDF) | Nasdaq Data Link WGC | ❌ | daily |
| Money/Silver | ✅ (FRED, USGS annual) | BIS Red Book | ❌ | weekly–annual |
| Crypto | ✅ (CoinGecko, Binance) | Glassnode ($29/mo) | ✅ (free!) | tick |

---

## 🔁 Reproducibility checklist

For each cell above, our pipeline must:

1. ✅ **Pull by code** — `requests.get()` or `fredapi.Fred().get_series()`, not copy-paste
2. ✅ **Snapshot dated** — every fetch saves `fetched_at` timestamp
3. ✅ **Stored in DuckDB/Parquet** — versioned, queryable
4. ✅ **CI sanity check** — alert if value moves > 10% from prior period
5. ✅ **License logged** — `data_providers.yaml` records ToS per source

---

## 📚 References

1. **Savills Research** — *World Residential, Commercial & Agricultural Land Report 2025* (private)
2. **World Federation of Exchanges (WFE)** — *Monthly Market Highlights, June 2025* — https://www.world-exchanges.org/our-work/statistics
3. **BIS Statistics** — *Debt Securities, Credit, Total* — https://www.bis.org/statistics/ (paid deep access)
4. **World Gold Council** — *Gold Demand Trends Q2 2025* — https://www.gold.org/goldhub/data
5. **CoinGecko** — *Global Crypto Market Data* — https://www.coingecko.com/api/documentation
6. **Farside Investors** — *Bitcoin ETF Flow Tracker* — https://farside.co.uk/bitcoin-etf-flow-all-data/
7. **FRED** — *Federal Reserve Economic Data* — https://fred.stlouisfed.org/ (free API with key)
8. **SETSMART** — *Thailand Stock Market Data* — https://www.setsmart.com/ (paid)
9. **ThaiBMA** — *Thai Bond Market Association* — https://www.thaibma.com/ (free registration)

---

## 🔄 Update cadence

| Cell | Update frequency | Pipeline cron |
|---|---|---|
| Real Estate (US Z.1) | quarterly | weekly Mon 06:00 |
| Equities (WFE) | monthly | daily 22:00 |
| M2 (FRED US) | weekly | daily 06:00 |
| Bonds (FRED yields) | daily | daily 06:00 |
| Gold (LBMA) | daily | daily 22:00 |
| Crypto (CoinGecko) | real-time | every 5 min |

---

**Related:**
- `../06-variable-framework/` — what variables to compute (L1-L5)
- `../../../projects/07-hierarchical-data-pipeline/` — how to ingest them
- `../../../projects/02-stock-analysis/` — equity consumers
