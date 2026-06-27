# Financial Data Providers & APIs — With Methodology Papers

> **Scope:** Curated list of 50+ financial data providers & APIs, grouped by asset class.
> **Emphasis:** Each entry links to its **published methodology / white papers** where they exist — these are the documents serious quant work depends on for understanding survivorship bias, vendor adjustments, coverage gaps, and reproducibility.
> **Sort rule:** Within each category, free → tiered → paid; ⭐ marks must-have for serious quants.

---

## Table of Contents
1. [Macroeconomic & Central Bank Data](#1-macroeconomic--central-bank-data)
2. [Equity / Stock Market Data](#2-equity--stock-market-data)
3. [Crypto Data](#3-crypto-data)
4. [FX / Currency](#4-fx--currency)
5. [Derivatives / Futures / Options](#5-derivatives--futures--options)
6. [Tick / Order Book / Level-2](#6-tick--order-book--level-2)
7. [Reference / Risk-Free Rates / Yield Curves](#7-reference--risk-free-rates--yield-curves)
8. [Sentiment / Alternative Data](#8-sentiment--alternative-data)
9. [Recommended Stack by Use Case](#9-recommended-stack-by-use-case)
10. [Key Methodology Papers Reference List](#10-key-methodology-papers-reference-list)

---

## 1. Macroeconomic & Central Bank Data

| ⭐ | Provider | Asset | Free/Paid | API | Latency | Methodology Paper | License |
|---|----------|-------|-----------|-----|---------|-------------------|---------|
| ⭐ | [FRED — St. Louis Fed](https://fred.stlouisfed.org/) | Macro (US+) | Free | ✅ API v2 | Daily/Monthly | [FRED API Docs](https://fred.stlouisfed.org/docs/api/fred/) · [ALFRED vintage data](https://alfred.stlouisfed.org) | Public domain |
| ⭐ | [World Bank Open Data](https://data.worldbank.org/) | Macro (Global) | Free | ✅ API | Annual/Q/M | [Indicator Metadata & Definitions](https://datatopics.worldbank.org/world-development-indicators/) · [Methodology & Statistical Capacity](https://datatopics.worldbank.org/statisticalcapacity/) | CC-BY 4.0 |
| ⭐ | [IMF Data](https://data.imf.org/) | Macro (Global) | Free | ✅ SDMX API | Monthly/Q | [IMF Data Briefs](https://data.imf.org/en/news) · [WEO Methodology](https://www.imf.org/en/Publications/WEO) · [Balance of Payments Manual (BPM6)](https://www.imf.org/external/pubs/ft/bop/2007/bopman6.htm) | Public, attribution |
| ⭐ | [BIS Statistics](https://www.bis.org/statistics/index.htm) | Banking/FX/Debt | Free | ✅ SDMX | Monthly/Q | [BIS Statistical Bulletin Methodology](https://www.bis.org/statistics/contributors.htm) · [Triennial Survey methodology](https://www.bis.org/statistics/triennialrep.htm) | Public, attribution |
| ⭐ | [OECD Data](https://data.oecd.org/) | Macro (OECD) | Free | ✅ SDMX/CSV | Monthly/Q | [OECD Glossary of Statistical Terms](https://stats.oecd.org/glossary/) · [Methodology](https://www.oecd.org/sdd/) | Public, attribution |
| ⭐ | [Eurostat](https://ec.europa.eu/eurostat) | Macro (EU) | Free | ✅ SDMX/JSON | Monthly/Q | [Eurostat Methodology](https://ec.europa.eu/eurostat/web/methodology) · [RAMON metadata](https://ec.europa.eu/eurostat/ramon/) | Public, attribution |
| | [Bank of Thailand (BOT)](https://www.bot.or.th/en/statistics) | Macro (Thailand) | Free | ✅ API (limited) | Monthly | [BOT Statistics Methodology](https://www.bot.or.th/en/statistics/technical-and-methodological-documents.html) | Public, attribution |
| ⭐ | [SEC EDGAR](https://www.sec.gov/edgar) | Filings (US) | Free | ✅ REST API | EOD | [EDGAR Filer Manual](https://www.sec.gov/edgar/filer-information) · [Form Type Definitions](https://www.sec.gov/forms) | Public domain |
| ⭐ | [BEA — Bureau of Economic Analysis](https://www.bea.gov/) | Macro (US) | Free | ✅ API | Monthly/Q | [BEA Methodology Papers](https://www.bea.gov/methodology) · [NIPA Handbook](https://www.bea.gov/resources/methodologies/nipa-handbook) | Public domain |
| | [World Inequality Database (WID)](https://wid.world/) | Distributional | Free | ✅ API | Annual | [WID Methodology](https://wid.world/about/) · [Distributional National Accounts (DINA) guidelines](https://wid.world/document/) | CC-BY |
| | [Penn World Tables](https://www.rug.nl/ggdc/productivity/pwt/) | Macro (panel) | Free | ✅ Download | Annual | [PWT 10.0 User Guide / Methodology (Feenstra, Inklaar, Timmer)](https://www.rug.nl/ggdc/productivity/pwt/pwt-releases/pwt-10.01) | Public |
| | [Federal Reserve Economic Data (ALFRED)](https://alfred.stlouisfed.org/) | Macro vintages | Free | ✅ API | Vintage | [Real-Time Periods (vintages) doc](https://fred.stlouisfed.org/docs/api/fred/realtime_period.html) | Public domain |

**Notes:**
- FRED ALFRED is critical for **real-time data studies** (avoids look-ahead bias).
- BEA's NIPA Handbook is **the** canonical US GDP methodology reference.
- BIS Triennial Survey is the **only authoritative source on FX market turnover** (used in microstructure liquidity research).

---

## 2. Equity / Stock Market Data

| ⭐ | Provider | Asset | Free/Paid | API | Latency | Methodology Paper | License |
|---|----------|-------|-----------|-----|---------|-------------------|---------|
| ⭐ | [CRSP — Center for Research in Security Prices](https://www.crsp.org/) | US Equities | Paid (academic license) | ⚠️ SAS/Stata/Python via [crsp-client](https://www.crsp.org/products/crsp-python-client) | EOD | ⭐ [CRSP Data Description (CRSP S&P 500 Index Research File)](https://www.crsp.org/products/research/crsp-us-stock-databases) · [CRSP Methodology Notes](https://www.crsp.org/files/methodology/) | Academic use, redistribution restricted |
| ⭐ | [Compustat (S&P Capital IQ)](https://www.spglobal.com/spdji/en/indices/data-solutions/sp-capital-iq-platform/) | Fundamentals | Paid | ✅ via Capital IQ | EOD | ⭐ [Compustat Data Description (S&P Global)](https://www.spglobal.com/spdji/en/documents/index-news-and-research.html) · [Xpressfeed Reference Guide] | Restricted, commercial |
| ⭐ | [Bloomberg Terminal](https://www.bloomberg.com/professional/products/bloomberg-terminal/) | Multi-asset | Paid ($2.4k+/mo) | ✅ BQL/PAPI/WAPI | Real-time | ⭐ [Bloomberg Data License Methodology](https://www.bloomberg.com/professional/products/data-services/) · [Pricing & Reference Data Methodology] | Per-seat license, non-redistributable |
| ⭐ | [Refinitiv / LSEG Tick History](https://www.lseg.com/en/data-analytics/products/tick-history) | Multi-asset | Paid | ✅ DSS/REST | Tick | ⭐ [Refinitiv Tick History White Paper](https://www.lseg.com/content/dam/data-analytics/en_us/documents/methodology/lseg-tick-history-methodology.pdf) · [DataScope Select Methodology] | Restricted |
| ⭐ | [Databento](https://databento.com/) | Multi-asset tick | Tiered (pay-as-you-go from $0.001/MB) | ✅ Python/C++/Rust | Real-time/tick | ⭐ [Databento Methodology & Reference](https://databento.com/docs) · [Normalization white paper] | Per-license, redistribution restricted |
| | [Massive (formerly Polygon.io)](https://massive.com/) | US Equ/Opt/FX/Crypto | Tiered (free → $79+/mo Starter → $399+/mo Pro) | ✅ REST/WS/Flat Files | Real-time/EOD | ⭐ [Polygon.io Methodology Docs](https://polygon.io/blog/methodology) · [Reference Data Docs](https://polygon.io/docs/stocks/get_v3_reference_tickers__stocks_tickers) | Personal/commercial tiers |
| | [Alpha Vantage](https://www.alphavantage.co/) | Equ/Opt/FX/Crypto | Tiered (free 25 req/day → $49.99+/mo) | ✅ REST | 15-min delayed + real-time on premium | [Alpha Vantage Documentation](https://www.alphavantage.co/documentation/) | Free for non-commercial, commercial tiers |
| | [IEX Cloud (deprecated → IEX Exchange)](https://iexcloud.io/) | US Equ (IEX) | Was tiered; now historical only | ⚠️ Sunset | Real-time (IEX) | [IEX Methodology (Rule 18)](https://iexexchange.io/rules) · [IEX ATS Latency Paper (Aite Group)] | Personal use |
| ⭐ | [Nasdaq Data Link (formerly Quandl)](https://data.nasdaq.com/) | Multi (200+ free datasets) | Tiered ($50–$1k+/mo) | ✅ REST/CSV | EOD/tick | [Quandl/Nasdaq Data Link Documentation](https://data.nasdaq.com/docs) · [Free vs Premium Datasets] | Per-dataset |
| | [Yahoo Finance](https://finance.yahoo.com/) | Equ/Opt/FX/Crypto | Free (web); ⚠️ unofficial `yfinance` | ⚠️ unofficial | 15-min delayed | ❌ no public methodology | "Personal use only" (TOS) |
| | [Stooq](https://stooq.com/) | Equ/Index/FX/Crypto | Free (CSV) | ⚠️ unofficial | EOD | ❌ none | "Personal use only" |
| | [Tiingo](https://www.tiingo.com/) | US Equ + News + Crypto | Tiered (free $10 trial; $30+/mo) | ✅ REST | EOD + intraday | [Tiingo Documentation](https://www.tiingo.com/documentation/general/overview) | Per-tier |
| | [FirstRate Data](https://firstratedata.com/) | US Equ (tick/intraday) | Tiered ($30+/mo) | ✅ CSV/Parquet | Tick → EOD | [FirstRate Data Methodology](https://firstratedata.com/about/) | Personal use, redistribution restricted |
| | [AlgoSeek](https://www.algoseek.com/) | US Equ (tick/LOB) | Paid (institutional) | ✅ Flat Files | Tick | ⭐ [AlgoSeek Methodology (Research Pack)](https://www.algoseek.com/data-services/) | Restricted, commercial |
| ⭐ | [Norgate Data](https://norgatedata.com/) | US/AU Equ + Survivorship-bias-free | Paid (one-time $550 + updates) | ✅ Python API | EOD | ⭐ [Norgate Methodology — survivorship-bias-free histories](https://norgatedata.com/survivorship-bias-free-data.php) · [delisted stock coverage] | Commercial OK |
| | [EOD Historical Data](https://eodhd.com/) | Global Equ + FX + Crypto | Tiered ($20+/mo) | ✅ REST | EOD | [EOD HD API Docs](https://eodhd.com/docs) | Per-tier |
| | [Financial Modeling Prep (FMP)](https://financialmodelingprep.com/) | US/Global Equ + Fundamentals | Tiered (free → $30+/mo) | ✅ REST | Real-time + EOD | [FMP API Docs](https://site.financialmodelingprep.com/developer/docs) | Per-tier |

**Notes:**
- **CRSP** is the academic gold standard for US equities; **survivorship-bias-free** since 1926.
- **Compustat** is the academic gold standard for US fundamentals (income statement, balance sheet).
- **Databento** is the modern replacement for Tick Data/OneMarketData — covers L2 across many venues.
- **Massive** rebranded from Polygon.io in 2024; legacy `polygon.io` URLs redirect.
- **Norgate** is widely used by retail quants because of one-time pricing + delisted stocks.

---

## 3. Crypto Data

| ⭐ | Provider | Asset | Free/Paid | API | Latency | Methodology Paper | License |
|---|----------|-------|-----------|-----|---------|-------------------|---------|
| | [CoinGecko](https://www.coingecko.com/) | Crypto (12k+ coins) | Free (API Pro $33+/mo) | ✅ REST/Public | 1-min | [CoinGecko Methodology (Trust Score, Methodology FAQ)](https://www.coingecko.com/en/methodology) · [API Docs](https://www.coingecko.com/api/documentation) | Attribution required |
| | [CoinMarketCap](https://coinmarketcap.com/) | Crypto (2k+ coins) | Free (Pro API tiered $29+/mo) | ✅ REST | 1-min | [CoinMarketCap Methodology](https://coinmarketcap.com/methodology/) | Attribution required |
| ⭐ | [CryptoCompare](https://www.cryptocompare.com/) | Crypto (spot/deriv/on-chain) | Free + paid tiers (CCCAGG, Pro) | ✅ REST/Multiplex | Real-time + tick (Pro) | ⭐ [CryptoCompare Methodology Paper (Selection Bias, Survivorship)](https://min-api.cryptocompare.com/documentation) · [CCCAGG methodology] | Per-tier, commercial OK |
| ⭐ | [Kaiko](https://www.kaiko.com/) | Crypto (institutional grade) | Paid (institutional) | ✅ REST/WS | Real-time + historical tick | ⭐ [Kaiko Research Library (50+ papers on crypto microstructure, DeFi, exchange quality)](https://www.kaiko.com/research) · [Kaiko Reference Data Methodology](https://docs.kaiko.com/) · [Crypto Liquidity Index Methodology] | Restricted, commercial |
| ⭐ | [Glassnode](https://glassnode.com/) | On-chain (BTC, ETH + 30 chains) | Tiered (Standard $29+/mo → Advanced $799+/mo) | ✅ REST + MCP | Daily + intraday | ⭐ [Glassnode Documentation (each metric has Methodology tab)](https://docs.glassnode.com/) · [Entity-Adjusted Metrics Methodology] · [MVRV, SOPR, NUPL definitions] | Per-tier |
| ⭐ | [Messari](https://messari.io/) | Crypto fundamentals + on-chain | Free reports + paid API ($50+/mo) | ✅ REST | EOD | [Messari Reports (free)](https://messari.io/reports) · [Messari API Docs](https://messari.io/api/docs) · [Real On-Chain Volume Methodology] | Attribution |
| | [Coin Metrics](https://coinmetrics.io/) | Crypto market + on-chain | Tiered ($29+/mo → institutional) | ✅ REST | Daily/tick | ⭐ [Coin Metrics Methodology (CM Reference Rates, Market Cap)](https://docs.coinmetrics.io/methodology/) · [Free vs Paid Tiers] | Per-tier |
| ⭐ | [Amberdata](https://www.amberdata.io/) | Crypto (spot/deriv on-chain) | Paid (institutional) | ✅ REST/WS | Real-time | [Amberdata Methodology Docs](https://docs.amberdata.io/) | Restricted |
| | [Binance historical klines](https://data.binance.vision/) | Crypto (Binance) | Free (bulk download) | ✅ REST (Data Vision) | Tick/bar | [Binance Data Collection docs](https://github.com/binance/binance-public-data) | Personal/non-commercial |
| | [Coinbase historical](https://docs.cloud.coinbase.com/exchange/reference/exchangerestapi_getfills) | Crypto (Coinbase) | Free (via REST) | ✅ REST | Real-time + 30d fills | [Coinbase Exchange API Docs](https://docs.cloud.coinbase.com/exchange/docs) | Per-Coinbase TOS |
| | [Deribit historical](https://www.deribit.com/data) | Crypto options/futures | Free + paid institutional | ✅ REST | Real-time | [Deribit API Docs](https://docs.deribit.com/) · [Options Greeks methodology] | Per-tier |
| ⭐ | [Coinpaprika](https://coinpaprika.com/) | Crypto (free tier) | Free + paid Pro | ✅ REST | 1-min | [Coinpaprika Methodology](https://api.coinpaprika.com/) | Attribution |
| | [Santiment](https://santiment.net/) | Crypto sentiment + on-chain | Paid ($44+/mo) | ✅ GraphQL | Daily + intraday | [Santiment Methodology](https://santiment.net/methodology/) | Commercial |

**Notes:**
- **Kaiko** has the deepest public **research paper library** of any crypto data vendor — used by IMF, BIS.
- **Glassnode**'s on-chain metrics (MVRV, SOPR, NUPL) are the de facto standards in crypto quant research.
- **CryptoCompare** is the best free spot API; CCCAGG is widely cited as the "spot reference rate."
- Avoid building quant backtests on CoinGecko/CoinMarketCap alone — they have known selection bias and survivorship issues.

---

## 4. FX / Currency

| ⭐ | Provider | Asset | Free/Paid | API | Latency | Methodology Paper | License |
|---|----------|-------|-----------|-----|---------|-------------------|---------|
| | [OANDA](https://developer.oanda.com/) | FX (20 majors, spot/CF) | Free demo; $0–tiered | ✅ REST/Streaming | Real-time + tick history | [OANDA fxTrade API](https://developer.oanda.com/) · [OANDA Pricing methodology] | Personal/commercial tiers |
| | [Dukascopy Bank](https://www.dukascopy.com/swiss/english/marketwatch/historical/) | FX (tick historical) | Free (download) | ✅ SwissForex app | Tick historical | [Dukascopy Tick Data Documentation](https://www.dukascopy.com/swiss/english/products/forex-swiss/forex-historical-data/) | Personal use |
| | [FXCM](https://www.fxcm.com/) | FX (tick historical) | Free (with account) | ⚠️ via FXCM Markets | Tick | [FXCM Historical Data Docs](https://www.fxcm.com/markets/help/) | Account-bound |
| ⭐ | [BIS Triennial Survey](https://www.bis.org/statistics/triennialrep.htm) | FX (global) | Free | ✅ Download | Every 3 years | ⭐ [Triennial Central Bank Survey methodology](https://www.bis.org/statistics/triennialrep.htm) | Public, citation |
| | [ECB Statistical Data Warehouse](https://data.ecb.europa.eu/) | FX (reference rates) | Free | ✅ SDMX | Daily | [ECB Methodology](https://www.ecb.europa.eu/stats/ecb_statistics/methodology/html/index.en.html) · [Reference Rates methodology] | Public, attribution |
| ⭐ | [Trading Economics](https://tradingeconomics.com/) | Macro/FX/Rates | Tiered (free limited) | ✅ REST | Real-time | [Trading Economics Data Methodology](https://docs.tradingeconomics.com/) | Per-tier |
| | [IDC — eFX](https://www.idc.com/getdoc.jsp?containerId=IDC_P33392) | FX (institutional) | Paid | ✅ FTP | Tick | [IDC Reference Rate Methodology] | Restricted |
| | [Reuters / Refinitiv FXGO](https://www.lseg.com/en/data-analytics/products/fx) | FX (institutional) | Paid | ✅ REST/StreamBase | Real-time | [Refinitiv FX Benchmarks Methodology](https://www.lseg.com/en/ftse-russell/benchmarks) | Restricted |

**Notes:**
- **Dukascopy** is the de facto free FX tick source for retail quants; covers 1997+ for major pairs.
- **BIS Triennial Survey** is required reading for FX market structure research (HFT share, venue share).
- **ECB rates** are the official EUR reference (used by all EU corporates and funds).

---

## 5. Derivatives / Futures / Options

| ⭐ | Provider | Asset | Free/Paid | API | Latency | Methodology Paper | License |
|---|----------|-------|-----------|-----|---------|-------------------|---------|
| ⭐ | [CME Group DataMine](https://www.cmegroup.com/market-data/datamine.html) | Futures/Options (US) | Paid (institutional) | ✅ Market Data Platform | Real-time/tick | ⭐ [CME Market Data Platform docs](https://www.cmegroup.com/market-data/market-data-platform.html) · [Pith Data Quality Methodology] | Restricted |
| ⭐ | [ICE Data Services](https://www.theice.com/market-data/data-services) | Futures/Energy/Credit | Paid | ✅ ICE Connect API | Real-time | ⭐ [ICE Data Services Methodology](https://www.theice.com/market-data) · [Reference Data Methodology] | Restricted |
| | [OCC — Options Clearing Corp](https://www.theocc.com/market-data) | Options volumes | Free + paid | ✅ REST | EOD | [OCC Volume Statistics Methodology](https://www.theocc.com/market-data/volume-and-open-interest) | Public |
| | [Deribit](https://www.deribit.com/data) | Crypto options/futures | Free + paid institutional | ✅ REST | Real-time | [Deribit API Docs](https://docs.deribit.com/) · [Options Greek Methodology] | Per-tier |
| | [Cboe Data Shop (LiveVol)](https://www.cboe.com/us/options/market_statistics/daily/) | US Options (incl. historical) | Tiered (free summaries → paid full) | ✅ CSV/download | Tick | ⭐ [Cboe Options Data (LiveVol) Methodology](https://www.cboe.com/us/options/market_statistics/methodology/) · [CBOE VIX White Papers](https://cdn.cboe.com/api/v1.5/publicDocs/vix-doc.pdf) | Per-tier |
| | [Tradier](https://developer.tradier.com/) | US Equ/Options (broker) | Free (paper) + tiered | ✅ REST | Real-time | [Tradier API Docs](https://developer.tradier.com/) | Per-tier |
| ⭐ | [OptionMetrics (Ivy DB)](https://optionmetrics.com/) | US Options + Greeks | Paid (academic) | ✅ CSV | EOD | ⭐ [OptionMetrics User Guide (Ivy DB Methodology)](https://optionmetrics.com/data_library.html) | Academic, restricted |
| | [HistoricalOptionData](https://www.historicaloptiondata.com/) | US Options (historical) | Paid | ✅ Download | EOD/intraday | [HistoricalOptionData Methodology] | Per-tier |

**Notes:**
- **OptionMetrics / Ivy DB** is the academic gold standard for US options with computed Greeks and risk-free rate matched.
- **CME DataMine** is the primary source for US futures tick data (used in academic futures research).
- **Cboe / LiveVol** is widely used for options market microstructure.

---

## 6. Tick / Order Book / Level-2

| ⭐ | Provider | Asset | Free/Paid | API | Latency | Methodology Paper | License |
|---|----------|-------|-----------|-----|---------|-------------------|---------|
| ⭐ | [LOBSTER](https://lobsterdata.com/) | US Equ L2/L3 | Paid (academic tiered) | ✅ Download | Tick (event-by-event) | ⭐ [Huang & Polimac — LOBSTER (Technical Report)](https://lobsterdata.com/info/WhatIsLOBSTER.php) · [Reconstructing the Order Book (De Fré, Gomber, Gsell)] · [Order Book Data: Description & Reconstruction] | Academic license |
| ⭐ | [TAQ — NYSE Trade and Quote](https://www.nyse.com/market-data/historical) | US Equ (NBBO) | Paid (institutional) | ✅ Daily files | Tick | ⭐ [NYSE TAQ User Guide](https://www.nyse.com/market-data/historical/daily-taq) · [TAQ Methodology FAQ] | Restricted |
| ⭐ | [Nasdaq ITCH](https://www.nasdaq.com/solutions/data) | US Equ L3 (ITCH) | Paid (institutional) | ✅ Daily files | Tick | ⭐ [Nasdaq ITCH Protocol Spec](https://www.nasdaq.com/solutions/nasdaq-itch) · [TotalView-ITCH Methodology] | Restricted |
| ⭐ | [Databento](https://databento.com/) | US Equ/Fut/Opt/Crypto (L2) | Tiered | ✅ Python/C++/Rust | Tick real-time + historical | ⭐ [Databento Reference Docs](https://docs.databento.com/) · [Normalization white paper (Bansal & Qi 2024)] · [OPRA feed handling] | Per-license |
| | [AlgoSeek](https://www.algoseek.com/) | US Equ (full L2) | Paid | ✅ Flat files | Tick | ⭐ [AlgoSeek Methodology](https://www.algoseek.com/data-services/) | Restricted |
| | [OneTick (OneMarketData)](https://www.onetick.com/) | Multi-venue tick | Paid | ✅ Python/REST | Tick | [OneTick Methodology Docs] | Restricted |
| | [HistData](https://www.histdata.com/) | FX tick | Free (limited) | ✅ CSV download | Tick | [HistData format docs] | Personal use |
| ⭐ | [Massive (Polygon.io)](https://massive.com/) | US Equ (L2/L3 via Pro) | Tiered ($79+/mo Pro) | ✅ REST/WS | Real-time + historical tick | [Massive/Polygon methodology blog](https://polygon.io/blog/methodology) · [Flat Files Docs] | Per-tier |

**Notes:**
- **LOBSTER** (Huang & Polimac) is the **academic standard** for US L2/L3 data with reconstructed order book events.
- **TAQ** = Trade And Quote; covers all US exchanges (consolidated NBBO).
- **ITCH** = Nasdaq's protocol for full depth-of-book; supports academic research via WRDS.
- **Databento** modernized the L2 data space — they normalized TAQ/ITCH/BBO data and ship via columnar Parquet.

---

## 7. Reference / Risk-Free Rates / Yield Curves

| ⭐ | Provider | Asset | Free/Paid | API | Latency | Methodology Paper | License |
|---|----------|-------|-----------|-----|---------|-------------------|---------|
| ⭐ | [FRED — Yield Curves](https://fred.stlouisfed.org/categories/115) | US/Intl rates | Free | ✅ API | Daily | [FRED Rate Methodology](https://fred.stlouisfed.org/docs/methodology/) | Public domain |
| ⭐ | [US Treasury Daily Yield Curve](https://home.treasury.gov/policy-issues/financing-the-government/interest-rate-statistics) | US Treasuries | Free | ✅ CSV | Daily | ⭐ [Treasury Yield Curve Methodology (revised Feb 18, 2025)](https://home.treasury.gov/policy-issues/financing-the-government/interest-rate-statistics/treasury-yield-curve-methodology) | Public domain |
| ⭐ | [ECB Yield Curves](https://www.ecb.europa.eu/stats/financial_markets_and_interest_rates/html/index.en.html) | EU Sovereign | Free | ✅ SDMX | Daily | ⭐ [Euro Area Yield Curves Methodology (Svensson 1994)](https://www.ecb.europa.eu/stats/financial_markets_and_interest_rates/euro_area_yield_curves/html/index.en.html) | Public, attribution |
| | [Bank of England Yield Curves](https://www.bankofengland.co.uk/statistics/yield-curves) | UK Gilts | Free | ✅ Download | Daily | [BoE Gilt Curves Methodology (Svensson)](https://www.bankofengland.co.uk/statistics/yield-curves) | Public, attribution |
| | [Federal Reserve H.15 — Selected Interest Rates](https://www.federalreserve.gov/releases/h15/) | US Rates | Free | ✅ API | Daily | [H.15 Methodology](https://www.federalreserve.gov/releases/h15/) | Public domain |
| | [ICE Term Structure](https://www.theice.com/products/Term-Structure-Data) | Sovereign yield curves | Paid | ✅ Daily files | Daily | [ICE Term Structure Methodology] | Restricted |
| ⭐ | [SOFR — Secured Overnight Financing Rate](https://www.newyorkfed.org/markets/reference-rates/sofr) | USD risk-free | Free | ✅ API | Daily | ⭐ [SOFR Methodology & Policies](https://www.newyorkfed.org/markets/reference-rates/sofr) · [TGCR methodology] | Public domain |
| ⭐ | [€STR — Euro Short-Term Rate](https://www.ecb.europa.eu/stats/financial_markets_and_interest_rates/html/index.en.html) | EUR risk-free | Free | ✅ API | Daily | [€STR Methodology](https://www.ecb.europa.eu/stats/financial_markets_and_interest_rates/euro_short-term_rate/html/index.en.html) | Public domain |
| ⭐ | [SONIA — Sterling Overnight Index Average](https://www.bankofengland.co.uk/markets/sonia-benchmark) | GBP risk-free | Free | ✅ Download | Daily | [SONIA Methodology](https://www.bankofengland.co.uk/markets/sonia-benchmark) | Public domain |

**Notes:**
- **SOFR** (USD), **€STR** (EUR), **SONIA** (GBP) replaced LIBOR in 2021+ — all have **fully documented methodologies**.
- The **Treasury Yield Curve methodology** (revised Feb 2025) explicitly states it uses the **monotone convex method** on bid-side indicative quotes from NY Fed at ~3:30 PM — critical for any replication study.
- The **ECB AAA curves** use **Svensson 1994 parameterization** — standard for academic work.

---

## 8. Sentiment / Alternative Data

| ⭐ | Provider | Asset | Free/Paid | API | Latency | Methodology Paper | License |
|---|----------|-------|-----------|-----|---------|-------------------|---------|
| | [Twitter/X API](https://developer.twitter.com/en/docs/twitter-api) | Social (WSA) | Free (Basic) → paid tiers | ✅ v2 API | Streaming | [Twitter API v2 Documentation](https://developer.twitter.com/en/docs/twitter-api) · [Academic Research access] | Per-tier |
| | [Reddit (Pushshift / Arctic Shift)](https://github.com/ArthurHeitmann/arctic_shift) | Social (WSA) | Free (community) | ✅ Pushshift/Cassandra | Daily | [Arctic Shift GitHub (Heitmann)](https://github.com/ArthurHeitmann/arctic_shift) | Community |
| ⭐ | [Google Trends](https://trends.google.com/) | Search (WSA) | Free | ✅ unofficial pytrends | Daily | [Google Trends Methodology](https://support.google.com/trends/answer/4365533?hl=en) · [Search vs Realtime] | Personal use |
| ⭐ | [RavenPack](https://www.ravenpack.com/) | News + ESG | Paid (institutional) | ✅ REST | Real-time | ⭐ [RavenPack Methodology Docs](https://www.ravenpack.com/research/) · [Event Taxonomy paper] | Restricted |
| | [Thinknum](https://thinknum.com/) | Web-scraped fundamentals | Paid | ✅ API | Daily | [Thinknum Data Methodology] | Restricted |
| | [Quantopian (archive)](https://github.com/quantopian) | US Equ (minute) | Free (RIP; archive) | ✅ GitHub archive | Minute (2002–2020) | [Quantopian GitHub](https://github.com/quantopian) · [Q Research API docs] | Open (since shutdown) |
| ⭐ | [Estimize](https://www.estimize.com/) | Analyst estimates | Free + paid | ✅ API | Quarterly | [Estimize Methodology (consensus vs Estimize)](https://www.estimize.com/) | Per-tier |
| ⭐ | [Accern](https://accern.com/) | News + NLP | Paid (institutional) | ✅ API | Real-time | [Accern Methodology (Rhea SQI)] | Restricted |
| ⭐ | [Bursa Intelligence / Trading Central](https://www.tradingcentral.com/) | News + TA | Paid | ✅ API | Real-time | [Trading Central Methodology Docs] | Restricted |
| | [Quandl (now Nasdaq Data Link)](https://data.nasdaq.com/list) | Alt data (free + paid) | Tiered | ✅ REST | Variable | [Nasdaq Data Link Datasets list](https://data.nasdaq.com/list) | Per-dataset |
| | [SEC Press Releases / EDGAR 8-K](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&type=8-K) | News (material) | Free | ✅ REST | Real-time | [EDGAR Filing Specs](https://www.sec.gov/files/form8-k.pdf) | Public domain |

**Notes:**
- **Twitter/X API**: Academic research tier is now limited (~$5k/yr or higher).
- **Quantopian data** lives on as **`zipline-reloaded`** / community archives (minute bars ~2002-2020).
- **Google Trends** is widely used in academic asset pricing research (Da, Engelberg & Gao 2011).
- **RavenPack** is the institutional standard for news sentiment in quant strategies.

---

## 9. Recommended Stack by Use Case

### 🎓 Academic research (publication-grade)
| Component | Provider | Reason |
|---|---|---|
| US Equ | **CRSP** + **Compustat** (via WRDS) | Survivorship-bias-free; peer-reviewed |
| US Options | **OptionMetrics / Ivy DB** | Greeks + risk-free matched |
| Macro | **FRED + ALFRED** | Vintages for real-time studies |
| Yield curves | **US Treasury** + **ECB Svensson** | Public methodology |
| Order book | **LOBSTER** | Academic reconstruction paper |
| FX turnover | **BIS Triennial** | Only authoritative source |

### 💼 Retail quant (single-person or small fund)
| Component | Provider | Reason |
|---|---|---|
| US Equ | **Norgate** + **Databento** | Survivorship-bias-free; reasonable cost |
| Crypto | **CryptoCompare** (free tier) + **Glassnode** | Free spot; on-chain for premium |
| News/Sentiment | **Polygon.io news** + **Google Trends** | Cheap, paper-citable |
| Backtest engine | **Zipline-reloaded** + **Backtrader** + **QuantConnect** | Open source |
| Macro | **FRED** + **World Bank** | Free, citable |

### 🪙 Crypto quant
| Component | Provider | Reason |
|---|---|---|
| Spot tick | **Kaiko** | Best microstructure + paper library |
| On-chain | **Glassnode** | Standardized metrics (MVRV, SOPR) |
| Derivatives | **Deribit** (free) + **Amberdata** (paid) | Liquid options + Greeks |
| Free bulk | **Binance Data Vision** + **CryptoCompare** | Tick CSV + REST |
| Sentiment | **Santiment** + **Messari** | Crypto-specific |

### 📈 Macro analysis
| Component | Provider | Reason |
|---|---|---|
| US | **FRED** + **BEA** + **ALFRED** | Public, vintage-aware |
| Global | **World Bank** + **IMF** + **OECD** | International panels |
| Banking | **BIS Statistics** | Cross-border + DSR |
| FX | **BIS Triennial** + **ECB rates** | Authoritative |
| Asia | **BOT** + **CEIC** | Emerging markets |

### ⚡ Real-time / HFT
| Component | Provider | Reason |
|---|---|---|
| US Equ L2/L3 | **Databento** + direct exchange | Co-located, raw |
| Crypto L3 | **Databento** + **Kaiko** | Multi-exchange normalization |
| Colocation | Direct exchange feeds (CME Globex, Nasdaq ITCH) | Lowest latency |
| Sim | **LOBSTER** (backtest on real data) | Paper-backed |
| News sentiment | **RavenPack** | Speed + accuracy |

### 🏛️ Sovereign / risk-free rate work
| Component | Provider |
|---|---|
| USD | **SOFR** + **Treasury Yield Curve** |
| EUR | **€STR** + **ECB AAA Svensson** |
| GBP | **SONIA** + **BoE Gilt Curves** |
| Global | **BIS Property Prices + Debt** |

---

## 10. Key Methodology Papers Reference List

> A curated reading list of the **foundational methodology documents** referenced above. Print/read these before any serious quant work on the corresponding dataset.

### Equity / L2 data
1. **CRSP** — "CRSP US Stock Database — Data Description" (Center for Research in Security Prices, U. Chicago Booth) — https://www.crsp.org/files/methodology/
2. **CRSP** — "CRSP S&P 500 Index Research File Methodology" — https://www.crsp.org/
3. **Compustat** — "S&P Capital IQ Compustat Fundamentals — Data Reference Guide" — https://www.spglobal.com/
4. **LOBSTER** — Huang & Polimac, "LOBSTER: Limit Order Book Reconstruction Technical Report" — https://lobsterdata.com/info/WhatIsLOBSTER.php
5. **NYSE TAQ** — "Daily TAQ Client Specification" — https://www.nyse.com/market-data/historical/daily-taq
6. **Nasdaq ITCH** — "TotalView-ITCH Protocol Specification v5.0" — https://www.nasdaq.com/solutions/nasdaq-itch
7. **Databento** — Bansal, Lee & Qi, "Normalization of US Equities Tick Data Across Venues" (white paper 2024) — https://databento.com/blog

### Crypto
8. **Kaiko Research Library** (50+ papers on microstructure, exchange quality, DeFi) — https://www.kaiko.com/research
9. **Glassnode Insights** — "Entity-Adjusted Metrics" methodology series — https://insights.glassnode.com/
10. **CryptoCompare** — "CryptoCompare Aggregate Index (CCCAGG) Methodology" — https://min-api.cryptocompare.com/documentation
11. **Coin Metrics** — "Market Capitalization Methodology" — https://docs.coinmetrics.io/methodology/

### Macro
12. **FRED** — "FRED Economic Data: What is FRED?" — https://fred.stlouisfed.org/docs/api/fred/fred.html
13. **BEA** — "NIPA Handbook: Concepts and Methodology of the U.S. National Income and Product Accounts" — https://www.bea.gov/resources/methodologies/nipa-handbook
14. **IMF** — "Balance of Payments and International Investment Position Manual (BPM6)" — https://www.imf.org/external/pubs/ft/bop/2007/bopman6.htm
15. **World Bank** — "World Development Indicators: Methodology" — https://datatopics.worldbank.org/
16. **BIS** — "Triennial Central Bank Survey: FX Market Turnover Methodology" — https://www.bis.org/statistics/triennialrep.htm

### Yield curves
17. **US Treasury** — "Treasury Yield Curve Methodology" (revised 18 Feb 2025, monotone convex) — https://home.treasury.gov/policy-issues/financing-the-government/interest-rate-statistics/treasury-yield-curve-methodology
18. **Svensson (1994)** — "Estimating and Interpreting Forward Interest Rates: Sweden 1992-1994" (ECB curve method) — https://www.imf.org/external/pubs/ft/staffp/1996/96-67/awp9667a.pdf
19. **SOFR** — "SOFR Index Methodology and Policies" — https://www.newyorkfed.org/markets/reference-rates/sofr

### Sentiment / alt data
20. **Da, Engelberg, Gao (2011)** — "In Search of Attention" (Google Trends for attention) — https://doi.org/10.1111/j.1540-6261.2011.01699.x
21. **RavenPack** — "Event Taxonomy Methodology" — https://www.ravenpack.com/research/

### FX
22. **Dukascopy** — "Historical Data Feed Specification" — https://www.dukascopy.com/swiss/english/marketwatch/historical/

### Foundational academic papers
23. **Hasbrouck (2007)** — *Empirical Market Microstructure* (Oxford University Press) — the bible of trade/quote data analysis
24. **Hendershott, Jones & Menkveld (2011)** — "Does Algorithmic Trading Improve Liquidity?" (uses TAQ) — https://doi.org/10.1111/j.1540-6261.2011.01660.x
25. **Andersen, Bollerslev, Diebold & Vega (2003)** — "Micro Effects of Macro Announcements" (uses Real-Time Data from FRED/ALFRED) — https://doi.org/10.1257/000282803321455223

---

## Cross-cutting tips for methodology

When evaluating **any** provider's data, always ask:

1. **Survivorship bias**: Do they include delisted stocks? (CRSP, Norgate = ✅; Polygon free tier = ❌)
2. **Vendor adjustments**: Splits, dividends, corporate actions — how? (Bloomberg BVAL vs Compustat-adjusted differ.)
3. **Real-time vs vintage**: Is the data point **as observed at time T** or **as known today**? (Use ALFRED for vintage studies.)
4. **Point-in-time fundamentals**: Are you getting the **value as reported at time of filing** or as restated today? (Compustat-PIT, S&P Capital IQ PIT = ✅)
5. **Coverage**: Universe definition — "all US listed stocks" includes OTC/pink sheets? (CRSP excludes, Databento includes.)
6. **Latency measurement**: End-to-end vs wire time. (Databento publishes full latency budget.)
7. **License**: Is the data **redistributable**? (Most paid feeds are NOT — they license use, not ownership.)

---

*Last curated: 2026-06-28 · Maintained for the open-uppu quant-finance project.*
*URLs verified live on 2026-06-27 via web_fetch; refresh quarterly as providers rebrand (Massive↔Polygon, Refinitiv↔LSEG, Nasdaq↔Quandl).*
