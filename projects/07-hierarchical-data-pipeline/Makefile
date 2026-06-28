.PHONY: help install sync refresh align coverage test clean

PYTHON ?= python
PIP    ?= uv pip

help:
	@echo "Qualabinance — Project 07 (Hierarchical Data Pipeline)"
	@echo ""
	@echo "  make install   — install data-pipeline optional deps"
	@echo "  make sync      — uv sync"
	@echo "  make refresh   — pull all series (requires API keys in .env)"
	@echo "  make refresh-L1 — pull only L1 series"
	@echo "  make align     — build wide daily aligned panel"
	@echo "  make coverage  — print per-series coverage report"
	@echo "  make test      — run pytest"
	@echo "  make clean     — remove data/ and duckdb"

install:
	$(PIP) install -e ".[data-pipeline]"

sync:
	uv sync --all-extras

refresh:
	$(PYTHON) -m src.cli refresh

refresh-L1:
	$(PYTHON) -m src.cli refresh --level L1

refresh-L3-TH:
	$(PYTHON) -m src.cli refresh --series wb_th_gdp,wb_th_cpi,fred_thb_usd

align:
	$(PYTHON) -m src.cli align --start 2010-01-01 --output wide_daily

coverage:
	$(PYTHON) -m src.cli coverage

test:
	$(PYTHON) -m pytest tests/ -v

clean:
	rm -rf data/
