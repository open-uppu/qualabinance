# 🌍 L1-L5 Variable Framework → Series Codes & API Calls

> **Purpose:** Lock down **exactly which series to pull** for each of the 5 hierarchical levels, with: dataset ID, frequency, Python call, alignment rule, and stationarity handling.
>
> **Built:** 2026-06-28 · **Owner:** Qualabinance / QuantResearcher
> **Companion docs:** [`../05-resources/data-providers/treemap-primary-mapping.md`](../05-resources/data-providers/treemap-primary-mapping.md)

---

## 🎯 Design principle

```
Macro  = monthly/quarterly  →  forward-fill to daily (NO leakage)
Price  = daily/minute       →  resample to daily with asof-join
Alt    = monthly (EPU/GPR)  →  forward-fill, marked daily
```

**Critical rule:** Macro features must be **point-in-time** — no look-ahead bias from forward-filling today's value into past days. Implementation in `projects/07-hierarchical-data-pipeline/src/align.py`.

---

## 🌍 L1 — GLOBAL

### L1.1 — Global Macro

| Variable | Series Code | Source | Frequency | Python |
|---|---|---|---|---|
| Global GDP growth (IMF) | `NGDP_RPCH` | IMF WEO | annual | `imfp.imf` |
| Global industrial production | `INDPRO` (US proxy) | FRED | monthly | `fred.get_series("INDPRO")` |
| Global CPI YoY | `FPCPITOTLZG` | World Bank | annual | `wb.download(indicator='FP.CPI.TOTL.ZG')` |
| Global trade value | `NE.EXP.GNFS.CN` | World Bank | annual | `wb.download` |

### L1.2 — Global Financial

| Variable | Series Code | Source | Frequency | Python |
|---|---|---|---|---|
| Fed Funds Rate | `FEDFUNDS` / `DFEDTARU` | FRED | monthly / daily | `fred.get_series("FEDFUNDS")` |
| US Dollar Index (DXY) | `DTWEXBGS` (Broad $) | FRED | daily | `fred.get_series("DTWEXBGS")` |
| TED Spread | `TEDRATE` | FRED | daily | `fred.get_series("TEDRATE")` |
| US 10Y Treasury | `DGS10` | FRED | daily | `fred.get_series("DGS10")` |
| US 2Y Treasury | `DGS2` | FRED | daily | `fred.get_series("DGS2")` |
| Yield curve slope (10Y-2Y) | `T10Y2Y` | FRED | daily | `fred.get_series("T10Y2Y")` |

### L1.3 — Global Risk

| Variable | Series Code | Source | Frequency | Python |
|---|---|---|---|---|
| VIX (US equity volatility) | `VIXCLS` | FRED / CBOE | daily | `fred.get_series("VIXCLS")` |
| MOVE Index (bond volatility) | manual / Bloomberg | ICE BofA | daily | (paid) |
| Crude Oil (WTI) | `DCOILWTICO` | FRED / EIA | daily | `fred.get_series("DCOILWTICO")` |

---

## 🌏 L2 — CONTINENTAL

### L2.1 — Regional Equity Indices

| Region | Index | Source | Ticker | Frequency |
|---|---|---|---|---|
| North America | S&P 500 | yfinance | `^GSPC` | daily |
| North America | NASDAQ Composite | yfinance | `^IXIC` | daily |
| Europe | STOXX 600 | yfinance | `^STOXX` | daily |
| Asia-Pacific | MSCI APAC | iShares ETF proxy | `AIA` | daily |
| Asia-Pacific | Nikkei 225 | yfinance | `^N225` | daily |
| EM | MSCI EM | iShares ETF proxy | `EEM` | daily |
| ASEAN | FTSE ASEAN 40 | yfinance | `^FSEA40` | daily |
| Thailand | SET Index | yfinance | `^SET.BK` / `^SET` | daily |

### L2.2 — Regional Macro (aggregate)

| Variable | Source | Coverage | Frequency |
|---|---|---|---|
| EU GDP growth | `NY.GDP.MKTP.KD.ZG` (WB) | 27 countries | annual |
| APAC GDP growth | `NY.GDP.MKTP.KD.ZG` (WB) | 38 countries | annual |
| EM GDP growth | `NY.GDP.MKTP.KD.ZG` (WB) | 24 countries | annual |

**Aggregation method:** `wb.download(indicator=..., country='EMU')` for EU, then build custom ASEAN/EM aggregates via mean/median GDP-weighted.

