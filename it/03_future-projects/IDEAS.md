# Future Projects — AI & Engineering Innovation Roadmap

> Questo file è il backlog vivente dei progetti che intendo sviluppare a partire da questa base di conoscenze farmaceutiche.

---

## 🎯 Visione

Partire dall'esperienza sul campo nella manutenzione farmaceutica GMP per costruire progetti concreti all'intersezione tra **engineering pharma** e **intelligenza artificiale**.

---

## 🚀 Progetti prioritari

### 1. 🤖 Agent AI Maintenance GMP

**Idea:** Un agente IA capace di simulare il ruolo di un coordinatore manutenzione in ambiente GMP. Gestisce ordini di lavoro, priorizza gli interventi secondo una matrice di criticità, e genera report KPI.

**Stack previsto:**
- Claude API (claude-sonnet-4-20250514)
- LangGraph o Claude agent loop
- Dati simulati Oracle CMMS (JSON)
- Interface React o Streamlit

**Valore:** Demo concreta dell'applicazione dell'IA a workflow pharma reali

**Stato:** 📋 Backlog — da avviare

---

### 2. 📊 GMP KPI Dashboard Interattivo

**Idea:** Un dashboard OEE / MTBF / MTTR interattivo con simulazione di scenari di manutenzione. L'utente può regolare parametri (frequenza PM, criticità, budget) e vedere l'impatto sui KPI.

**Stack previsto:**
- Python (Pandas, Plotly)
- Streamlit o React (Recharts)
- Dati sintetici realistici

**Valore:** Strumento pedagogico e demo portfolio per profili engineering pharma

**Stato:** 📋 Backlog

---

### 3. 🔍 Consensus Research Automation Bot

**Idea:** Automatizzare il workflow di ricerca accademica utilizzato per costruire questo progetto. Lo strumento prende un tema (es: "HPAPI containment biologics") e genera automaticamente i prompt Consensus, raccoglie i risultati, e struttura una prima bozza di sezione.

**Stack previsto:**
- Claude API con web search tool
- Consensus API (se disponibile) o scraping strutturato
- Output: markdown strutturato

**Valore:** Moltiplicare la velocità di produzione di contenuto accademico di qualità

**Stato:** 📋 Backlog

---

### 4. 📄 GMP SOP Generator

**Idea:** Un generatore di SOP farmaceutiche a partire da un template strutturato. L'utente descrive l'attività (es: "ispezione preventiva pompa peristaltica") e lo strumento genera una SOP conforme ALCOA con sezioni SCOPE, RESPONSIBILITIES, PROCEDURE, REFERENCES.

**Stack previsto:**
- Claude API (structured outputs)
- Interface semplice React o HTML
- Export .docx (via python-docx)

**Valore:** Strumento direttamente utile in un ruolo engineering pharma

**Stato:** 📋 Backlog

---

### 5. 🧠 FMEA Assistant AI

**Idea:** Un assistente IA per la realizzazione di FMEA attrezzature. L'utente descrive un'attrezzatura e il suo contesto d'uso, l'assistente genera i modi di guasto probabili, gli effetti, le cause, e propone una valutazione RPN iniziale da rivedere.

**Stack previsto:**
- Claude API
- Interface React con tabella FMEA interattiva
- Export Excel

**Valore:** Acceleratore concreto per l'engineering di manutenzione pharma

**Stato:** 📋 Backlog

---

### 6. 🏗️ Pharmaceutical Engineering Learning Hub

**Idea:** Trasformare questa knowledge base in un vero hub di apprendimento interattivo. Ogni sezione della tesi diventa un modulo con quiz, flashcard, ed esercizi pratici.

**Stack previsto:**
- React (app interattiva)
- Claude API (per i quiz generativi)
- Persistent storage

**Valore:** Riferimento di formazione per profili junior che entrano nel pharma engineering

**Stato:** 📋 Idea a lungo termine

---

## 📚 Risorse & ispirazioni

- [Anthropic Claude API docs](https://docs.anthropic.com)
- [Consensus](https://consensus.app) — academic search
- [ISPE](https://ispe.org) — pharmaceutical engineering standards
- [ICH Guidelines](https://www.ich.org) — regulatory framework
- [LangGraph](https://langchain-ai.github.io/langgraph/) — agent orchestration

---

## 📝 Note

> *Questo repo sarà utilizzato che si venga assunti da Lonza o meno. È un launchpad per progetti utili, reali e innovativi all'intersezione tra pharma engineering e IA.*

---

*Ultimo aggiornamento: Giugno 2026*