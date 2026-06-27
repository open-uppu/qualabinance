# 🌍 Global Markets — Asset Class Taxonomy

> **Every tradeable asset class on Earth, organized for systematic coverage.**

## 📊 Classification by asset class

### 📈 Equities (Stocks)
| Region | Exchanges | Examples |
|---|---|---|
| **US** | NYSE, NASDAQ | AAPL, MSFT, NVDA, TSLA |
| **Thailand** | SET, mai | AOT, PTT, CPALL |
| **Hong Kong** | HKEX | 0700 (Tencent), 9988 (Alibaba) |
| **Japan** | TSE, JPX | 7203 (Toyota), 6758 (Sony) |
| **Europe** | LSE, Euronext, Xetra | ASML, SAP, LVMH |
| **China** | SSE, SZSE | 600519 (Kweichow Moutai), 000858 |

**Data**: Polygon, Alpha Vantage, yfinance, CRSP (academic)
**Broker**: IB, Alpaca, KGI (TH), Phillip Securities (TH)

### 📊 ETFs
- **Broad market**: SPY, QQQ, VTI, KXI
- **Sector**: XLE, XLF, XLK, ARKK
- **Thailand**: TDEX, K-SET50, 1DIV
- **Bond**: BND, AGG, TLT

### 🏛️ Bonds / Fixed Income
| Type | Examples | Trading |
|---|---|---|
| **Gov (US)** | 2Y, 10Y, 30Y Treasury | OTC, broker-dealer |
| **Gov (TH)** | LB22DA, LB26DA | ThaiBMA |
| **Corporate** | Investment grade, high yield | OTC |
| **TIPS** | Inflation-protected | OTC |
| **Municipal** | US state/local | OTC |

**Data**: FRED (yield curves), OpenBond, Refinitiv, ThaiBMA
**Broker**: IB (most), institutional dealers

### 📜 Futures
| Contract | Exchange | Underlying |
|---|---|---|
| **ES** (E-mini S&P 500) | CME | S&P 500 |
| **NQ** (E-mini Nasdaq) | CME | Nasdaq 100 |
| **CL** (Crude oil) | NYMEX/CME | WTI crude |
| **GC** (Gold) | COMEX/CME | Gold |
| **SET50 futures** | TFEX | SET50 index |
| **BTC futures** | CME, Binance | Bitcoin |
| **ETH futures** | CME, Binance | Ethereum |

**Data**: CME DataMine, Quandl, Refinitiv
**Broker**: IB, NinjaTrader, Binance (crypto)

### 🎯 Options
| Type | Venue | Examples |
|---|---|---|
| **Equity options** | CBOE, OCC | AAPL calls, TSLA puts |
| **Index options** | CBOE, Eurex | SPX, VIX, NIFTY |
| **Crypto options** | Deribit, OKX | BTC-27JUN25-100000-C |
| **Weekly options** | CBOE | 0DTE SPX, big-tech |
| **Thai warrants** | SET | KBANK-W (Thai-style) |

**Data**: ORATS, CBOE DataShop, Deribit API
**Broker**: IB, TastyTrade, Deribit (crypto)

### ₿ Crypto
| Type | Examples |
|---|---|
| **Spot** | BTC, ETH, SOL, stablecoins (USDT, USDC) |
| **Perpetual futures** | BTC-PERP, ETH-PERP (no expiry) |
| **Quarterly futures** | BTC-27JUN25 |
| **Options** | BTC-27JUN25-100000-C (Deribit) |
| **DeFi tokens** | UNI, AAVE, CRV |
| **Memes** | DOGE, SHIB, PEPE |
| **L2s** | ARB, OP, MATIC |

**Data**: Binance, Kaiko, Glassnode, CryptoCompare
**Broker**: Binance, OKX, Bybit, Coinbase, Kraken

### 💱 FX (Foreign Exchange)
| Pair | Type | Examples |
|---|---|---|
| **Majors** | G10 | EUR/USD, USD/JPY, GBP/USD |
| **Crosses** | G10 cross | EUR/JPY, AUD/NZD |
| **EM** | Emerging | USD/THB, USD/TRY, USD/ZAR |
| **Exotics** | Illiquid | USD/SEK |

**Data**: OANDA, Dukascopy, BIS Triennial Survey
**Broker**: OANDA, IB, FXCM

### 🛢️ Commodities
| Type | Examples |
|---|---|
| **Energy** | WTI, Brent, Natural gas, Gasoline |
| **Metals** | Gold, Silver, Platinum, Palladium, Copper |
| **Agri** | Wheat, Corn, Soybeans, Coffee, Sugar |
| **Livestock** | Live cattle, Lean hogs |

**Data**: CME, Quandl, Refinitiv
**Broker**: IB

### 🏠 REITs / Property
- **US REITs**: O (Realty Income), SPG (Simon Property)
- **Thai REITs**: AIMIRT, WHART
- **Direct property**: usually not tradeable, REIT is the proxy

**Data**: yfinance
**Broker**: IB

### 🎰 Prediction Markets
| Platform | Asset |
|---|---|
| **Polymarket** | Politics, sports, current events |
| **Kalshi** | US-regulated prediction markets |

**Data**: on-chain, platform APIs
**Broker**: direct (web3 wallet)

### 🪙 Tokenized RWAs (Real-World Assets)
| Type | Example |
|---|---|
| **Tokenized treasuries** | BUIDL (BlackRock), USDY (Ondo) |
| **Tokenized gold** | PAXG, XAUT |
| **Tokenized credit** | MakerDAO RWA vaults |

**Data**: on-chain, MakerDAO API
**Broker**: on-chain (web3 wallet)

---

## 🔄 Classification by maturity / structure

### Money Market (< 1 year)
- T-bills, CP, repos, deposits
- Fed Funds, SOFR, EURIBOR
- Thai: BOT bonds, B/E bills

### Capital Market (> 1 year)
- Stocks, bonds, long-dated derivatives

### Primary vs Secondary
- **Primary**: IPO, bond issuance (new issuance)
- **Secondary**: ongoing trading (most liquidity here)

---

## 🌏 Priority order for Qualabinance

| Phase | Asset Class | Rationale |
|---|---|---|
| v0 | Crypto spot + perps | 24/7, free data, fast iteration |
| v0 | US equities | Best data, cleanest APIs |
| v1 | Thai equities + futures | Local market, IB/KGI accessible |
| v2 | Options | Higher margin, vol surface |
| v3 | FX | Largest market by volume |
| v4 | Bonds | Add after portfolio framework solid |
| v5 | Tokenized RWAs | Newest, research-heavy |

---

## 📚 Resources

- See [`../../../05-resources/data-providers/_with-papers.md`](../../../05-resources/data-providers/_with-papers.md) for data sources
- See [`../../../05-resources/papers/_q1-econometrics.md`](../../../05-resources/papers/_q1-econometrics.md) for microstructure papers
- See [`../../../05-resources/books/_canonical.md`](../../../05-resources/books/_canonical.md) → Hull for derivatives

---

*Status: 🟡 scaffold — content here, expand on each section over time.*
