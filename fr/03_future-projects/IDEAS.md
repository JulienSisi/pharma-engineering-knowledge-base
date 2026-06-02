# Future Projects — AI & Engineering Innovation Roadmap

> Ce fichier est le backlog vivant des projets que je compte développer à partir de cette base de connaissances pharmaceutique.

---

## 🎯 Vision

Partir de l'expérience terrain en maintenance pharmaceutique GMP pour construire des projets concrets à l'intersection de **l'engineering pharma** et de **l'intelligence artificielle**.

---

## 🚀 Projets prioritaires

### 1. 🤖 Agent AI Maintenance GMP

**Idée :** Un agent IA capable de simuler le rôle d'un coordinateur maintenance en environnement GMP. Il gère des ordres de travail, priorise les interventions selon une matrice de criticité, et génère des rapports KPIs.

**Stack envisagée :**
- Claude API (claude-sonnet-4-20250514)
- LangGraph ou Claude agent loop
- Données simulées Oracle CMMS (JSON)
- Interface React ou Streamlit

**Valeur :** Démo concrète de l'application de l'IA à des workflows pharma réels

**Statut :** 📋 Backlog — à démarrer

---

### 2. 📊 GMP KPI Dashboard Interactif

**Idée :** Un dashboard OEE / MTBF / MTTR interactif avec simulation de scénarios de maintenance. L'utilisateur peut ajuster des paramètres (fréquence PM, criticité, budget) et voir l'impact sur les KPIs.

**Stack envisagée :**
- Python (Pandas, Plotly)
- Streamlit ou React (Recharts)
- Données synthétiques réalistes

**Valeur :** Outil pédagogique et démo portfolio pour profils engineering pharma

**Statut :** 📋 Backlog

---

### 3. 🔍 Consensus Research Automation Bot

**Idée :** Automatiser le workflow de recherche académique utilisé pour construire ce projet. L'outil prend un thème (ex : "HPAPI containment biologics") et génère automatiquement les prompts Consensus, collecte les résultats, et structure une première ébauche de section.

**Stack envisagée :**
- Claude API avec web search tool
- Consensus API (si disponible) ou scraping structuré
- Output : markdown structuré

**Valeur :** Multiplier la vitesse de production de contenu académique de qualité

**Statut :** 📋 Backlog

---

### 4. 📄 GMP SOP Generator

**Idée :** Un générateur de SOPs pharmaceutiques à partir d'un template structuré. L'utilisateur décrit l'activité (ex : "inspection préventive pompe peristaltique") et l'outil génère une SOP conforme ALCOA avec sections SCOPE, RESPONSIBILITIES, PROCEDURE, REFERENCES.

**Stack envisagée :**
- Claude API (structured outputs)
- Interface simple React ou HTML
- Export .docx (via python-docx)

**Valeur :** Outil directement utile dans un rôle engineering pharma

**Statut :** 📋 Backlog

---

### 5. 🧠 FMEA Assistant AI

**Idée :** Un assistant IA pour la réalisation de FMEAs équipements. L'utilisateur décrit un équipement et son contexte d'utilisation, l'assistant génère les modes de défaillance probables, les effets, les causes, et propose une cotation RPN initiale à réviser.

**Stack envisagée :**
- Claude API
- Interface React avec tableau FMEA interactif
- Export Excel

**Valeur :** Accélérateur concret pour l'engineering de maintenance pharma

**Statut :** 📋 Backlog

---

### 6. 🏗️ Pharmaceutical Engineering Learning Hub

**Idée :** Transformer ce knowledge base en un vrai hub d'apprentissage interactif. Chaque section du mémoire devient un module avec quiz, flashcards, et exercices pratiques.

**Stack envisagée :**
- React (app interactive)
- Claude API (pour les quiz génératifs)
- Persistent storage

**Valeur :** Référence de formation pour profils junior entrant en pharma engineering

**Statut :** 📋 Idée long terme

---

## 📚 Ressources & inspirations

- [Anthropic Claude API docs](https://docs.anthropic.com)
- [Consensus](https://consensus.app) — academic search
- [ISPE](https://ispe.org) — pharmaceutical engineering standards
- [ICH Guidelines](https://www.ich.org) — regulatory framework
- [LangGraph](https://langchain-ai.github.io/langgraph/) — agent orchestration

---

## 📝 Notes

> *Ce repo sera utilisé qu'on soit recruté chez Lonza ou pas. C'est un launchpad pour des projets utiles, réels, et innovants à l'intersection du pharma engineering et de l'IA.*

---

*Last updated: June 2026*
