#!/usr/bin/env python3
"""
pull_more_sources.py — Pull from sources beyond arXiv/HF/Kaggle/OpenAlex/GitHub:
  1. StackExchange Quantitative Finance top voted questions
  2. Hacker News classic quant discussions
  3. dev.to tagged finance
  4. arXiv broad categories (econ.EM, stat.ML, q-fin.CP, physics.soc-ph)

Usage:
    python3 scripts/pull_more_sources.py --out knowledge/05-resources/more-live-sources.md
"""
import argparse
import json
import subprocess
import sys
import time
import urllib.parse
from datetime import datetime, timezone
from pathlib import Path

# ============================
# 1. StackExchange Quantitative Finance
# ============================
def fetch_se_questions(site: str, sort: str = "votes", pagesize: int = 20, tag: str = "") -> list:
    tag_filter = f"&tagged={tag}" if tag else ""
    url = (
        f"https://api.stackexchange.com/2.3/questions?order=desc&sort={sort}"
        f"&site={site}&pagesize={pagesize}&filter=default{tag_filter}"
    )
    try:
        r = subprocess.run(
            ["curl", "-sL", "--max-time", "20", "-A", "qualabinance/0.1", url],
            capture_output=True, text=True, timeout=25,
        )
        if r.returncode != 0 or not r.stdout.strip():
            return []
        return json.loads(r.stdout).get("items", [])
    except Exception as e:
        print(f"  ⚠️  SE:{site}:{tag} → {e}", file=sys.stderr)
        return []


# ============================
# 2. Hacker News via Algolia
# ============================
def fetch_hn(query: str, hits: int = 15) -> list:
    url = f"https://hn.algolia.com/api/v1/search?query={urllib.parse.quote(query)}&hitsPerPage={hits}"
    try:
        r = subprocess.run(
            ["curl", "-sL", "--max-time", "20", "-A", "Mozilla/5.0", url],
            capture_output=True, text=True, timeout=25,
        )
        if r.returncode != 0 or not r.stdout.strip():
            return []
        return json.loads(r.stdout).get("hits", [])
    except Exception as e:
        print(f"  ⚠️  HN:{query} → {e}", file=sys.stderr)
        return []


# ============================
# 3. dev.to
# ============================
def fetch_devto(tag: str, top: int = 7) -> list:
    url = f"https://dev.to/api/articles?tag={tag}&top={top}"
    try:
        r = subprocess.run(
            ["curl", "-sL", "--max-time", "20", "-A", "qualabinance/0.1", url],
            capture_output=True, text=True, timeout=25,
        )
        if r.returncode != 0 or not r.stdout.strip():
            return []
        return json.loads(r.stdout)
    except Exception as e:
        print(f"  ⚠️  dev.to:{tag} → {e}", file=sys.stderr)
        return []


# ============================
# 4. arXiv broad categories
# ============================
ARXIV_BROAD = ["econ.EM", "stat.ML", "stat.AP", "q-fin.CP", "physics.soc-ph"]


