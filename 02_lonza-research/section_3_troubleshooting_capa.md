# Section 3 — Troubleshooting & CAPA en environnement biologics

## 3.1 Spécificités des défaillances en biologics

Les modes de défaillance en environnement biologics présentent des spécificités qui compliquent le troubleshooting par rapport à un environnement small molecule :

```
Small molecule (Celgene)          Biologics (Lonza Visp)
─────────────────────────────     ──────────────────────────────
Procédé chimique déterministe     Procédé biologique variable
Contamination chimique mesurable  Contamination biologique (mycoplasmes, bioburden)
Cleaning chimique validé          CIP/SIP critique — intégrité biologique
Instruments classiques            Capteurs en ligne (pH, DO, conductivité, pression)
Confinement chimique              Confinement biologique + HPAPI
```

## 3.2 Outils RCA adaptés au contexte biologics

### FMEA Bioreacteur / Small Equipment

La FMEA en contexte biologics intègre des modes de défaillance spécifiques :

| Composant | Mode de défaillance | Effet potentiel | RPN guide |
|-----------|---------------------|-----------------|-----------|
| Joint peristaltique | Usure → fuite | Contamination lot | Élevé |
| Sonde pH | Dérive calibration | CPP hors limite | Élevé |
| Filtre ventilation | Colmatage | Pression différentielle hors spec | Moyen |
| Vanne stérile | Actionnement défaillant | Contamination croisée | Élevé |
| Autoclave | Cycle incomplet | Non-stérilité | Critique |

### Cycle intégré RCA-CAPA en GMP biologics

```
Signal qualité / défaillance équipement
              ↓
    Déviation formelle (GMP record)
              ↓
    Investigation RCA (5M / FMEA / 5 Whys)
              ↓
    Cause racine identifiée (systémique, pas superficielle)
              ↓
    Plan CAPA : correction immédiate + action préventive
              ↓
    Implémentation + documentation
              ↓
    Effectiveness check (vérification d'efficacité)
              ↓
    Clôture CAPA → Mise à jour CMMS + SOP si applicable
              ↓
    Alimentation OEE / KPI → boucle d'amélioration continue
```

*Figure 3.1 — Cycle intégré RCA-CAPA-amélioration continue en environnement GMP biologics*

## 3.3 Troubleshooting en production commerciale vs. développement

En phase de ramp-up commercial (contexte Visp 2026), une pression supplémentaire s'exerce sur le troubleshooting : chaque lot compte, chaque arrêt a un coût contractuel direct. La démarche doit combiner :

- **Réactivité** : identifier et contenir rapidement l'impact
- **Rigueur GMP** : documenter chaque étape malgré la pression temporelle
- **Profondeur d'investigation** : aller à la cause racine systémique pour éviter la récurrence

## 3.4 Compétences RCA-CAPA pour le rôle I&U Engineer Visp

L'analyse de la littérature converge sur trois exigences de maturité :

**Profondeur d'investigation** — aller au-delà de la cause proximale pour identifier les facteurs systémiques (conception, PM interval, conditions d'utilisation réelles vs. spécifications), en s'appuyant sur la combinaison 5M + FMEA + données CMMS historiques.

**Rigueur documentaire** — chaque investigation produit une trace formelle conforme aux exigences GMP, avec des recommandations concrètes, assignées, avec deadline et critères d'efficacité mesurables.

**Orientation amélioration continue** — le CAPA n'est pas une réponse ponctuelle à un incident isolé. Il alimente un cycle d'amélioration des stratégies de maintenance (PM intervals, criticité, procédures), des SOPs, et des indicateurs OEE/KPI du site.

L'expérience de rédaction et de suivi de CAPAs, de déviations et de SOPs acquise en environnement GMP API sous double surveillance FDA/SwissMedic constitue un ancrage direct dans ce référentiel.

---

*→ Section 4 : GMP Utilities biologics — CIP/SIP, WFI, clean steam*

---

### Références (extraits)

- Seely, R.J. et al. (2021). *Failure analysis biopharmaceutical manufacturing*
- ICH Q9. *Quality Risk Management — FMEA application*
- FDA. *Guidance on deviation and CAPA in biologics manufacturing*
