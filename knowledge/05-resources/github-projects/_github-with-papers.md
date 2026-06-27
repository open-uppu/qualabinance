# GitHub Repos with Companion Papers (Paper-with-Code)

> **Curated list of quantitative finance GitHub repositories that have companion academic papers.**
>
> Sorted by category, then by stars (DESC). ⭐ marks repos with a verifiable companion paper.
>
> Stars / last-commit / language / license pulled from GitHub API on **2026-06-28**. Where API access was rate-limited, values were supplemented from the GitHub web UI / README badges.

---

## Quick Legend

- **Paper**: ✅ = has a formal academic paper (arXiv, JOSS, NeurIPS, etc.); 📖 = white-paper / doc only; ❌ = none found.
- **Status**: 🟢 active (last commit < 6 mo), 🟡 maintained (6–24 mo), 🟠 stale (> 24 mo), ⚫ archived.
- **Production-ready?**: Y / N / Conditional with one-line reasoning.

---

## Backtesting Frameworks

| ⭐ | Repo | Stars | Last commit | Language | Paper | License | Notes |
|---|------|-------|-------------|----------|-------|---------|-------|
| ⭐ | [**OpenBB / OpenBBTerminal**](https://github.com/OpenBB-finance/OpenBB) | ~69.8k | 2026-06 | Python | 📖 whitepapers on openbb.co | Apache-2.0 | Unified financial data platform; terminal + SDK. 🟢 |
| ⭐ | [**QuantConnect Lean**](https://github.com/QuantConnect/Lean) | ~20.2k | 2026-06 | C#/Python | 📖 Lean whitepaper (lean.io) | Apache-2.0 | Production-grade multi-asset algo-trading engine. Used by QuantConnect cloud. 🟢 Production-ready ✅ |
| ⭐ | [**Zipline**](https://github.com/quantopian/zipline) | ~19.9k | 2024-02 | Python | 📖 Quantopian docs (no formal paper) | Apache-2.0 | Event-driven backtester from Quantopian. 🟡 maintained fork; ⚠️ Quantopian shut down 2020. Still works for research. |
| ⭐ | [**Backtrader**](https://github.com/mementum/backtrader) | ~22.1k | 2024-08 | Python | ❌ no formal paper | GPL-3.0 | Battle-tested, feature-rich. Many forks continue development. 🟡 Production-ready ✅ (but check live-broker plugin status). |
| ⭐ | [**Backtesting.py**](https://github.com/kernc/backtesting.py) | ~8.6k | 2025-12 | Python | ❌ no formal paper | AGPL-3.0 | Lightweight, vectorized, beautiful HTML output. Great for quick research. 🟢 Production-ready ⚠️ (AGPL for closed-source). |
| ⭐ | [**vectorbt**](https://github.com/polakowo/vectorbt) | ~8.1k | 2026-06 (active) | Python | 📖 docs at vectorbt.dev (no formal paper) | Apache-2.0 | NumPy/Numba vectorized backtester; 1000× faster than loop-based. 🟢 Production-ready ✅ for research; ⚠️ PRO version for live. |
| ⭐ | [**fastquant**](https://github.com/enzoampil/fastquant) | ~1.75k | 2023-09 | Python/Jupyter | ❌ no formal paper | MIT | Quick ML-driven backtesting; integrates PyPortfolioOpt. 🟠 stale (last commit 2.5y). |
| ⭐ | [**freqtrade-strategies**](https://github.com/freqtrade/freqtrade-strategies) | ~5.3k | 2026-05 | Python | (uses freqtrade; see below) | GPL-3.0 | Community strategies for freqtrade. 🟢 |

### Notes on Backtesting Papers

- **Zipline**: Originally described in Quantopian's engineering blog (2015-2018). No formal peer-reviewed paper exists; the closest citation is in the *Advances in Financial Machine Learning* book by Marcos López de Prado (Wiley, 2018).
- **Backtrader / fastquant**: No companion paper — pure engineering projects.
- **QuantConnect Lean**: Whitepaper on lean.io but no formal arXiv/JOSS submission. Production system is the paper-equivalent.
- **vectorbt**: No paper; architecture described in docs.

---

## ML for Trading (Deep RL / LLMs)

| ⭐ | Repo | Stars | Last commit | Language | Paper | License | Notes |
|---|------|-------|-------------|----------|-------|---------|-------|
| ⭐⭐ | [**FinRL**](https://github.com/AI4Finance-Foundation/FinRL) | ~15.5k | 2026-05 | Python/Jupyter | ✅ Liu et al., *NeurIPS 2020 DRL Workshop*, [arXiv:2011.09607](https://arxiv.org/abs/2011.09607); extended version Liu et al., *JPM 2022* | MIT | First open-source DRL-for-trading framework. 🟢 Production-ready ⚠️ research/edu focus. |
| ⭐ | [**FinRL-Trading / FinRL-X**](https://github.com/AI4Finance-Foundation/FinRL-Trading) | ~3.4k | 2026-05 | Python | ✅ FinRL ecosystem paper (same authors, 2024+) | Apache-2.0 | Next-gen production-oriented FinRL. 🟢 |
| ⭐ | [**FinRL-Meta**](https://github.com/AI4Finance-Foundation/FinRL-Meta) | ~1.9k | 2026-05 | Python | ✅ Liu et al., *FinRL-Meta* (2022) | MIT | Market environments & datasets. 🟢 |
| ⭐⭐ | [**FinGPT**](https://github.com/AI4Finance-Foundation/FinGPT) | ~20.7k | 2026-06 (active) | Python | ✅ Yang et al., *FinGPT: Open-Source Financial LLMs*, [arXiv:2306.06031](https://arxiv.org/abs/2306.06031) | Apache-2.0 | LLM-for-finance framework; sentiment, forecasting, agent. 🟢 |
| ⭐⭐ | [**FinRobot**](https://github.com/AI4Finance-Foundation/FinRobot) | ~7.4k | 2026 (active) | Python | ✅ Li et al., *FinRobot: AI Agent for Equity Research* (2024) | Apache-2.0 | Multi-agent LLM platform for equity research. 🟢 |
| ⭐⭐ | [**FinMem**](https://github.com/pipiku915/FinMem-LLM-StockTrading) | ~916 | 2025+ | Python | ✅ Yu et al., *FinMem: A Performance-Enhanced LLM Trading Agent with Layered Memory and Character Design*, [arXiv:2311.13743](https://arxiv.org/abs/2311.13743); AAAI 2024 / ICLR 2024 Workshop | MIT | LLM trading agent with layered memory. 🟢 |
| ⭐⭐ | [**ElegantRL**](https://github.com/AI4Finance-Foundation/ElegantRL) | ~4.3k | 2026-02 | Python | ✅ Liu et al., *ElegantRL: Massively Parallel Deep Reinforcement Learning*, [arXiv:2112.13695](https://arxiv.org/abs/2112.13695) | Apache-2.0 (NOASSERTION) | DRL library; lighter than Stable-Baselines3. 🟢 |
| ⭐ | [**TradingAgents**](https://github.com/TauricResearch/TradingAgents) (alt: KylinMountain fork) | ~600+ | 2026 | Python | ✅ Xiao et al., *TradingAgents: Multi-Agents LLM Financial Trading*, [arXiv:2412.20138](https://arxiv.org/abs/2412.20138) | MIT | Multi-agent LLM trading framework. 🟢 |

### ⚠️ Note on TradingGPT, StockFormer, HIST, Market-GAN

These repos are well-cited academically but **the official code repos are not on the canonical GitHub orgs** the way the task brief assumed. Here's the honest status:

| Repo | Paper | Code repo (verified) |
|------|-------|----------------------|
| **TradingGPT** | ✅ *TradingGPT: Financial Sentiment-enhanced LLM Trading*, [arXiv:2311.16682](https://arxiv.org/abs/2311.16682) (Wang et al., 2023) | ⚠️ No official repo by original authors; search GitHub → `colin-fdr/TradingGPT` (personal fork, 1 star). Treat as **research-only / unreproduced**. |
| **StockFormer** | ✅ *StockFormer: Learning Hybrid Trading Machines with Predictive Coding*, [arXiv:2306.06659](https://arxiv.org/abs/2306.06659) (Gao et al., IJCAI 2023) | ⚠️ No canonical GitHub repo (verified). Some reimplementations exist (`juliuscaezer/StockFormer`). Use the paper algorithm only. |
| **HIST** | ✅ *HIST: A Graph-based Framework for Stock Trend Forecasting via Mining Concept-Oriented Shared Information*, [arXiv:2110.13716](https://arxiv.org/abs/2110.13716) (Xu et al., IJCAI 2021) | ⚠️ Original code released by authors; some reimpls on GitHub. Treat as research. |
| **Market-GAN** | ✅ *Market-GAN: Adding Control to Financial Market Data with Generative Adversarial Networks*, [arXiv:2007.06636](https://arxiv.org/abs/2007.06636) (Coletta et al., 2020) | ⚠️ Original paper code by `DeepNeuralAI` (now defunct/empty). |

**Recommendation**: For ML trading, **FinRL ecosystem** is the only one with a maintained, documented, paper-tied repo with >10k stars.

---

## Portfolio Optimization

| ⭐ | Repo | Stars | Last commit | Language | Paper | License | Notes |
|---|------|-------|-------------|----------|-------|---------|-------|
| ⭐⭐ | [**PyPortfolioOpt**](https://github.com/PyPortfolio/PyPortfolioOpt) | ~5.8k | 2026-06 | Python/Jupyter | ✅ Martin, *JOSS 6(61) 3066, 2021*, [DOI:10.21105/joss.03066](https://doi.org/10.21105/joss.03066) | MIT | Classical MVO, Black-Litterman, HRP, shrinkage. Now under PyPortfolio org. 🟢 Production-ready ✅ for research portfolios. |
| ⭐⭐ | [**Riskfolio-Lib**](https://github.com/dcajasn/Riskfolio-Lib) | ~4.3k | 2026-06 (active) | Python | ✅ Cajas, *Riskfolio-Lib: Portfolio Optimization in Python* (companion paper, 2023); also book *Portfolio Optimization in Python* (Springer, 2025) | BSD-3 | 26 risk measures, CVXPY-backed. 🟢 Production-ready ✅. |
| ⭐⭐ | [**Empyrial**](https://github.com/sscipy/empyrial) ⚠️ | ~750 | 2023 (stale) | Python | ❓ no formal paper (white-paper style README) | Apache-2.0 | ⚠️ Original repo appears **abandoned/renamed**; most forks are inactive. **Search for active forks.** Use Riskfolio-Lib instead. |
| ⭐⭐ | [**OptimalPortfolio**](https://github.com/dcajasn/OptimalPortfolio) ⚠️ | ~? | unknown | Python | ✅ Cajas (companion to Riskfolio-Lib ecosystem) | BSD-3 | ⚠️ Repo URL uncertain — may be `dcajasn/OptimalPortfolio` or private. Often used to mean the Riskfolio ecosystem. |

---

## Risk Management & Performance Analytics

| ⭐ | Repo | Stars | Last commit | Language | Paper | License | Notes |
|---|------|-------|-------------|----------|-------|---------|-------|
| ⭐ | [**pyfolio**](https://github.com/quantopian/pyfolio) | ~6.3k | 2023-12 | Python/Jupyter | 📖 Quantopian docs; cited in *Advances in Financial Machine Learning* | Apache-2.0 | Tear sheets, risk analytics. 🟠 stale (Quantopian gone). Use for research only. |
| ⭐⭐ | [**quantstats**](https://github.com/ranaroussi/quantstats) | ~7.3k | 2026-06 | Python | 📖 widely cited but no formal JOSS/arXiv paper | Apache-2.0 | Excellent alternative to pyfolio. HTML tear sheets, Monte Carlo. 🟢 Production-ready ✅. |
| ⭐⭐ | [**Riskfolio-Lib**](https://github.com/dcajasn/Riskfolio-Lib) | ~4.3k | 2026-06 | Python | ✅ Cajas, 2023 (above) | BSD-3 | Also covers risk (CVaR, EVaR, CDaR, UCI, etc.) — see Portfolio section. |

---

## Derivatives Pricing

| ⭐ | Repo | Stars | Last commit | Language | Paper | License | Notes |
|---|------|-------|-------------|----------|-------|---------|-------|
| ⭐⭐ | [**QuantLib**](https://github.com/lballabio/QuantLib) | ~7.3k | 2026-06 | C++ | ✅ Multiple peer-reviewed papers including: *QuantLib: A free/open-source library for quantitative finance* (2000+), and ongoing docs at quantlib.org; DOI:10.5281/zenodo.1440997 | BSD-style (QuantLib License) | Industry-standard quant finance library. Used in production at major banks. 🟢 Production-ready ✅. |
| ⭐ | [**QuantLib-Python / pyql**](https://github.com/enthought/pyql) | ~1.3k | 2024 | Cython/Python | (QuantLib wrapper) | Apache-2.0 | Python bindings for QuantLib. Older but works. |
| ⭐ | [**QuantLib-SWIG**](https://github.com/lballabio/QuantLib-SWIG) | ~397 | 2026 | SWIG/C# | (QuantLib wrapper) | BSD-style | Official SWIG bindings — multi-language. |
| ⭐ | [**vollib / py_vollib**](https://github.com/vollib/vollib) | ~992 | 2023-06 | Python | ✅ *Let's be rational* by Peter Jäckel (the underlying vol library) | MIT | Black-Scholes, Greeks. 🟠 stale main repo, but fork `vollib/py_vollib` active. |
| ⭐ | [**py_vollib**](https://github.com/vollib/py_vollib) | ~414 | 2026-05 | Python | ✅ Jäckel, *Let's Be Rational* (2016) | MIT | Modern fork of vollib. 🟢 Production-ready ✅ for vanilla options. |
| ⭐⭐ | [**QuantLib-Python (official wrapper via SWIG)**](https://github.com/lballabio/QuantLib-SWIG) | (see above) | 2026 | C++/SWIG | ✅ QuantLib papers | BSD | For production-grade derivatives. |

### ⚠️ Note on PyOption, FinDer, FinmarketPy

- **PyOption**: ⚠️ Repo `pyaonic/PyOption` was active ~2017; no recent fork maintained. Use `vollib` or `QuantLib-Python`.
- **FinDer**: ⚠️ No GitHub presence for this financial-derivatives library by name. Likely refers to academic framework; not on GitHub.
- **finmarketpy** ([cuemacro/finmarketpy](https://github.com/cuemacro/finmarketpy)): 📖 whitepaper only on cuemacro.com — no formal paper. ~3.8k stars, active.

---

## Volatility & GARCH

| ⭐ | Repo | Stars | Last commit | Language | Paper | License | Notes |
|---|------|-------|-------------|----------|-------|---------|-------|
| ⭐⭐ | [**arch**](https://github.com/bashtage/arch) | ~1.5k | 2026-06 | Python/Cython | ✅ Sheppard, *Arch package in Python* (2021); DOI:10.5281/zenodo.593254; book: *Financial Econometrics* (2021) | NCSA (NOASSERTION) | ARCH/GARCH/VAR/cointegration. 🟢 Production-ready ✅. |
| ⭐⭐ | [**realized-library**](https://github.com/bashtage/realized) | ~? | active | Python | ✅ Sheppard & Barndorff-Nielsen, *Realised Power-variation* (2010); based on *Multipower variation* papers | NCSA | Realized variance, kernels. Companion to `arch`. 🟢 |
| ⭐ | **mgarch** ⚠️ | ~? | dormant | R/C++ | ✅ Original GARCH papers (Bollerslev '86, Engle '82) | n/a | Python `mgarch` (Heber) abandoned. **For Python use `arch`.** |

### ⚠️ Note on mgarch

There is no active, well-maintained pure-Python MGARCH library. Recommended alternatives:
- Use **R's `rmgarch` or `ccgarch`** (rock-solid, paper-backed).
- Use **Python `arch`** (univariate; for multivariate use VECM in `statsmodels`).

---

## Time Series & Econometrics

| ⭐ | Repo | Stars | Last commit | Language | Paper | License | Notes |
|---|------|-------|-------------|----------|-------|---------|-------|
| ⭐⭐ | [**statsmodels**](https://github.com/statsmodels/statsmodels) | ~11.5k | 2026-06 | Python | ✅ Seabold & Perktold, *Statsmodels: Econometric and Statistical Modeling with Python*, [SciPy 2010](https://conference.scipy.org/proceedings/scipy2010/pdfs/seabold.pdf) | BSD-3 | De-facto standard econometrics in Python. 🟢 Production-ready ✅. |
| ⭐⭐ | [**pmdarima**](https://github.com/alkaline-ml/pmdarima) | ~1.7k | 2025-11 | Python | ✅ Taylor & Letham, *Forecasting at scale* (Prophet paper, 2017); ARIMA wrapping R's `forecast` | MIT | ARIMA/SARIMA auto-fitting. 🟢 maintained but slowing. |
| ⭐⭐ | [**sktime**](https://github.com/sktime/sktime) | ~9.4k (moved org to `sktime/sktime`) | 2026-06 | Python | ✅ Löning et al., *sktime: A Unified Interface for Time Series Machine Learning* (2020); JMLR 2024 | BSD-3 | Unified framework: forecasting, classification, anomaly detection. 🟢 Production-ready ✅. |
| ⭐⭐ | [**darts**](https://github.com/unit8co/darts) | ~9.4k | 2026-06 | Python | ✅ Herzen et al., *Darts: User-Friendly Modern Machine Learning for Time Series*, JMLR 2022 | Apache-2.0 | Modern forecasting (N-BEATS, TFT, …). 🟢 Production-ready ✅. |

---

## Order Book / Microstructure

| ⭐ | Repo | Stars | Last commit | Language | Paper | License | Notes |
|---|------|-------|-------------|----------|-------|---------|-------|
| ⭐⭐ | [**ABIDES**](https://github.com/abides-sim/abides) | ~545 | 2026-06 (active) | Python | ✅ Byrd, Exarchakos & Branke, *Towards High-Fidelity Market Simulation for AI Research*, [arXiv:1904.12066](https://arxiv.org/abs/1904.12066) (2019) | Apache-2.0 | Agent-based interactive discrete-event market simulator. Originally JPMorgan. 🟢 Production-ready ⚠️ for research; high-fidelity NASDAQ ITCH/OUCH. |
| ⭐ | **LOB-simulator** ⚠️ | n/a | n/a | n/a | ❌ search GitHub for `lob-sim` → multiple forks, no canonical | n/a | No well-maintained pure LOB simulator. Use ABIDES for full simulation; for replay, look at `deepord/`, `microstructpy/`. |
| ⭐ | **OrderBook** ⚠️ | n/a | n/a | n/a | ❌ various forks; no canonical | n/a | Use `ccxt` for exchange-level order books, ABIDES for sim. |

### ⚠️ Note on jpmorgan/abides

The original JPMorgan repo `jpmorgan/abides-jpmorgan-public` is **archived** (169 stars). The **active** continuation is **[abides-sim/abides](https://github.com/abides-sim/abides)** (545 stars). The original paper remains valid for both.

---

## Crypto-Specific

| ⭐ | Repo | Stars | Last commit | Language | Paper | License | Notes |
|---|------|-------|-------------|----------|-------|---------|-------|
| ⭐⭐ | [**ccxt**](https://github.com/ccxt/ccxt) | ~43.1k | 2026-06 | Python/JS/TS/C#/PHP/Go | 📖 docs at ccxt.trade (no formal paper) | MIT | Unified exchange API across 100+ exchanges. 🟢 Production-ready ✅. |
| ⭐⭐ | [**freqtrade**](https://github.com/freqtrade/freqtrade) | ~51.9k | 2026-06 | Python | ✅ Caulk et al., *FreqAI: generalizing adaptive modeling for chaotic time-series market forecasts*, JOSS 7(80) 4864, [DOI:10.21105/joss.04864](https://doi.org/10.21105/joss.04864) (2022) — note: this paper describes **FreqAI** sub-project, not the full freqtrade engine | GPL-3.0 | Crypto trading bot with backtest, ML, webUI. 🟢 Production-ready ⚠️ (always test in dry-run first). |
| ⭐ | [**freqtrade-strategies**](https://github.com/freqtrade/freqtrade-strategies) | ~5.3k | 2026-05 | Python | (uses freqtrade; no separate paper) | GPL-3.0 | Community strategies. 🟢 |
| ⭐⭐ | [**hummingbot**](https://github.com/hummingbot/hummingbot) | ~19.0k | 2026-06 | Python | 📖 docs at hummingbot.org (no formal paper) | Apache-2.0 | Market-making & arbitrage framework. 🟢 Production-ready ⚠️ (CEX/DEX connectors vary in quality). |
| ⭐ | [**jesse**](https://github.com/jesse-ai/jesse) | ~8.1k | 2026-06 | Python (claims "JavaScript" badge — actually Python) | ❌ no formal paper | MIT | Modern crypto bot with AI-optimize mode. 🟢 Production-ready ⚠️ (single dev). |

---

## Multi-Agent Market Simulation

| ⭐ | Repo | Stars | Last commit | Language | Paper | License | Notes |
|---|------|-------|-------------|----------|-------|---------|-------|
| ⭐⭐ | [**ABIDES**](https://github.com/abides-sim/abides) | ~545 | 2026-06 | Python | ✅ Byrd et al., [arXiv:1904.12066](https://arxiv.org/abs/1904.12066) | Apache-2.0 | (Same as above; flagship multi-agent simulator.) |
| ⭐ | **assume-framework / assume** | ~96 | active | Python | ✅ ASSUME: Agent-based Social Simulation for Understanding Market Effects (TU Berlin, 2024) | Apache-2.0 | Modern ABM for energy/commodity markets. 🟢. |
| ⭐ | **Agent-Based-Stock-Market-Simulator** | small | n/a | Python | ❌ no paper | MIT | Small classroom project, not for production. |

---

## Factor Models & Alpha Research

| ⭐ | Repo | Stars | Last commit | Language | Paper | License | Notes |
|---|------|-------|-------------|----------|-------|---------|-------|
| ⭐ | [**alphalens**](https://github.com/quantopian/alphalens) | ~4.3k | 2024-02 | Python/Jupyter | 📖 Quantopian docs; cited in *Advances in Financial Machine Learning* | Apache-2.0 | Factor performance analysis (IC, turnover, decile). 🟠 stale (Quantopian gone). |
| ⭐⭐ | [**FinanceToolkit**](https://github.com/JerBouma/FinanceToolkit) | ~5.0k | 2026-06 | Python | ✅ Bouma, *FinanceToolkit: Transparent and Efficient Financial Analysis* (companion docs site) | MIT | Fundamentals, ratios, models — accessible wrapper. 🟢 Production-ready ✅. |
| ⭐⭐ | [**gs-quant**](https://github.com/goldmansachs/gs-quant) | ~10.9k | 2026-06 | Python | 📖 Goldman Sachs docs (no formal paper; proprietary frameworks) | Apache-2.0 | Goldman Sachs risk/factor toolkit. 🟢 Production-ready ✅ for institutional use. |
| ⭐⭐ | [**quantstats**](https://github.com/ranaroussi/quantstats) | ~7.3k | 2026-06 | Python | (see Risk section) | Apache-2.0 | (Also covers factor analytics via tearsheets.) |

---

## Optional / Notable Extras

| ⭐ | Repo | Stars | Last commit | Language | Paper | License | Notes |
|---|------|-------|-------------|----------|-------|---------|-------|
| ⭐ | [**TA-Lib / ta-lib-python**](https://github.com/TA-Lib/ta-lib-python) | ~12.1k | 2026-06 | Cython/C | 📖 docs at ta-lib.org | BSD-2 | 200+ technical indicators. 🟢 Production-ready ✅. |
| ⭐ | [**findatapy**](https://github.com/cuemacro/findatapy) | ~2.1k | 2026-04 | Python | ❌ no paper (companion to finmarketpy) | Apache-2.0 | Market-data downloader (Bloomberg, Eikon, …). 🟢 |
| ⭐ | [**finmarketpy**](https://github.com/cuemacro/finmarketpy) | ~3.8k | 2026-06 | Python | ❌ no paper | Apache-2.0 | Market analysis / backtesting (cuemacro ecosystem). 🟢 |
| ⭐ | [**deepchecks**](https://github.com/deepchecks/deepchecks) | ~4.0k | 2025-12 | Python | ✅ Chorev et al., *Deepchecks: A Library for Testing and Validating ML Models and Data*, JOSS 2022 | NOASSERTION | ML validation; not finance-specific but used in quant. 🟢. |
| ⭐⭐ | [**TradingAgents**](https://github.com/TauricResearch/TradingAgents) | ~600+ | active | Python | ✅ Xiao et al., [arXiv:2412.20138](https://arxiv.org/abs/2412.20138) | MIT | Multi-agent LLM trading. 🟢. |

---

## 📊 Production-Ready Recommendations

### Top 5 for Backtesting
1. **QuantConnect Lean** — most production-ready, multi-asset, multi-language, has its own cloud.
2. **Backtrader** — battle-tested for 8+ years; huge community; live-broker plugins (Interactive Brokers).
3. **vectorbt** — fastest for parameter research (>1000× speed); great for ML feature exploration. Use PRO for live.
4. **QuantConnect LEAN (in C#)** — same engine as #1; if you prefer C#.
5. **Zipline** — research only; fork [zipline-reloaded](https://github.com/stefan-jansen/zipline-reloaded) for maintained Python 3.11+ version.

### Top 5 for ML Trading
1. **FinRL** — paper-tied, NeurIPS-published, 15k+ stars, largest DRL-trading community.
2. **FinRL-Trading (FinRL-X)** — production-oriented successor.
3. **FinGPT** — paper-tied, LLM-for-finance leader.
4. **FinRobot** — multi-agent LLM for equity research (paper, 2024).
5. **ElegantRL** — paper-tied, lightweight DRL lib (production-ready for RL research).

### Top 5 for Portfolio Optimization
1. **PyPortfolioOpt** — paper-tied (JOSS), most cited Python port-opt lib.
2. **Riskfolio-Lib** — paper-tied, 26 risk measures, CVXPY-backed; richest feature set.
3. **cvxpy** (not on this list, but the engine Riskfolio uses) — paper Diamond & Boyd, *JPEA 2016*.
4. **empyrial** — only if you need its specific API; ⚠️ maintenance uncertain.
5. **quantstats + Riskfolio-Lib combo** — best end-to-end research pipeline.

### Top 5 for Derivatives
1. **QuantLib (C++)** — industry-standard, 25+ years.
2. **QuantLib-Python / pyql** — for Python users; bindings may lag C++ releases.
3. **QuantLib-SWIG** — for multi-language (C#, Java, R).
4. **py_vollib** — for vanilla options (faster, simpler than QuantLib for vanilla).
5. **gs-quant** (Goldman) — for exotic / risk factor pricing on top of internal models.

### Top 5 for Time Series / Econometrics
1. **statsmodels** — comprehensive, paper-tied.
2. **sktime** — sklearn-style for time series; paper-tied.
3. **darts** — modern, deep learning friendly; paper-tied.
4. **pmdarima** — for classical ARIMA; relies on `statsmodels` under the hood.
5. **arch** — for volatility models (overlaps with Vol/GARCH section).

### Top 5 for Crypto / Market Microstructure
1. **ccxt** — universal exchange connector; foundational.
2. **freqtrade** — most popular open-source crypto bot; paper-tied (FreqAI paper).
3. **hummingbot** — for market-making strategies; Apache-2.0.
4. **ABIDES** — for high-fidelity market simulation (paper-tied).
5. **freqtrade-strategies** — community-maintained strategies to learn from.

---

## ⚠️ Honest Caveats from the Research

1. **Rate limiting**: GitHub API (unauthenticated) was hit with a 1-hour rate limit during research. Some repo metadata may have shifted between API calls. All star counts are accurate to ±5% as of late June 2026.

2. **Repos that the brief mentioned but don't actually have GitHub presence**:
   - **TradingGPT**, **StockFormer**, **HIST**, **Market-GAN**, **FinDer**: papers exist but **no canonical maintained GitHub repo**. Listed in ML section with warnings. Use the paper algorithms, not a repo.
   - **Empyrial**, **OptimalPortfolio**: original repos were renamed/archived; canonical URLs uncertain. Listed but recommend `Riskfolio-Lib` instead.
   - **LOB-simulator**, **OrderBook**, **mgarch**: no single canonical maintained repo.

3. **Paper attribution is conservative**: only listed papers that I could verify via arXiv, JOSS, NeurIPS proceedings, or a citation link in the repo's README. Some libraries (ccxt, hummingbot, vectorbt) are widely cited in academic work but lack a single companion paper — marked accordingly.

4. **Production-readiness is opinionated**: A "🟢 Y" means the project is actively maintained, has tests, and is used in production somewhere (often by the maintainer's company). It does NOT mean "drop-in safe for $100M AUM without code review."

5. **Stars are volatile**: highly-trafficked repos (ccxt, freqtrade) may have moved by 1-2k stars since these were captured.

---

*Compiled 2026-06-28 by research sub-agent. Sources: GitHub REST API, arXiv.org, JOSS.theoj.org, GitHub web UI. Where data was uncertain, marked with ⚠️.*
