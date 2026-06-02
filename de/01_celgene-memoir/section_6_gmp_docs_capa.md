# Abschnitt 6 — GMP-Dokumentation & CAPA-Zyklus

## 6.1 Dokumentation als Nachweis der Beherrschung

In GMP-Umgebungen ist die grundlegende Regel einfach und absolut: **"If it's not documented, it didn't happen."** Diese Maxime ist kein bürokratisches Klischee — sie spiegelt die regulatorische Logik wider, wonach der Nachweis einer Aktivität untrennbar mit der Aktivität selbst verbunden ist.

Für die Instandhaltung bedeutet dies, dass jeder Eingriff, jede Kalibrierung, jede erkannte Abweichung eine formelle, datierte, unterschriebene Spur erzeugen und in ein kohärentes Dokumentationssystem integriert werden muss.

## 6.2 Dokumentationsarchitektur

```
SOPs (Standard Operating Procedures)
  ↓ "Was zu tun ist und wie"
  
WPs (Work Procedures / Instructions)
  ↓ "Detaillierte Ausführungsschritte"
  
FORMs (Registrierungsformulare)
  ↓ "Nachweis, dass es gemacht wurde"
  
MDS (Maintenance Data Sheets)
  ↓ "Technische Referenzdaten pro Ausrüstung"
```

Diese Dokumentationshierarchie gewährleistet die Kohärenz zwischen regulatorischen Anforderungen (SOPs), Feldpraktiken (WPs) und Ausführungsnachweisen (FORMs). Die Erstellung, Überprüfung und Aktualisierung dieser Dokumente stellen einen bedeutenden Teil der Koordinationsarbeit in der Instandhaltung dar.

## 6.3 ALCOA-Prinzipien & Datenintegrität

Die **ALCOA**-Prinzipien (Attributable, Legible, Contemporaneous, Original, Accurate) definieren die Eigenschaften gültiger GMP-Daten:

| Prinzip | Definition | Anwendung Instandhaltung |
|---------|-----------|------------------------|
| **A**ttributable | Identifizierbar durch ihren Urheber | Obligatorische Unterschrift bei jeder Aufzeichnung |
| **L**egible | Lesbar und verständlich | Keine Durchstreichungen, Korrekturen mit Paraphe |
| **C**ontemporaneous | Zum Zeitpunkt der Handlung aufgezeichnet | Keine ungerechtfertigte rückwirkende Aufzeichnung |
| **O**riginal | Primärdaten werden aufbewahrt | Keine Übertragung ohne Verweis auf das Original |
| **A**ccurate | Korrekt und vollständig | Reale Werte, keine ungerechtfertigten Rundungen |

In Oracle CMMS werden die Aufzeichnungen der Instandhaltungs-WOs automatisch mit Zeitstempel versehen und mit dem angemeldeten Benutzer verknüpft, wodurch natürlich die Prinzipien A, C und teilweise L gewährleistet werden.

## 6.4 Dokumentationslebenszyklus

```
Erstellung (Autor) → Überprüfung (Peer) → Genehmigung (Manager/QA) 
→ Personalschulung → Anwendung 
→ Periodische Überprüfung → Aktualisierung bei Bedarf → Archivierung
```

## 6.5 Abweichungsmanagement

Eine **Abweichung** ist jede Abweichung von einer genehmigten Verfahrensweise oder einer definierten Spezifikation. In der Instandhaltung können Abweichungen sein:

- **Ausrüstungsabweichungen**: Kalibrierungsergebnis außerhalb der Grenzwerte, ungeplante Panne bei qualifizierter Ausrüstung
- **Verfahrensabweichungen**: Eingriff ohne genehmigten WO durchgeführt, SOP nicht eingehalten
- **Dokumentationsabweichungen**: fehlende Daten, falsche Unterschriften

Das Management einer Abweichung folgt einem strukturierten Ablauf:
```
Erkennung → Sofortige Meldung → Containment (Auswirkung isolieren)
→ Erste Bewertung (Qualitätsauswirkung?) → Formelle Abweichungseröffnung
→ RCA-Untersuchung → CAPA-Plan → QA-Genehmigung → Abschluss
```

## 6.6 Root Cause Analysis (RCA)

Die in der pharmazeutischen GMP-Umgebung verwendeten RCA-Werkzeuge:

**5 Whys** — Einfache und effektive Methode für direkte Ausfälle:
```
Pumpenpanne → Warum? Lager abgenutzt
→ Warum? Unzureichende Schmierung
→ Warum? Unangepasste PM-Häufigkeit
→ Warum? Kritikalität bei Inbetriebnahme unterschätzt
→ Warum? Klassifizierungsverfahren seit Installation nicht überarbeitet
→ GRUNDURSACHE: Verfahren zur Kritikalitätsklassifizierung veraltet
```

**Ishikawa-Diagramm (5M)** — Für komplexe multifaktorielle Ausfälle:
- **M**itarbeiter (Kompetenzen, Schulung)
- **M**ethode (SOP, befolgte Verfahrensweise?)
- **M**aschine (Ausrüstungszustand, Pannenhistorie)
- **M**aterial (Ersatzteile, Qualität der Verbrauchsmaterialien)
- **M**ilieu (Umgebung, Temperatur, Vibrationen)

**FMEA** — Für systematische präventive Analyse (siehe Abschnitt 2)

## 6.7 CAPA basierend auf Trends

Über die Behandlung einzelner Abweichungen hinaus ermöglicht die Überwachung von **Trends** die Identifizierung systemischer Probleme, bevor sie eine größere Abweichung verursachen:

- Monatliche Verfolgung der Anzahl und Art der Abweichungen pro Linie / Ausrüstung
- Analyse von Wiederholungen (gleiche Ausrüstung, gleiche Ursache)
- Vierteljährliche CAPA-Überprüfung mit der Qualitätsabteilung

## 6.8 CAPA & Change Control

Jede Korrektur- oder Präventivmaßnahme, die eine qualifizierte Ausrüstung, eine genehmigte SOP oder einen Verfahrensparameter modifiziert, muss durch den **Change Control**-Prozess (Änderungsmanagement) gehen:

```
Änderungsvorschlag → Auswirkungsbewertung (Qualifizierung erforderlich?)
→ Multidisziplinäre Genehmigung (Engineering + Quality + Process)
→ Kontrollierte Umsetzung → Wirksamkeitsüberprüfung → Abschluss
```

## 6.9 Lean Six Sigma & kontinuierliche Verbesserung

Die Integration von Lean Six Sigma-Werkzeugen in den kontinuierlichen Verbesserungsansatz der pharmazeutischen Instandhaltung ist von Da Silva et al. (2023) dokumentiert:

- **DMAIC** (Define, Measure, Analyze, Improve, Control) für strukturierte Verbesserungsprojekte
- **5S** für die Organisation von Instandhaltungswerkstätten und -lagern
- **Kaizen** für schrittweise Verbesserungen im Alltag

Die in der Literatur identifizierte Hauptspannung ist die **Angst vor Requalifizierungen** im Zusammenhang mit Prozessänderungen — was die kontinuierliche Verbesserung in regulatorisch sehr konservativen Umgebungen bremsen kann.

---

*→ Abschnitt 7: Schlussfolgerung & Perspektiven Industry 4.0*

---

### Literaturverzeichnis (Auszüge)

- Da Silva, A. et al. (2023). *Lean Six Sigma pharmaceutical GMP continuous improvement*
- ICH Q10. *Pharmaceutical Quality System*
- FDA. *Guidance for Industry — Investigating Out-of-Specification (OOS) Test Results*
- EMA. *Guideline on good pharmacovigilance practices — CAPA*