### L2.3 — Regional Risk Premium

| Variable | Source | Frequency |
|---|---|---|
| US Equity Risk Premium (ERP) | computed: `^GSPC return - DGS10` | daily |
| EU Equity Risk Premium | computed: `^STOXX return - 10Y bund yield` | daily |
| EM Equity Risk Premium | computed: `EEM return - DGS10` | daily |

**Note:** Implied ERP via dividend yield + growth (Gordon) is also valid: `Damodaran dataset`.

---

## 🏛️ L3 — COUNTRY

### L3.1 — Thailand (focus market — Tier 1)

| Variable | Series Code | Source | Frequency | Notes |
|---|---|---|---|---|
| Thailand GDP growth | `NY.GDP.MKTP.KD.ZG` (WB) / BOT | annual/qtr | annual | BOT quarterly |
| Thailand CPI | `FPCPITOTLZG` (WB) / BOT | monthly | monthly | BOT monthly headline + core |
| Thailand unemployment | `SL.UEM.TOTL.ZS` (WB) | annual | annual | Thai NESDC quarterly |
| BOT policy rate | `BOT_RATE` (manual) | BOT | monthly | via BOT API Portal |
| THB/USD FX | `DEXTHUS` (FRED) | daily | daily | FRED |
| Thai trade balance | `BN.CAB.XOKA.CD` (WB) | annual | annual | MOC monthly |
| Thai 10Y govt bond | `THGB10Y` | ThaiBMA | daily | registration required |

**Python — BOT API Portal (free, requires registration):**
```python
import requests
# https://apiportal.bot.or.th/
r = requests.get(
    "https://apigw1.bot.or.th/bot/public/Stat-ReferenceRate/v2/DAILY_REF_RATE",
    headers={"X-IBM-Client-Id": BOT_KEY}
).json()
```

### L3.2 — United States

| Variable | Series Code | Frequency | Notes |
|---|---|---|---|
| US GDP growth | `GDPC1` (real) | quarterly | FRED |
| US CPI | `CPIAUCSL` | monthly | FRED |
| US Core CPI | `CPILFESL` | monthly | FRED |
| US unemployment | `UNRATE` | monthly | FRED |
| US Fed Funds Rate | `FEDFUNDS` / `DFEDTARU` | monthly/daily | FRED |
| US trade balance | `BOPGSTB` | monthly | FRED |
| US Financial Conditions | `NFCI` (Chicago Fed) | weekly | FRED |
| US 10Y-2Y spread | `T10Y2Y` | daily | FRED |
| US HY credit spread | `BAMLH0A0HYM2` | daily | FRED |

### L3.3 — China

| Variable | Source | Frequency | Notes |
|---|---|---|---|
| China GDP growth | `NY.GDP.MKTP.KD.ZG` (WB) / NBS | quarterly | NBS English portal |
| China CPI | `FPCPITOTLZG.CHN` (WB) / NBS | monthly | NBS |
| China M2 | NBS / PBoC | monthly | bulk download |
| CNY/USD | `DEXCHUS` (FRED) | daily | FRED |
| China 10Y govt bond | `CBB10Y` manual | daily | CCDC |

### L3.4 — Japan / EU / UK (template — same pattern)

For each: `CPI`, `GDP`, `unemployment`, `policy rate`, `FX vs USD`, `10Y govt bond`.

---

## 📈 L4 — MARKET (instrument level)

### L4.1 — Equity (per-instrument)

| Variable | Source | Code |
|---|---|---|
| OHLCV | yfinance | `yf.Ticker("AAPL").history(period="max")` |
| Market cap | yfinance / FRED `MCAPTC` (US only) | — |
| P/E ratio | yfinance `.info["trailingPE"]` | — |
| P/B ratio | yfinance `.info["priceToBook"]` | — |
| Dividend yield | yfinance `.info["dividendYield"]` | — |
| 52-week high/low | yfinance `.info` | — |
| Sector / Industry | yfinance `.info["sector"]` | — |
| Beta (vs S&P 500) | yfinance `.info["beta"]` | — |
| Short interest | FINRA / yfinance `.info["shortRatio"]` | — |

### L4.2 — Fixed Income

