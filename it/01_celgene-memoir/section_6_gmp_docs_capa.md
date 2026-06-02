# Sezione 6 — Documentazione GMP & Ciclo CAPA

## 6.1 La documentazione come prova di controllo

In ambiente GMP, la regola fondamentale è semplice e assoluta: **"If it's not documented, it didn't happen."** Questa massima non è un cliché burocratico — riflette la logica regolatoria secondo la quale la prova di un'attività è indissociabile dall'attività stessa.

Per la manutenzione, questo significa che ogni intervento, ogni calibrazione, ogni deviazione rilevata deve generare una traccia formale, datata, firmata, e integrata in un sistema documentario coerente.

## 6.2 Architettura documentaria

```
SOPs (Standard Operating Procedures)
  ↓ "Cosa fare e come"
  
WPs (Work Procedures / Instructions)
  ↓ "Fasi dettagliate di esecuzione"
  
FORMs (Formulari di registrazione)
  ↓ "Prova che è stato fatto"
  
MDS (Maintenance Data Sheets)
  ↓ "Dati tecnici di riferimento per attrezzatura"
```

Questa gerarchia documentaria assicura la coerenza tra i requisiti regolatori (SOPs), le pratiche sul campo (WPs), e le prove di esecuzione (FORMs). La redazione, la revisione e l'aggiornamento di questi documenti costituiscono una parte significativa del lavoro di coordinamento della manutenzione.

## 6.3 Principi ALCOA & integrità dei dati

I principi **ALCOA** (Attributable, Legible, Contemporaneous, Original, Accurate) definiscono le caratteristiche di un dato GMP valido:

| Principio | Definizione | Applicazione manutenzione |
|---------|-----------|------------------------|
| **A**ttributable | Identificabile al suo autore | Firma obbligatoria su ogni registrazione |
| **L**egible | Leggibile e comprensibile | No cancellature, correzione con sigla |
| **C**ontemporaneous | Registrato al momento dell'azione | No registrazione retroattiva non giustificata |
| **O**riginal | Dati primari conservati | No trascrizione senza riferimento all'originale |
| **A**ccurate | Corretto e completo | Valori reali, no arrotondamenti non giustificati |

In Oracle CMMS, le registrazioni dei WOs di manutenzione sono datate automaticamente e collegate all'utente connesso, assicurando naturalmente i principi A, C e parzialmente L.

## 6.4 Ciclo di vita documentario

```
Redazione (autore) → Revisione (peer) → Approvazione (manager/QA) 
→ Formazione del personale → Messa in applicazione 
→ Revisione periodica → Aggiornamento se necessario → Archiviazione
```

## 6.5 Gestione delle deviazioni

Una **deviazione** è qualsiasi scostamento rispetto a una procedura approvata o a una specifica definita. Nella manutenzione, le deviazioni possono essere:

- **Deviazioni attrezzatura**: risultato di calibrazione fuori limite, guasto non pianificato su attrezzatura qualificata
- **Deviazioni procedurali**: intervento realizzato senza WO approvato, SOP non rispettata
- **Deviazioni documentarie**: dati mancanti, firme incorrette

La gestione di una deviazione segue un flusso strutturato:
```
Rilevazione → Notifica immediata → Containment (isolare l'impatto)
→ Valutazione iniziale (impatto qualità?) → Apertura deviazione formale
→ Investigazione RCA → Piano CAPA → Approvazione QA → Chiusura
```

## 6.6 Analisi di Causa Radice (RCA)

Gli strumenti di RCA utilizzati in ambiente GMP farmaceutico:

**5 Whys** — Metodo semplice ed efficace per i guasti diretti:
```
Guasto pompa → Perché? Cuscinetto usurato
→ Perché? Lubrificazione insufficiente
→ Perché? Frequenza PM inadeguata
→ Perché? Criticità sottovalutata alla messa in servizio
→ Perché? Procedura di classificazione non rivista dall'installazione
→ CAUSA RADICE: procedura di classificazione delle criticità obsoleta
```

**Diagramma Ishikawa (5M)** — Per i guasti complessi multi-fattoriali:
- **M**ano d'opera (competenze, formazione)
- **M**etodo (SOP, procedura seguita?)
- **M**acchina (stato attrezzatura, storico guasti)
- **M**ateriale (ricambi, qualità dei consumabili)
- **M**ezzo ambiente (ambiente, temperatura, vibrazioni)

**FMEA** — Per l'analisi preventiva sistematica (vedere Sezione 2)

## 6.7 CAPA basato sui trend

Oltre al trattamento delle deviazioni individuali, il monitoraggio dei **trend** permette di identificare i problemi sistemici prima che generino una deviazione maggiore:

- Monitoraggio mensile del numero e tipo di deviazioni per linea / attrezzatura
- Analisi delle ricorrenze (stessa attrezzatura, stessa causa)
- Revisione trimestrale CAPA con il dipartimento Qualità

## 6.8 CAPA & Change Control

Qualsiasi azione correttiva o preventiva che modifichi un'attrezzatura qualificata, una SOP approvata, o un parametro di processo deve passare attraverso il processo di **Change Control** (gestione del cambiamento):

```
Proposta di cambiamento → Valutazione dell'impatto (qualifica richiesta?)
→ Approvazione multi-disciplinare (Engineering + Quality + Process)
→ Implementazione controllata → Verifica di efficacia → Chiusura
```

## 6.9 Lean Six Sigma & miglioramento continuo

L'integrazione degli strumenti Lean Six Sigma nell'approccio di miglioramento continuo della manutenzione farmaceutica è documentata da Da Silva et al. (2023):

- **DMAIC** (Define, Measure, Analyze, Improve, Control) per i progetti di miglioramento strutturati
- **5S** per l'organizzazione delle officine e magazzini manutenzione
- **Kaizen** per i miglioramenti incrementali del quotidiano

La principale tensione identificata nella letteratura è la **paura delle riqualificazioni** legate ai cambiamenti di processo — che può frenare il miglioramento continuo in ambienti molto conservatori dal punto di vista regolatorio.

---

*→ Sezione 7: Conclusione & Prospettive Industry 4.0*

---

### Riferimenti (estratti)

- Da Silva, A. et al. (2023). *Lean Six Sigma pharmaceutical GMP continuous improvement*
- ICH Q10. *Pharmaceutical Quality System*
- FDA. *Guidance for Industry — Investigating Out-of-Specification (OOS) Test Results*
- EMA. *Guideline on good pharmacovigilance practices — CAPA*