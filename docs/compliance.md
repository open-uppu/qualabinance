# ⚖️ Compliance — Multi-Jurisdiction Considerations

> **Trading across borders = regulatory complexity. Read carefully.**

---

## 🌍 Jurisdictions covered

Qualabinance operates across multiple regulatory regimes:

| Region | Asset Class | Key Regulators | Notes |
|---|---|---|---|
| 🇹🇭 **Thailand** | Thai equities, futures | SEC Thailand, BoT, AMLO | Strict FX controls |
| 🇺🇸 **USA** | US equities, options, futures | SEC, CFTC, FINRA, IRS | Pattern Day Trader rule, wash sale |
| 🇪🇺 **EU** | EU equities, bonds | ESMA, MiFID II, local regulators | GDPR on data |
| 🇬🇧 **UK** | UK equities | FCA | Post-Brexit separate |
| 🇭🇰 **HK** | HK equities | SFC | — |
| 🇯🇵 **JP** | JP equities | FSA | — |
| 🌍 **Crypto** | Crypto (most jurisdictions) | Mostly unregulated or evolving | High risk of sudden rule changes |

---

## 🚨 Key compliance issues

### 🇹🇭 Thailand-specific
- **FX controls** — can't freely move THB > $50k/day without BoT approval
- **Crypto** — SEC Thailand regulates; only licensed exchanges (Binance Thailand, Bitkub) for retail
- **Tax** — capital gains from securities = 15% withholding at source (for listed stocks); crypto unclear
- **AMLO** — Anti-Money Laundering Act applies; report large transactions

### 🇺🇸 USA-specific
- **Pattern Day Trader (PDT)** — 4+ day trades in 5 days = $25k minimum account
- **Wash sale rule** — can't claim loss if you buy back within 30 days
- **Section 1256** — favorable tax treatment for futures (60/40 long/short term)
- **Mark-to-market** — required for certain trader statuses
- **IRS Form 8949** — every trade reported

### 🌍 Crypto (universal)
- **Mostly unregulated** — but changing fast (MiCA in EU, etc.)
- **Tax treatment varies wildly** — property vs commodity vs currency
- **Exchange licensing** — Binance banned in UK, US, Thailand (use licensed alternatives)
- **Stablecoin reserves** — counterparty risk (USDC, USDT)
- **DeFi** — even less clear; potential securities law issues

---

## ✅ Compliance checklist

### Before going live
- [ ] Identify jurisdictions of operation
- [ ] Identify asset classes traded
- [ ] Check local licensing requirements
- [ ] Check tax obligations (record-keeping)
- [ ] Verify broker/exchange licenses in your jurisdiction
- [ ] Set up proper accounting (every trade, every cost)
- [ ] Consider engaging local tax advisor + lawyer
- [ ] Document compliance posture

### Ongoing
- [ ] Quarterly review of regulatory changes
- [ ] Annual tax filing
- [ ] Maintain audit trail (10 years for tax)
- [ ] Monitor broker regulatory status
- [ ] Update risk policy if rules change

---

## 🛡️ Platform-level compliance

### What Qualabinance does
- ✅ Logs every order (timestamp, instrument, qty, price)
- ✅ Logs every state change
- ✅ Logs every API call (for audit)
- ✅ Immutable audit log (10-year retention)
- ✅ Multi-account support (different entities)
- ✅ Reports exportable (CSV, JSON, PDF)
- ✅ Tax lot tracking (FIFO, LIFO, HIFO, specific identification)

### What Qualabinance does NOT do
- ❌ Tax filing (use accountant)
- ❌ Legal advice (consult lawyer)
- ❌ Custody (use qualified custodians)
- ❌ AML/KYC reporting (broker's responsibility)

---

## 📋 Asset-specific notes

### Equities
- Listed = regulated, but reporting varies
- OTC/pink sheets = high risk, often fraud

### Futures
- CFTC-regulated (US) or equivalent
- Highly leveraged = high risk
- Rollover can trigger tax events

### Options
- Complex tax (Section 1256 in US)
- Assignment risk (short options)
- Greeks change rapidly

### Crypto
- **Binance** — banned in UK, US (use Binance.US), Thailand (use licensed local)
- **Coinbase** — US-regulated, publicly listed
- **Kraken** — US-regulated
- **DEX** — no KYC, but regulatory risk high
- **Stablecoins** — USDC is safest (Circle, US-regulated)

### FX
- Highly leveraged, OANDA regulated in multiple jurisdictions
- BIS Triennial Survey data for academic use

---

## 📚 Resources

- 🇹🇭 SEC Thailand: https://www.sec.or.th/
- 🇺🇸 SEC: https://www.sec.gov/
- 🇺🇸 CFTC: https://www.cftc.gov/
- 🇪🇺 ESMA: https://www.esma.europa.eu/
- 🌍 IOSCO: https://www.iosco.org/
- IRS Publication 550 (investment income): https://www.irs.gov/publications/p550

---

## ⚠️ Disclaimer

**This document is informational only and does NOT constitute legal or tax advice.** Always consult qualified professionals in your jurisdiction before trading. Trading involves substantial risk of loss.

---

*Compliance v0.1.0 · 2026-06-28 · Not legal advice*
