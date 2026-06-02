# Section 3 — Troubleshooting & CAPA in biologics-Umgebung

## 3.1 Spezifika von Ausfällen in biologics

Die Ausfallarten in biologics-Umgebung weisen Besonderheiten auf, die das Troubleshooting im Vergleich zu einer small molecule-Umgebung erschweren:

```
Small molecule (Celgene)          Biologics (Lonza Visp)
─────────────────────────────     ──────────────────────────────
Deterministischer chemischer     Variabler biologischer Prozess
Prozess
Messbare chemische Kontamination Biologische Kontamination (Mykoplasmen, Bioburden)
Validierte chemische Reinigung   CIP/SIP kritisch — biologische Integrität
Klassische Instrumente          Online-Sensoren (pH, DO, Leitfähigkeit, Druck)
Chemische Einschließung         Biologische Einschließung + HPAPI
```

## 3.2 RCA-Werkzeuge angepasst an den biologics-Kontext

### FMEA Bioreaktor / Small Equipment

Die FMEA im biologics-Kontext integriert spezifische Ausfallarten:

| Komponente | Ausfallart | Potentielle Auswirkung | RPN-Leitfaden |
|-----------|------------|------------------------|---------------|
| Peristaltikdichtung | Verschleiß → Leckage | Chargenkontamination | Hoch |
| pH-Sonde | Kalibrierungsdrift | CPP außerhalb Grenze | Hoch |
| Belüftungsfilter | Verstopfung | Differenzdruck außerhalb Spez. | Mittel |
| Sterilventil | Fehlerhafter Betrieb | Kreuzkontamination | Hoch |
| Autoklav | Unvollständiger Zyklus | Nicht-Sterilität | Kritisch |

### Integrierter RCA-CAPA-Zyklus in GMP biologics

```
Qualitätssignal / Anlagenausfall
              ↓
    Formale Abweichung (GMP record)
              ↓
    RCA-Untersuchung (5M / FMEA / 5 Whys)
              ↓
    Grundursache identifiziert (systemisch, nicht oberflächlich)
              ↓
    CAPA-Plan: sofortige Korrektur + vorbeugende Maßnahme
              ↓
    Umsetzung + Dokumentation
              ↓
    Effectiveness check (Wirksamkeitsüberprüfung)
              ↓
    CAPA-Abschluss → CMMS + SOP-Update falls anwendbar
              ↓
    Einspeisung OEE / KPI → kontinuierlicher Verbesserungskreislauf
```

*Abbildung 3.1 — Integrierter RCA-CAPA-Verbesserungskreislauf in GMP biologics-Umgebung*

## 3.3 Troubleshooting in kommerzieller Produktion vs. Entwicklung

In der kommerziellen Ramp-up-Phase (Kontext Visp 2026) entsteht zusätzlicher Druck auf das Troubleshooting: Jede Charge zählt, jeder Stillstand hat direkte Vertragskosten. Der Ansatz muss kombinieren:

- **Reaktionsfähigkeit**: Auswirkungen schnell identifizieren und eingrenzen
- **GMP-Rigor**: Jeden Schritt trotz zeitlichem Druck dokumentieren
- **Untersuchungstiefe**: Zur systemischen Grundursache gehen, um Wiederholung zu vermeiden

## 3.4 RCA-CAPA-Kompetenzen für die Rolle I&U Engineer Visp

Die Literaturanalyse konvergiert zu drei Reifegrad-Anforderungen:

**Untersuchungstiefe** — über die proximale Ursache hinausgehen, um systemische Faktoren zu identifizieren (Design, PM-Intervall, reale vs. spezifizierte Nutzungsbedingungen), basierend auf der Kombination 5M + FMEA + historische CMMS-Daten.

**Dokumentationsrigor** — jede Untersuchung erzeugt eine formale Spur konform zu GMP-Anforderungen, mit konkreten Empfehlungen, zugewiesen, mit Deadline und messbaren Wirksamkeitskriterien.

**Kontinuierliche Verbesserungsorientierung** — das CAPA ist keine punktuelle Antwort auf einen isolierten Vorfall. Es speist einen Verbesserungskreislauf der Wartungsstrategien (PM-Intervalle, Kritikalität, Prozeduren), der SOPs und der OEE/KPI-Indikatoren des Standorts.

Die Erfahrung in Erstellung und Verfolgung von CAPAs, Abweichungen und SOPs, erworben in GMP API-Umgebung unter doppelter FDA/SwissMedic-Überwachung, bildet eine direkte Verankerung in diesem Referenzsystem.

---

*→ Section 4: GMP Utilities biologics — CIP/SIP, WFI, clean steam*

---

### Referenzen (Auszüge)

- Seely, R.J. et al. (2021). *Failure analysis biopharmaceutical manufacturing*
- ICH Q9. *Quality Risk Management — FMEA application*
- FDA. *Guidance on deviation and CAPA in biologics manufacturing*