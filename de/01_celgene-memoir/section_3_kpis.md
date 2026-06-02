# Sektion 3 — Steuerung über KPIs & Dashboard

## 3.1 Der KPI als gemeinsame Sprache

In einer pharmazeutischen Multi-Abteilungsumgebung spielen Leistungsindikatoren eine Rolle, die über die reine Messung hinausgeht: Sie bilden eine **gemeinsame Sprache** zwischen Instandhaltung, Produktion, Qualität und Management. Ein gut definierter KPI übersetzt eine komplexe Realität vor Ort in eine umsetzbare Entscheidungsdatenbasis.

Die Konzeption des Instandhaltungs-Dashboards muss drei Leseebenen berücksichtigen:

```
Strategische Ebene  →  Langfristige Trends, Benchmarking, Budget
Taktische Ebene     →  Wochenplanung, Einhaltungsrate der Planung
Operative Ebene     →  Offene/geschlossene WOs, laufende Störungen, Notfälle
```

## 3.2 OEE — Overall Equipment Effectiveness

Der OEE ist der Referenzindikator für die Anlagenleistung. Er setzt sich aus drei multiplikativen Faktoren zusammen:

```
OEE = Verfügbarkeit × Leistung × Qualität

Verfügbarkeit  = Tatsächliche Betriebszeit / Geplante verfügbare Zeit
Leistung       = Tatsächliche Produktion / Theoretische Produktion
Qualität       = Konforme Chargen / Insgesamt produzierte Chargen
```

Ein OEE von Weltklasse liegt in der Regel bei etwa 85%. In einer pharmazeutischen GMP-Umgebung können regulatorische Zwänge (Stillstände für Reinigung, Kalibrierung, Qualifizierungen) angepasste Ziele je nach Anlagentyp rechtfertigen.

## 3.3 MTBF / MTTR — Zuverlässigkeit und Instandhaltbarkeit

| Indikator | Formel | Interpretation |
|-----------|---------|----------------|
| MTBF | Gesamte Betriebszeit / Anzahl der Ausfälle | Je höher, desto zuverlässiger ist die Anlage |
| MTTR | Gesamte Reparaturzeit / Anzahl der Ausfälle | Je niedriger, desto effektiver ist die Instandhaltung |
| Verfügbarkeit | MTBF / (MTBF + MTTR) | Zusammenfassung Zuverlässigkeit + Instandhaltbarkeit |

Die MTBF/MTTR-Verfolgung pro Anlage im Oracle CMMS ermöglicht es, chronisch fehlerhafte Anlagen zu identifizieren und eine Neuklassifizierung ihrer Instandhaltungsstrategie zu rechtfertigen (Wechsel von periodisch-präventiv zu zustandsorientiert oder Austausch).

## 3.4 Budget-KPIs

Die Verwaltung eines Budgets von ~1,5M CHF erfordert eine strukturierte monatliche Verfolgung:

- **Realisierungsrate des präventiven Instandhaltungsplans** (Ziel: >95%)
- **Verhältnis korrektive / präventive Instandhaltung** (Ziel: <20% korrektiv)
- **Instandhaltungskosten pro Anlage** (Identifizierung der kostspieligsten Ausrüstungen)
- **Service-Rate Ersatzteile** (Verfügbarkeit der Teile bei Interventionen)
- **Abweichung Budget vs. realisiert** nach Kostenstelle

## 3.5 Architektur des Oracle-Dashboards

```
┌─────────────────────────────────────────────────────────┐
│           MONATLICHES INSTANDHALTUNGS-DASHBOARD         │
├──────────────┬──────────────┬──────────────┬────────────┤
│ VERFÜGBARKEIT│    OEE       │  BUDGET      │  WOs       │
│   98,2%      │   84,7%      │  CHF 127K/M  │  142 offen │
│   ▲ +0,3%    │   ▲ +1,2%   │  ▼ -3% vs P  │  ▼ -8 vs M-1│
├──────────────┼──────────────┼──────────────┼────────────┤
│ MTBF         │  MTTR        │ PM Compliance│ CAPAs offen│
│  847 h       │   2,3 h      │   97,4%      │    4       │
└──────────────┴──────────────┴──────────────┴────────────┘
```

## 3.6 Verknüpfung KPIs → Entscheidung → Aktion

Der Wert der KPIs liegt in ihrer Fähigkeit, Aktionen auszulösen. Ein Dashboard, das misst, ohne Entscheidungen zu generieren, ist ein kostspieliges Werkzeug ohne ROI. Der Kreislauf der kontinuierlichen Verbesserung:

```
KPI-Messung → Trendanalyse → Abweichungsidentifizierung → 
Korrekturentscheidung → Implementierung → Wirkungsverifikation → 
KPI-Aktualisierung → ...
```

Dieser Kreislauf ist direkt mit dem CAPA-Zyklus verknüpft, der in Sektion 6 dokumentiert ist.

---

*→ Sektion 4: Abteilungsübergreifende Koordination*

---

### Referenzen (Auszüge)

- Dal et al. (2000). *OEE definition and application*
- Nakajima, S. (1988). *TPM — Total Productive Maintenance*
- Muchiri, P. & Pintelon, L. (2008). *Performance measurement using OEE*