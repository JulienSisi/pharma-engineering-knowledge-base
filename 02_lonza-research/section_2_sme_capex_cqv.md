# Section 2 — SME dans les projets CAPEX : Framework CQV en environnement biologics

## 2.1 Le rôle SME dans le cycle de vie des équipements CAPEX

Le Subject Matter Expert (SME) équipements dans un projet CAPEX n'est pas un observateur technique — il est l'interface critique entre les équipes engineering projet, la production, la qualité et les fournisseurs. Son intervention couvre l'intégralité du cycle CQV :

```
CAPEX Project Lifecycle — SME Touchpoints

Phase DESIGN          → Spécifications techniques (URS)
Phase PROCUREMENT     → Sélection fournisseur, FAT
Phase INSTALLATION    → Supervision mise en œuvre, IQ
Phase COMMISSIONING   → Vérification fonctionnelle, C&Q
Phase QUALIFICATION   → OQ/PQ, protocoles, rapports
Phase PRODUCTION      → Handover, support ramp-up
```

## 2.2 URS — User Requirement Specification

Le document URS est le point de départ de toute qualification. Il translate les besoins process en exigences techniques formelles :

- **Exigences fonctionnelles** : capacités, plages d'utilisation, précision
- **Exigences GMP** : matériaux en contact produit, nettoyabilité CIP/SIP, DQ/IQ/OQ/PQ requis
- **Exigences SHE** : confinement HPAPI, sécurité opérateur
- **Exigences utilities** : alimentation électrique, fluides, HVAC
- **Exigences documentation** : data integrity, audit trail, 21 CFR Part 11

## 2.3 FAT / SAT — Factory & Site Acceptance Tests

Le FAT (Factory Acceptance Test) et le SAT (Site Acceptance Test) sont des étapes critiques que le SME co-pilote avec le fournisseur :

| Test | Lieu | Objectif | SME Role |
|------|------|---------|---------|
| DQ | Bureau/Fournisseur | Vérifier que le design répond à l'URS | Review documentation |
| FAT | Usine fournisseur | Vérifier l'équipement avant expédition | Superviser tests fonctionnels |
| SAT | Site Visp | Vérifier après installation | Co-signer les résultats |
| IQ | Site Visp | Installation conforme specs | Auteur ou reviewer protocole |
| OQ | Site Visp | Fonctionnement dans limites | Auteur ou reviewer protocole |
| PQ | Site Visp | Performance en conditions réelles | Auteur ou reviewer protocole |

## 2.4 C&Q — Commissioning & Qualification

Le cadre ISPE GAMP définit la frontière entre commissioning (vérification fonctionnelle ingénierie) et qualification (preuve GMP formelle). En pratique, le bon engineering en phase commissioning est la condition d'une qualification efficace et sans surprise.

La littérature (Calnan et al., 2017) souligne que les déficiences dans les phases early du projet (URS incomplet, FAT insuffisant) se manifestent systématiquement comme des déviations et retards en phase OQ/PQ — un coût masqué majeur dans les projets CAPEX biologics.

## 2.5 Connexion Celgene → Visp

L'expérience de maintenance en environnement FDA/SwissMedic chez Celgene — en particulier la familiarité avec les cycles IQ/OQ/PQ, la gestion des déviations de qualification, et la coordination avec les équipes Validation — constitue une base directement transférable. Le delta à combler est la maîtrise du contexte biologics (contraintes spécifiques bioreacteurs, systèmes CIP/SIP, WFI) et du rôle actif SME CAPEX vs. le rôle de support maintenance.

---

*→ Section 3 : Troubleshooting & CAPA en biologics*

---

### Références (extraits)

- Calnan, N. et al. (2017). *Commissioning and qualification pharmaceutical biologics*
- ISPE. *GAMP 5 — A Risk-Based Approach to Compliant GxP Computerized Systems*
- ICH Q8/Q9/Q10. *Pharmaceutical development, quality risk management, quality system*
