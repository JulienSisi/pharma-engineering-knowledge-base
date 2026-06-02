# Section 2 — Maintenance Strategy & Oracle ERP

## 2.1 From reactive to preventive: paradigmatic evolution

Pharmaceutical maintenance has undergone a profound transformation over the past two decades, moving from a purely corrective logic (intervening after failure) to a structured preventive logic, then toward predictive approaches. In a GMP environment, this evolution is not optional: an unanticipated failure on critical equipment can trigger a regulatory deviation, compromise a production batch, or even require requalification.

The maintenance strategy documented in this thesis is based on three pillars:

```
┌────────────────────────────────────────────────────────┐
│  1. CLASSIFICATION BY CRITICALITY                      │
│     RPN Matrix (Risk Priority Number)                  │
│     → differentiated strategy by asset                 │
├────────────────────────────────────────────────────────┤
│  2. Oracle CMMS PLANNING                               │
│     Auto-generated preventive WOs, historical tracking │
│     → total visibility on fleet status                 │
├────────────────────────────────────────────────────────┤
│  3. SHUTDOWN & SPARE PARTS MANAGEMENT                  │
│     Anticipation of periodic shutdowns                 │
│     → budget ~1.5M CHF, integrated Oracle warehouse    │
└────────────────────────────────────────────────────────┘
```

## 2.2 Criticality matrix and asset classification

Equipment classification by criticality is the prerequisite for any differentiated maintenance strategy. In GMP pharmaceutical environments, this classification incorporates two dimensions:

- **Quality/regulatory impact**: does the equipment come into direct contact with the product? Does it condition a critical process parameter (CPP)?
- **Availability impact**: does its failure cause line shutdown? Is there redundancy?

The FMEA (Failure Mode and Effects Analysis) method, enhanced by calculating the RPN (Risk Priority Number = Severity × Occurrence × Detectability), enables prioritization of maintenance resources on the highest-risk assets.

## 2.3 Oracle CMMS: architecture and data flows

The Oracle EAM (Enterprise Asset Management) system constitutes the central nervous system of the maintenance function. Its architecture in pharmaceutical environments covers:

**Asset management:**
- Equipment hierarchy (site → line → equipment → sub-assembly)
- Technical sheets and intervention history
- Qualification documents linked to each asset

**Maintenance planning:**
- Automatic generation of preventive Work Orders (WO)
- Priority and technician resource management
- Tracking of actual vs planned intervention times

**Spare parts management:**
- Minimum stock per critical reference
- Supplier links and procurement lead times
- Stock valuation for budget reporting

The ISA-95 architecture defines integration levels between Oracle EAM (level 4 — ERP) and production control systems (level 3 — MES/SCADA), enabling automatic escalation of equipment alarms to the WO management system.

## 2.4 Spare parts strategy for periodic shutdowns

Planning periodic shutdowns constitutes a multi-constraint management exercise: regulatory constraints (requalification windows), production constraints (minimize impact on batches), stock constraints (avoid capital over-immobilization).

The applied approach is structured around:

1. **Critical parts identification** through FMEA criticality analysis + Oracle history
2. **Safety stock calculation** based on supplier lead times and shutdown frequency
3. **Shutdown kit assembly** grouping parts by equipment/line
4. **Warehouse supervision** for reception, GMP-compliant storage and traceability

## 2.5 Budgeting and reporting

Managing a maintenance budget of ~1.5M CHF involves structured reporting that distinguishes:

- **Maintenance OPEX**: spare parts, outsourced maintenance contracts, internal resources
- **Maintenance CAPEX**: major equipment replacement, upgrades
- **Failure costs**: unplanned repairs, production impact

The Oracle dashboard enables monthly extraction of budget KPIs and their comparison with initial commitments.

---

*→ Section 3: KPI Management & Dashboard*

---

### References (excerpts)

- Pasipatorwa, S. et al. (2022). *CMMS implementation and maintenance performance improvement*
- Pintelon, L. & Parodi-Herz, A. (2008). *Maintenance: An evolutionary perspective*
- ISA-95. *Enterprise-Control System Integration standard*