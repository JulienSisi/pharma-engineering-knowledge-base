# Section 6 — Documentation GMP & Cycle CAPA

## 6.1 La documentation comme preuve de maîtrise

En environnement GMP, la règle fondamentale est simple et absolue : **"If it's not documented, it didn't happen."** Cette maxime n'est pas un cliché bureaucratique — elle reflète la logique réglementaire selon laquelle la preuve d'une activité est indissociable de l'activité elle-même.

Pour la maintenance, cela signifie que chaque intervention, chaque calibration, chaque déviation détectée doit générer une trace formelle, datée, signée, et intégrée dans un système documentaire cohérent.

## 6.2 Architecture documentaire

```
SOPs (Standard Operating Procedures)
  ↓ "Quoi faire et comment"
  
WPs (Work Procedures / Instructions)
  ↓ "Étapes détaillées d'exécution"
  
FORMs (Formulaires d'enregistrement)
  ↓ "Preuve que c'a été fait"
  
MDS (Maintenance Data Sheets)
  ↓ "Données techniques de référence par équipement"
```

Cette hiérarchie documentaire assure la cohérence entre les exigences réglementaires (SOPs), les pratiques terrain (WPs), et les preuves d'exécution (FORMs). La rédaction, la révision et la mise à jour de ces documents constituent une part significative du travail de coordination de la maintenance.

## 6.3 Principes ALCOA & intégrité des données

Les principes **ALCOA** (Attributable, Legible, Contemporaneous, Original, Accurate) définissent les caractéristiques d'une donnée GMP valide :

| Principe | Définition | Application maintenance |
|---------|-----------|------------------------|
| **A**ttributable | Identifiable à son auteur | Signature obligatoire sur chaque enregistrement |
| **L**egible | Lisible et compréhensible | Pas de raturage, correction avec paraphe |
| **C**ontemporaneous | Enregistré au moment de l'action | Pas d'enregistrement rétroactif non justifié |
| **O**riginal | Données primaires conservées | Pas de transcription sans référence à l'original |
| **A**ccurate | Correct et complet | Valeurs réelles, pas d'arrondis non justifiés |

Dans Oracle CMMS, les enregistrements des WOs de maintenance sont horodatés automatiquement et liés à l'utilisateur connecté, assurant naturellement les principes A, C et partiellement L.

## 6.4 Cycle de vie documentaire

```
Rédaction (auteur) → Revue (peer) → Approbation (manager/QA) 
→ Formation du personnel → Mise en application 
→ Révision périodique → Mise à jour si nécessaire → Archivage
```

## 6.5 Gestion des déviations

Une **déviation** est tout écart par rapport à une procédure approuvée ou à une spécification définie. En maintenance, les déviations peuvent être :

- **Déviations équipement** : résultat de calibration hors limite, panne non planifiée sur un équipement qualifié
- **Déviations procédurales** : intervention réalisée sans WO approuvé, SOP non respectée
- **Déviations documentaires** : données manquantes, signatures incorrectes

La gestion d'une déviation suit un flux structuré :
```
Détection → Notification immédiate → Containment (isoler l'impact)
→ Évaluation initiale (impact qualité ?) → Ouverture déviation formelle
→ Investigation RCA → Plan CAPA → Approbation QA → Clôture
```

## 6.6 Analyse de Cause Racine (RCA)

Les outils de RCA utilisés en environnement GMP pharmaceutique :

**5 Whys** — Méthode simple et efficace pour les défaillances directes :
```
Panne pompe → Pourquoi ? Roulement usé
→ Pourquoi ? Lubrification insuffisante
→ Pourquoi ? Fréquence PM inadaptée
→ Pourquoi ? Criticité sous-évaluée à la mise en service
→ Pourquoi ? Procédure de classification non révisée depuis installation
→ CAUSE RACINE : procédure de classification des criticités obsolète
```

**Diagramme Ishikawa (5M)** — Pour les défaillances complexes multi-facteurs :
- **M**ain d'œuvre (compétences, formation)
- **M**éthode (SOP, procédure suivie ?)
- **M**achine (état équipement, historique pannes)
- **M**atière (spare parts, qualité des consommables)
- **M**ilieu (environnement, température, vibrations)

**FMEA** — Pour l'analyse préventive systématique (voir Section 2)

## 6.7 CAPA basé sur les tendances

Au-delà du traitement des déviations individuelles, la surveillance des **tendances** permet d'identifier les problèmes systémiques avant qu'ils ne génèrent une déviation majeure :

- Suivi mensuel du nombre et type de déviations par ligne / équipement
- Analyse des récurrences (même équipement, même cause)
- Revue trimestrielle CAPA avec le département Qualité

## 6.8 CAPA & Change Control

Toute action corrective ou préventive qui modifie un équipement qualifié, une SOP approuvée, ou un paramètre de procédé doit passer par le processus de **Change Control** (gestion du changement) :

```
Proposition de changement → Évaluation de l'impact (qualification requise ?)
→ Approbation multi-disciplinaire (Engineering + Quality + Process)
→ Implémentation contrôlée → Vérification d'efficacité → Clôture
```

## 6.9 Lean Six Sigma & amélioration continue

L'intégration des outils Lean Six Sigma dans la démarche d'amélioration continue de la maintenance pharmaceutique est documentée par Da Silva et al. (2023) :

- **DMAIC** (Define, Measure, Analyze, Improve, Control) pour les projets d'amélioration structurés
- **5S** pour l'organisation des ateliers et magasins maintenance
- **Kaizen** pour les améliorations incrémentales du quotidien

La principale tension identifiée dans la littérature est la **peur des requalifications** liées aux changements de process — ce qui peut freiner l'amélioration continue dans des environnements très conservateurs sur le plan réglementaire.

---

*→ Section 7 : Conclusion & Perspectives Industry 4.0*

---

### Références (extraits)

- Da Silva, A. et al. (2023). *Lean Six Sigma pharmaceutical GMP continuous improvement*
- ICH Q10. *Pharmaceutical Quality System*
- FDA. *Guidance for Industry — Investigating Out-of-Specification (OOS) Test Results*
- EMA. *Guideline on good pharmacovigilance practices — CAPA*
