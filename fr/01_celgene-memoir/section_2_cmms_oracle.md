# Section 2 — Stratégie de maintenance & ERP Oracle

## 2.1 Du réactif au préventif : évolution paradigmatique

La maintenance pharmaceutique a connu une transformation profonde au cours des deux dernières décennies, passant d'une logique purement corrective (intervenir après la panne) à une logique préventive structurée, puis vers des approches prédictives. Dans un environnement GMP, cette évolution n'est pas optionnelle : une panne non anticipée sur un équipement critique peut déclencher une déviation réglementaire, compromettre un lot de production, voire exiger une requalification.

La stratégie de maintenance documentée dans ce mémoire s'appuie sur trois piliers :

```
┌────────────────────────────────────────────────────────┐
│  1. CLASSIFICATION PAR CRITICITÉ                       │
│     Matrice RPN (Risk Priority Number)                 │
│     → stratégie différenciée par actif                 │
├────────────────────────────────────────────────────────┤
│  2. PLANIFICATION ORACLE CMMS                          │
│     WOs préventifs auto-générés, tracking historique   │
│     → visibilité totale sur l'état du parc             │
├────────────────────────────────────────────────────────┤
│  3. GESTION DES SHUTDOWNS & SPARE PARTS                │
│     Anticipation des arrêts périodiques                │
│     → budget ~1.5M CHF, magasin intégré Oracle         │
└────────────────────────────────────────────────────────┘
```

## 2.2 Matrice de criticité et classification des actifs

La classification des équipements par criticité est le prérequis à toute stratégie de maintenance différenciée. En environnement GMP pharmaceutique, cette classification intègre deux dimensions :

- **Impact qualité/réglementaire** : l'équipement entre-t-il en contact direct avec le produit ? Conditionne-t-il un paramètre critique du procédé (CPP) ?
- **Impact disponibilité** : sa défaillance provoque-t-elle l'arrêt de la ligne ? Existe-t-il une redondance ?

La méthode FMEA (Failure Mode and Effects Analysis), enrichie par le calcul du RPN (Risk Priority Number = Sévérité × Occurrence × Détectabilité), permet de prioriser les ressources de maintenance sur les actifs à risque le plus élevé.

## 2.3 Oracle CMMS : architecture et flux de données

Le système Oracle EAM (Enterprise Asset Management) constitue le système nerveux central de la fonction maintenance. Son architecture en environnement pharmaceutique couvre :

**Gestion des actifs :**
- Arborescence équipements (site → ligne → équipement → sous-ensemble)
- Fiches techniques et historique des interventions
- Documents de qualification liés à chaque actif

**Planification de la maintenance :**
- Génération automatique des Ordres de Travail (WO) préventifs
- Gestion des priorités et des ressources techniciens
- Suivi des temps d'intervention réels vs planifiés

**Gestion des spare parts :**
- Stock minimum par référence critique
- Liaisons fournisseurs et délais d'approvisionnement
- Valorisation des stocks pour reporting budgétaire

L'architecture ISA-95 définit les niveaux d'intégration entre Oracle EAM (niveau 4 — ERP) et les systèmes de contrôle de production (niveau 3 — MES/SCADA), permettant la remontée automatique des alarmes équipements vers le système de gestion des WOs.

## 2.4 Stratégie spare parts pour les shutdowns périodiques

La planification des shutdowns périodiques constitue un exercice de gestion multi-contraintes : contraintes réglementaires (fenêtres de requalification), contraintes de production (minimiser l'impact sur les lots), contraintes de stock (éviter la sur-immobilisation de capital).

La démarche appliquée s'articule autour de :

1. **Identification des pièces critiques** par analyse de criticité FMEA + historique Oracle
2. **Calcul du stock de sécurité** basé sur les délais fournisseurs et la fréquence des shutdowns
3. **Constitution des kits shutdown** regroupant les pièces par équipement/ligne
4. **Supervision du magasinier** pour la réception, le stockage conforme GMP et la traçabilité

## 2.5 Budgétisation et reporting

La gestion d'un budget maintenance de ~1.5M CHF implique un reporting structuré permettant de distinguer :

- **OPEX maintenance** : pièces de rechange, contrats de maintenance externalisés, ressources internes
- **CAPEX maintenance** : remplacement d'équipements majeurs, upgrades
- **Coûts de défaillance** : réparations non planifiées, impact sur la production

Le tableau de bord Oracle permet l'extraction mensuelle des KPIs budgétaires et leur comparaison avec les engagements initiaux.

---

*→ Section 3 : Pilotage par les KPIs & Tableau de bord*

---

### Références (extraits)

- Pasipatorwa, S. et al. (2022). *CMMS implementation and maintenance performance improvement*
- Pintelon, L. & Parodi-Herz, A. (2008). *Maintenance: An evolutionary perspective*
- ISA-95. *Enterprise-Control System Integration standard*
