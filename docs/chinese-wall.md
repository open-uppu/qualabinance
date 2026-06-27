# 🔒 Chinese Wall — Isolation from Other Companies

> **Qualabinance is company #5. Strict isolation from Bank, Software House, DungWai, omyxia.**

---

## 🏢 Companies overview

| # | Company | Sector | Conflict Risk with Qualabinance |
|---|---|---|---|
| 1 | 🏦 **Bank** | Financial | 🔴 HIGH — same industry, regulatory overlap |
| 2 | 💻 **Software House** | SCADA / Industrial | 🟢 LOW — different sector |
| 3 | 📱 **DungWai** | SMM / Marketing | 🟢 LOW — different sector |
| 4 | 🆕 **omyxia** | Enterprise IT SaaS | 🟡 MEDIUM — both tech, but different domains |
| 5 | 🧪 **Qualabinance** | Quant Finance | (this company) |

---

## 🔒 Hard isolation rules

### Code & Data
- ❌ **No code sharing** between Qualabinance and Bank — even if mathematically similar (e.g., risk models)
- ❌ **No data sharing** — Qualabinance market data ≠ Bank customer data
- ❌ **No team overlap** — separate developers, separate code reviews
- ❌ **No secrets crossing** — bank API keys never enter Qualabinance env

### Compliance / Legal
- ❌ **Bank customer data** never touches Qualabinance systems (PNL, transactions, KYC)
- ❌ **Qualabinance strategies** never use bank customer data
- ✅ If overlap seems beneficial, escalate to CEO + legal review

### Technical
- ❌ Different CI/CD pipelines
- ❌ Different secrets vaults
- ❌ Different cloud accounts (recommended)
- ✅ Open-source / public data is fair game (FRED, public market data)

---

## 🎯 When escalation is required

Any of these triggers CEO + legal review:
- Considering sharing code with another company
- Considering hiring someone from another company
- Considering using proprietary data from another company
- Considering joint research / co-authorship
- Regulatory overlap concerns (e.g., bank compliance team asks for algo explanation)

---

## 📋 Operating norms

### Communication
- ✅ Public open-source contributions are fine
- ✅ Conference talks / papers are fine
- ❌ Internal company Slack ≠ shared with other companies
- ❌ "By the way, at the bank..." — never reference other company specifics

### Documentation
- ✅ Each company has its own `companies/<name>.md`
- ✅ Each agent only loads its own company context
- ❌ No cross-references in core docs (unless necessary, mark clearly)

### Tools
- ✅ Each company uses its own CLI tools (jito for open-uppu, etc.)
- ❌ Bank's `psql` not used in Qualabinance
- ❌ DungWai's `puppeteer` not used in Qualabinance

---

## 📊 Cross-company data flow matrix

| From → To | 🏦 Bank | 💻 SW House | 📱 DungWai | 🆕 omyxia | 🧪 Qualabinance |
|---|---|---|---|---|---|
| 🏦 Bank | — | ❌ | ❌ | ❌ | ❌ |
| 💻 SW House | ❌ | — | ❌ | ❌ | ❌ |
| 📱 DungWai | ❌ | ❌ | — | ❌ | ❌ |
| 🆕 omyxia | ❌ | ❌ | ❌ | — | ❌ |
| 🧪 Qualabinance | ❌ | ❌ | ❌ | ❌ | — |

**Rule**: All ❌ unless CEO + legal explicitly approves.

---

## ✅ What's allowed (no escalation needed)

- Using the same open-source libraries (pandas, numpy, etc.)
- Reading the same public papers (arXiv, etc.)
- Attending the same conferences
- General industry knowledge
- Personal social media (no company-specific info)

---

## 🚨 Violation response

1. **Suspected violation** → report to CEO immediately
2. **Confirmed violation** → stop, contain, audit, escalate
3. **Recurring** → formal review + potential disciplinary action

---

## 🔗 References

- [`risk-policy.md`](risk-policy.md) — operational risk rules
- [`compliance.md`](compliance.md) — regulatory rules
- [`../companies/qualabinance.md`](../companies/qualabinance.md) — company profile

---

*Chinese Wall Policy v1.0 · 2026-06-28 · Enforced by CEO-Profile loop*
