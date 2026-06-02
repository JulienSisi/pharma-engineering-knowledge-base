# Section 1 — Equipment Management & Reliability: Strategische Grundlagen für eine CDMO biologics Umgebung

## 1.1 Kontext: Anlagenzuverlässigkeit als operativer Imperativ für CDMO

In einem Entwicklungs- und Fertigungsvertrag (CDMO) ist die Verfügbarkeit von Anlagen nicht nur eine operative Kennzahl unter vielen — sie ist eine vertragliche Bedingung. Jede produzierte Charge verpflichtet die Reputation des Standorts gegenüber pharmazeutischen Kunden, die ihrerseits Markteinführungsverpflichtungen gegenüber Regulierungsbehörden und Patienten haben.

Diese Realität ist besonders ausgeprägt im Kontext des kommerziellen Ramp-ups, wo neu qualifizierte Linien vom Validierungsregime zum Vollproduktionsregime übergehen, mit null Toleranz für nicht antizipierte Verfügbarkeitsabweichungen.

## 1.2 Besonderheiten des Small Equipment bei biologics

Das "Small Equipment" in einem CDMO biologics Kontext umfasst eine breite Palette von Anlagen: Peristaltikpumpen, Integritätsfilter, Transferverbindungen, Analysenwaagen, Inline-Kontrollausrüstung (pH, DO, Leitfähigkeit), Sampling-Systeme, Autoklaven kleiner Kapazität.

Diese Anlagen teilen mehrere Eigenschaften, die die Wartungsstrategie bestimmen:

```
Hohe Nutzungsfrequenz          → Beschleunigte Abnutzung, hohe Kritikalität
Direkter Kontakt mit Produkt   → Unmittelbare Auswirkung auf Chargenqualität
Häufiger Austausch            → Intensive Verwaltung der Ersatzteile
Vervielfachung der Referenzen → Komplexität der Lagerverwaltung
```

## 1.3 Klassifizierung nach Kritikalität — Anpassung an den biologics Kontext

Die Standard-Kritikalitätsmatrix (Schweregrad × Häufigkeit × Erkennbarkeit = RPN) muss für den biologics Kontext mit spezifischen Parametern erweitert werden:

| Kriterium | Beschreibung | Gewichtung |
|-----------|-------------|------------|
| Produktqualitätsauswirkung | Direkter Produktkontakt? CPP beteiligt? | Hoch |
| Kontaminationsauswirkung | Biologisches Risiko bei Ausfall? | Hoch |
| Redundanzverfügbarkeit | Backup-Ausrüstung verfügbar? | Mittel |
| Wartbarkeit | Geschätzte MTTR bei Ausfall? | Mittel |
| Beschaffungszeit | Lead Time kritische Ersatzteile? | Mittel |

## 1.4 Differenzierte Strategie: PM / CBM / verbleibende Korrektive

```
┌─────────────────────────────────────────────────────────────┐
│  1. KLASSIFIZIERUNG NACH KRITIKALITÄT                      │
│     SIA / CCA / RPN erweitert (maintainability complexity)  │
│     → differenzierte Strategie pro Anlage                   │
├─────────────────────────────────────────────────────────────┤
│  2. TPM/RCM-RAHMEN FOKUSSIERT AUF OEE                      │
│     Angriff auf die 6 großen Verluste, autonome TPM,        │
│     CBM-Integration bei hochkritischen Anlagen              │
├─────────────────────────────────────────────────────────────┤
│  3. DATENINFRASTRUKTUR UND CMMS                            │
│     Bestehende Sensoren + CMMS/MES als CBM-Basis,          │
│     bedingungsabhängiges Monitoring vor ML/PdM erweitert    │
├─────────────────────────────────────────────────────────────┤
│  4. INTEGRATION PRODUKTIONSPLANUNG                         │
│     Opportunistische PM, Fenster mit geringer Auswirkung,   │
│     Synchronisation mit Multi-Produkt CDMO Scheduling       │
└─────────────────────────────────────────────────────────────┘
```

## 1.5 Verbindung mit der Celgene Erfahrung

Die Erfahrung mit kritikalitätsbasiertem Wartungsmanagement Oracle + periodischem Shutdown bei Celgene bildet eine direkte Verankerung in diesem Referenzrahmen. Die wichtigsten Unterschiede, die für den biologics Kontext Visp zu integrieren sind:

- **Produktprofil**: Übergang von Small Molecules (chemische APIs) zu biologics (Proteine, Antikörper, ADCs) — Anlagen mit direktem Kontakt haben unterschiedliche Anforderungen an CIP/SIP-Reinigbarkeit und Containment-Integrität
- **Anlagenkomplexität**: CDMO Multi-Produkt-Umgebung impliziert komplexere Verwaltung von Scheduling-Konflikten  
- **Dynamischer Ramp-up**: der Anlagenpark entwickelt sich schnell mit neuen in Produktion gesetzten Linien

---

*→ Section 2: SME in CAPEX Projekten — Framework CQV*

---

### Referenzen (Auszüge)

- Pasipatorwa, S. et al. (2022). *CMMS pharmaceutical reliability improvement*
- Macchi, M. & Fumagalli, L. (2013). *Maintenance maturity assessment method*
- Garg, A. & Deshmukh, S.G. (2006). *Maintenance management — literature review*