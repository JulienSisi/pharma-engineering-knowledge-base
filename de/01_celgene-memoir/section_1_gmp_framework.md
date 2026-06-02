# Abschnitt 1 — GMP-Rechtsrahmen: Kontext und Anforderungen

## 1.1 Einführung in den regulatorischen Kontext

Die pharmazeutische Produktion von Wirkstoffen für den menschlichen Gebrauch erfolgt in einem strengen normativen Rahmen, der gemeinsam von der **FDA** (*Food and Drug Administration*, Vereinigte Staaten) und den europäischen und schweizerischen Behörden, einschließlich **SwissMedic**, definiert wird. Diese Organisationen schreiben die Einhaltung der *current Good Manufacturing Practices* (cGMP) vor, deren zentrales Ziel es ist, zu gewährleisten, dass jede produzierte Charge ihren Qualitäts-, Identitäts- und Reinheitsspezifikationen entspricht.

In diesem Rahmen ist die Wartung von Ausrüstung und Betriebsmitteln keine periphere Aktivität: sie stellt eine **Säule der regulatorischen Konformität** dar. Wie Tibesso et al. (2024) sowie Ahmed (2024) betonen, verlangen die cGMP, dass Anlagen und Ausrüstungen *fit for purpose* sind, proaktiv gewartet und vollständig dokumentiert werden — die Prävention von Ausfällen hat Vorrang vor deren Behebung.

## 1.2 Auf die Wartung angewandte regulatorische Anforderungen

Das **21 CFR Part 211**-Regelwerk der FDA legt die rechtlichen Grundlagen für die Qualifikation und Kalibrierung von Ausrüstungen fest.

Die grundlegenden Anforderungen umfassen:

- **21 CFR 211.68** — Automatische, mechanische und elektronische Systeme: formelle Wartung und Qualifikation erforderlich
- **21 CFR 211.182** — Equipment cleaning and maintenance: obligatorische Aufzeichnungen mit Datum, Uhrzeit, Unterschrift
- **21 CFR 211.68(b)** — Validierung von Computersystemen (anwendbar auf Oracle CMMS)

SwissMedic fügt über die Guten Herstellungspraxis-Standards, die an den EU-GMP-Richtlinien ausgerichtet sind, eine spezifische dokumentarische Anforderungsebene hinzu, insbesondere bezüglich der Nachverfolgbarkeit von Kalibrierungen und dem Management von Abweichungen.

## 1.3 Qualifikation der Ausrüstungen: IQ / OQ / PQ

Der IQ/OQ/PQ-Qualifikationszyklus bildet den strukturierenden Rahmen für jede Ausrüstung, die in eine GMP-Umgebung integriert wird:

```
IQ — Installation Qualification
     ↓ Die Ausrüstung ist gemäß den Spezifikationen installiert
OQ — Operational Qualification
     ↓ Die Ausrüstung funktioniert innerhalb der definierten Grenzen
PQ — Performance Qualification
     ↓ Die Ausrüstung erzeugt konforme Ergebnisse unter realen Bedingungen
```

Laut Sharma (2020) muss die präventive Wartung in Übereinstimmung mit den während der OQ/PQ definierten Requalifikationsintervallen geplant werden. Eine nicht dokumentierte Abweichung zwischen dem Wartungsplan und den Qualifikationsanforderungen stellt eine potenzielle regulatorische Nichtkonformität dar.

## 1.4 Kalibrierung und Metrologie in regulierter Umgebung

Die Kalibrierung von Mess- und Kontrollinstrumenten ist eine direkte Anforderung des 21 CFR Part 211.68. In einem multi-departmentalen Kontext (Utilities, Process, Calibration) ermöglicht die zentralisierte Verwaltung der Kalibrierungsintervalle über Oracle CMMS:

- Die automatische Generierung von Kalibrierungs-Arbeitsaufträgen (WO)
- Die Nachverfolgung der Kalibrierungszertifikate mit Verknüpfung zu den betroffenen Instrumenten
- Die frühzeitige Erkennung von Instrumenten außerhalb der Toleranz, bevor sie die Produktion beeinträchtigen

## 1.5 Synthese: Wartung als regulatorische Funktion

Die Positionierung der Wartung als regulatorische Funktion — und nicht nur als technische — ist der Schlussstein des in dieser Abhandlung dokumentierten Ansatzes. In einer Umgebung unter doppelter FDA/SwissMedic-Überwachung erzeugt jede Wartungsaktivität einen dokumentarischen Nachweis, der während eines Audits oder einer Inspektion geprüft werden kann.

> **Praktische Implikation**: Die Qualität der Wartungsdokumentation korreliert direkt mit der Fähigkeit des Standorts, seine Praktiken vor den Regulierungsbehörden zu verteidigen.

---

*→ Abschnitt 2: Wartungsstrategie & ERP Oracle*

---

### Referenzen (Auszüge)

- Ahmed, A. (2024). *GMP compliance in pharmaceutical maintenance management*
- Tibesso, G. et al. (2024). *Preventive maintenance in FDA-regulated environments*
- Sharma, R. (2020). *Equipment qualification lifecycle pharmaceutical industry*
- FDA. *21 CFR Part 211 — Current Good Manufacturing Practice for Finished Pharmaceuticals*