# Sezione 4 — Coordinamento interdisciplinare: Utilities, Process & Calibration

## 4.1 Il coordinamento come competenza centrale

In un ambiente farmaceutico GMP, la manutenzione non è mai un'attività isolata. Si inserisce in una rete di dipendenze funzionali che coinvolge come minimo tre dipartimenti operativi:

- **Utilities**: produzione e distribuzione dei fluidi di processo (aria compressa, acqua purificata, vapore, HVAC)
- **Process**: produzione degli APIs, con i suoi vincoli di schedulazione dei lotti
- **Calibration**: mantenimento della metrologia e degli strumenti di misura conformi

Il coordinamento tra queste tre funzioni — spesso con obiettivi parzialmente divergenti — è una competenza organizzativa critica che i modelli di performance della manutenzione riconoscono come determinante per l'efficacia globale del sito.

## 4.2 Modello TPM e coinvolgimento trasversale

Il Total Productive Maintenance (TPM) — sviluppato da Nakajima (1988) e formalizzato dal Japan Institute of Plant Maintenance — è il quadro di riferimento per una manutenzione integrata nell'organizzazione di produzione. I suoi otto pilastri includono esplicitamente la **manutenzione autonoma** (coinvolgimento degli operatori) e la **manutenzione pianificata** (coordinamento tra manutenzione e produzione).

```
Gli 8 pilastri TPM:
1. Manutenzione autonoma (operatori)
2. Manutenzione pianificata (manutenzione)
3. Miglioramento caso per caso (Kaizen)
4. Formazione & sviluppo delle competenze
5. Controllo iniziale (nuove attrezzature/prodotti)
6. Manutenzione della qualità (collegamenti processo-attrezzature)
7. Sicurezza, salute, ambiente
8. TPM negli uffici (funzioni di supporto)
```

In ambiente farmaceutico GMP, i pilastri 2, 6 e 7 sono particolarmente critici: la manutenzione pianificata si integra nelle finestre di produzione, la manutenzione qualità sorveglia i CPPs, e la sicurezza integra i requisiti HPAPI/GMP.

## 4.3 Scheduling e gestione dei conflitti di risorse

La pianificazione degli interventi di manutenzione in un ambiente multi-dipartimento genera conflitti di risorse ricorrenti:

| Conflitto tipo | Parti coinvolte | Arbitraggio |
|-------------|-------------------|-----------|
| Arresto utility durante produzione | Utilities vs Process | Pianificazione anticipata, slot validati |
| Calibrazione strumento in servizio | Calibration vs Process | Strumento di sostituzione, termine negoziato |
| Shutdown preventivo vs lotto in corso | Manutenzione vs Process | Finestre shutdown integrate nella pianificazione produzione |
| Risorse tecnici condivise | Manutenzione vs Calibration | Matrice di priorità, escalation manager |

La risoluzione di questi conflitti necessita di un **meccanismo di riunione strutturato** (daily/weekly meeting manutenzione-produzione) e di **regole di escalation** chiare documentate nelle SOPs.

## 4.4 Oracle come piattaforma di coordinamento

Oracle CMMS svolge un ruolo di **piattaforma di coordinamento** oltre al suo utilizzo CMMS puro:

- I WOs generati sono visibili da tutti i dipartimenti interessati
- Gli stati (pianificato, in corso, terminato) sono aggiornati in tempo reale
- Gli storici di intervento per attrezzatura sono consultabili da Process e Calibration
- Le notifiche automatiche informano le parti interessate degli interventi pianificati

Questa trasparenza condivisa riduce gli attriti inter-dipartimentali e rafforza la fiducia reciproca tra le squadre.

## 4.5 Comunicazione formale e informale

Il coordinamento efficace si basa su due canali complementari:

**Formale:** riunioni settimanali manutenzione/produzione, report mensili KPIs, registrazioni Oracle, SOPs di coordinamento
**Informale:** presenza sul campo, disponibilità, reattività alle richieste urgenti, fiducia costruita nel tempo

Modgil & Sharma (2016) sottolineano che **"Total Productive Maintenance and Total Quality Management together have a significant positive impact on operational performance"** — una convergenza che è possibile solo se le due funzioni condividono indicatori comuni e un linguaggio di coordinamento stabilito.

---

*→ Sezione 5: Contesto prodotti*

---

### Riferimenti (estratti)

- Nakajima, S. (1988). *Introduction to TPM*
- Modgil, S. & Sharma, S. (2016). *TPM and TQM — meta-analysis*
- Ahuja, I.P.S. & Khamba, J.S. (2008). *Total productive maintenance — literature review*