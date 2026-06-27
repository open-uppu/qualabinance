# 📊 02 — Stock Analysis

> **Pull stock data, compute indicators, build a dashboard.**

## 🎯 Purpose

End-to-end introductory project:
1. Fetch stock data (yfinance)
2. Compute indicators (MA, volatility, returns)
3. Visualize in interactive dashboard

## 📚 Knowledge dependencies

- [`../../knowledge/01-foundations/`](../../knowledge/01-foundations/)
- [`../../knowledge/05-resources/data-providers/_with-papers.md`](../../knowledge/05-resources/data-providers/_with-papers.md)

## 📁 Structure

```
02-stock-analysis/
├── README.md
├── SPEC.md
├── notebooks/
│   ├── exploration.ipynb
│   └── indicators.ipynb
├── src/
│   ├── data.py            # yfinance fetcher
│   ├── indicators.py      # MA, vol, RSI
│   └── dashboard.py       # Plotly Dash app
└── tests/
```

## 🚀 Quick start

```bash
uv sync
uv run python src/data.py AAPL MSFT NVDA --period 2y
uv run python src/dashboard.py
```

## 🎯 Features

- [ ] Fetch OHLCV from yfinance
- [ ] Compute MA(20, 50, 200)
- [ ] Compute volatility (20d, 60d rolling std)
- [ ] Compute RSI, MACD
- [ ] Interactive dashboard with tabs

## 📚 Resources

- yfinance docs: https://pypi.org/project/yfinance/
- Plotly Dash: https://dash.plotly.com/

---

*Status: 🟡 scaffold.*
