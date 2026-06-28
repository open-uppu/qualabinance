#!/usr/bin/env bash
# maintenance-loop.sh — Continuous research loop for Qualabinance knowledge library.
#
# Runs in CONTINUOUS RESEARCH mode (active librarian):
#   1. Pull newest arXiv q-fin papers (weekly)
#   2. Pull top HuggingFace finance models/datasets (bi-weekly)
#   3. Pull top Kaggle finance datasets (monthly)
#   4. Pull OpenAlex cross-disciplinary papers (monthly)
#   5. Update live catalog files
#
# Usage:
#   ./maintenance-loop.sh weekly    # arXiv + HF
#   ./maintenance-loop.sh monthly   # + Kaggle + OpenAlex
#   ./maintenance-loop.sh all       # all sources
#   ./maintenance-loop.sh arxiv     # arXiv only (fastest)

set -euo pipefail

cd "$(dirname "$0")/.."
KNOWLEDGE_DIR="knowledge/05-resources"

mode="${1:-weekly}"

echo "🔄 Qualabinance knowledge maintenance loop"
echo "   mode: $mode"
echo "   date: $(date -u +'%Y-%m-%d %H:%M:%S UTC')"
echo

case "$mode" in
    arxiv|weekly|monthly|all)
        echo "📜 Pulling arXiv frontier (last 30 days)..."
        python3 scripts/pull_arxiv.py --out "$KNOWLEDGE_DIR/arxiv-frontier-live.md"
        echo
        ;;
esac

case "$mode" in
    weekly|monthly|all)
        echo "🤗 Pulling HuggingFace finance catalog..."
        python3 scripts/pull_huggingface.py --out "$KNOWLEDGE_DIR/huggingface-finance-catalog.md"
        echo
        ;;
esac

case "$mode" in
    monthly|all)
        echo "📊 Pulling Kaggle finance catalog..."
        python3 scripts/pull_kaggle.py --out "$KNOWLEDGE_DIR/kaggle-finance-catalog.md"
        echo
        echo "📚 Pulling OpenAlex cross-disciplinary papers..."
        python3 scripts/pull_openalex.py --out "$KNOWLEDGE_DIR/openalex-cross-disciplinary.md"
        echo
        ;;
esac

echo "✅ Done"
echo "Next: review changes, commit with:"
echo "  git add knowledge/"
echo "  git commit -m '🔄 refresh: arxiv + hf + kaggle + openalex (\$(date +%Y-%m-%d))'"
