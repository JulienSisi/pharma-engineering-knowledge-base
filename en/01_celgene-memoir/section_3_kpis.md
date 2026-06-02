# Section 3 — KPI Steering & Dashboard Management

## 3.1 KPI as a Common Language

In a multi-departmental pharmaceutical environment, performance indicators play a role that goes beyond simple measurement: they constitute a **common language** between maintenance, production, quality and management. A well-defined KPI translates a complex field reality into actionable decision-making data.

The design of the maintenance dashboard must respond to three levels of reading:

```
Strategic level     →  Long-term trends, benchmarking, budget
Tactical level      →  Weekly planning, schedule compliance rate
Operational level   →  Open/closed WOs, ongoing failures, emergencies
```

## 3.2 OEE — Overall Equipment Effectiveness

OEE is the reference indicator for equipment performance. It breaks down into three multiplicative factors:

```
OEE = Availability × Performance × Quality

Availability  = Actual operating time / Planned available time
Performance   = Actual production / Theoretical production
Quality       = Compliant lots / Total lots produced
```

A world-class OEE is generally around 85%. In a GMP pharmaceutical environment, regulatory constraints (shutdowns for cleaning, calibration, qualifications) may justify adjusted targets depending on the type of equipment.

## 3.3 MTBF / MTTR — Reliability and maintainability

| Indicator | Formula | Interpretation |
|-----------|---------|----------------|
| MTBF | Total operating time / Number of failures | The higher it is, the more reliable the equipment |
| MTTR | Total repair time / Number of failures | The lower it is, the more efficient the maintenance |
| Availability | MTBF / (MTBF + MTTR) | Reliability + maintainability synthesis |

MTBF/MTTR tracking by equipment in Oracle CMMS allows identification of chronically failing assets and justification for reclassifying their maintenance strategy (switching from periodic preventive to conditional, or replacement).

## 3.4 Budget KPIs

Managing a budget of ~1.5M CHF requires structured monthly tracking:

- **Preventive maintenance plan completion rate** (target: >95%)
- **Corrective/preventive maintenance ratio** (target: <20% corrective)
- **Maintenance cost per asset** (identification of most expensive equipment)
- **Spare parts service rate** (parts availability during interventions)
- **Budget vs actual variance** by cost line

## 3.5 Oracle Dashboard Architecture

```
┌─────────────────────────────────────────────────────────┐
│              MONTHLY MAINTENANCE DASHBOARD              │
├──────────────┬──────────────┬──────────────┬────────────┤
│ AVAILABILITY │    OEE       │  BUDGET      │  WOs       │
│   98.2%      │   84.7%      │  CHF 127K/M  │  142 open  │
│   ▲ +0.3%    │   ▲ +1.2%   │  ▼ -3% vs P  │  ▼ -8 vs M-1│
├──────────────┼──────────────┼──────────────┼────────────┤
│ MTBF         │  MTTR        │ PM Compliance│ CAPAs open │
│  847 h       │   2.3 h      │   97.4%      │    4       │
└──────────────┴──────────────┴──────────────┴────────────┘
```

## 3.6 KPI → Decision → Action Link

The value of KPIs lies in their ability to trigger actions. A dashboard that measures without generating decisions is an expensive tool without ROI. The virtuous loop:

```
KPI Measurement → Trend Analysis → Gap Identification → 
Corrective Decision → Implementation → Impact Verification → 
KPI Update → ...
```

This loop directly articulates with the CAPA cycle documented in Section 6.

---

*→ Section 4: Interdepartmental coordination*

---

### References (extracts)

- Dal et al. (2000). *OEE definition and application*
- Nakajima, S. (1988). *TPM — Total Productive Maintenance*
- Muchiri, P. & Pintelon, L. (2008). *Performance measurement using OEE*