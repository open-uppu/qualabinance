# 📜 arXiv Frontier — Live Daily Snapshot

> **Live arXiv q-fin feed, re-fetchable any time.** Shows the freshest frontier papers submitted to q-fin.ST, q-fin.TR, q-fin.GN, q-fin.PR, q-fin.RM.
>
> **Built:** 2026-06-28 · **Re-fetch cadence:** weekly recommended

---

## 🎯 Why this file

The static curated lists (`_q1-ml-finance.md`, `_q1-portfolio-risk.md`, `_q1-econometrics.md`, `_q1-2024-2026-frontier.md`) capture the **important** papers.

This file captures the **fresh** papers — the ones submitted last week that haven't been cited yet but might be the next big thing. Refresh this file weekly to catch frontier work.

---

## 🆕 Latest submissions (sorted by date, pulled 2026-06-28)

### q-fin.ST + q-fin.TR (Statistical / Trading)

| Date | Title | Category | Quick take |
|---|---|---|---|
| **2026-06-24** | The Inference-Compute Frontier and a Latency-Efficient Architecture for Limit Order Book Prediction | q-fin.TR | Pareto frontier for HFT inference cost vs LOB-pred accuracy. Practical deploy angle. |
| **2026-06-24** | Hierarchical Graph Learning for Calendar Spread Strategies in Commodity Futures Markets | q-fin.TR | GNN for commodity calendar spreads. |
| **2026-06-24** | Time-dependent weighted directed networks of cryptocurrency interaction from high-frequency returns | q-fin.TR | Network analysis of crypto from HF data. |
| **2026-06-22** | Empirical Confirmation of the Square-Root Law of Market Impact in a U.S. Large-Cap Equity | q-fin.TR | Confirms square-root law on US large-cap (joins futures + options evidence). |
| **2026-06-22** | Continuous Hidden Markov Models for Equity Returns: Heavy-Tail Emission Families and Regime-Conditional Value-at-Risk | q-fin.ST | HMM + Student-t for regime-conditional VaR. |
| **2026-06-22** | Mitigating Adverse Selection in Concentrated Liquidity AMMs with Dynamic Fees: An Agent-Based Model Approach | q-fin.TR | Dynamic fees in AMMs (Uniswap V3 style). |
| **2026-06-20** | When Staking Rewards Compound: Measuring the Impact of Ethereum's Pectra Upgrade | q-fin.GN | Empirical impact of ETH Pectra upgrade. |
| **2026-06-19** | KineticSim: A Lightweight, High-Performance Execution Engine for Real-Time Market Simulators | q-fin.TR | Open-source market simulator (ABIDES alternative). |
| **2026-06-19** | Endogenous Randomness from Adversarial Market Learning | q-fin.TR | Theory: markets become random when learners compete adversarially. |
| **2026-06-19** | Leakage-Aware Benchmarking of LLM Forecasting: Real-Time Nowcasts as the Decision-Time Input for Macro Factor Ranking | q-fin.ST | Critical: how to benchmark LLM forecasts without leakage. |
| **2026-06-18** | AI Economist Agent: An Agentic Framework for Model-Grounded Economic Analysis with RAG, Knowledge Graphs, and LLMs | q-fin.GN | LLM agent + RAG + KG for grounded economic research. |
| **2026-06-18** | Trends, Volatility, Correlations, and Critical Phenomena in Financial Markets | q-fin.ST | Statistical physics view of vol clustering. |
| **2026-06-18** | Multi-Stream Temporal Fusion for Financial Fraud Detection | q-fin.ST | Multi-stream TFT for fraud. |
| **2026-06-17** | Which Portfolios? The Construction Dependence of Factor Model Performance | q-fin.PR | Factor perf is portfolio-construction dependent. |
| **2026-06-17** | Fitting Accumulated Stock Returns with Tempered Skew t-Distribution | q-fin.ST | Distribution choice for cumulative returns. |
| **2026-06-15** | Revisiting Trade-sign Long-memory and Square-root Law price impact | q-fin.TR | Long-memory trade signs + square-root law. |
| **2026-06-14** | Trading in the Sunshine or in the Shade: Market Impact and Adverse Selection on Hyperliquid | q-fin.TR | Hyperliquid (on-chain perp DEX) microstructure. |
| **2026-06-12** | Correlation emergence and the Epps effect in two coupled limit order books | q-fin.TR | Theory of correlation between coupled LOBs. |
| **2026-06-11** | CFOs Meet LLMs | q-fin.GN | Empirical study of LLM impact on CFO decisions. |
| **2026-06-11** | Resolution-Aware Perpetual Futures on Binary Prediction Markets | q-fin.GN | Risk design for prediction-market perps. |
| **2026-06-11** | Manipulation, Insider Information, and Regulation in Leveraged Event-Linked Markets | q-fin.GN | Manipulation on leveraged event contracts. |
| **2026-06-11** | A Taxonomy of Event-Linked Perpetual Futures | q-fin.GN | Taxonomy of event-perp designs. |
| **2026-06-10** | Composite likelihood inference of fractional Gaussian processes | q-fin.ST | Long-memory vol via fGNP. |
| **2026-06-09** | Auditing Asset-Specific Preferences in Financial LLMs: Evidence from Bitcoin Representations and Portfolio Allocation | q-fin.GN | Probes LLMs for BTC bias. |
| **2026-06-07** | TT-DAC-PS: Twin-Target Deterministic Actor-Critic with Policy Smoothing for Optimal Trade Execution | q-fin.TR | Twin-target TD3 for execution. |
| **2026-06-06** | Post-Rejection Follow-up Sampling: A Methodology for Counterfactual Outcome Measurement in Algorithmic DEX Trading | q-fin.TR | Counterfactual measurement for DEX. |
| **2026-06-04** | Multi-Scale Markov Switching GARCH | q-fin.ST | Multi-horizon MS-GARCH for vol term-structure. |
| **2026-06-04** | Market Informedness and Market-Maker Profitability | q-fin.TR | Theory + empirics of MM PnL. |
| **2026-06-03** | Dynamic Multi-Pair Trading Strategy in Cryptocurrency Markets with Deep Reinforcement Learning | q-fin.TR | Multi-pair RL for crypto. |
| **2026-06-01** | VIX options in Bergomi models | q-fin.PR | Pricing VIX options under rough Bergomi. |
| **2026-06-01** | Foresight Arena: An On-Chain Benchmark for Evaluating AI Forecasting Agents | q-fin.GN | Crypto-incentivized AI forecasting benchmark. |

