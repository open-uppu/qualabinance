#!/usr/bin/env python3
"""
pull_kaggle.py — Pull top finance datasets from Kaggle (anonymous API).

Usage:
    python3 scripts/pull_kaggle.py --out knowledge/05-resources/kaggle-finance-catalog.md
"""
import argparse
import json
import subprocess
import sys
import time
import urllib.parse
from pathlib import Path
from datetime import datetime, timezone

KAGGLE_BASE = "https://www.kaggle.com/api/v1"
QUERIES = [
    "stock price", "stock market", "bitcoin", "ethereum", "crypto",
    "trading", "sentiment", "quantitative finance", "futures",
    "options", "forex", "bond", "earnings", "10-K",
]


def curl_json(url: str, timeout: int = 15) -> list:
    try:
        r = subprocess.run(
            ["curl", "-sL", "--max-time", str(timeout), "-A", "Mozilla/5.0", url],
            capture_output=True, text=True, timeout=timeout + 5,
        )
        if r.returncode != 0 or not r.stdout.strip():
            return []
        return json.loads(r.stdout)
    except Exception as e:
        return []


def search_kaggle(query: str, page_size: int = 12) -> list:
    url = f"{KAGGLE_BASE}/datasets/list?search={urllib.parse.quote(query)}&page_size={page_size}"
    return curl_json(url)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="knowledge/05-resources/kaggle-finance-catalog.md")
    args = parser.parse_args()

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    print("📊 Kaggle datasets:")
    seen = {}
    for q in QUERIES:
        print(f"  search '{q}' ...", end=" ", flush=True)
        results = search_kaggle(q, 12)
        print(f"got {len(results)}")
        for d in results:
            url = d.get("urlNullable") or d.get("url")
            if not url:
                continue
            slug = url.split("datasets/")[-1] if "datasets/" in url else url
            if slug in seen:
                continue
            seen[slug] = {
                "title": d.get("titleNullable", ""),
                "size": d.get("totalBytesNullable", 0),
                "url": f"https://www.kaggle.com/datasets/{slug}",
                "creator": d.get("creatorNameNullable", ""),
                "usability": d.get("usabilityRatingNullable", 0),
                "license": d.get("licenseNameNullable", ""),
                "version": d.get("currentVersionNumberNullable", 0),
                "votes": d.get("totalVotes", 0),
            }
        time.sleep(0.4)

    sorted_datasets = sorted(seen.values(), key=lambda x: x["size"], reverse=True)

    lines = [
        "# 📊 Kaggle Finance Catalog (Live API)",
        "",
        f"> **Live catalog from `kaggle.com/api/v1/datasets/list` on {today}.**",
        "> Sorted by size (descending). Bulk datasets first.",
        "",
        "---",
        "",
        f"**Total unique datasets found:** {len(sorted_datasets)}",
        "",
        "| Size | Usability | Title | Creator | URL |",
        "|---|---|---|---|---|",
    ]
    for d in sorted_datasets[:60]:
        size_mb = d["size"] / (1024 * 1024)
        size_str = f"{size_mb:.1f} MB" if size_mb < 1024 else f"{size_mb / 1024:.2f} GB"
        title = d["title"][:60] + ("…" if len(d["title"]) > 60 else "")
        usability = f"{d['usability']:.1f}" if d["usability"] else "—"
        lines.append(f"| {size_str:>10} | {usability} | {title} | {d['creator']} | [link]({d['url']}) |")

    lines.extend([
        "",
        "---",
        "",
        "## 🎯 Top picks (ranked for QuantResearcher)",
        "",
        "1. **Bulk US equities**: any >1GB all-tickers dataset",
        "2. **Crypto sentiment**: 16M Bitcoin tweets for NLP",
        "3. **Long-history benchmark**: S&P 500 daily 1986-2018",
        "4. **Sentiment + market aligned**: pre-joined sentiment data",
        "5. **Commodity futures**: NYMEX CL dataset",
        "",
        "---",
        "",
        "## 🔧 Authentication for private datasets",
        "",
        "```bash",
        "# .env",
        "KAGGLE_USERNAME=your_name",
        "KAGGLE_KEY=***",
        "```",
        "",
        "```python",
        "import kaggle",
        "kaggle.api.authenticate()",
        'kaggle.api.dataset_download_files("owner/dataset-slug", path="data/kaggle/", unzip=True)',
        "```",
        "",
        "---",
        "",
        f"**Refreshed:** {today} · **Queries:** {len(QUERIES)}",
        "**Re-fetch:** `python3 scripts/pull_kaggle.py`",
        "",
        "**Mode:** 🔄 CONTINUOUS RESEARCH (auto-refresh monthly)",
    ])

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines) + "\n")
    print(f"\n✅ Wrote {len(sorted_datasets)} datasets to {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
