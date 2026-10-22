# Publication de la vitrine publique — procédure

## Prérequis

Créer un **nouveau dépôt public dédié**, nommé de préférence `suntinel-updates`.

Ne JAMAIS rendre public le dépôt d'application SunTinel ni utiliser ses branches ou worktrees privés comme source de publication.

## Avec l'interface GitHub

1. Sur GitHub, créer un nouveau dépôt public `suntinel-updates` (sans copier les fichiers de l'application).
2. Ajouter uniquement les fichiers de ce dossier de vitrine (par exemple via `git` local, ci-dessous).
3. Ouvrir `Settings` → `Pages`.
4. Choisir `Deploy from a branch` → `main` → `/(root)` puis enregistrer.
5. Vérifier l'URL affichée dans `Settings` → `Pages` ; elle aura normalement la forme `https://VOTRE_IDENTIFIANT.github.io/suntinel-updates/`.

## Avec Git depuis un dossier dédié

Exécuter uniquement depuis le dossier extrait de cette archive, JAMAIS depuis le dépôt privé :

```bash
cd /chemin/vers/suntinel-public-pages
git init -b main
git add README.md ROADMAP.md CHANGELOG.md PUBLISHING.md index.html styles.css script.js favicon.svg data/progress.json .nojekyll
git status --short
git commit -m "docs: launch public SunTinel progress page"
git remote add origin https://github.com/VOTRE_IDENTIFIANT/suntinel-updates.git
git push -u origin main
```

La connexion GitHub et la création du dépôt doivent avoir été effectuées au préalable. Ne pas copier-coller la commande avec `VOTRE_IDENTIFIANT` inchangé.

## Mettre à jour le site

- Modifier `data/progress.json` pour le contenu visible sur la page.
- Modifier `CHANGELOG.md` et `ROADMAP.md` pour les notes en Markdown.
- Vérifier la cohérence des statuts et des dates.
- Revoir les modifications **comme s'il s'agissait d'une communication publique définitive**.
- Publier uniquement depuis le dépôt public séparé.

## Revue de sécurité avant chaque publication

Ne pas inclure :

- Identités, recherches, résultats ou captures d'enquêtes.
- Chemins internes, IP, comptes, clés, jetons ou secrets.
- Reproductions de vulnérabilités ou modes d'exploitation.
- Rapports confidentiels de sécurité, logs ou détails d'infrastructure.
- Commits privés, descriptions détaillées de failles encore ouvertes, captures de l'application interne sans validation.
- Assertions de certification ou de déploiement non confirmées.

Ne pas automatiser la copie de fichiers du dépôt privé vers ce dépôt. Ne pas publier automatiquement le résumé brut d'un agent ou d'un audit.

## Prévisualisation locale

Depuis le répertoire extrait :

```bash
python3 -m http.server 8080
```

Puis ouvrir `http://127.0.0.1:8080/`.

`data/progress.json` est chargé par le navigateur via `fetch`, ce qui exige un petit serveur local et non un simple double-clic sur `index.html`.