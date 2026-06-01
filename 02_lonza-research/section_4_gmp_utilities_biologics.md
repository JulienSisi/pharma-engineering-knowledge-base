# Section 4 — GMP Utilities Biologics : CIP/SIP, WFI & Clean Steam

## 4.1 Les utilities biologics : infrastructure critique du procédé

En manufacturing biologics, les utilities ne sont pas de simples fluides de service — ce sont des **intrants process** dont la qualité conditionne directement la conformité du produit. Cette réalité distingue fondamentalement le contexte biologics du contexte small molecule API.

### Hiérarchie des utilities critiques

```
WFI (Water for Injection)          → Contact direct produit / nettoyage
Pure Steam / Clean Steam           → Stérilisation, SIP
Purified Water                     → Préparation solutions, nettoyage
Air comprimé pharma grade          → Actionnement, séchage, pressurisation
Gaz inertes (N2, CO2)              → Bullage, pressurisation bioréacteurs
HVAC - Air classification          → Environnement salles propres
```

## 4.2 WFI — Water for Injection

Le WFI est produit par distillation (méthode traditionnelle) ou par osmose inverse + CEDI (méthode émergente acceptée par l'EMA depuis 2017). Ses exigences de maintenance sont parmi les plus critiques du site :

- **Surveillance qualité continue** : conductivité, TOC, endotoxines, bioburden
- **Boucles de distribution** : maintien de la température (80°C en hot loop) ou de la vitesse d'écoulement turbulent pour éviter la formation de biofilm
- **Qualification de la boucle** : validation complète du système de distribution incluant les points d'usage

La dégradation d'une boucle WFI se manifeste insidieusement par une augmentation progressive du bioburden — sans alarme franche. La maintenance préventive (inspections, sanitisations programmées) est le seul levier pour prévenir une non-conformité.

## 4.3 CIP/SIP — Cleaning & Sterilization In Place

Les systèmes CIP (nettoyage) et SIP (stérilisation à la vapeur) sont les gardiens de l'intégrité biologique des équipements entre les lots.

**Maintenance critique CIP/SIP :**
- Vérification des buses de spray (colmatage → couverture nettoyage insuffisante)
- Intégrité des circuits (joints, vannes → fuites → efficacité réduite)
- Validation des paramètres de cycle (température, concentration, contact time)
- Enregistrement de chaque cycle dans le système de gestion des recettes

La moindre défaillance non détectée peut compromettre l'intégrité d'un lot entier — avec des conséquences réglementaires et économiques majeures.

## 4.4 Transition depuis le contexte Celgene

Chez Celgene, les utilities gérées (air comprimé, eau purifiée, HVAC de base) s'inscrivaient dans un contexte small molecule. Le delta à maîtriser pour le contexte Visp biologics porte sur :

- La criticité biologique du WFI et des boucles de distribution
- Les systèmes CIP/SIP automatisés et leur qualification
- La gestion de la vapeur stérile (pureté vapeur, validations)
- L'intégration utilities / bioréacteurs (feeds, harvest)

---

*→ Section 5 : HPAPI Containment Engineering*

---

### Références (extraits)

- Parenteral Drug Association (PDA). *Technical Report on Water for Injection*
- EMA. *Guideline on WFI production by non-distillation methods*
- ISPE. *Baseline Guide Vol. 4 — Water and Steam Systems*
