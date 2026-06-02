# Abschnitt 2 — SME in CAPEX-Projekten: CQV-Framework in der Biologics-Umgebung

## 2.1 Die SME-Rolle im Lebenszyklus von CAPEX-Ausrüstung

Der Subject Matter Expert (SME) für Ausrüstung in einem CAPEX-Projekt ist kein technischer Beobachter — er ist die kritische Schnittstelle zwischen den Engineering-Projektteams, der Produktion, der Qualität und den Lieferanten. Sein Eingreifen umfasst den gesamten CQV-Zyklus:

```
CAPEX Project Lifecycle — SME Touchpoints

Phase DESIGN          → Spécifications techniques (URS)
Phase PROCUREMENT     → Sélection fournisseur, FAT
Phase INSTALLATION    → Supervision mise en œuvre, IQ
Phase COMMISSIONING   → Vérification fonctionnelle, C&Q
Phase QUALIFICATION   → OQ/PQ, protocoles, rapports
Phase PRODUCTION      → Handover, support ramp-up
```

## 2.2 URS — User Requirement Specification

Das URS-Dokument ist der Ausgangspunkt jeder Qualifizierung. Es übersetzt die Prozessanforderungen in formelle technische Anforderungen:

- **Funktionale Anforderungen**: Kapazitäten, Anwendungsbereiche, Genauigkeit
- **GMP-Anforderungen**: produktkontaktierende Materialien, CIP/SIP-Reinigbarkeit, erforderliche DQ/IQ/OQ/PQ
- **SHE-Anforderungen**: HPAPI-Containment, Operatorsicherheit
- **Utility-Anforderungen**: Stromversorgung, Fluide, HVAC
- **Dokumentationsanforderungen**: Data Integrity, Audit Trail, 21 CFR Part 11

## 2.3 FAT / SAT — Factory & Site Acceptance Tests

Der FAT (Factory Acceptance Test) und der SAT (Site Acceptance Test) sind kritische Schritte, die der SME gemeinsam mit dem Lieferanten steuert:

| Test | Ort | Ziel | SME-Rolle |
|------|-----|------|-----------|
| DQ | Büro/Lieferant | Verifizieren, dass das Design dem URS entspricht | Dokumentation prüfen |
| FAT | Lieferantenwerk | Ausrüstung vor Versand verifizieren | Funktionstests überwachen |
| SAT | Standort Visp | Nach Installation verifizieren | Ergebnisse mitsignieren |
| IQ | Standort Visp | Installation entspricht Spezifikationen | Protokoll erstellen oder prüfen |
| OQ | Standort Visp | Funktionieren innerhalb der Grenzen | Protokoll erstellen oder prüfen |
| PQ | Standort Visp | Leistung unter realen Bedingungen | Protokoll erstellen oder prüfen |

## 2.4 C&Q — Commissioning & Qualification

Das ISPE GAMP-Framework definiert die Grenze zwischen Commissioning (funktionale Engineering-Verifizierung) und Qualification (formeller GMP-Nachweis). In der Praxis ist gutes Engineering in der Commissioning-Phase die Voraussetzung für eine effiziente und überraschungsfreie Qualifizierung.

Die Fachliteratur (Calnan et al., 2017) betont, dass Mängel in den frühen Projektphasen (unvollständiges URS, unzureichendes FAT) sich systematisch als Abweichungen und Verzögerungen in der OQ/PQ-Phase manifestieren — ein bedeutender versteckter Kostenfaktor in Biologics-CAPEX-Projekten.

## 2.5 Verbindung Celgene → Visp

Die Wartungserfahrung in FDA/SwissMedic-Umgebung bei Celgene — insbesondere die Vertrautheit mit IQ/OQ/PQ-Zyklen, das Management von Qualifizierungsabweichungen und die Koordination mit Validierungsteams — bildet eine direkt übertragbare Grundlage. Die zu schließende Lücke ist die Beherrschung des Biologics-Kontexts (spezifische Zwänge bei Bioreaktoren, CIP/SIP-Systemen, WFI) und der aktiven SME-CAPEX-Rolle vs. der unterstützenden Wartungsrolle.

---

*→ Abschnitt 3: Troubleshooting & CAPA in Biologics*

---

### Literatur (Auszüge)

- Calnan, N. et al. (2017). *Commissioning and qualification pharmaceutical biologics*
- ISPE. *GAMP 5 — A Risk-Based Approach to Compliant GxP Computerized Systems*
- ICH Q8/Q9/Q10. *Pharmaceutical development, quality risk management, quality system*