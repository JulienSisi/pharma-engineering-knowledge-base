# Section 1 — Cadre réglementaire GMP : Contexte et Exigences

## 1.1 Introduction au contexte réglementaire

La production pharmaceutique de principes actifs à usage humain s'inscrit dans un cadre normatif strict, défini conjointement par la **FDA** (*Food and Drug Administration*, États-Unis) et les autorités européennes et suisses, dont **SwissMedic**. Ces organismes imposent le respect des *current Good Manufacturing Practices* (cGMP), dont l'objectif central est de garantir que chaque lot produit est conforme à ses spécifications de qualité, d'identité et de pureté.

Dans ce cadre, la maintenance des équipements et des utilités n'est pas une activité périphérique : elle constitue un **pilier de la conformité réglementaire**. Comme le soulignent Tibesso et al. (2024) ainsi qu'Ahmed (2024), les cGMP exigent que les installations et équipements soient *fit for purpose*, maintenus de manière proactive et intégralement documentés — la prévention des défaillances primant sur leur correction.

## 1.2 Exigences réglementaires appliquées à la maintenance

Le référentiel **21 CFR Part 211** de la FDA établit les bases légales de la qualification et de la calibration des équipements.

Les exigences fondamentales couvrent :

- **21 CFR 211.68** — Systèmes automatiques, mécaniques et électroniques : maintenance et qualification formelle requises
- **21 CFR 211.182** — Equipment cleaning and maintenance : enregistrements obligatoires avec date, heure, signature
- **21 CFR 211.68(b)** — Validation des systèmes informatiques (applicable à Oracle CMMS)

SwissMedic, via les Bonnes Pratiques de Fabrication suisses alignées sur les directives EU-GMP, ajoute une couche d'exigence documentaire spécifique, notamment sur la traçabilité des calibrations et la gestion des déviations.

## 1.3 Qualification des équipements : IQ / OQ / PQ

Le cycle de qualification IQ/OQ/PQ constitue le cadre structurant de tout équipement intégré dans un environnement GMP :

```
IQ — Installation Qualification
     ↓ L'équipement est installé conformément aux spécifications
OQ — Operational Qualification
     ↓ L'équipement fonctionne dans les limites définies
PQ — Performance Qualification
     ↓ L'équipement produit des résultats conformes en conditions réelles
```

Selon Sharma (2020), la maintenance préventive doit être planifiée en cohérence avec les intervalles de requalification définis lors de l'OQ/PQ. Un écart non documenté entre le plan de maintenance et les exigences de qualification constitue une non-conformité réglementaire potentielle.

## 1.4 Calibration et métrologie en environnement réglementé

La calibration des instruments de mesure et de contrôle est une exigence directe du 21 CFR Part 211.68. Dans un contexte multi-départemental (Utilities, Process, Calibration), la gestion centralisée des intervalles de calibration via Oracle CMMS permet :

- La génération automatique des ordres de travail (WO) de calibration
- Le suivi des certificats de calibration avec lien vers les instruments concernés
- La détection précoce des instruments hors tolérance avant qu'ils n'impactent la production

## 1.5 Synthèse : la maintenance comme fonction réglementaire

Le positionnement de la maintenance comme fonction réglementaire — et non simplement technique — est la clé de voûte de l'approche documentée dans ce mémoire. Dans un environnement sous double surveillance FDA/SwissMedic, chaque activité de maintenance génère une preuve documentaire qui peut être examinée lors d'un audit ou d'une inspection.

> **Implication pratique** : La qualité de la documentation de maintenance est directement corrélée à la capacité du site à défendre ses pratiques devant les régulateurs.

---

*→ Section 2 : Stratégie de maintenance & ERP Oracle*

---

### Références (extraits)

- Ahmed, A. (2024). *GMP compliance in pharmaceutical maintenance management*
- Tibesso, G. et al. (2024). *Preventive maintenance in FDA-regulated environments*
- Sharma, R. (2020). *Equipment qualification lifecycle pharmaceutical industry*
- FDA. *21 CFR Part 211 — Current Good Manufacturing Practice for Finished Pharmaceuticals*
