# 📊 Kaggle Finance Catalog (Live API)

> **Live catalog pulled from `kaggle.com/api/v1/datasets/list` on 2026-06-28.**
> Curated for **practical quant use** — skip the toy tutorials and highlight production-quality.

---

## 📈 Stock / Equity Datasets

| Size (bytes) | Title | Use case |
|---|---|---|
| **12,425,985** | **World Stock Prices (Daily Updating)** | 🏆 **Best bulk source** — multi-index daily, updated regularly. |
| **1,918,054,636** | **9000+ Tickers of Stock Market Data (Full History)** | 🏆 Massive US universe, full history. ~2 GB. |
| 220,015 | Apple Stock Price | Single ticker for tutorials. |
| 160,726 | Netflix Stock Price History | Single ticker. |
| 117,048 | Google Stock Price | Single ticker. |
| 106,655 | Netflix Stock Price | Duplicate (use the History version). |
| 104,879 | NVIDIA Daily Stock Prices (2016–2026) | Multi-year single ticker. |
| 94,666 | Tesla Stock Price History | Single ticker. |
| 81,522 | Tesla Stock Price | Duplicate. |
| 65,301 | Alibaba (BABA) Stock Market Dataset (2014–2023) | ADRs. |
| 41,317 | S&P 500 Daily Prices 1986 - 2018 | Long-history index. |
| 34,499 / 21,417 / 12,133 | Various duplicates | Skip. |
| 1,481,314 | Goldman Sachs (GS) Stock Data (1999–2026) | Single ticker, 27-year history. |

---

## ₿ Crypto / Bitcoin Datasets

| Size (bytes) | Title | Use case |
|---|---|---|
| **1,700,101,813** | **Bitcoin tweets - 16M tweets** | 🏆 Largest crypto sentiment corpus. |
| 728,456,658 | Bitcoin Tweets (other version) | Smaller variant. |
| 108,173,820 | Bitcoin Historical Data | Price + volume history. |
| 84,059,816 | Bitcoin Historical Dataset | Variant. |
| 10,165,737 | Bitcoin Price (USD) | Clean simple price series. |
| 116,825 / 78,757 / 77,757 | Smaller Bitcoin price datasets | For tutorials only. |
| 0 | Bitcoin Blockchain Historical Data | ⚠️ Zero-size — link broken. |

---

## 📰 News / Sentiment

| Size | Title | Use case |
|---|---|---|
| 1,046,646 | Financial News Sentiment vs Market 2020 - Present | Sentiment-aligned to market data. |
| 12,001,191 | Multi-Label Classification Dataset | NLP on Research Articles. |
| 11,978,949 | Topic Modeling for Research Articles | Methodology paper companion. |
| 1,116,612 | NYMEX Crude Oil Futures Dataset (CL Contract) | Commodity prices. |

---

## 🎯 How to use Kaggle data in Qualabinance

```python
# 1. Install + authenticate
pip install kaggle
export KAGGLE_USERNAME=...
export KAGGLE_KEY=...

# 2. Download a dataset programmatically
import kaggle
kaggle.api.authenticate()
kaggle.api.dataset_download_files(
    "mattiuzc/stock-exchange-data",
    path="data/kaggle/",
    unzip=True,
)

# 3. Or use the Kaggle CLI
!kaggle datasets download -d borismarjanovic/price-volume-data-for-all-us-stocks-etfs
```

---

## 🏆 Top picks (ranked for Qualabinance use)

1. **`borismarjanovic/price-volume-data-for-all-us-stocks-etfs`** (1.9 GB) — bulk US universe
2. **`mattiuzc/stock-exchange-data`** — multi-index daily
3. **`defeatbeta/yahoo-finance-data` (HuggingFace)** — alternative bulk pull
4. **`Bitcoin tweets - 16M tweets`** — sentiment ground truth for crypto
5. **`S&P 500 Daily Prices 1986 - 2018`** — long-history benchmark
6. **`Financial News Sentiment vs Market 2020 - Present`** — already aligned

---

## 🔁 Maintenance

```bash
curl -sL "https://www.kaggle.com/api/v1/datasets/list?search=stock+price&page_size=50" \
  | python3 -c "import json,sys; [print(d['totalBytesNullable'],d['titleNullable']) for d in json.load(sys.stdin)]"
```

**Verified:** 2026-06-28 · **API:** `kaggle.com/api/v1/datasets/list?search=<query>` (anonymous, rate-limited)
