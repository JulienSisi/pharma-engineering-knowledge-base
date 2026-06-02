# Sezione 1 — Quadro normativo GMP: Contesto e Requisiti

## 1.1 Introduzione al contesto normativo

La produzione farmaceutica di principi attivi per uso umano si inserisce in un quadro normativo rigoroso, definito congiuntamente dalla **FDA** (*Food and Drug Administration*, Stati Uniti) e dalle autorità europee e svizzere, tra cui **SwissMedic**. Questi organismi impongono il rispetto delle *current Good Manufacturing Practices* (cGMP), il cui obiettivo centrale è garantire che ogni lotto prodotto sia conforme alle sue specifiche di qualità, identità e purezza.

In questo contesto, la manutenzione delle apparecchiature e delle utilities non è un'attività periferica: costituisce un **pilastro della conformità normativa**. Come sottolineano Tibesso et al. (2024) e Ahmed (2024), le cGMP richiedono che le installazioni e le apparecchiature siano *fit for purpose*, mantenute in modo proattivo e integralmente documentate — la prevenzione dei guasti ha la precedenza sulla loro correzione.

## 1.2 Requisiti normativi applicati alla manutenzione

Il riferimento **21 CFR Part 211** della FDA stabilisce le basi legali della qualifica e della calibrazione delle apparecchiature.

I requisiti fondamentali coprono:

- **21 CFR 211.68** — Sistemi automatici, meccanici ed elettronici: manutenzione e qualifica formale richieste
- **21 CFR 211.182** — Equipment cleaning and maintenance: registrazioni obbligatorie con data, ora, firma
- **21 CFR 211.68(b)** — Validazione dei sistemi informatici (applicabile a Oracle CMMS)

SwissMedic, tramite le Buone Pratiche di Fabbricazione svizzere allineate alle direttive EU-GMP, aggiunge un livello di requisito documentale specifico, in particolare sulla tracciabilità delle calibrazioni e la gestione delle deviazioni.

## 1.3 Qualifica delle apparecchiature: IQ / OQ / PQ

Il ciclo di qualifica IQ/OQ/PQ costituisce il quadro strutturante di ogni apparecchiatura integrata in un ambiente GMP:

```
IQ — Installation Qualification
     ↓ L'apparecchiatura è installata conformemente alle specifiche
OQ — Operational Qualification
     ↓ L'apparecchiatura funziona entro i limiti definiti
PQ — Performance Qualification
     ↓ L'apparecchiatura produce risultati conformi in condizioni reali
```

Secondo Sharma (2020), la manutenzione preventiva deve essere pianificata in coerenza con gli intervalli di riqualifica definiti durante l'OQ/PQ. Uno scostamento non documentato tra il piano di manutenzione e i requisiti di qualifica costituisce una potenziale non conformità normativa.

## 1.4 Calibrazione e metrologia in ambiente regolamentato

La calibrazione degli strumenti di misura e controllo è un requisito diretto del 21 CFR Part 211.68. In un contesto multi-dipartimentale (Utilities, Process, Calibration), la gestione centralizzata degli intervalli di calibrazione tramite Oracle CMMS permette:

- La generazione automatica degli ordini di lavoro (WO) di calibrazione
- Il monitoraggio dei certificati di calibrazione con collegamento agli strumenti interessati
- La rilevazione precoce degli strumenti fuori tolleranza prima che impattino la produzione

## 1.5 Sintesi: la manutenzione come funzione normativa

Il posizionamento della manutenzione come funzione normativa — e non semplicemente tecnica — è la chiave di volta dell'approccio documentato in questa tesi. In un ambiente sotto doppia sorveglianza FDA/SwissMedic, ogni attività di manutenzione genera una prova documentale che può essere esaminata durante un audit o un'ispezione.

> **Implicazione pratica**: La qualità della documentazione di manutenzione è direttamente correlata alla capacità del sito di difendere le proprie pratiche davanti ai regolatori.

---

*→ Sezione 2: Strategia di manutenzione & ERP Oracle*

---

### Riferimenti (estratti)

- Ahmed, A. (2024). *GMP compliance in pharmaceutical maintenance management*
- Tibesso, G. et al. (2024). *Preventive maintenance in FDA-regulated environments*
- Sharma, R. (2020). *Equipment qualification lifecycle pharmaceutical industry*
- FDA. *21 CFR Part 211 — Current Good Manufacturing Practice for Finished Pharmaceuticals*