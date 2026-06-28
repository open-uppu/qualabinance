# 🔄 Continuous Research — Auto-Refresh System

> **Library mode = CONTINUOUS RESEARCH (active).**
> Knowledge is pulled continuously from live APIs and committed regularly.

---

## 🎯 How it works

```
┌─────────────────────────────────────────────────────────────────────┐
│  1. CRON (or manual) calls maintenance-loop.sh                      │
│     └─ bash knowledge/maintenance-loop.sh {weekly|monthly|all}      │
│                                                                       │
│  2. Loop runs 4 Python pull scripts (in scripts/)                    │
│     ├─ pull_arxiv.py        → 219 papers last 30 days                 │
│     ├─ pull_huggingface.py  → 68 models + 79 datasets                  │
│     ├─ pull_kaggle.py       → 269 datasets                             │
│     └─ pull_openalex.py     → 96 papers cross-disciplinary            │
│                                                                       │
│  3. Each script overwrites its target markdown file                  │
│     └─ knowledge/05-resources/{arxiv-frontier-live, huggingface-finance-│
│        catalog, kaggle-finance-catalog, openalex-cross-disciplinary}.md │
│                                                                       │
│  4. Operator (or cron) commits the changes                            │
│     └─ git add knowledge/ && git commit -m '🔄 refresh: ...'           │
│                                                                       │
│  5. Library stats grow monotonically                                   │
│     └─ LIBRARY.md / 00-INDEX.md auto-stats                            │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 🕒 Refresh cadence

| Source | Cadence | Why |
|---|---|---|
| **arXiv q-fin** | weekly | New frontier papers every few days |
| **HuggingFace** | bi-weekly | Model downloads shift slowly |
| **Kaggle** | monthly | Dataset catalog relatively stable |
| **OpenAlex** | monthly | Citation counts mature slowly |
| **GitHub repos** | quarterly | Star counts shift slowly |
| **Books** | annually | Canonical texts rarely change |

---

## 🤖 Cron config (drop in your crontab)

```bash
# Refresh Qualabinance knowledge library every week (Sunday 02:00)
0 2 * * 0 cd /path/to/qualabinance && /path/to/qualabinance/.venv/bin/python scripts/pull_arxiv.py >> /var/log/qualabinance-refresh.log 2>&1

# Bi-weekly HuggingFace (1st & 15th, 02:30)
30 2 1,15 * * cd /path/to/qualabinance && /path/to/qualabinance/.venv/bin/python scripts/pull_huggingface.py >> /var/log/qualabinance-refresh.log 2>&1

# Monthly Kaggle + OpenAlex (1st of month, 03:00)
0 3 1 * * cd /path/to/qualabinance && /path/to/qualabinance/.venv/bin/python scripts/pull_kaggle.py >> /var/log/qualabinance-refresh.log 2>&1
0 4 1 * * cd /path/to/qualabinance && /path/to/qualabinance/.venv/bin/python scripts/pull_openalex.py >> /var/log/qualabinance-refresh.log 2>&1
```

For OpenClaw integration, use the `cron` tool:
```bash
# Weekly arxiv
cron.add({
  "name": "qualabinance-arxiv-refresh",
  "schedule": {"kind": "cron", "expr": "0 2 * * 0", "tz": "Asia/Bangkok"},
  "payload": {
    "kind": "agentTurn",
    "message": "cd /home/up-ubuntu/wokrspace/open-uppu/qualabinance && .venv/bin/python scripts/pull_arxiv.py && git add knowledge/ && git commit -m '🔄 arxiv refresh: $(date +%Y-%m-%d)' && git push",
    "timeoutSeconds": 180
  }
})
```

---

## 🛠️ Manual invocation

```bash
# Just arXiv (fastest, ~30s)
bash knowledge/maintenance-loop.sh arxiv

# Weekly: arXiv + HF (~3 min)
bash knowledge/maintenance-loop.sh weekly

# Monthly: all 4 sources (~10 min)
bash knowledge/maintenance-loop.sh monthly

# Or all (same as monthly)
bash knowledge/maintenance-loop.sh all

