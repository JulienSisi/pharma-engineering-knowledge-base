# Sezione 2 — SME nei progetti CAPEX: Framework CQV in ambiente biologics

## 2.1 Il ruolo SME nel ciclo di vita delle attrezzature CAPEX

Il Subject Matter Expert (SME) attrezzature in un progetto CAPEX non è un osservatore tecnico — è l'interfaccia critica tra i team di engineering del progetto, la produzione, la qualità e i fornitori. Il suo intervento copre l'interezza del ciclo CQV:

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

Il documento URS è il punto di partenza di ogni qualifica. Trasforma i bisogni di processo in requisiti tecnici formali:

- **Requisiti funzionali**: capacità, range di utilizzo, precisione
- **Requisiti GMP**: materiali a contatto con il prodotto, pulibilità CIP/SIP, DQ/IQ/OQ/PQ richiesti
- **Requisiti SHE**: confinamento HPAPI, sicurezza operatore
- **Requisiti utilities**: alimentazione elettrica, fluidi, HVAC
- **Requisiti documentazione**: data integrity, audit trail, 21 CFR Part 11

## 2.3 FAT / SAT — Factory & Site Acceptance Tests

Il FAT (Factory Acceptance Test) e il SAT (Site Acceptance Test) sono fasi critiche che il SME co-pilota con il fornitore:

| Test | Luogo | Obiettivo | SME Role |
|------|-------|----------|----------|
| DQ | Ufficio/Fornitore | Verificare che il design risponda all'URS | Review documentazione |
| FAT | Stabilimento fornitore | Verificare l'attrezzatura prima della spedizione | Supervisionare test funzionali |
| SAT | Sito Visp | Verificare dopo l'installazione | Co-firmare i risultati |
| IQ | Sito Visp | Installazione conforme alle specifiche | Autore o reviewer protocollo |
| OQ | Sito Visp | Funzionamento nei limiti | Autore o reviewer protocollo |
| PQ | Sito Visp | Performance in condizioni reali | Autore o reviewer protocollo |

## 2.4 C&Q — Commissioning & Qualification

Il framework ISPE GAMP definisce il confine tra commissioning (verifica funzionale ingegneristica) e qualifica (prova GMP formale). In pratica, il buon engineering in fase commissioning è la condizione di una qualifica efficace e senza sorprese.

La letteratura (Calnan et al., 2017) sottolinea che le carenze nelle fasi early del progetto (URS incompleto, FAT insufficiente) si manifestano sistematicamente come deviazioni e ritardi in fase OQ/PQ — un costo nascosto maggiore nei progetti CAPEX biologics.

## 2.5 Connessione Celgene → Visp

L'esperienza di manutenzione in ambiente FDA/SwissMedic presso Celgene — in particolare la familiarità con i cicli IQ/OQ/PQ, la gestione delle deviazioni di qualifica, e il coordinamento con i team Validation — costituisce una base direttamente trasferibile. Il delta da colmare è la padronanza del contesto biologics (vincoli specifici bioreattori, sistemi CIP/SIP, WFI) e del ruolo attivo SME CAPEX vs. il ruolo di supporto manutenzione.

---

*→ Sezione 3: Troubleshooting & CAPA in biologics*

---

### Riferimenti (estratti)

- Calnan, N. et al. (2017). *Commissioning and qualification pharmaceutical biologics*
- ISPE. *GAMP 5 — A Risk-Based Approach to Compliant GxP Computerized Systems*
- ICH Q8/Q9/Q10. *Pharmaceutical development, quality risk management, quality system*