---

## 🔄 How to re-fetch (cron-friendly)

```python
import requests
import xml.etree.ElementTree as ET
from datetime import datetime, timezone

NS = {"a": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}

def fetch_arxiv(query: str, max_results: int = 50) -> list[dict]:
    """Pull papers from arXiv API."""
    url = "https://export.arxiv.org/api/query"
    params = {
        "search_query": query,
        "max_results": max_results,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }
    r = requests.get(url, params=params, headers={"User-Agent": "qualabinance/0.1"})
    r.raise_for_status()
    root = ET.fromstring(r.text)
    papers = []
    for entry in root.findall("a:entry", NS):
        title = entry.find("a:title", NS).text.strip().replace("\n", " ")
        arxiv_id = entry.find("a:id", NS).text.split("/")[-1]
        published = entry.find("a:published", NS).text[:10]
        summary = entry.find("a:summary", NS).text.strip()[:280] + "..."
        authors = [a.find("a:name", NS).text for a in entry.findall("a:author", NS)]
        papers.append({
            "arxiv_id": arxiv_id,
            "title": title,
            "date": published,
            "authors": authors[:3] + (["…"] if len(authors) > 3 else []),
            "summary": summary,
            "url": f"https://arxiv.org/abs/{arxiv_id}",
        })
    return papers

# Pull last 30 days
papers = (
    fetch_arxiv("cat:q-fin.ST", 25)
    + fetch_arxiv("cat:q-fin.TR", 25)
    + fetch_arxiv("cat:q-fin.GN", 15)
    + fetch_arxiv("cat:q-fin.PR", 10)
    + fetch_arxiv("cat:qfin.RM", 10)
)
print(f"Pulled {len(papers)} papers")

# Save to file
import json
with open("knowledge/05-resources/arxiv-frontier-live.md", "a") as f:
    f.write(f"\n\n## Re-fetched {datetime.now(timezone.utc).date()}\n")
    for p in papers:
        f.write(f"\n### [{p['title']}]({p['url']})\n")
        f.write(f"**{', '.join(p['authors'])}** · {p['date']} · `{p['arxiv_id']}`\n\n")
        f.write(f"> {p['summary']}\n")
```

---

## 🎯 Reading priority rule

When you re-fetch, sort the new papers by this priority:

1. **Multi-author + recent + well-known lab** (e.g., AI4Finance, Chicago, Oxford, ETH)
2. **Has public code link** in abstract
3. **Has reproducibility claim** (dataset + benchmark)
4. **Cites one of the canonical 2024-2026 frontier papers** (chains into existing knowledge)

If it scores 3+, add to `_q1-2024-2026-frontier.md` static list. If 1-2, log here for awareness.

---

## 📊 Coverage stats

- **Last refresh:** 2026-06-28
- **Total papers in this snapshot:** 31 (across all q-fin categories)
- **Date range covered:** last ~30 days
- **Refresh cadence:** weekly recommended, monthly acceptable

**API:** `https://export.arxiv.org/api/query?search_query=cat:q-fin.*&max_results=50&sortBy=submittedDate&sortOrder=descending` (free, no auth, rate-limited via 429 after burst)
