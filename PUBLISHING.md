# Mettre à jour le site public SunTinel

Ce dépôt contient uniquement le site de présentation. Ne jamais y copier le code ou les rapports confidentiels de l'application.

## Publier avec GitHub Pages

Dans **Settings → Pages** du dépôt, choisir **Deploy from a branch**, la branche **main**, et le dossier **/(root)**. Vérifier ensuite que le site est accessible avant de le partager.

## Mettre à jour les actualités

1. Vérifier l'information avant de l'annoncer.
2. Modifier \`data/progress.json\` pour les cartes et actualités visibles sur le site.
3. Mettre à jour \`ROADMAP.md\` ou \`CHANGELOG.md\` si nécessaire.
4. Vérifier que les statuts sont identiques partout.
5. Lancer \`python3 scripts/check_site.py\` depuis la racine du dépôt.
6. Relire chaque phrase comme une information **publique et définitive**.

## À ne jamais publier

- Identité de personnes recherchées, dossiers, captures d'enquête.
- Mots de passe, clés, adresses internes, journaux confidentiels.
- Détails de vulnérabilités ou techniques de contournement.
- Code privé, commits privés, documents de travail internes.
- Annonce de conformité, chiffrement intégral ou disponibilité non vérifiée.

**Les mots à employer sont simples :** « testé », « en cours », « prévu », « accepté avec réserves ». Éviter de confondre « terminé par le développeur » avec « vérifié et accepté ».

**Aucun formulaire de demande de compte ni recherche nominative n'est ouvert depuis cette vitrine.**

## Identité visuelle

La charte Shield Beacon et ses tokens sont documentés dans [BRAND.md](BRAND.md). Les assets SVG sont locaux et ne contiennent pas de données d'enquête. Ne pas ajouter de police distante, script publicitaire, traceur ou fournisseur externe sans justification et validation explicites.

Conserver le focus clavier, les contrastes, les textes alternatifs pertinents et la prise en charge de `prefers-reduced-motion`.
