# Section 5 — Contexte produits : Lénalidomide, Thalidomide & Aprémilast

> **Note méthodologique :** Cette section s'appuie exclusivement sur des données publiques issues de la littérature scientifique et des publications réglementaires. Aucune information propriétaire ou confidentielle relative au site de production n'est divulguée.

## 5.1 Lénalidomide (Revlimid®)

### Profil pharmacologique public

Le lénalidomide est un agent immunomodulateur (IMiD) de deuxième génération, dérivé structural de la thalidomide. Il est indiqué dans le traitement du myélome multiple et de certains syndromes myélodysplasiques. Sa classification comme **REMS drug** (Risk Evaluation and Mitigation Strategy) aux États-Unis impose des contraintes de distribution et de traçabilité particulièrement strictes.

### Implications pour la maintenance

- **Confinement** : La fabrication d'un IMiD en environnement API impose des mesures de confinement renforcé et une gestion rigoureuse des effluents.
- **Nettoyage validé** : Les procédures de nettoyage (CIP — Cleaning In Place ou nettoyage manuel validé) doivent être qualifiées et leurs limites de résidus justifiées. La maintenance des équipements de nettoyage est directement critique.
- **Qualification des équipements** : Tout équipement entrant en contact avec le produit ou ses intermédiaires est soumis au cycle IQ/OQ/PQ et à des révisions périodiques de qualification (Annual Product Review).

## 5.2 Thalidomide (Thalomid®)

### Profil pharmacologique public

La thalidomide, premier IMiD historique, reste utilisée dans des indications hématologiques spécifiques (myélome multiple en association). Son histoire réglementaire a contribué à modeler les exigences cGMP modernes en matière de traçabilité et de gestion des risques.

### Implications pour la maintenance

Les contraintes de maintenance thalidomide sont similaires à celles du lénalidomide sur le plan GMP, avec un accent particulier sur :
- La validation analytique des méthodes de détection des résidus (HPLCs, spectroscopies)
- La maintenance des systèmes de confinement et d'aspiration
- La gestion documentaire des déviations liées à des équipements de mesure hors spécification

## 5.3 Aprémilast (Otezla®)

### Profil pharmacologique public

L'aprémilast est un inhibiteur de la phosphodiestérase 4 (PDE4), indiqué dans le traitement du psoriasis et de l'arthrite psoriasique. Contrairement aux IMiDs, il présente un profil de risque différent qui se reflète dans ses exigences de fabrication.

### Transition vers la fabrication continue

La littérature récente (Burcham et al., 2018 ; Müller et al., 2021) documente l'intérêt croissant pour la **fabrication continue d'APIs** (Continuous Manufacturing), dont l'aprémilast est un candidat étudié. Cette transition vers des procédés continus implique des exigences de maintenance différentes des procédés batch :

- **Surveillance en temps réel** des paramètres procédé (PAT — Process Analytical Technology)
- **Maintenance prédictive** rendue possible par la génération continue de données process
- **Qualification des équipements continus** — cadre réglementaire encore en maturation

## 5.4 Implications transverses pour la stratégie de maintenance

La diversité des profils de ces trois molécules — deux IMiDs en process batch à confinement renforcé, un inhibiteur de PDE4 en voie de transition vers la fabrication continue — justifie une **approche de maintenance différenciée par ligne et par équipement**.

Un équipement dégradé mais non détecté devient directement une **déviation réglementaire potentielle**. C'est précisément la logique qui sous-tend la matrice de criticité et le système de surveillance Oracle CMMS décrits en Section 2.

---

*→ Section 6 : Documentation GMP & Cycle CAPA*

---

### Références (extraits)

- Burcham, C.L. et al. (2018). *Continuous manufacturing of API — regulatory perspective*
- Müller, F. et al. (2021). *Continuous manufacturing transition pharma*
- FDA. *REMS Program requirements — lenalidomide, thalidomide*
- EMA. *Apremilast public assessment report*
