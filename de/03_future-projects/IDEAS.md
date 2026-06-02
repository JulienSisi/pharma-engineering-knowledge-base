# Zukünftige Projekte — AI & Engineering Innovation Roadmap

> Diese Datei ist das lebendige Backlog der Projekte, die ich basierend auf dieser pharmazeutischen Wissensbasis entwickeln möchte.

---

## 🎯 Vision

Ausgehend von der praktischen Erfahrung in der pharmazeutischen GMP-Instandhaltung konkrete Projekte an der Schnittstelle zwischen **Pharma Engineering** und **künstlicher Intelligenz** entwickeln.

---

## 🚀 Prioritätsprojekte

### 1. 🤖 Agent AI Instandhaltung GMP

**Idee:** Ein KI-Agent, der die Rolle eines Instandhaltungskoordinators in GMP-Umgebung simulieren kann. Er verwaltet Arbeitsaufträge, priorisiert Eingriffe nach einer Kritikalitätsmatrix und erstellt KPI-Berichte.

**Anvisierter Stack:**
- Claude API (claude-sonnet-4-20250514)
- LangGraph oder Claude agent loop
- Simulierte Oracle CMMS Daten (JSON)
- React oder Streamlit Interface

**Wert:** Konkrete Demo der KI-Anwendung in realen Pharma-Workflows

**Status:** 📋 Backlog — noch zu starten

---

### 2. 📊 GMP KPI Dashboard Interaktiv

**Idee:** Ein interaktives OEE / MTBF / MTTR Dashboard mit Simulation von Instandhaltungsszenarien. Der Benutzer kann Parameter anpassen (PM-Frequenz, Kritikalität, Budget) und die Auswirkungen auf die KPIs sehen.

**Anvisierter Stack:**
- Python (Pandas, Plotly)
- Streamlit oder React (Recharts)
- Realistische synthetische Daten

**Wert:** Pädagogisches Tool und Portfolio-Demo für Pharma Engineering Profile

**Status:** 📋 Backlog

---

### 3. 🔍 Consensus Research Automation Bot

**Idee:** Automatisierung des akademischen Recherche-Workflows, der für den Aufbau dieses Projekts verwendet wurde. Das Tool nimmt ein Thema (z.B.: "HPAPI containment biologics") und generiert automatisch die Consensus Prompts, sammelt die Ergebnisse und strukturiert einen ersten Abschnittsentwurf.

**Anvisierter Stack:**
- Claude API mit Web Search Tool
- Consensus API (falls verfügbar) oder strukturiertes Scraping
- Output: strukturiertes Markdown

**Wert:** Vervielfachung der Produktionsgeschwindigkeit von qualitativ hochwertigem akademischem Inhalt

**Status:** 📋 Backlog

---

### 4. 📄 GMP SOP Generator

**Idee:** Ein Generator für pharmazeutische SOPs basierend auf einem strukturierten Template. Der Benutzer beschreibt die Aktivität (z.B.: "präventive Inspektion Peristaltikpumpe") und das Tool generiert eine ALCOA-konforme SOP mit den Abschnitten SCOPE, RESPONSIBILITIES, PROCEDURE, REFERENCES.

**Anvisierter Stack:**
- Claude API (structured outputs)
- Einfaches React oder HTML Interface
- Export .docx (via python-docx)

**Wert:** Direkt nützliches Tool in einer Pharma Engineering Rolle

**Status:** 📋 Backlog

---

### 5. 🧠 FMEA Assistant AI

**Idee:** Ein KI-Assistent für die Durchführung von Equipment-FMEAs. Der Benutzer beschreibt ein Gerät und seinen Nutzungskontext, der Assistent generiert wahrscheinliche Ausfallmodi, Effekte, Ursachen und schlägt eine zu überarbeitende RPN-Bewertung vor.

**Anvisierter Stack:**
- Claude API
- React Interface mit interaktiver FMEA-Tabelle
- Excel Export

**Wert:** Konkreter Beschleuniger für Pharma-Instandhaltungsengineering

**Status:** 📋 Backlog

---

### 6. 🏗️ Pharmaceutical Engineering Learning Hub

**Idee:** Diese Wissensbasis in einen echten interaktiven Lernhub umwandeln. Jeder Abschnitt des Mémoires wird zu einem Modul mit Quiz, Karteikarten und praktischen Übungen.

**Anvisierter Stack:**
- React (interaktive App)
- Claude API (für generative Quiz)
- Persistent Storage

**Wert:** Ausbildungsreferenz für Junior-Profile beim Einstieg ins Pharma Engineering

**Status:** 📋 Langfristige Idee

---

## 📚 Ressourcen & Inspirationen

- [Anthropic Claude API docs](https://docs.anthropic.com)
- [Consensus](https://consensus.app) — academic search
- [ISPE](https://ispe.org) — pharmaceutical engineering standards
- [ICH Guidelines](https://www.ich.org) — regulatory framework
- [LangGraph](https://langchain-ai.github.io/langgraph/) — agent orchestration

---

## 📝 Notizen

> *Dieses Repo wird verwendet, egal ob man bei Lonza rekrutiert wird oder nicht. Es ist ein Startplatz für nützliche, reale und innovative Projekte an der Schnittstelle zwischen Pharma Engineering und KI.*

---

*Zuletzt aktualisiert: Juni 2026*