| Variable | Series Code | Source | Frequency |
|---|---|---|---|
| US 10Y yield | `DGS10` | FRED | daily |
| US 10Y-2Y slope | `T10Y2Y` | FRED | daily |
| IG Credit Spread | `BAMLC0A0CM` | FRED | daily |
| HY Credit Spread | `BAMLH0A0HYM2` | FRED | daily |
| TED Spread | `TEDRATE` | FRED | daily |
| 30Y mortgage rate | `MORTGAGE30US` | FRED | weekly |
| Thailand 10Y govt bond | ThaiBMA | ThaiBMA | daily |

### L4.3 — Forex

| Variable | Series Code | Source | Frequency |
|---|---|---|---|
| EUR/USD | `DEXUSEU` | FRED | daily |
| USD/JPY | `DEXJPUS` | FRED | daily |
| GBP/USD | `DEXUSUK` | FRED | daily |
| USD/CNY | `DEXCHUS` | FRED | daily |
| THB/USD | `DEXTHUS` | FRED | daily |
| Trade-weighted USD | `DTWEXBGS` | FRED | daily |
| Interest rate differential | computed | derived | daily |

**Tick FX data:** Dukascopy (free historical tick), HistData, TrueFX — free but tick-to-1m aggregation.

### L4.4 — Commodities

| Variable | Series Code | Source | Frequency |
|---|---|---|---|
| WTI Crude | `DCOILWTICO` | FRED / EIA | daily |
| Brent Crude | `DCOILBRENTEU` | FRED / EIA | daily |
| Gold spot | `LBMA/GOLD_USD_PM` | FRED | daily |
| Silver spot | `LBMA/SILVER_USD_PM` | FRED | daily |
| Copper | `PCOPPUSDM` | FRED | monthly |
| Wheat/Corn/Soy | `PWHEAMTUSDM` etc. | FRED / WB | monthly |
| GSCPI (supply chain pressure) | manual CSV | NY Fed | monthly |
| US oil inventory | `WCSSTUS1` | EIA | weekly |

### L4.5 — Crypto

| Variable | Source | Free? | Frequency |
|---|---|---|---|
| OHLCV (top 100) | CoinGecko `/coins/{id}/market_chart` | ✅ | 5-min granularity |
| Total market cap | CoinGecko `/global` | ✅ | real-time |
| BTC Fear & Greed | alternative.me `/fng/` | ✅ | daily |
| BTC ETF flows | Farside Investors CSV | ✅ | daily |
| On-chain BTC supply | Blockchain.com | ✅ | daily |
| Stablecoin supply | DefiLlama | ✅ | daily |
| Funding rate (perp) | Binance `/fapi/v1/fundingRate` | ✅ | 8-hourly |

```python
import ccxt
binance = ccxt.binance()
btc_ohlcv = binance.fetch_ohlcv("BTC/USDT", timeframe="1d", limit=1000)
```

---

## 🌪️ L5 — EXTERNAL / EXOGENOUS

### L5.1 — Geopolitical Risk

| Variable | Source | Frequency | Access |
|---|---|---|---|
| GPR Index (Caldara & Iacoviello) | matteoiacoviello.com | daily | free CSV |
| GPR Threat Index | matteoiacoviello.com | daily | free CSV |
| GDELT news event count | gdeltproject.org | 15-min | BigQuery free tier |
| Conflict events (ACLED) | acleddata.com | daily | free w/ registration |

```python
import pandas as pd
gpr = pd.read_csv("https://www.matteoiacoviello.com/gpr_files/data_gpr_daily_recent.csv")
```

### L5.2 — Policy Uncertainty

| Variable | Source | Frequency | Access |
|---|---|---|---|
| US EPU Index | policyuncertainty.com | monthly | free CSV |
| Thailand EPU | manual — NESDC / BOT | quarterly | manual |
| EU EPU | policyuncertainty.com | monthly | free CSV |

```python
epu = pd.read_excel("https://www.policyuncertainty.com/media/US_Policy_Uncertainty_Data.xlsx")
```

### L5.3 — Climate / Weather

| Variable | Source | Frequency | Access |
|---|---|---|---|
| NOAA climate indices | ncdc.noaa.gov | monthly | free API |
| ENSO / El Niño | cpc.ncep.noaa.gov | monthly | free |
| Agri disaster events | EM-DAT | annual | free w/registration |
| Carbon price (EU ETS) | yfinance `CO2.XP` | daily | free |

### L5.4 — Market Microstructure (alternative)

