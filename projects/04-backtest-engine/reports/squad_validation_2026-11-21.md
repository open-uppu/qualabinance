# Squad Validation (rigorous engine) — 2026-11-21

Engine: SL-before-TP | spread both sides | next-bar-open entry | live signal fn | no daily gates

| Asset | TF | Trades | Win% | Exp(R) | PF | Sharpe | DSR | Verdict |
|---|---|---|---|---|---|---|---|---|
| XAUUSD | M5 | 568 | 29.6 | -0.014 | 0.98 | -0.009 | 0.051 | FAIL (expectancy<=0) |
| BTCUSD | M5 | 865 | 29.0 | -0.126 | 0.83 | -0.085 | 0.000 | FAIL (expectancy<=0) |
| ETHUSD | M5 | 1056 | 31.2 | -0.240 | 0.70 | -0.174 | 0.000 | FAIL (expectancy<=0) |
| XAGUSD | M15 | 7 | 42.9 | 0.178 | 1.30 | 0.118 | 0.000 | SAMPLE_NOK (<20 trades) |
| XPTUSD | M15 | 5 | 60.0 | 0.474 | 2.08 | 0.325 | 0.730 | SAMPLE_NOK (<20 trades) |
| GBPUSD | M15 | 4 | 25.0 | -0.289 | 0.63 | -0.189 | 0.391 | SAMPLE_NOK (<20 trades) |
| EURUSD | M15 | 4 | 50.0 | 0.333 | 1.63 | 0.208 | 0.643 | SAMPLE_NOK (<20 trades) |
| UKOIL | M15 | 36 | 36.1 | 0.570 | 1.87 | 0.252 | 0.753 | WEAK (expectancy>0 but DSR<0.90) |
| XNGUSD | M15 | 26 | 30.8 | -0.169 | 0.77 | -0.124 | 0.021 | FAIL (expectancy<=0) |
