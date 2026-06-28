#!/usr/bin/env python3
"""
pull_openalex.py — Pull cross-disciplinary quant finance papers from OpenAlex.

Usage:
    python3 scripts/pull_openalex.py --out knowledge/05-resources/openalex-cross-disciplinary.md
"""
import argparse
import json
import subprocess
import sys
import time
import urllib.parse
from pathlib import Path
from datetime import datetime, timezone

OPENALEX_BASE = "https://api.openalex.org"
QUERIES = [
    "foundation model finance",
    "time series foundation model",
    "reinforcement learning trading",
    "large language model asset pricing",
    "spurious predictability backtest",
    "Polymarket prediction market microstructure",
    "cross-chain spillover crypto",
    "optimal execution deep reinforcement learning",
    "GARCH volatility forecasting neural",
    "FinGPT FinBERT financial sentiment",
]


def curl_json(url: str, timeout: int = 25) -> dict:
    try:
        r = subprocess.run(
            ["curl", "-sL", "--max-time", str(timeout), "-A",
             "qualabinance/0.1 (mailto:research@qualabinance.local)", url],
            capture_output=True, text=True, timeout=timeout + 5,
        )
        if r.returncode != 0 or not r.stdout.strip():
            return {}
        return json.loads(r.stdout)
    except Exception as e:
        return {}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="knowledge/05-resources/openalex-cross-disciplinary.md")
    parser.add_argument("--per-query", type=int, default=10)
    args = parser.parse_args()

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    print("📚 OpenAlex cross-disciplinary papers:")
    seen = {}
    for q in QUERIES:
        print(f"  search '{q}' ...", end=" ", flush=True)
        url = (
            f"{OPENALEX_BASE}/works?search={urllib.parse.quote(q)}"
            f"&per-page={args.per_query}&sort=relevance_score:desc"
            "&filter=from_publication_date:2023-01-01,type:article|preprint"
        )
        try:
            data = curl_json(url)
            if not isinstance(data, dict):
                print(f'BAD RESPONSE: {data!r}'[:80])
                continue
            results = data.get("results", [])
            if not isinstance(results, list):
                print(f'BAD results type: {type(results)}')
                continue
            print(f"got {len(results)}")
            for w in results:
                if not w or not isinstance(w, dict):
                    continue
                wid_raw = w.get("id")
                if not wid_raw:
                    continue
                wid = wid_raw.split("/")[-1]
                if not wid or wid in seen:
                    continue
                authors = []
                for a in (w.get("authorships") or [])[:3]:
                    if isinstance(a, dict) and a.get("author"):
                        authors.append(a["author"].get("display_name", "?"))
                seen[wid] = {
                    "id": wid,
                    "title": w.get("title", "") or w.get("display_name", ""),
                    "year": w.get("publication_year"),
                    "date": w.get("publication_date", "")[:10],
                    "cited_by": w.get("cited_by_count", 0),
                    "type": w.get("type", ""),
                    "doi": w.get("doi", ""),
                    "venue": ((w.get("primary_location") or {}).get("source") or {}).get("display_name", "") or (w.get("host_venue") or {}).get("display_name", ""),
                    "authors": authors,
                    "open_access": w.get("open_access", {}).get("is_oa", False),
                    "url": w.get("doi") or f"https://openalex.org/{wid}",
                    "query": q,
                }
        except Exception as e:
            print(f"FAILED: {e}")
        time.sleep(0.5)

    sorted_papers = sorted(seen.values(), key=lambda x: x["cited_by"], reverse=True)

    lines = [
        "# 📚 OpenAlex Cross-Disciplinary Quant Finance (Live API)",
        "",
        f"> **Live catalog from `api.openalex.org/works` on {today}.**",
        "> Cross-disciplinary search across econ + finance + CS + stats.",
        "> Sorted by citation count (most cited first).",
        "",
        "**Why OpenAlex (vs arXiv)?**",
        "- ✅ Cross-disciplinary coverage (econ, finance, stats, CS)",
        "- ✅ Citation count + author metrics",
        "- ✅ Journal + conference + repository unified",
        "- ✅ Open Access flag (free PDFs)",
        "- ✅ Concept/topic tagging",
        "- ⚠️ Rate-limited but generous",
        "",
        "---",
        "",
        f"**Total unique papers found:** {len(sorted_papers)}",
        "",
        "| Citations | Year | OA | Title | Authors | Venue |",
        "|---|---|---|---|---|---|",
    ]
    for p in sorted_papers[:120]:
        title = (p["title"] or "")[:80].replace("|", "-")
        if len(p["title"] or "") > 80:
            title += "…"
        authors = ", ".join(p["authors"])
        if len(authors) > 40:
            authors = authors[:37] + "…"
        venue = p["venue"][:30] if p["venue"] else "—"
        oa = "🟢" if p["open_access"] else "⚪"
        link = f"[{p['id']}]({p['url']})"
        lines.append(f"| {p['cited_by']:>5} | {p['year']} | {oa} | {title} ({link}) | {authors} | {venue} |")

    lines.extend([
        "",
        "---",
        "",
        "## 🔍 Search queries used",
        "",
    ])
    for q in QUERIES:
        lines.append(f"- `{q}`")

    lines.extend([
        "",
        "---",
        "",
        f"**Refreshed:** {today} · **Queries:** {len(QUERIES)} · **Filter:** from 2023-01-01",
        "**Re-fetch:** `python3 scripts/pull_openalex.py`",
        "",
        "**Mode:** 🔄 CONTINUOUS RESEARCH (auto-refresh monthly)",
    ])

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines) + "\n")
    print(f"\n✅ Wrote {len(sorted_papers)} papers to {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
