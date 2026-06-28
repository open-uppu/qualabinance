#!/usr/bin/env python3
"""
pull_huggingface.py — Pull top finance models + datasets from HuggingFace.

Usage:
    python3 scripts/pull_huggingface.py --out knowledge/05-resources/huggingface-finance-catalog.md
"""
import argparse
import json
import subprocess
import sys
import time
from pathlib import Path
from datetime import datetime, timezone

HF_BASE = "https://huggingface.co/api"
SEARCHES = {
    "models": ["finance", "trading", "stock", "crypto", "quant", "finbert", "finma"],
    "datasets": ["finance", "stock", "trading", "crypto", "sentiment", "earnings", "10-K", "fed"],
}


def curl_json(url: str, timeout: int = 15) -> list:
    """Use curl directly — Python urllib was hanging in this env."""
    try:
        r = subprocess.run(
            ["curl", "-sL", "--max-time", str(timeout), "-A", "Mozilla/5.0", url],
            capture_output=True, text=True, timeout=timeout + 5,
        )
        if r.returncode != 0 or not r.stdout.strip():
            return []
        return json.loads(r.stdout)
    except Exception as e:
        print(f"    ⚠️  {url[:60]}... → {e}", file=sys.stderr)
        return []


def search_kind(kind: str, query: str, limit: int = 10) -> list:
    url = f"{HF_BASE}/{kind}?search={query}&limit={limit}"
    return curl_json(url)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="knowledge/05-resources/huggingface-finance-catalog.md")
    parser.add_argument("--limit", type=int, default=10)
    args = parser.parse_args()

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    # Collect models
    print("📦 Models:")
    models_seen = {}
    for q in SEARCHES["models"]:
        print(f"  search '{q}' ...", end=" ", flush=True)
        results = search_kind("models", q, args.limit)
        print(f"got {len(results)}")
        for m in results:
            mid = m.get("id") or m.get("modelId")
            if not mid or mid in models_seen:
                continue
            models_seen[mid] = {
                "id": mid,
                "downloads": m.get("downloads", 0),
                "likes": m.get("likes", 0),
                "tags": [t for t in m.get("tags", []) if not t.startswith("base_model") and not t.startswith("license")][:5],
                "pipeline": m.get("pipeline_tag", ""),
                "created": m.get("createdAt", "")[:10],
                "private": m.get("private", False),
            }
        time.sleep(0.5)  # be nice to HF

    # Collect datasets
    print("\n📦 Datasets:")
    datasets_seen = {}
    for q in SEARCHES["datasets"]:
        print(f"  search '{q}' ...", end=" ", flush=True)
        results = search_kind("datasets", q, args.limit)
        print(f"got {len(results)}")
        for d in results:
            did = d.get("id")
            if not did or did in datasets_seen:
                continue
            datasets_seen[did] = {
                "id": did,
                "downloads": d.get("downloads", 0),
                "likes": d.get("likes", 0),
                "tags": [t for t in d.get("tags", []) if not t.startswith("base_model")][:5],
                "created": d.get("createdAt", "")[:10],
            }
        time.sleep(0.5)

    # Sort by downloads
    models_sorted = sorted(models_seen.values(), key=lambda x: x["downloads"], reverse=True)
    datasets_sorted = sorted(datasets_seen.values(), key=lambda x: x["downloads"], reverse=True)

    # Build markdown
    lines = [
        "# 🤗 HuggingFace Finance Catalog (Live API)",
        "",
        f"> **Live catalog pulled from `huggingface.co/api` on {today}.**",
        "> Sorted by downloads (descending) — what people actually use.",
        "",
        "---",
        "",
        "## 🧠 Models — Finance LLMs, Classifiers, RL agents",
        "",
        f"**Total unique models found:** {len(models_sorted)}",
        "",
        "| Downloads | Likes | Created | Model ID | Tags |",
        "|---|---|---|---|---|",
    ]
    for m in models_sorted[:50]:
        if m["private"]:
            continue
        tags = ", ".join(m["tags"][:3]) if m["tags"] else "—"
        lines.append(f"| {m['downloads']:>6} | {m['likes']:>4} | {m['created']} | `{m['id']}` | {tags} |")

    lines.extend([
        "",
        "## 📊 Datasets — Prices, Returns, News, On-chain",
        "",
        f"**Total unique datasets found:** {len(datasets_sorted)}",
        "",
        "| Downloads | Likes | Created | Dataset ID | Tags |",
        "|---|---|---|---|---|",
    ])
    for d in datasets_sorted[:50]:
        tags = ", ".join(d["tags"][:3]) if d["tags"] else "—"
        lines.append(f"| {d['downloads']:>6} | {d['likes']:>3} | {d['created']} | `{d['id']}` | {tags} |")

    lines.extend([
        "",
        "---",
        "",
        "## 🏗️ How to use HF data in Qualabinance",
        "",
        "```python",
        "from datasets import load_dataset",
        "from transformers import pipeline",
        "",
        '# Bulk OHLCV',
        'ds = load_dataset("defeatbeta/yahoo-finance-data", "AAPL", split="train")',
        "",
        '# Sentiment (top model by downloads)',
        'classifier = pipeline("text-classification", model="ProsusAI/finbert")',
        "",
        '# Finance LLM (8B, open)',
        'llm = pipeline("text-generation", model="DragonLLM/Llama-Open-Finance-8B")',
        "```",
        "",
        "---",
        "",
        f"**Refreshed:** {today} · **Search queries:** {len(SEARCHES['models']) + len(SEARCHES['datasets'])}",
        "**Re-fetch:** `python3 scripts/pull_huggingface.py`",
        "",
        "**Mode:** 🔄 CONTINUOUS RESEARCH (auto-refresh bi-weekly)",
    ])

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines) + "\n")
    print(f"\n✅ Wrote {len(models_sorted)} models + {len(datasets_sorted)} datasets to {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
