# Sezione 2 — Strategia di manutenzione & ERP Oracle

## 2.1 Dal reattivo al preventivo: evoluzione paradigmatica

La manutenzione farmaceutica ha conosciuto una trasformazione profonda nel corso degli ultimi due decenni, passando da una logica puramente correttiva (intervenire dopo il guasto) a una logica preventiva strutturata, poi verso approcci predittivi. In un ambiente GMP, questa evoluzione non è opzionale: un guasto non anticipato su un'apparecchiatura critica può scatenare una deviazione normativa, compromettere un lotto di produzione, o addirittura richiedere una riqualificazione.

La strategia di manutenzione documentata in questo documento si basa su tre pilastri:

```
┌────────────────────────────────────────────────────────┐
│  1. CLASSIFICAZIONE PER CRITICITÀ                      │
│     Matrice RPN (Risk Priority Number)                 │
│     → strategia differenziata per asset                │
├────────────────────────────────────────────────────────┤
│  2. PIANIFICAZIONE Oracle CMMS                         │
│     WOs preventivi auto-generati, tracking storico     │
│     → visibilità totale sullo stato del parco          │
├────────────────────────────────────────────────────────┤
│  3. GESTIONE DEI SHUTDOWNS & SPARE PARTS               │
│     Anticipazione delle fermate periodiche             │
│     → budget ~1.5M CHF, magazzino integrato Oracle     │
└────────────────────────────────────────────────────────┘
```

## 2.2 Matrice di criticità e classificazione degli asset

La classificazione delle apparecchiature per criticità è il prerequisito per qualsiasi strategia di manutenzione differenziata. In ambiente GMP farmaceutico, questa classificazione integra due dimensioni:

- **Impatto qualità/normativo**: l'apparecchiatura entra in contatto diretto con il prodotto? Condiziona un parametro critico del processo (CPP)?
- **Impatto disponibilità**: il suo guasto provoca la fermata della linea? Esiste una ridondanza?

Il metodo FMEA (Failure Mode and Effects Analysis), arricchito dal calcolo del RPN (Risk Priority Number = Severità × Occorrenza × Rilevabilità), permette di dare priorità alle risorse di manutenzione sugli asset a rischio più elevato.

## 2.3 Oracle CMMS: architettura e flussi di dati

Il sistema Oracle EAM (Enterprise Asset Management) costituisce il sistema nervoso centrale della funzione manutenzione. La sua architettura in ambiente farmaceutico copre:

**Gestione degli asset:**
- Struttura ad albero delle apparecchiature (sito → linea → apparecchiatura → sotto-insieme)
- Schede tecniche e storico degli interventi
- Documenti di qualificazione collegati a ogni asset

**Pianificazione della manutenzione:**
- Generazione automatica degli Ordini di Lavoro (WO) preventivi
- Gestione delle priorità e delle risorse tecniche
- Monitoraggio dei tempi di intervento reali vs pianificati

**Gestione delle spare parts:**
- Stock minimo per riferimento critico
- Collegamenti fornitori e tempi di approvvigionamento
- Valorizzazione degli stock per reporting budgetario

L'architettura ISA-95 definisce i livelli di integrazione tra Oracle EAM (livello 4 — ERP) e i sistemi di controllo di produzione (livello 3 — MES/SCADA), permettendo la risalita automatica degli allarmi apparecchiature verso il sistema di gestione dei WOs.

## 2.4 Strategia spare parts per gli shutdowns periodici

La pianificazione degli shutdowns periodici costituisce un esercizio di gestione multi-vincoli: vincoli normativi (finestre di riqualificazione), vincoli di produzione (minimizzare l'impatto sui lotti), vincoli di stock (evitare la sovra-immobilizzazione di capitale).

L'approccio applicato si articola intorno a:

1. **Identificazione dei pezzi critici** tramite analisi di criticità FMEA + storico Oracle
2. **Calcolo dello stock di sicurezza** basato sui tempi di consegna fornitori e la frequenza degli shutdowns
3. **Costituzione dei kit shutdown** raggruppando i pezzi per apparecchiatura/linea
4. **Supervisione del magazziniere** per la ricezione, lo stoccaggio conforme GMP e la tracciabilità

## 2.5 Budgetizzazione e reporting

La gestione di un budget manutenzione di ~1.5M CHF implica un reporting strutturato che permette di distinguere:

- **OPEX manutenzione**: pezzi di ricambio, contratti di manutenzione esternalizzati, risorse interne
- **CAPEX manutenzione**: sostituzione di apparecchiature maggiori, upgrade
- **Costi di guasto**: riparazioni non pianificate, impatto sulla produzione

Il cruscotto Oracle permette l'estrazione mensile dei KPIs budgetari e il loro confronto con gli impegni iniziali.

---

*→ Sezione 3: Pilotaggio tramite KPIs & Cruscotto*

---

### Riferimenti (estratti)

- Pasipatorwa, S. et al. (2022). *CMMS implementation and maintenance performance improvement*
- Pintelon, L. & Parodi-Herz, A. (2008). *Maintenance: An evolutionary perspective*
- ISA-95. *Enterprise-Control System Integration standard*