def fetch_arxiv_broad(cat: str, max_results: int = 8) -> list:
    """Returns list of (title, arxiv_id, date) tuples."""
    url = f"https://export.arxiv.org/api/query?search_query=cat:{cat}&max_results={max_results}&sortBy=submittedDate&sortOrder=descending"
    try:
        r = subprocess.run(
            ["curl", "-sL", "--max-time", "15", "-A", "Mozilla/5.0", url],
            capture_output=True, text=True, timeout=20,
        )
        if r.returncode != 0 or not r.stdout.strip():
            return []
        import xml.etree.ElementTree as ET
        NS = {"a": "http://www.w3.org/2005/Atom"}
        root = ET.fromstring(r.stdout)
        results = []
        for entry in root.findall("a:entry", NS):
            title_el = entry.find("a:title", NS)
            id_el = entry.find("a:id", NS)
            pub_el = entry.find("a:published", NS)
            if title_el is None or id_el is None:
                continue
            title = title_el.text.strip().replace("\n", " ")
            arxiv_id = id_el.text.split("/")[-1]
            date = pub_el.text[:10] if pub_el is not None else ""
            results.append({"title": title, "id": arxiv_id, "date": date})
        return results
    except Exception as e:
        print(f"  ⚠️  arXiv:{cat} → {e}", file=sys.stderr)
        return []


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="knowledge/05-resources/more-live-sources.md")
    args = parser.parse_args()

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    # 1. StackExchange Quantitative Finance — top voted all-time
    print("📚 StackExchange Quantitative Finance...")
    se_quant = fetch_se_questions("quant", sort="votes", pagesize=20)

    # StackExchange CrossValidated (stats)
    print("📊 StackExchange CrossValidated (stats, time-series tag)...")
    se_stats = fetch_se_questions("stats", sort="votes", pagesize=10, tag="time-series")

    time.sleep(0.5)

    # 2. HN — classic quant threads (high-signal terms)
    print("🟠 Hacker News classics...")
    hn_all = []
    for q in ["trading strategy", "quantitative finance", "algorithmic trading",
              "factor model investing", "portfolio optimization"]:
        hn_all.extend(fetch_hn(q, 8))
        time.sleep(0.5)
    # Dedupe by objectID
    hn_seen = set()
    hn_unique = []
    for h in hn_all:
        oid = h.get("objectID")
        if oid and oid not in hn_seen:
            hn_seen.add(oid)
            hn_unique.append(h)
    hn_unique.sort(key=lambda x: x.get("points") or 0, reverse=True)

    time.sleep(0.5)

    # 3. dev.to finance tagged
    print("🟣 dev.to finance...")
    devto = fetch_devto("finance", top=10)

    time.sleep(0.5)

    # 4. arXiv broad categories
    print("📜 arXiv broad categories...")
    arxiv_broad = {}
    for cat in ARXIV_BROAD:
        arxiv_broad[cat] = fetch_arxiv_broad(cat, 8)
        time.sleep(0.7)

    # Build markdown
    lines = [
        "# 🌐 More Live Sources — Beyond arXiv/HF/Kaggle/OpenAlex/GitHub",
        "",
        f"> **Live pull from multiple APIs on {today}.**",
        "> Different vantage points: discussion (HN/SE), cross-disciplinary (econ.EM/stat.ML/q-fin.CP), blog (dev.to).",
        "",
        "---",
        "",
        "## 🟢 StackExchange Quantitative Finance — Top Voted",
        "",
        f"**Questions found:** {len(se_quant)}",
        "",
        "| ↑ | 💬 | 👁 | Tags | Title |",
        "|---|---|---|---|---|",
    ]
    for q in se_quant[:15]:
        tags = ",".join(q.get("tags", [])[:4])
        title = q.get("title", "")[:80].replace("|", "-")
        link = q.get("link", "")
        lines.append(
            f"| {q.get('score', 0):>4} | {q.get('answer_count', 0):>3} "
            f"| {q.get('view_count', 0):>6} | [{tags}] | [{title}]({link}) |"
        )

    if se_stats:
        lines.extend([
            "",
            "## 🟢 StackExchange CrossValidated — stats/time-series tag",
            "",
            "| ↑ | 💬 | 👁 | Title |",
            "|---|---|---|---|",
        ])
        for q in se_stats[:8]:
            title = q.get("title", "")[:80].replace("|", "-")
            link = q.get("link", "")
            lines.append(
                f"| {q.get('score', 0):>4} | {q.get('answer_count', 0):>3} "
                f"| {q.get('view_count', 0):>6} | [{title}]({link}) |"
            )

    lines.extend([
        "",
        "---",
        "",
        "## 🟠 Hacker News — Quant Classics",
        "",
        f"**Stories found (deduped):** {len(hn_unique)}",
        "",
        "| ↑ | 💬 | Date | Title |",
        "|---|---|---|---|",
    ])
    for h in hn_unique[:25]:
        title = (h.get("title") or h.get("story_title", ""))[:80]
        if not title:
            continue
        date = h.get("created_at", "")[:10]
        url = h.get("url") or f"https://news.ycombinator.com/item?id={h.get('objectID')}"
        lines.append(
            f"| {h.get('points', 0):>4} | {h.get('num_comments', 0):>3} "
            f"| {date} | [{title}]({url}) |"
        )

    lines.extend([
        "",
        "---",
        "",
        "## 🟣 dev.to — Tagged `finance`",
        "",
        f"**Articles found:** {len(devto)}",
        "",
        "| ❤️ | 💬 | Author | Title |",
        "|---|---|---|---|",
    ])
    for a in devto[:10]:
        title = a.get("title", "")[:80]
        user = a.get("user", {}).get("username", "?")
        url = a.get("url", "")
        reactions = a.get("public_reactions_count", 0)
        comments = a.get("comments_count", 0) or a.get("comments", 0)
        lines.append(f"| {reactions:>3} | {comments:>3} | @{user} | [{title}]({url}) |")

    lines.extend([
        "",
        "---",
        "",
        "## 📜 arXiv Broad Categories (last 7 days)",
        "",
    ])
    for cat, papers in arxiv_broad.items():
        if not papers:
            continue
        lines.append(f"### `{cat}` — {len(papers)} papers")
        lines.append("")
        for p in papers[:8]:
            lines.append(f"- [{p['title'][:100]}](https://arxiv.org/abs/{p['id']}) (`{p['id']}`, {p['date']})")
        lines.append("")

    lines.extend([
        "---",
        "",
        f"**Refreshed:** {today}",
        f"**SE Quant:** {len(se_quant)} · **SE Stats:** {len(se_stats)} · "
        f"**HN:** {len(hn_unique)} · **dev.to:** {len(devto)} · "
        f"**arXiv broad:** {sum(len(v) for v in arxiv_broad.values())}",
        "",
        "**Re-fetch:** `python3 scripts/pull_more_sources.py`",
        "",
        "**Mode:** 🔄 CONTINUOUS RESEARCH (auto-refresh monthly)",
    ])

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines) + "\n")
    print(f"\n✅ Wrote {len(lines)} lines to {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())