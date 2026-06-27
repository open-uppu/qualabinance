# 📊 Hierarchical Variable Framework (L1-L5)

> **Master framework for organizing the entire quant research data pipeline.**

## 🎯 Why this exists

A quant strategy lives or dies by its **inputs**. If you feed it garbage, you get garbage. This framework organizes every input variable along a **5-level hierarchy** so you know exactly:
- What data to pull
- Where to get it
- How often it updates
- What it predicts
- How to combine it

---

## 🏗️ The 5 levels

```
🌍 L1 — GLOBAL          → affects everything
   ↓
🌏 L2 — CONTINENTAL     → regional dynamics
   ↓
🏛️ L3 — COUNTRY         → nation-specific
   ↓
📈 L4 — MARKET          → asset class / instrument
   ↓
🌪️ L5 — EXTERNAL        → shocks / regime changes
```

---

## 📂 Variables per level

### 🌍 L1 — Global
- Global GDP, industrial production
- Global inflation
- Global trade
- VIX (US volatility)
- Fed Funds Rate
- DXY (USD index)
- Capital flows

### 🌏 L2 — Continental
- Regional GDP growth
- Regional equity index (MSCI Asia, MSCI Europe)
- Regional risk premium
- Regional market integration

### 🏛️ L3 — Country
- Real sector: GDP, CPI, unemployment, trade balance
- Financial: policy rate, yield curve, FX, public debt
- FCI (financial conditions index)

### 📈 L4 — Market
- **Equity**: fundamentals (P/E, P/B, div yield), technical (MA, MACD), quant factors (size, value, momentum, quality)
- **Bond**: yield curve, credit spread
- **FX**: rates, IR differential, inflation expectations, PPP
- **Commodity**: inventory, production, consumption
- **Derivatives**: OI, IV, skew
- **Crypto**: price, market cap, volume, Fear & Greed, ETF flows

### 🌪️ L5 — External
- **Geopolitical**: GPR index, conflict, sanctions, trade war
- **Climate**: extreme weather, transition risk
- **Policy uncertainty**: EPU index
- **Sentiment**: VIX, AAII, put/call ratio

---

## 🔄 Cross-cutting concerns

### Frequency alignment
- Macro (monthly/quarterly) vs Market (daily/minute) vs Tick (millisecond)
- Must be aligned when combining (forward-fill, interpolation)

### Stationarity
- Most macro variables (GDP, prices) are non-stationary
- Must differencing or use returns
- Test: ADF, KPSS

### Dimensionality reduction
- 200+ variables is too many → PCA, factor models
- Use Fama-French factors as baseline

---

## 📂 Files in this folder

| File | Status |
|---|---|
| `README.md` | ✅ this file |
| `L1-global.md` | ⏳ pending |
| `L2-continental.md` | ⏳ pending |
| `L3-country.md` | ⏳ pending |
| `L4-market.md` | ⏳ pending |
| `L5-external.md` | ⏳ pending |
| `cross-cutting.md` | ⏳ pending |

---

## 📚 Data sources by level

| Level | Free sources | Paid sources |
|---|---|---|
| L1 Global | FRED, World Bank, IMF | Bloomberg, Refinitiv |
| L2 Continental | MSCI public, BIS | MSCI licensed |
| L3 Country | FRED, OECD, BOT | CEIC, Bloomberg |
| L4 Market | yfinance, Binance, CoinGecko | Polygon, CRSP, Kaiko |
| L5 External | GPR index, EPU, Climate Watch | RavenPack, Thinknum |

See [`../05-resources/data-providers/_with-papers.md`](../05-resources/data-providers/_with-papers.md) for full list.

---

## 🎯 How to use

1. **Start with L1** — pull 10-20 macro variables
2. **Build L4** — pull your target asset class data
3. **Add L2-L3** — only if strategy crosses borders
4. **Add L5** — for tail-risk / regime-change strategies
5. **Reduce dimensionality** — PCA, factor models
6. **Backtest** — purged CV, deflated Sharpe

---

*Status: 🟡 scaffold — variable lists to be populated per file.*
