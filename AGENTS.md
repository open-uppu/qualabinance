# Qualabinance — Team Guidance & Agent Invariants

Guidance for all AI agents working on the **Qualabinance** multi-asset quantitative finance platform.

---

## 1. Project Identity & Repository Scope

- **Repository:** `git@github.com:open-uppu/qualabinance.git`
- **Cluster:** `open-uppu` (Public / Software House products)
- **Local Path:** `/Users/up-mac/wokrspace/open-uppu/qualabinance`
- **Isolation Invariant:** Strictly isolated to `open-uppu`. Never push to or interact with other clusters (`mind/`, `gym`, etc.).

---

## 2. Qualabinance Team Roster

| Agent Name | Role | Responsibilities |
|---|---|---|
| **Qualabinance Manager 👔** | Quant Product & Research Manager | Sprint planning, Roadmap, Release governance |
| **Qualabinance 📊** | Quant Finance Lead | Financial modeling, strategy evaluation, portfolio logic |
| **Qualabinance Backend ⚙️** | Quantitative Engine Lead | Core pipeline, data ingest, execution engines |
| **Qualabinance Frontend / UXUI 🎨** | Visualizations Engineer | Analytics dashboard, chart visualizers |
| **Qualabinance QA Test 🧪** | Model Validation & Risk QA | Test suites, mathematical correctness, data integrity |
| **Qualabinance HR 👥** | Research Knowledge Ops | Documentation, reference catalogs, papers & datasets |

---

## 3. Mandatory Release & Git Rules (AGENTS.md Rule 3.6)

1. **Version Bump Before Push:**
   - Every release push to `origin/main` must carry an updated version number in `pyproject.toml` (`[project].version` and `[tool.qualabinance].version`).
   - SemVer rules:
     - **Patch (`x.y.Z`):** Bug fixes, test maintenance, governance compliance.
     - **Minor (`x.Y.0`):** New quant models, indicators, data connectors, features.
     - **Major (`X.0.0`):** Breaking pipeline/engine changes, schema overhauls.
2. **Atomic Release Commit:**
   - Version bump must be included in the same commit as the changes.
   - Commit message must follow Conventional Commits (e.g., `chore(release): bump version to 0.1.1`).
   - Must include the Co-authored trailer:
     `Co-authored-by: OpenBot <335604065+openbotgit[bot]@users.noreply.github.com>`
3. **Verification Before Push:**
   - All tests must pass 100% (`.venv/bin/pytest projects/07-hierarchical-data-pipeline/tests/ -v`).
