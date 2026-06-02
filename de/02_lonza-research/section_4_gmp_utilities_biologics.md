# Abschnitt 4 — GMP Utilities Biologics : CIP/SIP, WFI & Clean Steam

## 4.1 Die Biologics-Utilities: kritische Infrastruktur des Verfahrens

Im Manufacturing von Biologics sind Utilities nicht einfach nur Versorgungsflüssigkeiten — sie sind **Prozesseingangsstoffe**, deren Qualität direkt die Konformität des Produkts bedingt. Diese Realität unterscheidet grundlegend den Biologics-Kontext vom Kontext der small molecule API.

### Hierarchie der kritischen Utilities

```
WFI (Water for Injection)          → Direkter Produktkontakt / Reinigung
Pure Steam / Clean Steam           → Sterilisation, SIP
Purified Water                     → Lösungsvorbereitung, Reinigung
Druckluft pharma grade             → Betätigung, Trocknung, Druckbeaufschlagung
Inertgase (N2, CO2)                → Begasung, Druckbeaufschlagung Bioreaktoren
HVAC - Luftklassifizierung         → Reinraumum gebung
```

## 4.2 WFI — Water for Injection

WFI wird durch Destillation (traditionelle Methode) oder durch Umkehrosmose + CEDI (aufkommende Methode, seit 2017 von der EMA akzeptiert) produziert. Seine Wartungsanforderungen gehören zu den kritischsten des Standorts:

- **Kontinuierliche Qualitätsüberwachung**: Leitfähigkeit, TOC, Endotoxine, Bioburden
- **Verteilungskreisläufe**: Aufrechterhaltung der Temperatur (80°C im Hot Loop) oder der turbulenten Strömungsgeschwindigkeit zur Vermeidung von Biofilmbildung
- **Qualifikation des Kreislaufs**: vollständige Validierung des Verteilungssystems einschließlich der Nutzungspunkte

Die Verschlechterung eines WFI-Kreislaufs manifestiert sich schleichend durch einen progressiven Anstieg des Bioburdens — ohne deutlichen Alarm. Die präventive Wartung (Inspektionen, programmierte Sanitisationen) ist der einzige Hebel zur Verhinderung einer Nichtkonformität.

## 4.3 CIP/SIP — Cleaning & Sterilization In Place

Die CIP- (Reinigung) und SIP-Systeme (Dampfsterilisation) sind die Hüter der biologischen Integrität der Ausrüstung zwischen den Chargen.

**Kritische CIP/SIP-Wartung:**
- Überprüfung der Sprühdüsen (Verstopfung → unzureichende Reinigungsabdeckung)
- Integrität der Kreisläufe (Dichtungen, Ventile → Leckagen → reduzierte Wirksamkeit)
- Validierung der Zyklusparameter (Temperatur, Konzentration, Kontaktzeit)
- Aufzeichnung jedes Zyklus im Rezeptverwaltungssystem

Die geringste unentdeckte Störung kann die Integrität einer ganzen Charge kompromittieren — mit erheblichen regulatorischen und wirtschaftlichen Konsequenzen.

## 4.4 Übergang vom Celgene-Kontext

Bei Celgene fügten sich die verwalteten Utilities (Druckluft, gereinigtes Wasser, Basis-HVAC) in einen Small-Molecule-Kontext ein. Das zu beherrschende Delta für den Visp Biologics-Kontext betrifft:

- Die biologische Kritikalität des WFI und der Verteilungskreisläufe
- Die automatisierten CIP/SIP-Systeme und deren Qualifikation
- Das Management von sterilem Dampf (Dampfreinheit, Validierungen)
- Die Integration Utilities / Bioreaktoren (Feeds, Harvest)

---

*→ Abschnitt 5: HPAPI Containment Engineering*

---

### Referenzen (Auszüge)

- Parenteral Drug Association (PDA). *Technical Report on Water for Injection*
- EMA. *Guideline on WFI production by non-distillation methods*
- ISPE. *Baseline Guide Vol. 4 — Water and Steam Systems*