# Section 1 — Equipment Management & Reliability: Strategic Foundations for a CDMO Biologics Environment

## 1.1 Context: Equipment Reliability as a CDMO Operational Imperative

In a Contract Development and Manufacturing Organization (CDMO), equipment availability is not just one operational metric among others—it is a contractual condition. Every batch produced commits the site's reputation with respect to pharmaceutical clients who, in turn, have market authorization obligations to regulators and patients.

This reality is particularly acute in a commercial ramp-up context, where newly qualified lines transition from validation mode to full-scale production mode, with zero tolerance for unanticipated availability deviations.

## 1.2 Specifics of Small Equipment in Biologics

"Small equipment" in a CDMO biologics context covers a wide range of assets: peristaltic pumps, integrity filters, transfer connections, analytical balances, in-line control equipment (pH, DO, conductivity), sampling systems, small-capacity autoclaves.

These equipment types share several characteristics that condition the maintenance strategy:

```
High frequency of use             → Accelerated wear, high criticality
Direct product contact           → Immediate impact on batch quality
Frequent replacement             → Intensive spare parts management
Multiplication of references     → Stock management complexity
```

## 1.3 Criticality Classification — Adaptation to Biologics Context

The standard criticality matrix (Severity × Occurrence × Detectability = RPN) must be enhanced for the biologics context with specific parameters:

| Criterion | Description | Weighting |
|-----------|-------------|-----------|
| Product quality impact | Direct product contact? CPP involved? | High |
| Contamination impact | Biological risk if failure? | High |
| Redundancy availability | Backup equipment available? | Medium |
| Maintainability | Estimated MTTR if breakdown? | Medium |
| Supply lead time | Critical spare parts lead time? | Medium |

## 1.4 Differentiated Strategy: PM / CBM / Residual Corrective

```
┌─────────────────────────────────────────────────────────────┐
│  1. CRITICALITY CLASSIFICATION                              │
│     SIA / CCA / Enhanced RPN (maintainability complexity)   │
│     → differentiated strategy by asset                      │
├─────────────────────────────────────────────────────────────┤
│  2. OEE-CENTERED TPM/RCM FRAMEWORK                          │
│     Attack on the 6 big losses, autonomous TPM,             │
│     CBM integration on high criticality assets              │
├─────────────────────────────────────────────────────────────┤
│  3. DATA INFRASTRUCTURE AND CMMS                            │
│     Existing sensors + CMMS/MES as CBM foundation,          │
│     conditional monitoring before advanced ML/PdM           │
├─────────────────────────────────────────────────────────────┤
│  4. PRODUCTION PLANNING INTEGRATION                         │
│     Opportunistic PM, low-impact windows,                   │
│     synchronization with CDMO multi-product scheduling      │
└─────────────────────────────────────────────────────────────┘
```

## 1.5 Connection with Celgene Experience

The experience of managing maintenance by criticality with Oracle + periodic shutdown at Celgene provides a direct anchor in this framework. The key differences to integrate for the Visp biologics context:

- **Product profile**: transition from small molecules (chemical APIs) to biologics (proteins, antibodies, ADCs) — equipment in direct contact has different CIP/SIP cleanability and containment integrity requirements
- **Fleet complexity**: multi-product CDMO environment implies more complex management of scheduling conflicts
- **Dynamic ramp-up**: the equipment fleet evolves rapidly with new lines brought into production

---

*→ Section 2: SME in CAPEX Projects — CQV Framework*

---

### References (excerpts)

- Pasipatorwa, S. et al. (2022). *CMMS pharmaceutical reliability improvement*
- Macchi, M. & Fumagalli, L. (2013). *Maintenance maturity assessment method*
- Garg, A. & Deshmukh, S.G. (2006). *Maintenance management — literature review*

---END OF DOCUMENT---