| Variable | Source | Frequency | Access |
|---|---|---|---|
| Options IV (SPY) | yfinance `.info` / CBOE | daily | free |
| Put/Call ratio (CBOE) | CBOE | daily | free |
| AAII Bull-Bear | aaii.com | weekly | free |
| Margin debt (FINRA) | FINRA | monthly | free |

---

## ⚙️ Frequency alignment rules

Critical for avoiding **look-ahead bias** in backtests:

```
┌──────────────────────────────────────────────────────────────────────┐
│ Rule 1: Macro (monthly/quarterly) → forward-fill to DAILY            │
│         but stamp with original publication date, NOT release date    │
│                                                                      │
│ Rule 2: Price (daily/minute) → resample UP to daily close            │
│         daily = 16:00 ET (US) / 16:30 ICT (TH) close                  │
│                                                                      │
│ Rule 3: EPU/GPR (monthly) → forward-fill + add publication_lag_days  │
│         (US EPU lags by ~1 month release)                              │
│                                                                      │
│ Rule 4: Earnings (quarterly) → asof-join with next-day rule           │
│         (you only know earnings AFTER the announcement date)          │
│                                                                      │
│ Rule 5: Cross-asset alignment → use UTC timestamps, convert per-asset│
└──────────────────────────────────────────────────────────────────────┘
```

---

## 📊 Stationarity handling

| Type | Transform | Why |
|---|---|---|
| Price levels | `log_return = log(P_t) - log(P_{t-1})` | remove trend, stationarity |
| Macro levels (GDP, M2) | YoY % change | remove trend |
| Yields / rates | levels (already I(0)) | rates are usually mean-reverting |
| Spreads (T10Y2Y, HY) | levels | typically stationary |
| Index values (CPI) | YoY % change | remove seasonality |
| FX | log_return | standard FX convention |

```python
def make_stationary(series, method="log_return"):
    if method == "log_return":
        return np.log(series).diff()
    elif method == "yoy_pct":
        return series.pct_change(periods=252)  # for daily, 252 trading days
    elif method == "diff":
        return series.diff()
    elif method == "level":
        return series
```

---

## 🔁 Implementation map (Project 07)

| File | Responsibility |
|---|---|
| `src/l1_global.py` | pull all L1 series → DuckDB table `l1_global` |
| `src/l2_continental.py` | pull all L2 indices + aggregates → `l2_continental` |
| `src/l3_country.py` | country-specific (TH/US/CN/JP/EU/UK) → `l3_country` |
| `src/l4_market.py` | OHLCV + per-instrument features → `l4_market` |
| `src/l5_external.py` | GPR/EPU/climate → `l5_external` |
| `src/align.py` | frequency alignment (rules above) → wide daily table |
| `src/reduce.py` | PCA / factor extraction on macro block |
| `src/store.py` | DuckDB writer + Parquet snapshot |

---

## ✅ Checklist before model training

- [ ] All L1-L5 series documented with source code
- [ ] API keys stored in `.env` (never in git)
- [ ] Point-in-time alignment verified (no future leakage)
- [ ] Stationarity tested via ADF / KPSS
- [ ] Missing data ratio per column < 5%
- [ ] Outlier capping via 99th/1st percentile
- [ ] Each series has `fetched_at` timestamp
- [ ] Each series has `source_license` field
- [ ] Reproducible end-to-end via `make refresh-data`

---

## 📚 References

1. **FRED API docs** — https://fred.stlouisfed.org/docs/api/
2. **yfinance docs** — https://pypi.org/project/yfinance/
3. **CoinGecko API** — https://www.coingecko.com/api/documentation
4. **ccxt (unified crypto exchange API)** — https://github.com/ccxt/ccxt
5. **BOT API Portal** — https://apiportal.bot.or.th/
6. **ThaiBMA** — https://www.thaibma.com/
7. **SETSMART** — https://www.setsmart.com/
8. **matteoiacoviello.com GPR** — https://www.matteoiacoviello.com/gpr.htm
9. **policyuncertainty.com** — https://www.policyuncertainty.com/
10. **NY Fed GSCPI** — https://www.newyorkfed.org/markets/global-financial-stress
11. **World Bank API** — https://data.worldbank.org/
12. **IMF Data API** — https://data.imf.org/
13. **EIA API** — https://www.eia.gov/opendata/
14. **BIS Statistics** — https://www.bis.org/statistics/

---

**Next:** [`../../../projects/07-hierarchical-data-pipeline/`](../../../projects/07-hierarchical-data-pipeline/) — implement these as code.
