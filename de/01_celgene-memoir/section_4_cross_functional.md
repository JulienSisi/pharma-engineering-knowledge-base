# Abschnitt 4 — Abteilungsübergreifende Koordination: Utilities, Process & Calibration

## 4.1 Die Koordination als zentrale Kompetenz

In einer pharmazeutischen GMP-Umgebung ist die Wartung niemals eine isolierte Aktivität. Sie ist eingebettet in ein Netzwerk funktionaler Abhängigkeiten, das mindestens drei operative Abteilungen umfasst:

- **Utilities**: Produktion und Verteilung der Prozessmedien (Druckluft, gereinigtes Wasser, Dampf, HVAC)
- **Process**: Produktion der APIs mit ihren Beschränkungen der Chargenplanung
- **Calibration**: Aufrechterhaltung der Metrologie und der konformen Messinstrumente

Die Koordination zwischen diesen drei Funktionen — oft mit teilweise divergierenden Zielen — ist eine kritische organisatorische Kompetenz, die von den Wartungsleistungsmodellen als entscheidend für die Gesamteffizienz des Standorts anerkannt wird.

## 4.2 TPM-Modell und abteilungsübergreifende Einbindung

Das Total Productive Maintenance (TPM) — entwickelt von Nakajima (1988) und formalisiert durch das Japan Institute of Plant Maintenance — ist der Referenzrahmen für eine in die Produktionsorganisation integrierte Wartung. Seine acht Säulen umfassen explizit die **autonome Wartung** (Einbindung der Bediener) und die **geplante Wartung** (Koordination zwischen Wartung und Produktion).

```
Die 8 TPM-Säulen:
1. Autonome Wartung (Bediener)
2. Geplante Wartung (Wartung)
3. Einzelfallverbesserung (Kaizen)
4. Schulung & Kompetenzentwicklung
5. Anfangssteuerung (neue Anlagen/Produkte)
6. Qualitätswartung (Verbindungen Prozess-Anlagen)
7. Sicherheit, Gesundheit, Umwelt
8. TPM in den Büros (Unterstützungsfunktionen)
```

In pharmazeutischen GMP-Umgebungen sind die Säulen 2, 6 und 7 besonders kritisch: die geplante Wartung integriert sich in die Produktionsfenster, die Qualitätswartung überwacht die CPPs, und die Sicherheit integriert die HPAPI/GMP-Anforderungen.

## 4.3 Scheduling und Management von Ressourcenkonflikten

Die Planung von Wartungsinterventionen in einer Multi-Abteilungs-Umgebung erzeugt wiederkehrende Ressourcenkonflikte:

| Konflikttyp | Beteiligte Parteien | Entscheidung |
|-------------|-------------------|-----------|
| Utility-Stillstand während Produktion | Utilities vs Process | Vorausplanung, validierte Zeitfenster |
| Kalibrierung von Instrumenten im Betrieb | Calibration vs Process | Ersatzinstrument, ausgehandelte Frist |
| Präventiver Shutdown vs laufende Charge | Wartung vs Process | In Produktionsplanung integrierte Shutdown-Fenster |
| Geteilte Technikerressourcen | Wartung vs Calibration | Prioritätenmatrix, Manager-Eskalation |

Die Lösung dieser Konflikte erfordert einen **strukturierten Besprechungsmechanismus** (tägliche/wöchentliche Wartungs-Produktions-Besprechung) und klare **Eskalationsregeln**, die in den SOPs dokumentiert sind.

## 4.4 Oracle als Koordinationsplattform

Oracle CMMS spielt eine Rolle als **Koordinationsplattform** über seinen reinen CMMS-Einsatz hinaus:

- Die generierten WOs sind für alle betroffenen Abteilungen sichtbar
- Die Status (geplant, in Bearbeitung, abgeschlossen) werden in Echtzeit aktualisiert
- Die Interventionshistorie pro Anlage ist für Process und Calibration einsehbar
- Automatische Benachrichtigungen informieren die Stakeholder über geplante Interventionen

Diese geteilte Transparenz reduziert abteilungsübergreifende Reibungen und stärkt das gegenseitige Vertrauen zwischen den Teams.

## 4.5 Formelle und informelle Kommunikation

Die effiziente Koordination basiert auf zwei komplementären Kanälen:

**Formell:** wöchentliche Wartungs-/Produktionsbesprechungen, monatliche KPI-Berichte, Oracle-Aufzeichnungen, Koordinations-SOPs
**Informell:** Präsenz vor Ort, Verfügbarkeit, Reaktionsfähigkeit auf dringende Anfragen, über die Zeit aufgebautes Vertrauen

Modgil & Sharma (2016) betonen, dass **"Total Productive Maintenance and Total Quality Management together have a significant positive impact on operational performance"** — eine Konvergenz, die nur möglich ist, wenn beide Funktionen gemeinsame Indikatoren und eine etablierte Koordinationssprache teilen.

---

*→ Abschnitt 5: Produktkontext*

---

### Literaturverzeichnis (Auszüge)

- Nakajima, S. (1988). *Introduction to TPM*
- Modgil, S. & Sharma, S. (2016). *TPM and TQM — meta-analysis*
- Ahuja, I.P.S. & Khamba, J.S. (2008). *Total productive maintenance — literature review*