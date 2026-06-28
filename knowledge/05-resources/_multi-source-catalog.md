# 🌐 Multi-Source Knowledge Catalog — Live API Catalog

> **Beyond papers + GitHub.** Live data catalog from HuggingFace, Kaggle, arXiv (the three we can pull programmatically) + curated lists for sources that need API keys (NYT, Reddit, Semantic Scholar) or are content-behind-paywall (WSJ, FT, Bloomberg).
>
> **Built:** 2026-06-28 · **Owner:** Qualabinance / QuantResearcher
>
> **Companions:**
> - [`huggingface-finance-catalog.md`](huggingface-finance-catalog.md) — HF live catalog
> - [`kaggle-finance-catalog.md`](kaggle-finance-catalog.md) — Kaggle live catalog
> - [`arxiv-frontier-live.md`](arxiv-frontier-live.md) — arXiv live frontier
> - [`papers/_q1-2024-2026-frontier.md`](papers/_q1-2024-2026-frontier.md) — curated frontier papers
> - [`_additional-sources.md`](_additional-sources.md) — newsletters/podcasts/CBs

---

## 📊 Coverage matrix

| Source | API free? | Rate limit | Auth needed | What you get |
|---|---|---|---|---|
| **arXiv** | ✅ | soft (429 after burst) | none | papers (q-fin.ST/TR/GN/PR/RM) |
| **HuggingFace** | ✅ | generous | none (token for private) | models + datasets + spaces |
| **Kaggle** | ✅ | soft | username+API key | datasets + competitions + notebooks |
| **Semantic Scholar** | ✅ | 100 req / 5 min (anonymous) | optional key | papers + citations + authors |
| **OpenAlex** | ✅ | generous | none | papers + authors + concepts |
| **CrossRef** | ✅ | 50 req/s | none | DOIs + citation metadata |
| **Reddit JSON** | ⚠️ | blocked in many envs | none | posts + comments (rate-limited) |
| **NYT Archive API** | ✅ | 500/day free, 5000/day paid | API key required | news articles since 1851 |
| **WSJ / FT / Bloomberg** | ❌ | paid | subscription | news + opinion + research |
| **GDELT** | ✅ | generous | none | global events database (15-min resolution) |
| **OpenSecrets** | ✅ | 200/day | key optional | US political finance |
| **USPTO PatentsView** | ✅ | generous | none | US patents (NLP-friendly) |
| **Twitter/X API** | ❌ | paid tier required | $100-$5000/mo | tweets + users (was free) |
| **Mastodon (Fediverse)** | ✅ | per-instance | none | posts + toots |
| **YouTube Data API** | ✅ | 10,000 units/day | OAuth key | videos + comments + channels |

---

## 🗞️ News sources (NYT, FT, WSJ, Bloomberg)

> **Note:** Most paywalled. Listed with API + scrape-respect notes.

### New York Times
- **Archive API** — `api.nytimes.com/svc/archive/v1/{YEAR}/{MONTH}.json?api-key=...`
  - Free: 500 req/day. Returns article metadata (headline, lead_paragraph, pub_date, section, person, gloc, org, des_facet).
  - Best for: financial news back to 1851, well-tagged.
- **Article Search API** — search articles since 1981 by query, date, section.
- **Books API** — bestseller lists.
- **Most Popular API** — trending.
- **Top Stories API** — current headlines.
- **Signup:** https://developer.nytimes.com/

### Financial Times
- **FT API (paid)** — full-text access, used by quant funds for news alpha.
- **FT Lex API (paid)** — sentiment + entity extraction from FT articles (the original "news sentiment" service).
- **Signup:** enterprise sales, ~$10k+/yr

### Wall Street Journal
- **WSJ via Dow Jones** — paid enterprise API, Factiva integration.
- **Signup:** enterprise only.

### Bloomberg
- **B-PIPE / Terminal API** — the gold standard. Used by every institutional quant.
- **Signup:** ~$24k-$28k/yr per seat for Terminal + API tier.

### Other credible news

| Source | URL | Notes |
|---|---|---|
| **Reuters Connect** | reuters.com/connect | paid enterprise |
| **Associated Press** | apnews.com | syndication only |
| **BBC RSS** | bbc.co.uk/news | free + legal |
| **The Guardian Open Platform** | openplatform.theguardian.com | free tier, 500 req/day |
| **ProPublica** | propublica.org/api | free, investigative |
| **The Conversation** | theconversation.com | free, academic-penned |
| **ArxivTimes** | arxivtimes.com | TL;DR of arXiv (curated) |
| **Hacker News (Algolia API)** | hn.algolia.com/api | free, tech/quant adjacent |
| **Lobsters** | lobste.rs | free, tech-curve |
| **Slashdot** | slashdot.org | free, legacy tech |
| **Quartz** | qz.com | free, business |
| **Marketplace (NPR)** | marketplace.org | free, econ |

