#!/usr/bin/env python3
"""
pull_github_trending.py — Pull trending quant/finance repos from GitHub API.

Strategy:
  1. Search by quant/finance keywords + recency filter
  2. Sort by stars (proxy for mass awareness) + by recency (proxy for dark horses)
  3. Cross-reference both views in output markdown

Usage:
    python3 scripts/pull_github_trending.py --out knowledge/05-resources/github-trending.md
    python3 scripts/pull_github_trending.py --since-days 60  # shorter window = darker
"""
import argparse
import json
import subprocess
import sys
import time
import urllib.parse
from datetime import datetime, timezone
from pathlib import Path

GITHUB_API = "https://api.github.com"

# (query, label) — query: search terms; label: how to describe it in output
QUERIES = [
    ("language:python finance trading", "Python · finance trading"),
    ("language:python quant backtest", "Python · quant backtest"),
    ("language:python stock prediction", "Python · stock prediction"),
    ("language:rust quant trading", "Rust · quant trading"),
    ("factor model alpha research", "Factor model alpha"),
    ("reinforcement learning trading", "RL trading"),
    ("cryptocurrency bitcoin trading bot", "Crypto trading bot"),
    ("polymarket prediction market", "Prediction market"),
    ("LLM financial agent", "LLM financial agent"),
    ("trading agents multi-agent", "Multi-agent trading"),
]


def curl_json(url: str, timeout: int = 20) -> dict:
    """Use curl (urllib hangs in this env)."""
    try:
        r = subprocess.run(
            ["curl", "-sL", "--max-time", str(timeout), "-A",
             "qualabinance/0.1 (mailto:research@qualabinance.local)",
             "-H", "Accept: application/vnd.github+json", url],
            capture_output=True, text=True, timeout=timeout + 5,
        )
        if r.returncode != 0 or not r.stdout.strip():
            return {}
        return json.loads(r.stdout)
    except Exception as e:
        print(f"  ⚠️  {url[:60]}... → {e}", file=sys.stderr)
        return {}