# Or just one script
.venv/bin/python scripts/pull_kaggle.py
```

---

## 📊 What each script does

### `pull_arxiv.py`
- **Queries:** `cat:q-fin.ST`, `cat:q-fin.TR`, `cat:q-fin.GN`, `cat:q-fin.PR`, `cat:q-fin.RM`
- **Output:** `knowledge/05-resources/arxiv-frontier-live.md`
- **Last run:** 219 unique papers (deduped across categories)
- **API:** `export.arxiv.org/api/query` (free, no key)
- **Rate limit:** soft (HTTP 429 after burst)

### `pull_huggingface.py`
- **Queries:** finance, trading, stock, crypto, quant, finbert, finma (models) + 8 dataset queries
- **Output:** `knowledge/05-resources/huggingface-finance-catalog.md`
- **Last run:** 68 models + 79 datasets (deduped)
- **API:** `huggingface.co/api/{models,datasets}?search=...`
- **Rate limit:** generous (anonymous OK)
- **Sort:** by downloads (what people actually use)

### `pull_kaggle.py`
- **Queries:** 14 finance keywords (stock, bitcoin, sentiment, futures, options, forex, bond, …)
- **Output:** `knowledge/05-resources/kaggle-finance-catalog.md`
- **Last run:** 269 datasets (deduped)
- **API:** `kaggle.com/api/v1/datasets/list?search=...` (anonymous OK)
- **Rate limit:** soft, page_size capped at 12
- **Sort:** by size (bulk datasets first)

### `pull_openalex.py`
- **Queries:** 10 high-value cross-disciplinary queries
- **Output:** `knowledge/05-resources/openalex-cross-disciplinary.md`
- **Last run:** 96 papers (deduped, since 2023)
- **API:** `api.openalex.org/works?search=...&filter=from_publication_date:2023-01-01`
- **Rate limit:** generous (but include `mailto:` UA per their ToS)
- **Sort:** by citations (most cited first)

---

## 🧪 Tested & working

All 4 scripts verified to run end-to-end:
- ✅ arXiv: 219 papers pulled, sorted by date
- ✅ HuggingFace: 68 models + 79 datasets, sorted by downloads
- ✅ Kaggle: 269 datasets, sorted by size
- ✅ OpenAlex: 96 papers, sorted by citations (bug-fixed: `w.get("primary_location") or {}` chain)

---

## 🚧 Future expansion (when needed)

Add new pull scripts following the same pattern:

```python
# scripts/pull_xxx.py
- Use curl via subprocess (avoid Python urllib hangs in this env)
- Sleep 0.4-0.5s between requests
- Dedupe by unique ID
- Sort by a meaningful key (downloads, citations, size, date)
- Output markdown table to knowledge/05-resources/
```

**Candidate additions:**
- `pull_github_trending.py` — top quant repos by star velocity
- `pull_ssrn.py` — finance working papers (need custom search)
- `pull_bls_bds.py` — business dynamics stats (US macro)
- `pull_bis_quarterly.py` — BIS Quarterly Review latest issue
- `pull_aqr_ideas.py` — AQR Insights new articles (RSS feed)
- `pull_econ_papers.py` — NBER working papers

---

## 🎯 When in library mode, behavior

**Default behavior (no user prompt):**
- ✅ Library files are referenced for any question
- ✅ LIBRARY.md / TOPIC-INDEX.md / QUICK-REFERENCE.md used as entry points
- ✅ When user asks something in library → answer from existing content
- ✅ When user asks something not in library → flag gap + propose research plan
- ❌ No unsolicited research pulls (would burn through rate limits)

**Triggered research (user asks):**
- ✅ "research [topic]" → pull new content into library
- ✅ "what's new in [topic]" → run targeted pull
- ✅ "find papers on [x]" → run pull with custom query
- ✅ "refresh library" → run maintenance loop

---

**Built:** 2026-06-28 · **Mode:** 🔄 CONTINUOUS RESEARCH · **Status:** Auto-refresh infra live · **Custodian:** Qualabinance / QuantResearcher
