# Section 1 — Equipment Management & Reliability : Fondements stratégiques pour un environnement CDMO biologics

## 1.1 Contexte : la fiabilité équipements comme impératif opérationnel CDMO

Dans un contrat de développement et de fabrication (CDMO), la disponibilité des équipements n'est pas une métrique opérationnelle parmi d'autres — c'est une condition contractuelle. Chaque lot produit engage la réputation du site vis-à-vis de clients pharmaceutiques qui, à leur tour, ont des obligations de mise sur le marché envers des régulateurs et des patients.

Cette réalité est particulièrement aiguë dans un contexte de ramp-up commercial, où des lignes nouvellement qualifiées passent du régime de validation au régime de production à plein régime, avec une tolérance zéro aux dérives de disponibilité non anticipées.

## 1.2 Spécificités du small equipment en biologics

Le "small equipment" dans un contexte CDMO biologics couvre une gamme large d'actifs : pompes péristaltiques, filtres d'intégrité, connections de transfert, balances analytiques, équipements de contrôle en ligne (pH, DO, conductivité), systèmes de sampling, autoclaves de petite capacité.

Ces équipements partagent plusieurs caractéristiques qui conditionnent la stratégie de maintenance :

```
Haute fréquence d'utilisation    → Usure accélérée, criticité élevée
Contact direct avec le produit   → Impact immédiat sur la qualité du lot
Renouvellement fréquent          → Gestion intensive des spare parts
Multiplication des références    → Complexité de gestion du stock
```

## 1.3 Classification par criticité — adaptation au contexte biologics

La matrice de criticité standard (Sévérité × Occurrence × Détectabilité = RPN) doit être enrichie pour le contexte biologics avec des paramètres spécifiques :

| Critère | Description | Pondération |
|---------|-------------|-------------|
| Impact qualité produit | Contact direct produit ? CPP impliqué ? | Élevée |
| Impact contamination | Risque biologique si défaillance ? | Élevée |
| Disponibilité redondance | Équipement de backup disponible ? | Moyenne |
| Maintenabilité | MTTR estimé si panne ? | Moyenne |
| Délai d'approvisionnement | Lead time spare parts critique ? | Moyenne |

## 1.4 Stratégie différenciée : PM / CBM / corrective résiduelle

```
┌─────────────────────────────────────────────────────────────┐
│  1. CLASSIFICATION PAR CRITICITÉ                            │
│     SIA / CCA / RPN enrichi (maintainability complexity)    │
│     → stratégie différenciée par actif                      │
├─────────────────────────────────────────────────────────────┤
│  2. CADRE TPM/RCM CENTRÉ OEE                                │
│     Attaque des 6 grandes pertes, TPM autonome,             │
│     intégration CBM sur actifs haute criticité              │
├─────────────────────────────────────────────────────────────┤
│  3. INFRASTRUCTURE DONNÉES ET CMMS                          │
│     Capteurs existants + CMMS/MES comme socle CBM,          │
│     monitoring conditionnel avant ML/PdM avancé             │
├─────────────────────────────────────────────────────────────┤
│  4. INTÉGRATION PLANNING PRODUCTION                         │
│     PM opportuniste, fenêtres à faible impact,              │
│     synchronisation avec scheduling multi-produit CDMO      │
└─────────────────────────────────────────────────────────────┘
```

## 1.5 Connexion avec l'expérience Celgene

L'expérience de gestion de la maintenance par criticité Oracle + shutdown périodique chez Celgene constitue un ancrage direct dans ce référentiel. Les différences clés à intégrer pour le contexte biologics Visp :

- **Profil produit** : passage de small molecules (APIs chimiques) à biologics (protéines, anticorps, ADCs) — les équipements en contact direct ont des exigences de nettoyabilité CIP/SIP et d'intégrité de confinement différentes
- **Complexité du parc** : environnement CDMO multi-produit implique une gestion plus complexe des conflits de scheduling
- **Ramp-up dynamique** : le parc équipements évolue rapidement avec les nouvelles lignes mises en production

---

*→ Section 2 : SME dans les projets CAPEX — Framework CQV*

---

### Références (extraits)

- Pasipatorwa, S. et al. (2022). *CMMS pharmaceutical reliability improvement*
- Macchi, M. & Fumagalli, L. (2013). *Maintenance maturity assessment method*
- Garg, A. & Deshmukh, S.G. (2006). *Maintenance management — literature review*
