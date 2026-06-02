# Sezione 3 — Pilotaggio tramite KPI e Dashboard

## 3.1 I KPI come linguaggio comune

In un ambiente farmaceutico multi-dipartimentale, gli indicatori di performance svolgono un ruolo che va oltre la semplice misurazione: costituiscono un **linguaggio comune** tra manutenzione, produzione, qualità e management. Un KPI ben definito traduce una realtà operativa complessa in un dato decisionale azionabile.

La progettazione del dashboard di manutenzione deve rispondere a tre livelli di lettura:

```
Livello strategico    →  Tendenze lungo termine, benchmarking, budget
Livello tattico       →  Pianificazione settimanale, tasso di rispetto della pianificazione
Livello operativo     →  WO aperti/chiusi, guasti in corso, urgenze
```

## 3.2 OEE — Overall Equipment Effectiveness

L'OEE è l'indicatore di riferimento della performance degli equipaggiamenti. Si decompone in tre fattori moltiplicativi:

```
OEE = Disponibilità × Performance × Qualità

Disponibilità  = Tempo di funzionamento reale / Tempo disponibile pianificato
Performance    = Produzione reale / Produzione teorica
Qualità        = Lotti conformi / Lotti totali prodotti
```

Un OEE world-class è generalmente situato attorno all'85%. In ambiente farmaceutico GMP, i vincoli normativi (fermate per pulizia, calibrazione, qualificazioni) possono giustificare target adeguati secondo il tipo di equipaggiamento.

## 3.3 MTBF / MTTR — Affidabilità e manutenibilità

| Indicatore | Formula | Interpretazione |
|-----------|---------|----------------|
| MTBF | Tempo totale di funzionamento / Numero di guasti | Più è elevato, più l'equipaggiamento è affidabile |
| MTTR | Tempo totale di riparazione / Numero di guasti | Più è basso, più la manutenzione è efficace |
| Disponibilità | MTBF / (MTBF + MTTR) | Sintesi affidabilità + manutenibilità |

Il monitoraggio MTBF/MTTR per equipaggiamento in Oracle CMMS permette di identificare gli asset cronicamente difettosi e di giustificare una riclassificazione della loro strategia di manutenzione (passaggio da preventivo periodico a condizionale, o sostituzione).

## 3.4 KPI budgetari

La gestione di un budget di ~1.5M CHF richiede un monitoraggio mensile strutturato:

- **Tasso di realizzazione del piano di manutenzione preventiva** (target: >95%)
- **Rapporto manutenzione correttiva / preventiva** (target: <20% correttivo)
- **Costo di manutenzione per asset** (identificazione degli equipaggiamenti più costosi)
- **Tasso di servizio spare parts** (disponibilità dei pezzi durante gli interventi)
- **Scostamento budget vs realizzato** per linea di costo

## 3.5 Architettura del dashboard Oracle

```
┌─────────────────────────────────────────────────────────┐
│              DASHBOARD MANUTENZIONE MENSILE             │
├──────────────┬──────────────┬──────────────┬────────────┤
│ DISPONIBILITÀ│    OEE       │  BUDGET      │  WO        │
│   98.2%      │   84.7%      │  CHF 127K/M  │  142 aperti│
│   ▲ +0.3%    │   ▲ +1.2%   │  ▼ -3% vs P  │  ▼ -8 vs M-1│
├──────────────┼──────────────┼──────────────┼────────────┤
│ MTBF         │  MTTR        │ PM Compliance│ CAPA aperti│
│  847 h       │   2.3 h      │   97.4%      │    4       │
└──────────────┴──────────────┴──────────────┴────────────┘
```

## 3.6 Collegamento KPI → Decisione → Azione

Il valore dei KPI risiede nella loro capacità di innescare azioni. Un dashboard che misura senza generare decisioni è uno strumento costoso senza ROI. Il circolo virtuoso:

```
Misurazione KPI → Analisi tendenza → Identificazione scostamento → 
Decisione correttiva → Implementazione → Verifica impatto → 
Aggiornamento KPI → ...
```

Questo circolo si articola direttamente con il ciclo CAPA documentato nella Sezione 6.

---

*→ Sezione 4: Coordinamento interdipartimentale*

---

### Riferimenti (estratti)

- Dal et al. (2000). *OEE definition and application*
- Nakajima, S. (1988). *TPM — Total Productive Maintenance*
- Muchiri, P. & Pintelon, L. (2008). *Performance measurement using OEE*