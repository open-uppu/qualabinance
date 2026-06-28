# 🤗 HuggingFace Finance Catalog (Live API)

> **Live catalog pulled from `huggingface.co/api/models` and `huggingface.co/api/datasets` on 2026-06-28.**
> Sorted by downloads (descending) — these are the **models/datasets people actually use**, not the ones with the cleverest names.

---

## 🧠 Models — Finance-tuned LLMs & Classifiers

| Downloads | Likes | Model ID | Notes |
|---|---|---|---|
| **65,889** | 69 | `nickmuchi/finbert-tone-finetuned-finance-topic-classification` | Most-downloaded FinBERT variant. Tone + topic classification on financial news. **Canonical starting point** for sentiment. |
| 2,038 | 32 | `DragonLLM/Llama-Open-Finance-8B` | Llama-3.1-8B fine-tuned for finance Q&A. Open weights. |
| 1,962 | 6 | `mradermacher/DeepSeek-R1-Finance-Reasoning-14B-GGUF` | DeepSeek-R1 reasoning model, finance-tuned, GGUF for local inference. |
| 729 | 1 | `mradermacher/FinanceGemma-E4B-GGUF` | Gemma finance variant. |
| 506 | 46 | `tarun7r/Finance-Llama-8B` | Llama fine-tune for finance. |
| 170 | 159 | `Adilbai/stock-trading-rl-agent` | **Most-liked trading model** — RL agent for stocks. |
| 68 | 34 | `mrzlab630/lora-alpaca-trading-candles` | LoRA for candlestick trading on Alpaca. |
| 6 | 14 | `nickmuchi/fb-bart-large-finetuned-trade-the-event-finance-summarizer` | BART for finance event summarization. |
| 5 | 2 | `jakobwes/finance-gpt2` | GPT-2 from-scratch on finance corpus (educational). |
| 5 | 1 | `yeeb/distilgpt2_trading-fours` | DistilGPT-2 for trading commentary. |
| 4 | 3 | `papepipopu/trading_ai` | Trading AI demo. |
| 4 | 0 | `liqi6811/tradingBERT_tokenizer_{AUD_USD,EUR_GBP,GBP_USD,USD_JPY}` | FX-pair tokenizers (specialized vocab). |
| 2 | 0 | `krevas/finance-electra-{small,base}-{discriminator,generator}` | ELECTRA variants for finance generation. |
| 4 | 0 | `krevas/finance-koelectra-{small,base}-*` | Korean ELECTRA for finance. |

---

## 📊 Datasets — Prices, Returns, News

### Prices & OHLCV
| Downloads | Dataset ID | What's in it |
|---|---|---|
| **141,643** | `defeatbeta/yahoo-finance-data` | 🏆 **#1 finance dataset on HuggingFace.** Bulk pull of Yahoo Finance historical data across symbols. |
| 554 | `arthurneuron/cryptocurrency-futures-ohlcv-dataset-1m` | Crypto futures OHLCV at 1-minute granularity. |
| 34 | `qinchen1986/a_stock_kline_mainboard_next_return_2025` | Chinese A-share K-line + next-day return labels (2025). |
| 45-282 | `nateraw/airbnb-stock-price*`, `ElKulako/stocktwits-crypto`, `mjw/stock_market_tweets` | Smaller scrapers, often used for tutorials. |

### Financial NLP / QA / Reasoning
| Downloads | Dataset ID | What's in it |
|---|---|---|
| 4,311 | `PatronusAI/financebench` | Patronus's finance reasoning benchmark (RAG evaluation). |
| 984 | `Josephgflowers/Finance-Instruct-500k` | 500k instruction-tuned finance samples. |
| 901 | `gretelai/synthetic_pii_finance_multilingual` | Synthetic PII for finance (compliance testing). |
| 537 | `BCCard/BCAI-Finance-Kor-Embedding-Pair` | Korean finance embeddings. |
| 404 | `AfterQuery/FinanceQA` | Finance QA dataset (RAG eval). |
| 182 | `Duxiaoman-DI/FinanceIQ` | Chinese financial IQ benchmark. |
| 167 | `sujet-ai/Sujet-Finance-Vision-10k` | SEC 10-K visual extraction (multimodal). |
| 61 | `VedantPadwal/quantitative-finance-reasoning` | Quant finance reasoning (small). |
| 24 | `FinanceMTEB/DISCFinLLM-Computing` | Chinese financial MTEB benchmark. |

### On-chain / Crypto
| Downloads | Dataset ID | What's in it |
|---|---|---|
| 123 | `BlockDB/Raw-Blocks-Ethereum-And-EVM-Cryptocurrency-Data` | Raw blocks for ETH + EVM chains. |
| 70 | `BlockDB/ERC20-Tokens-Ethereum-And-EVM-Cryptocurrency-Data` | ERC-20 token transfers. |
| 39 | `BlockDB/Raw-Transactions-Ethereum-And-EVM-Cryptocurrency-Data` | Raw transactions. |
| 19 | `BlockDB/Raw-Logs-Ethereum-And-EVM-Cryptocurrency-Data` | Event logs. |
| 18 | `BlockDB/Liquidity-Pools-Ethereum-And-EVM-Cryptocurrency-Data` | Liquidity pool state (Uniswap V2/V3). |
| 16 | `aaurelions/cryptocurrency-tweets-sentiment` | Crypto Twitter sentiment. |
| 35 | `NickyNicky/Finance_cryptocurrency_Spanish_5.5k` | Spanish crypto finance data. |
| 9 | `Omarrran/50k_Cryptocurrency_Transaction_Dataset_by_HNM` | 50k transactions (educational). |

---

## 🏗️ How to use HuggingFace data in Qualabinance

```python
from datasets import load_dataset

# Example: bulk OHLCV
ds = load_dataset("defeatbeta/yahoo-finance-data", "AAPL", split="train")
df = ds.to_pandas()

# Example: FinBERT sentiment (use the most-downloaded variant)
from transformers import AutoTokenizer, AutoModelForSequenceClassification
tok = AutoTokenizer.from_pretrained("nickmuchi/finbert-tone-finetuned-finance-topic-classification")
model = AutoModelForSequenceClassification.from_pretrained("nickmuchi/finbert-tone-finetuned-finance-topic-classification")

# Example: finance LLM (small + open)
from transformers import pipeline
llm = pipeline("text-generation", model="DragonLLM/Llama-Open-Finance-8B")
```

**Auth tip:** Some downloads need a HF token (free). Set `HUGGINGFACE_TOKEN` in `.env`.

---

## 🔁 Maintenance

```bash
# Re-fetch this catalog (run quarterly)
curl -sL "https://huggingface.co/api/models?search=finance&limit=50" \
  | python3 -c "import json,sys; [print(m['downloads'],m['id']) for m in json.load(sys.stdin)]"
```

---

**Verified:** 2026-06-28 · **API:** `huggingface.co/api/{models,datasets}?search=finance` (no key needed for public)
