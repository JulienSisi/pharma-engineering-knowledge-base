# Sezione 1 — Equipment Management & Reliability: Fondamenti strategici per un ambiente CDMO biologics

## 1.1 Contesto: l'affidabilità delle apparecchiature come imperativo operativo CDMO

In un contratto di sviluppo e produzione (CDMO), la disponibilità delle apparecchiature non è una metrica operativa tra le altre — è una condizione contrattuale. Ogni lotto prodotto impegna la reputazione del sito nei confronti di clienti farmaceutici che, a loro volta, hanno obblighi di immissione sul mercato verso regolatori e pazienti.

Questa realtà è particolarmente acuta in un contesto di ramp-up commerciale, dove linee di recente qualificazione passano dal regime di validazione al regime di produzione a pieno regime, con tolleranza zero a derive di disponibilità non anticipate.

## 1.2 Specificità del small equipment in biologics

Il "small equipment" in un contesto CDMO biologics copre una gamma ampia di asset: pompe peristaltiche, filtri di integrità, connessioni di trasferimento, bilance analitiche, apparecchiature di controllo in linea (pH, DO, conduttività), sistemi di campionamento, autoclavi di piccola capacità.

Queste apparecchiature condividono diverse caratteristiche che condizionano la strategia di manutenzione:

```
Alta frequenza di utilizzo        → Usura accelerata, criticità elevata
Contatto diretto con il prodotto  → Impatto immediato sulla qualità del lotto
Rinnovo frequente                 → Gestione intensiva degli spare parts
Moltiplicazione dei riferimenti  → Complessità di gestione dello stock
```

## 1.3 Classificazione per criticità — adattamento al contesto biologics

La matrice di criticità standard (Gravità × Occorrenza × Rilevabilità = RPN) deve essere arricchita per il contesto biologics con parametri specifici:

| Criterio | Descrizione | Ponderazione |
|----------|-------------|--------------|
| Impatto qualità prodotto | Contatto diretto prodotto? CPP coinvolto? | Elevata |
| Impatto contaminazione | Rischio biologico se guasto? | Elevata |
| Disponibilità ridondanza | Apparecchiatura di backup disponibile? | Media |
| Manutenibilità | MTTR stimato se guasto? | Media |
| Tempo di approvvigionamento | Lead time spare parts critici? | Media |

## 1.4 Strategia differenziata: PM / CBM / correttiva residuale

```
┌─────────────────────────────────────────────────────────────┐
│  1. CLASSIFICAZIONE PER CRITICITÀ                           │
│     SIA / CCA / RPN arricchito (maintainability complexity) │
│     → strategia differenziata per asset                     │
├─────────────────────────────────────────────────────────────┤
│  2. FRAMEWORK TPM/RCM CENTRATO SU OEE                       │
│     Attacco delle 6 grandi perdite, TPM autonomo,           │
│     integrazione CBM su asset alta criticità                │
├─────────────────────────────────────────────────────────────┤
│  3. INFRASTRUTTURA DATI E CMMS                              │
│     Sensori esistenti + CMMS/MES come base CBM,             │
│     monitoraggio condizionale prima ML/PdM avanzato         │
├─────────────────────────────────────────────────────────────┤
│  4. INTEGRAZIONE PIANIFICAZIONE PRODUZIONE                  │
│     PM opportunistica, finestre a basso impatto,            │
│     sincronizzazione con scheduling multi-prodotto CDMO     │
└─────────────────────────────────────────────────────────────┘
```

## 1.5 Connessione con l'esperienza Celgene

L'esperienza di gestione della manutenzione per criticità Oracle + shutdown periodico presso Celgene costituisce un ancoraggio diretto in questo quadro di riferimento. Le differenze chiave da integrare per il contesto biologics Visp:

- **Profilo prodotto**: passaggio da small molecules (API chimici) a biologics (proteine, anticorpi, ADC) — le apparecchiature a contatto diretto hanno esigenze diverse di pulibilità CIP/SIP e di integrità di confinamento
- **Complessità del parco**: ambiente CDMO multi-prodotto implica una gestione più complessa dei conflitti di scheduling
- **Ramp-up dinamico**: il parco apparecchiature evolve rapidamente con le nuove linee messe in produzione

---

*→ Sezione 2: SME nei progetti CAPEX — Framework CQV*

---

### Riferimenti (estratti)

- Pasipatorwa, S. et al. (2022). *CMMS pharmaceutical reliability improvement*
- Macchi, M. & Fumagalli, L. (2013). *Maintenance maturity assessment method*
- Garg, A. & Deshmukh, S.G. (2006). *Maintenance management — literature review*