---

## 💬 Social media (Reddit, Twitter, Stocktwits, Discord)

### Reddit
- **JSON API**: `reddit.com/r/{subreddit}/top.json?t=week&limit=100` — **frequently blocked** in cloud IPs.
- **Better:** use [Pushshift](https://pushshift.io) or [Camas](https://camas.github.io/) for historical, or [Arctic Shift](https://github.com/ArthurHeitmann/arctic_shift) for new.
- **Key subs**: r/quant, r/algotrading, r/wallstreetbets, r/options, r/finance, r/economics, r/CryptoCurrency, r/Bitcoin, r/ethereum, r/defi

### Twitter/X
- **Basic tier:** $100/mo — 10,000 tweets/mo read.
- **Pro tier:** $5,000/mo — 1M tweets + filtering + full archive.
- **Alternatives:**
  - **Nitter** (free, but unreliable since X crackdown)
  - **Mastodon** (Fediverse) — finance community exists at `infosec.exchange`, `social.linux.pizza`
  - **Bluesky** — `public.api.bsky.app` (free, growing finance presence)
  - **Threads** (Meta) — limited API

### Stocktwits
- **Streaming API** (free tier) — `stocktwits.com/streaming`
- **Historical:** via partnerships ($$$)
- **Why it matters:** retail sentiment for US equities, very fast signal.

### Discord
- **No public bulk API**, but invite links:
  - **WorldQuant BRAIN** — alphas + competitions
  - **Optuna** — hyperparameter tuning
  - **HuggingFace** — open-source LLMs
  - **QuantConnect** — Lean algo trading
  - **Numerai** — crowdsourced hedge fund

---

## 📚 Academic / Paper sources (beyond arXiv)

### OpenAlex
- **API:** `api.openalex.org/works?search=Kronos&per-page=10`
- **Better than arXiv for cross-disciplinary** — covers arXiv + journals + conferences + repositories.
- **Free, generous rate limits.**
- **Schema:** works (papers), authors, sources (venues), concepts (topics), institutions, funders.

### Semantic Scholar
- **API:** `api.semanticscholar.org/graph/v1/paper/search?query=...`
- **Free tier:** 100 req / 5 min. **Paid API key** for higher.
- **Schema:** title, year, authors, citationCount, referenceCount, fieldsOfStudy, tldr (AI-generated), embedding.
- **Why:** citation graph + TLDR summaries.

### CrossRef
- **API:** `api.crossref.org/works/{DOI}`
- **Free, no auth.**
- **Why:** DOI metadata, citation links, funder info, license, references.

### Connected Papers
- **API:** paid tier only.
- **UI:** connectedpapers.com — paper graph visualization.

### Papers With Code
- **API:** `paperswithcode.com/api/v1/papers/?q=...`
- **Free tier.**
- **Why:** links papers ↔ code ↔ benchmarks ↔ datasets ↔ SOTA leaderboards.

### Google Scholar
- **No public API** (scrape violates ToS).
- **Alternatives:** OpenAlex / Semantic Scholar (above).
- **SerpAPI** (paid proxy) — $50/mo for 5,000 searches.

### ResearchGate
- **No public API.**
- **UI only:** researchgate.net — author contact + full-text requests.

---

## 📊 Datasets (beyond HuggingFace + Kaggle)

### Government / Open data
| Source | URL | What |
|---|---|---|
| **data.gov** | catalog.data.gov | US open data catalog |
| **EU Open Data** | data.europa.eu | EU open data |
| **data.gov.uk** | data.gov.uk | UK open data |
| **data.go.jp** | data.go.jp | Japan open data |
| **data.govt.nz** | data.govt.nz | New Zealand open data |
| **data.th** (planned) | — | Thailand (sparse) |
| **Singapore Open Data** | data.gov.sg | SG open data |
| **CKAN global catalog** | catalog.data.gov/dataset | meta-catalog |
| **World Bank Open Data** | data.worldbank.org | macro |
| **UN Data** | data.un.org | global stats |
| **Eurostat** | ec.europa.eu/eurostat | EU stats |
| **OECD Data** | data.oecd.org | OECD stats |
| **IMF Data** | data.imf.org | macro |
| **WHO GHO** | apps.who.int/gho | health (matters for ESG) |
| **NASA Earthdata** | earthdata.nasa.gov | climate + remote sensing |
| **NOAA Climate** | ncdc.noaa.gov | weather + climate |
| **USGS** | usgs.gov | geology + water |
| **OpenStreetMap** | openstreetmap.org | geospatial |

### Financial-specific
| Source | URL | What |
|---|---|---|
| **Quandl / Nasdaq Data Link** | data.nasdaq.com | 250+ providers |
| **FRED** | fred.stlouisfed.org | US macro |
| **World Federation of Exchanges** | world-exchanges.org | monthly aggregates |
| **Bank for International Settlements** | bis.org/statistics | global liquidity |
| **CME DataMine** | cmegroup.com/market-data/datamine.html | historical futures tick |
| **ICE Data Services** | theice.com/market-data | historical futures/options |
| **LSEG (LSE Group)** | refinitiv.com | enterprise data |
| **Bloomberg BQL** | bloomberg.com | enterprise data |
| **Databento** | databento.com | modern tick data API |
| **Polygon.io** | polygon.io | US equities + options |
| **Tardis** | tardis.dev | crypto tick |
| **Kaiko** | kaiko.com | institutional crypto |
| **Glassnode** | glassnode.com | on-chain |
| **Dune Analytics** | dune.com | on-chain SQL |
| **Flipside Crypto** | flipsidecrypto.com | on-chain analytics |
| **Messari** | messari.io | crypto research |
| **The Block** | theblock.co | crypto data + research |
| **DefiLlama** | defillama.com | DeFi TVL |
| **Coin Metrics** | coinmetrics.io | network data + market |
| **CoinMarketCap** | coinmarketcap.com | price + market cap |
| **CryptoCompare** | cryptocompare.com | aggregated prices |
| **CoinGecko** | coingecko.com | aggregated prices |

### Academic datasets
| Source | URL | What |
|---|---|---|
| **CRSP** | crsp.org | US equities (academic subscription) |
| **Compustat** | moodys.com | fundamentals (subscription) |
| **TAQ** | nyse.com/taq | US tick (academic subscription) |
| **Thomson Reuters Tick History** | refinitiv.com | tick (subscription) |
| **OptionMetrics** | optionmetrics.com | options (academic subscription) |
| **IBES** | ibes.com | analyst estimates |
| **SDC Platinum** | refinitiv.com | M&A + IPO deals |
| **WRDS** | wrds-www.wharton.upenn.edu | meta-platform for academic data |
| **Pandas-Datareader** | pandas-datareader.org | unified interface to many sources |
| **Tiingo** | tiingo.com | EOD + news + fundamentals |

---

## 🎥 Video & Lecture sources

| Platform | URL | Best for |
|---|---|---|
| **YouTube** | youtube.com | free lectures (MIT, Stanford, Simons, 3Blue1Brown) |
| **Coursera** | coursera.org | structured courses |
| **edX** | edx.org | MITx, ColumbiaX, HarvardX |
| **Udacity** | udacity.com | nanodegrees (some free) |
| **DataCamp** | datacamp.com | interactive Python finance |
| **Kaggle Learn** | kaggle.com/learn | free micro-courses |
| **HuggingFace Course** | huggingface.co/learn | NLP + transformers |
| **fast.ai** | fast.ai | deep learning for coders |
| **MIT OpenCourseWare** | ocw.mit.edu | full MIT curriculum |
| **Stanford Lagunita** | lagunita.stanford.edu | Stanford courses |
| **Tib Academy (QuantInsti)** | quantinsti.com | EPAT quant algo trading |
| **Udemy** | udemy.com | cheap paid courses (often on sale) |
| **Pluralsight** | pluralsight.com | tech-focused |
| **MasterClass** | masterclass.com | not technical but high-quality |

---

## 🎙️ Podcast directories

| Platform | URL |
|---|---|
| **Apple Podcasts** | podcasts.apple.com |
| **Spotify** | open.spotify.com |
| **Pocket Casts** | pocketcasts.com |
| **Overcast** | overcast.fm |
| **Castro** | castro.fm |
| **Google Podcasts** (sunset, archive at) | podcasts.google.com |
| **YouTube Music** | music.youtube.com (audio) |
| **Listen Notes** | listennotes.com | search engine for podcasts |
| **Podchaser** | podchaser.com | ratings + reviews |
| **Podcast Index** | podcastindex.org | open podcast directory |

---

## 📡 Real-time data streams (low-latency)

| Source | URL | Latency |
|---|---|---|
| **IEX DEEP+** | iexexchange.io | ~50 µs |
| **Polygon.io WebSocket** | polygon.io | ~10ms |
| **Databento live** | databento.com | ~50ms |
| **Binance WebSocket** | binance.com | ~100ms |
| **Coinbase Pro WS** | pro.coinbase.com | ~100ms |
| **Kraken WS** | kraken.com | ~100ms |
| **Interactive Brokers TWS API** | interactivebrokers.com | ~100ms |
| **Tradier Streaming** | tradier.com | ~100ms |
| **Alpaca Stream** | alpaca.markets | ~200ms |
| **Finnhub Stream** | finnhub.io | ~250ms |
| **Quandl Streaming (defunct → use Nasdaq Data Link)** | data.nasdaq.com | varies |

---

## 📊 Charting & Visualization

| Tool | URL | Notes |
|---|---|---|
| **TradingView** | tradingview.com | retail, free tier + paid Pro+ |
| **Plotly** | plotly.com | open-source + Dash enterprise |
| **Bokeh** | bokeh.org | Python interactive |
| **Matplotlib + mplfinance** | matplotlib.org / mplfinance | classic Python |
| **Seaborn** | seaborn.pydata.org | statistical viz |
| **Vega-Altair** | altair-viz.github.io | declarative |
| **Apache ECharts** | echarts.apache.org | web-native |
| **D3.js** | d3js.org | max flexibility, steep curve |
| **Chart.js** | chartjs.org | web simple |
| **Highcharts** | highcharts.com | enterprise |
| **Observable Plot** | observablehq.com/plot | D3 + JS + notebook |
| **Streamlit** | streamlit.io | Python dashboarding |
| **Gradio** | gradio.app | ML demo UI |
| **Dash** | dash.plotly.com | Python enterprise dashboard |

---

## 🔁 How to keep this catalog fresh

```bash
# HuggingFace (already done)
curl -sL "https://huggingface.co/api/models?search=finance&limit=50" > /tmp/hf.json

# Kaggle (already done)
curl -sL "https://www.kaggle.com/api/v1/datasets/list?search=stock&page_size=50" > /tmp/kg.json

# arXiv frontier
curl -sL "https://export.arxiv.org/api/query?search_query=cat:q-fin.ST+OR+cat:q-fin.TR&max_results=50&sortBy=submittedDate&sortOrder=descending" > /tmp/arxiv.xml

# OpenAlex (new addition)
curl -sL "https://api.openalex.org/works?search=Kronos+foundation+model+finance&per-page=10" | python3 -m json.tool

# Semantic Scholar (rate limited, use key)
curl -sL -H "x-api-key: $S2_KEY" "https://api.semanticscholar.org/graph/v1/paper/search?query=Kronos&limit=10"

# NYT (needs key)
curl -sL "https://api.nytimes.com/svc/archive/v1/2026/6.json?api-key=$NYT_KEY" | python3 -m json.tool | head
```

**Cadence:** quarterly re-fetch. Add entries that emerged since last sync.

---

## 🛡️ Auth checklist

```bash
# Add to .env at repo root
HUGGINGFACE_TOKEN=...            # free, hf.co/settings/tokens
KAGGLE_USERNAME=...              # kaggle.com/settings
KAGGLE_KEY=...
NYT_API_KEY=...                  # developer.nytimes.com (free 500/day)
GUARDIAN_API_KEY=...             # openplatform.theguardian.com/access
SEMANTIC_SCHOLAR_KEY=...         # semanticscholar.org/product/api (optional, lifts rate limit)
ALPHAVANTAGE_KEY=...             # alphavantage.co (free 25/day)
FRED_API_KEY=...                 # fred.stlouisfed.org (free)
COINGECKO_PRO_KEY=...            # coingecko.com/en/api/pricing (optional, $129/mo)
BINANCE_API_KEY=...              # for live trading
```

---

## 🎯 Recommendations by use case

| You want to… | Use |
|---|---|
| Trade US stocks (research) | Kaggle 9000-tickers + HuggingFace yahoo-finance + FRED |
| Trade crypto (research) | Binance OHLCV via ccxt + CoinGecko + on-chain via Dune |
| Build a financial LLM | HuggingFace FinBERT/Llama-Pro-Finance + Finance-Instruct-500k |
| Sentiment features | NYT API + Financial News Sentiment Kaggle + FinBERT |
| Build a portfolio | AQR Insights + Robeco + Man Institute + BlackRock |
| Find new papers | arXiv + OpenAlex + Semantic Scholar |
| Find new repos | GitHub Trending + Papers With Code |
| Find news alpha | Bloomberg/FT (paid) + NYT Archive + Reddit (open) |
| Get jobs | LinkedIn + QuantNet + Wilmott + eFinancialCareers |

---

**Verified:** 2026-06-28 · **Coverage:** 11 source categories · **Next sync:** 2026-09-28
