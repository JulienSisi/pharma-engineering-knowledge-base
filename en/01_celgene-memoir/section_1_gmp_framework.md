# Section 1 — GMP Regulatory Framework: Context and Requirements

## 1.1 Introduction to the regulatory context

The pharmaceutical production of active pharmaceutical ingredients for human use operates within a strict regulatory framework, jointly defined by the **FDA** (*Food and Drug Administration*, United States) and European and Swiss authorities, including **SwissMedic**. These organizations mandate compliance with *current Good Manufacturing Practices* (cGMP), whose central objective is to ensure that each batch produced conforms to its quality, identity, and purity specifications.

In this framework, equipment and utilities maintenance is not a peripheral activity: it constitutes a **pillar of regulatory compliance**. As highlighted by Tibesso et al. (2024) and Ahmed (2024), cGMP requires that facilities and equipment be *fit for purpose*, proactively maintained, and comprehensively documented — with failure prevention taking precedence over correction.

## 1.2 Regulatory requirements applied to maintenance

The **21 CFR Part 211** reference framework from the FDA establishes the legal foundations for equipment qualification and calibration.

The fundamental requirements cover:

- **21 CFR 211.68** — Automatic, mechanical, and electronic systems: formal maintenance and qualification required
- **21 CFR 211.182** — Equipment cleaning and maintenance: mandatory records with date, time, signature
- **21 CFR 211.68(b)** — Computer systems validation (applicable to Oracle CMMS)

SwissMedic, through Swiss Good Manufacturing Practices aligned with EU-GMP directives, adds a specific layer of documentary requirements, particularly regarding calibration traceability and deviation management.

## 1.3 Equipment qualification: IQ / OQ / PQ

The IQ/OQ/PQ qualification cycle constitutes the structural framework for any equipment integrated into a GMP environment:

```
IQ — Installation Qualification
     ↓ Equipment is installed according to specifications
OQ — Operational Qualification
     ↓ Equipment operates within defined limits
PQ — Performance Qualification
     ↓ Equipment produces compliant results under real conditions
```

According to Sharma (2020), preventive maintenance must be planned in accordance with requalification intervals defined during OQ/PQ. An undocumented gap between the maintenance plan and qualification requirements constitutes a potential regulatory non-compliance.

## 1.4 Calibration and metrology in a regulated environment

Calibration of measuring and control instruments is a direct requirement of 21 CFR Part 211.68. In a multi-departmental context (Utilities, Process, Calibration), centralized management of calibration intervals via Oracle CMMS enables:

- Automatic generation of calibration work orders (WO)
- Tracking of calibration certificates with links to concerned instruments
- Early detection of out-of-tolerance instruments before they impact production

## 1.5 Summary: maintenance as a regulatory function

Positioning maintenance as a regulatory function — not merely technical — is the cornerstone of the approach documented in this report. In an environment under dual FDA/SwissMedic oversight, each maintenance activity generates documentary evidence that can be examined during an audit or inspection.

> **Practical implication**: The quality of maintenance documentation is directly correlated with the site's ability to defend its practices before regulators.

---

*→ Section 2: Maintenance strategy & Oracle ERP*

---

### References (excerpts)

- Ahmed, A. (2024). *GMP compliance in pharmaceutical maintenance management*
- Tibesso, G. et al. (2024). *Preventive maintenance in FDA-regulated environments*
- Sharma, R. (2020). *Equipment qualification lifecycle pharmaceutical industry*
- FDA. *21 CFR Part 211 — Current Good Manufacturing Practice for Finished Pharmaceuticals*

---END OF DOCUMENT---