def fetch_repo_meta(full_name: str) -> dict:
    """Fetch detailed repo metadata."""
    return curl_json(f"{GITHUB_API}/repos/{full_name}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="knowledge/05-resources/github-trending.md")
    parser.add_argument("--since-days", type=int, default=180,
                        help="Look back N days for dark horses (default 180)")
    parser.add_argument("--per-query", type=int, default=15)
    args = parser.parse_args()

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    since_date = (
        datetime.now(timezone.utc)
        .replace(hour=0, minute=0, second=0, microsecond=0)
    )
    from datetime import timedelta
    since_date -= timedelta(days=args.since_days)
    since_str = since_date.strftime("%Y-%m-%d")

    print(f"🐙 GitHub trending (since {since_str}, {args.per_query} per query)")

    seen = {}
    for query, label in QUERIES:
        encoded = urllib.parse.quote(query)
        # Trending (most stars, recent)
        url = (
            f"{GITHUB_API}/search/repositories"
            f"?q={encoded}+created:>{since_str}&sort=stars&order=desc"
            f"&per_page={args.per_query}"
        )
        print(f"  🔥 trending: {label} ...", end=" ", flush=True)
        data = curl_json(url, timeout=20)
        results = data.get("items", []) if isinstance(data, dict) else []
        print(f"got {len(results)}")
        for r in results:
            full = r.get("full_name")
            if not full or full in seen:
                continue
            seen[full] = {
                "full_name": full,
                "stars": r.get("stargazers_count", 0),
                "forks": r.get("forks_count", 0),
                "desc": (r.get("description") or "")[:120],
                "lang": r.get("language", ""),
                "url": r.get("html_url", ""),
                "created": r.get("created_at", "")[:10],
                "pushed": r.get("pushed_at", "")[:10],
                "topics": r.get("topics", [])[:5],
                "query": label,
                "velocity": None,  # computed below
            }
        time.sleep(0.7)  # respect rate limits

        # Dark horse (newest, then by stars)
        url = (
            f"{GITHUB_API}/search/repositories"
            f"?q={encoded}+created:>{since_str}&sort=created&order=desc"
            f"&per_page={args.per_query}"
        )
        print(f"  🐴 new:      {label} ...", end=" ", flush=True)
        data = curl_json(url, timeout=20)
        results = data.get("items", []) if isinstance(data, dict) else []
        print(f"got {len(results)}")
        for r in results:
            full = r.get("full_name")
            if not full or full in seen:
                continue
            seen[full] = {
                "full_name": full,
                "stars": r.get("stargazers_count", 0),
                "forks": r.get("forks_count", 0),
                "desc": (r.get("description") or "")[:120],
                "lang": r.get("language", ""),
                "url": r.get("html_url", ""),
                "created": r.get("created_at", "")[:10],
                "pushed": r.get("pushed_at", "")[:10],
                "topics": r.get("topics", [])[:5],
                "query": label,
                "velocity": None,
            }
        time.sleep(0.7)

    # Compute velocity (stars / days_since_create) for dark horse detection
    today_dt = datetime.now(timezone.utc).replace(tzinfo=None)
    for r in seen.values():
        try:
            created = datetime.fromisoformat(r["created"])
            age_days = max(1, (today_dt - created).days)
            r["velocity"] = r["stars"] / age_days
        except Exception:
            r["velocity"] = 0

    # Split into trending (high stars) and dark horse (high velocity but low absolute stars)
    trending = sorted(
        [r for r in seen.values() if r["stars"] >= 50],
        key=lambda x: x["stars"], reverse=True,
    )
    dark_horses = sorted(
        [r for r in seen.values() if r["velocity"] >= 0.5 and r["stars"] < 500],
        key=lambda x: x["velocity"], reverse=True,
    )

    # Build markdown
    lines = [
        "# 🐙 GitHub Trending — Quant/Finance Repos",
        "",
        f"> **Live catalog from `api.github.com/search/repositories` on {today}.**",
        f"> Search window: since **{since_str}** ({args.since_days} days).",
        f"> Two views: **🔥 Trending** (high stars = mass attention) + **🐴 Dark horses** (high velocity = rising stars).",
        "",
        "---",
        "",
        "## 🔥 Trending (mass attention) — high stars, recent",
        "",
        "| ⭐ | Forks | Lang | Created | Last push | Repo | Topics |",
        "|---|---|---|---|---|---|---|",
    ]
    for r in trending[:50]:
        topics = ", ".join(f"`{t}`" for t in r["topics"][:3]) or "—"
        title_link = f"[{r['full_name']}]({r['url']})"
        lines.append(
            f"| {r['stars']:>5} | {r['forks']:>4} | {r['lang'][:10]:<10} "
            f"| {r['created']} | {r['pushed']} | {title_link} | {topics} |"
        )

    lines.extend([
        "",
        "## 🐴 Dark horses (rising stars) — high velocity, low absolute stars",
        "",
        "Velocity = stars / days_since_create. Watch these for breakout potential.",
        "",
        "| vel | ⭐ | Age | Lang | Created | Repo | Description |",
        "|---|---|---|---|---|---|---|",
    ])
    for r in dark_horses[:30]:
        try:
            created = datetime.fromisoformat(r["created"])
            age = (today_dt - created).days
            age_str = f"{age}d"
        except Exception:
            age_str = "?"
        desc = r["desc"].replace("|", "-")[:80]
        title_link = f"[{r['full_name']}]({r['url']})"
        lines.append(
            f"| {r['velocity']:>4.1f} | {r['stars']:>4} | {age_str:>5} "
            f"| {r['lang'][:10]:<10} | {r['created']} | {title_link} | {desc} |"
        )

    lines.extend([
        "",
        "---",
        "",
        "## 📊 Detection heuristics",
        "",
        "**Trending = stars ≥ 50** (proven attention)  ",
        "**Dark horse = velocity ≥ 0.5 stars/day AND stars < 500** (fast-rising under the radar)",
        "",
        "**Red flags (don't be fooled):**",
        "- 🚩 Repo with marketing hype but no code",
        "- 🚩 'Revolutionary AI' without reproducibility",
        "- 🚩 Claims of beating market with no live track record",
        "",
        "---",
        "",
        f"**Refreshed:** {today} · **Queries:** {len(QUERIES)} · **Repos found:** {len(seen)}",
        f"**Trending:** {len(trending)} · **Dark horses:** {len(dark_horses)}",
        "**Re-fetch:** `python3 scripts/pull_github_trending.py`",
        "",
        "**Mode:** 🔄 CONTINUOUS RESEARCH (auto-refresh weekly)",
    ])

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines) + "\n")
    print(f"\n✅ Wrote {len(trending)} trending + {len(dark_horses)} dark horses to {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())