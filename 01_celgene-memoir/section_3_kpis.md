# Section 3 — Pilotage par les KPIs & Tableau de bord

## 3.1 Le KPI comme langage commun

Dans un environnement pharmaceutique multi-départemental, les indicateurs de performance jouent un rôle qui dépasse la simple mesure : ils constituent un **langage commun** entre la maintenance, la production, la qualité et le management. Un KPI bien défini traduit une réalité terrain complexe en une donnée décisionnelle actionnable.

La conception du tableau de bord maintenance doit répondre à trois niveaux de lecture :

```
Niveau stratégique  →  Tendances long terme, benchmarking, budget
Niveau tactique     →  Planification hebdomadaire, taux de respect du planning
Niveau opérationnel →  WOs ouverts/fermés, pannes en cours, urgences
```

## 3.2 OEE — Overall Equipment Effectiveness

L'OEE est l'indicateur de référence de la performance équipements. Il se décompose en trois facteurs multiplicatifs :

```
OEE = Disponibilité × Performance × Qualité

Disponibilité  = Temps de fonctionnement réel / Temps disponible planifié
Performance    = Production réelle / Production théorique
Qualité        = Lots conformes / Lots totaux produits
```

Un OEE world-class est généralement situé autour de 85%. En environnement pharmaceutique GMP, les contraintes réglementaires (arrêts pour nettoyage, calibration, qualifications) peuvent justifier des cibles ajustées selon le type d'équipement.

## 3.3 MTBF / MTTR — Fiabilité et maintenabilité

| Indicateur | Formule | Interprétation |
|-----------|---------|----------------|
| MTBF | Temps total de fonctionnement / Nombre de pannes | Plus il est élevé, plus l'équipement est fiable |
| MTTR | Temps total de réparation / Nombre de pannes | Plus il est bas, plus la maintenance est efficace |
| Disponibilité | MTBF / (MTBF + MTTR) | Synthèse fiabilité + maintenabilité |

Le suivi MTBF/MTTR par équipement dans Oracle CMMS permet d'identifier les actifs chroniquement défaillants et de justifier un reclassement de leur stratégie de maintenance (passage de préventif périodique à conditionnel, ou remplacement).

## 3.4 KPIs budgétaires

La gestion d'un budget de ~1.5M CHF nécessite un suivi mensuel structuré :

- **Taux de réalisation du plan de maintenance préventive** (cible : >95%)
- **Ratio maintenance corrective / préventive** (cible : <20% correctif)
- **Coût de maintenance par actif** (identification des équipements les plus coûteux)
- **Taux de service spare parts** (disponibilité des pièces lors des interventions)
- **Variance budget vs réalisé** par ligne de coût

## 3.5 Architecture du tableau de bord Oracle

```
┌─────────────────────────────────────────────────────────┐
│              DASHBOARD MAINTENANCE MENSUEL              │
├──────────────┬──────────────┬──────────────┬────────────┤
│ DISPONIBILITÉ│    OEE       │  BUDGET      │  WOs       │
│   98.2%      │   84.7%      │  CHF 127K/M  │  142 open  │
│   ▲ +0.3%    │   ▲ +1.2%   │  ▼ -3% vs P  │  ▼ -8 vs M-1│
├──────────────┼──────────────┼──────────────┼────────────┤
│ MTBF         │  MTTR        │ PM Compliance│ CAPAs open │
│  847 h       │   2.3 h      │   97.4%      │    4       │
└──────────────┴──────────────┴──────────────┴────────────┘
```

## 3.6 Lien KPIs → Décision → Action

La valeur des KPIs réside dans leur capacité à déclencher des actions. Un tableau de bord qui mesure sans générer de décision est un outil coûteux sans ROI. La boucle vertueuse :

```
Mesure KPI → Analyse tendance → Identification écart → 
Décision corrective → Implémentation → Vérification impact → 
Mise à jour KPI → ...
```

Cette boucle s'articule directement avec le cycle CAPA documenté en Section 6.

---

*→ Section 4 : Coordination interdépartementale*

---

### Références (extraits)

- Dal et al. (2000). *OEE definition and application*
- Nakajima, S. (1988). *TPM — Total Productive Maintenance*
- Muchiri, P. & Pintelon, L. (2008). *Performance measurement using OEE*
