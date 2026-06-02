# Abschnitt 2 — Instandhaltungsstrategie & ERP Oracle

## 2.1 Von reaktiv zu präventiv: paradigmatische Entwicklung

Die pharmazeutische Instandhaltung hat in den letzten beiden Jahrzehnten eine tiefgreifende Transformation durchlaufen, vom rein korrektiven Ansatz (Eingriff nach dem Ausfall) zu einer strukturierten präventiven Logik und dann zu prädiktiven Ansätzen. In einer GMP-Umgebung ist diese Entwicklung nicht optional: Ein unvorhergesehener Ausfall einer kritischen Anlage kann eine regulatorische Abweichung auslösen, eine Produktionscharge gefährden oder sogar eine Requalifizierung erfordern.

Die in dieser Abhandlung dokumentierte Instandhaltungsstrategie stützt sich auf drei Säulen:

```
┌────────────────────────────────────────────────────────┐
│  1. KLASSIFIZIERUNG NACH KRITIKALITÄT                  │
│     Matrixe RPN (Risk Priority Number)                 │
│     → differenzierte Strategie pro Asset               │
├────────────────────────────────────────────────────────┤
│  2. PLANUNG ORACLE CMMS                                │
│     Automatisch generierte präventive WOs, Historie    │
│     → vollständige Sichtbarkeit des Anlagenbestands    │
├────────────────────────────────────────────────────────┤
│  3. SHUTDOWN- & ERSATZTEIL-MANAGEMENT                   │
│     Antizipation periodischer Stillstände              │
│     → Budget ~1.5M CHF, integriertes Oracle-Lager      │
└────────────────────────────────────────────────────────┘
```

## 2.2 Kritikalitätsmatrix und Klassifizierung der Assets

Die Klassifizierung der Anlagen nach Kritikalität ist die Voraussetzung für jede differenzierte Instandhaltungsstrategie. In pharmazeutischen GMP-Umgebungen integriert diese Klassifizierung zwei Dimensionen:

- **Qualitäts-/Regulatorischer Einfluss**: Hat die Anlage direkten Kontakt mit dem Produkt? Beeinflusst sie einen kritischen Prozessparameter (CPP)?
- **Verfügbarkeitseinfluss**: Führt ihr Ausfall zum Stillstand der Linie? Gibt es eine Redundanz?

Die FMEA-Methode (Failure Mode and Effects Analysis), erweitert durch die Berechnung des RPN (Risk Priority Number = Schweregrad × Häufigkeit × Entdeckbarkeit), ermöglicht es, die Instandhaltungsressourcen auf die Assets mit dem höchsten Risiko zu priorisieren.

## 2.3 Oracle CMMS: Architektur und Datenflüsse

Das Oracle EAM-System (Enterprise Asset Management) bildet das zentrale Nervensystem der Instandhaltungsfunktion. Seine Architektur in pharmazeutischen Umgebungen umfasst:

**Asset-Management:**
- Anlagenhierarchie (Standort → Linie → Anlage → Untereinheit)
- Technische Datenblätter und Eingriffshistorie
- Mit jedem Asset verknüpfte Qualifizierungsdokumente

**Instandhaltungsplanung:**
- Automatische Generierung präventiver Arbeitsaufträge (WO)
- Verwaltung von Prioritäten und Technikerressourcen
- Verfolgung tatsächlicher vs. geplanter Eingriffszeiten

**Ersatzteil-Management:**
- Mindestbestand pro kritischer Referenz
- Lieferantenverbindungen und Beschaffungszeiten
- Bestandsbewertung für Budget-Reporting

Die ISA-95-Architektur definiert die Integrationsniveaus zwischen Oracle EAM (Niveau 4 — ERP) und den Produktionskontrollsystemen (Niveau 3 — MES/SCADA), wodurch die automatische Weiterleitung von Anlagenalarmen an das WO-Managementsystem ermöglicht wird.

## 2.4 Ersatzteilstrategie für periodische Shutdowns

Die Planung periodischer Shutdowns stellt eine Aufgabe des Multi-Constraint-Managements dar: regulatorische Einschränkungen (Requalifizierungsfenster), Produktionseinschränkungen (Minimierung der Auswirkungen auf Chargen), Lagereinschränkungen (Vermeidung von Kapitalüberimmobilisierung).

Der angewandte Ansatz gliedert sich wie folgt:

1. **Identifizierung kritischer Teile** durch FMEA-Kritikalitätsanalyse + Oracle-Historie
2. **Berechnung des Sicherheitsbestands** basierend auf Lieferantenterminen und Shutdown-Häufigkeit
3. **Zusammenstellung der Shutdown-Kits** mit Teilegruppen nach Anlage/Linie
4. **Lagerverwaltung** für GMP-konforme Annahme, Lagerung und Rückverfolgbarkeit

## 2.5 Budgetierung und Reporting

Die Verwaltung eines Instandhaltungsbudgets von ~1.5M CHF erfordert ein strukturiertes Reporting, das folgende Unterscheidungen ermöglicht:

- **OPEX Instandhaltung**: Ersatzteile, externalisierte Instandhaltungsverträge, interne Ressourcen
- **CAPEX Instandhaltung**: Austausch größerer Anlagen, Upgrades
- **Ausfallkosten**: ungeplante Reparaturen, Produktionsauswirkungen

Das Oracle-Dashboard ermöglicht die monatliche Extraktion budgetärer KPIs und deren Vergleich mit den ursprünglichen Verpflichtungen.

---

*→ Abschnitt 3: KPI-Steuerung & Dashboard*

---

### Literatur (Auszüge)

- Pasipatorwa, S. et al. (2022). *CMMS implementation and maintenance performance improvement*
- Pintelon, L. & Parodi-Herz, A. (2008). *Maintenance: An evolutionary perspective*
- ISA-95. *Enterprise-Control System Integration standard*