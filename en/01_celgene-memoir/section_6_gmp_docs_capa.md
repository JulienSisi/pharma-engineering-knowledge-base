# Section 6 — GMP Documentation & CAPA Cycle

## 6.1 Documentation as proof of control

In a GMP environment, the fundamental rule is simple and absolute: **"If it's not documented, it didn't happen."** This maxim is not a bureaucratic cliché — it reflects the regulatory logic whereby proof of an activity is inseparable from the activity itself.

For maintenance, this means that every intervention, every calibration, every detected deviation must generate a formal trace, dated, signed, and integrated into a coherent documentation system.

## 6.2 Documentary architecture

```
SOPs (Standard Operating Procedures)
  ↓ "What to do and how"
  
WPs (Work Procedures / Instructions)
  ↓ "Detailed execution steps"
  
FORMs (Recording forms)
  ↓ "Proof that it was done"
  
MDS (Maintenance Data Sheets)
  ↓ "Technical reference data by equipment"
```

This documentary hierarchy ensures consistency between regulatory requirements (SOPs), field practices (WPs), and execution evidence (FORMs). The drafting, review and updating of these documents constitute a significant part of maintenance coordination work.

## 6.3 ALCOA principles & data integrity

The **ALCOA** principles (Attributable, Legible, Contemporaneous, Original, Accurate) define the characteristics of valid GMP data:

| Principle | Definition | Maintenance application |
|---------|-----------|------------------------|
| **A**ttributable | Identifiable to its author | Mandatory signature on each record |
| **L**egible | Readable and understandable | No crossing out, correction with initial |
| **C**ontemporaneous | Recorded at the time of action | No unjustified retroactive recording |
| **O**riginal | Primary data preserved | No transcription without reference to original |
| **A**ccurate | Correct and complete | Actual values, no unjustified rounding |

In Oracle CMMS, maintenance WO records are automatically timestamped and linked to the connected user, naturally ensuring principles A, C and partially L.

## 6.4 Documentary lifecycle

```
Drafting (author) → Review (peer) → Approval (manager/QA) 
→ Personnel training → Implementation 
→ Periodic review → Update if necessary → Archiving
```

## 6.5 Deviation management

A **deviation** is any departure from an approved procedure or defined specification. In maintenance, deviations can be:

- **Equipment deviations**: calibration result out of limit, unplanned failure on qualified equipment
- **Procedural deviations**: intervention performed without approved WO, SOP not followed
- **Documentary deviations**: missing data, incorrect signatures

Deviation management follows a structured flow:
```
Detection → Immediate notification → Containment (isolate impact)
→ Initial assessment (quality impact?) → Formal deviation opening
→ RCA investigation → CAPA plan → QA approval → Closure
```

## 6.6 Root Cause Analysis (RCA)

RCA tools used in pharmaceutical GMP environments:

**5 Whys** — Simple and effective method for direct failures:
```
Pump failure → Why? Worn bearing
→ Why? Insufficient lubrication
→ Why? Inappropriate PM frequency
→ Why? Criticality underestimated at commissioning
→ Why? Criticality classification procedure not revised since installation
→ ROOT CAUSE: obsolete criticality classification procedure
```

**Ishikawa diagram (5M)** — For complex multi-factor failures:
- **M**anpower (skills, training)
- **M**ethod (SOP, procedure followed?)
- **M**achine (equipment condition, failure history)
- **M**aterial (spare parts, consumables quality)
- **M**ilieu (environment, temperature, vibrations)

**FMEA** — For systematic preventive analysis (see Section 2)

## 6.7 Trend-based CAPA

Beyond treating individual deviations, **trend** monitoring allows identification of systemic problems before they generate a major deviation:

- Monthly monitoring of number and type of deviations by line / equipment
- Analysis of recurrences (same equipment, same cause)
- Quarterly CAPA review with Quality department

## 6.8 CAPA & Change Control

Any corrective or preventive action that modifies qualified equipment, an approved SOP, or a process parameter must go through the **Change Control** process:

```
Change proposal → Impact assessment (qualification required?)
→ Multi-disciplinary approval (Engineering + Quality + Process)
→ Controlled implementation → Effectiveness verification → Closure
```

## 6.9 Lean Six Sigma & continuous improvement

The integration of Lean Six Sigma tools into the continuous improvement approach for pharmaceutical maintenance is documented by Da Silva et al. (2023):

- **DMAIC** (Define, Measure, Analyze, Improve, Control) for structured improvement projects
- **5S** for organization of maintenance workshops and stores
- **Kaizen** for daily incremental improvements

The main tension identified in the literature is the **fear of requalifications** related to process changes — which can hinder continuous improvement in environments that are very conservative from a regulatory standpoint.

---

*→ Section 7: Conclusion & Industry 4.0 Perspectives*

---

### References (excerpts)

- Da Silva, A. et al. (2023). *Lean Six Sigma pharmaceutical GMP continuous improvement*
- ICH Q10. *Pharmaceutical Quality System*
- FDA. *Guidance for Industry — Investigating Out-of-Specification (OOS) Test Results*
- EMA. *Guideline on good pharmacovigilance practices — CAPA*