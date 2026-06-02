# Section 3 — Troubleshooting & CAPA in biologics environment

## 3.1 Specifics of failures in biologics

Failure modes in biologics environment present specificities that complicate troubleshooting compared to a small molecule environment:

```
Small molecule (Celgene)          Biologics (Lonza Visp)
─────────────────────────────     ──────────────────────────────
Deterministic chemical process    Variable biological process
Measurable chemical contamination Biological contamination (mycoplasmas, bioburden)
Validated chemical cleaning       Critical CIP/SIP — biological integrity
Classical instruments             Online sensors (pH, DO, conductivity, pressure)
Chemical containment              Biological containment + HPAPI
```

## 3.2 RCA tools adapted to biologics context

### Bioreactor / Small Equipment FMEA

FMEA in biologics context integrates specific failure modes:

| Component | Failure mode | Potential effect | RPN guide |
|-----------|--------------|------------------|-----------|
| Peristaltic joint | Wear → leak | Batch contamination | High |
| pH probe | Calibration drift | CPP out of limit | High |
| Ventilation filter | Clogging | Differential pressure out of spec | Medium |
| Sterile valve | Faulty actuation | Cross contamination | High |
| Autoclave | Incomplete cycle | Non-sterility | Critical |

### Integrated RCA-CAPA cycle in GMP biologics

```
Quality signal / equipment failure
              ↓
    Formal deviation (GMP record)
              ↓
    RCA investigation (5M / FMEA / 5 Whys)
              ↓
    Root cause identified (systemic, not superficial)
              ↓
    CAPA plan: immediate correction + preventive action
              ↓
    Implementation + documentation
              ↓
    Effectiveness check (verification of effectiveness)
              ↓
    CAPA closure → CMMS + SOP update if applicable
              ↓
    OEE / KPI feed → continuous improvement loop
```

*Figure 3.1 — Integrated RCA-CAPA-continuous improvement cycle in GMP biologics environment*

## 3.3 Troubleshooting in commercial production vs. development

In commercial ramp-up phase (Visp 2026 context), additional pressure is exerted on troubleshooting: every batch counts, every stop has a direct contractual cost. The approach must combine:

- **Reactivity**: quickly identify and contain impact
- **GMP rigor**: document each step despite time pressure
- **Investigation depth**: go to systemic root cause to avoid recurrence

## 3.4 RCA-CAPA skills for the I&U Engineer Visp role

Literature analysis converges on three maturity requirements:

**Investigation depth** — go beyond proximal cause to identify systemic factors (design, PM interval, actual vs. specification usage conditions), based on the combination of 5M + FMEA + historical CMMS data.

**Documentary rigor** — each investigation produces a formal trace compliant with GMP requirements, with concrete recommendations, assigned, with deadline and measurable effectiveness criteria.

**Continuous improvement orientation** — CAPA is not a one-time response to an isolated incident. It feeds a cycle of improvement for maintenance strategies (PM intervals, criticality, procedures), SOPs, and site OEE/KPI indicators.

Experience in writing and following up CAPAs, deviations and SOPs acquired in GMP API environment under dual FDA/SwissMedic surveillance constitutes a direct anchor in this framework.

---

*→ Section 4: GMP Utilities biologics — CIP/SIP, WFI, clean steam*

---

### References (excerpts)

- Seely, R.J. et al. (2021). *Failure analysis biopharmaceutical manufacturing*
- ICH Q9. *Quality Risk Management — FMEA application*
- FDA. *Guidance on deviation and CAPA in biologics manufacturing*