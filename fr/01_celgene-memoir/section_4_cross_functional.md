# Section 4 — Coordination interdépartementale : Utilities, Process & Calibration

## 4.1 La coordination comme compétence centrale

Dans un environnement pharmaceutique GMP, la maintenance n'est jamais une activité isolée. Elle s'inscrit dans un réseau de dépendances fonctionnelles impliquant au minimum trois départements opérationnels :

- **Utilities** : production et distribution des fluides process (air comprimé, eau purifiée, vapeur, HVAC)
- **Process** : production des APIs, avec ses contraintes de scheduling de lots
- **Calibration** : maintien de la métrologie et des instruments de mesure conformes

La coordination entre ces trois fonctions — souvent aux objectifs partiellement divergents — est une compétence organisationnelle critique que les modèles de performance maintenance reconnaissent comme déterminante pour l'efficacité globale du site.

## 4.2 Modèle TPM et implication transverse

Le Total Productive Maintenance (TPM) — développé par Nakajima (1988) et formalisé par le Japan Institute of Plant Maintenance — est le cadre de référence pour une maintenance intégrée à l'organisation de production. Ses huit piliers incluent explicitement la **maintenance autonome** (implication des opérateurs) et la **maintenance plannifiée** (coordination entre maintenance et production).

```
Les 8 piliers TPM :
1. Maintenance autonome (opérateurs)
2. Maintenance planifiée (maintenance)
3. Amélioration au cas par cas (Kaizen)
4. Formation & développement des compétences
5. Contrôle initial (nouveaux équipements/produits)
6. Maintenance de la qualité (liens process-équipements)
7. Sécurité, santé, environnement
8. TPM dans les bureaux (support functions)
```

En environnement pharmaceutique GMP, les piliers 2, 6 et 7 sont particulièrement critiques : la maintenance planifiée s'intègre dans les fenêtres de production, la maintenance qualité surveille les CPPs, et la sécurité intègre les exigences HPAPI/GMP.

## 4.3 Scheduling et gestion des conflits de ressources

La planification des interventions de maintenance dans un environnement multi-département génère des conflits de ressources récurrents :

| Conflit type | Parties impliquées | Arbitrage |
|-------------|-------------------|-----------|
| Arrêt utilité pendant production | Utilities vs Process | Planning anticipé, créneaux validés |
| Calibration instrument en service | Calibration vs Process | Instrument de remplacement, délai négocié |
| Shutdown préventif vs lot en cours | Maintenance vs Process | Fenêtres shutdown intégrées au planning production |
| Ressources techniciens partagées | Maintenance vs Calibration | Matrice de priorités, escalade manager |

La résolution de ces conflits nécessite un **mécanisme de réunion structuré** (daily/weekly meeting maintenance-production) et des **règles d'escalade** claires documentées dans les SOPs.

## 4.4 Oracle comme plateforme de coordination

Oracle CMMS joue un rôle de **plateforme de coordination** au-delà de son usage CMMS pur :

- Les WOs générés sont visibles par tous les départements concernés
- Les statuts (planifié, en cours, terminé) sont mis à jour en temps réel
- Les historiques d'intervention par équipement sont consultables par Process et Calibration
- Les notifications automatiques informent les parties prenantes des interventions planifiées

Cette transparence partagée réduit les frictions inter-départementales et renforce la confiance mutuelle entre les équipes.

## 4.5 Communication formelle et informelle

La coordination efficace repose sur deux canaux complémentaires :

**Formel :** réunions hebdomadaires maintenance/production, rapports mensuels KPIs, enregistrements Oracle, SOPs de coordination
**Informel :** présence terrain, disponibilité, réactivité aux demandes urgentes, confiance construite dans la durée

Modgil & Sharma (2016) soulignent que **"Total Productive Maintenance and Total Quality Management together have a significant positive impact on operational performance"** — une convergence qui n'est possible que si les deux fonctions partagent des indicateurs communs et un langage de coordination établi.

---

*→ Section 5 : Contexte produits*

---

### Références (extraits)

- Nakajima, S. (1988). *Introduction to TPM*
- Modgil, S. & Sharma, S. (2016). *TPM and TQM — meta-analysis*
- Ahuja, I.P.S. & Khamba, J.S. (2008). *Total productive maintenance — literature review*
