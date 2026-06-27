# 📚 Daily Research Update

> **Refresh the knowledge layer with new papers, repos, books daily.**

## 🎯 Purpose

Keep `knowledge/05-resources/` up to date with:
- New Q1 papers (arxiv, top journals)
- New GitHub repos with companion papers
- New canonical books (rare)
- Data provider methodology updates

## ⏰ Trigger

Daily at 06:00 GMT+7 (before market open Asia)

## 📋 Steps

1. **Search arXiv** for new quant papers
   - Categories: q-fin.ST, q-fin.TR, q-fin.PR, q-fin.GN, q-fin.MF, q-fin.RM
   - Filter by date (last 24h)
2. **Search Papers with Code** for finance updates
3. **Search GitHub trending** for finance repos
4. **Verify candidates** — Q1 venue, citations > 5, code available
5. **Add to appropriate research file**
6. **Update counts** in `knowledge/README.md`
7. **Commit to git** with message "research: daily update YYYY-MM-DD"

## 📥 Inputs

- arXiv API (free): http://export.arxiv.org/api/
- GitHub API (rate-limited): https://api.github.com/
- Papers with Code RSS: https://paperswithcode.com/

## 📤 Outputs

- Updated `knowledge/05-resources/papers/*.md`
- Updated `knowledge/05-resources/github-projects/*.md`
- Git commit

## ⚠️ Failure handling

- arXiv API down → retry next day, manual run
- GitHub rate limit → use API token, throttle
- Repo no longer exists → mark as archived

---

*Workflow v0.1.0 · 2026-06-28*
