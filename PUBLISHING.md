# SunTinel — Publication de la vitrine

Dépôt public : **AshtraySunn/suntinel-updates**.

Site prévu : https://ashtraysunn.github.io/suntinel-updates/

## GitHub Pages

Depuis les paramètres du dépôt :

1. Ouvrir **Settings → Pages**.
2. Sous **Build and deployment**, choisir **Deploy from a branch**.
3. Sélectionner **main** et **/(root)**.
4. Enregistrer et vérifier l'URL publiée, puis contrôler l'affichage.

Ne pas annoncer que GitHub Pages est activé sans l'avoir vérifié.

## Préparer une mise à jour

1. Identifier l'événement à communiquer et son état exact : **conception**, **livraison de candidat**, **acceptation indépendante** ou **fonctionnalité à venir**.
2. Vérifier les éléments internes au regard de la source gelée, sans reprendre mot pour mot les conclusions brutes d'un agent.
3. Mettre à jour **data/progress.json** pour la page.
4. Mettre à jour **ROADMAP.md** et **CHANGELOG.md** de manière cohérente.
5. N'actualiser la date que si l'information vérifiée a réellement changé.
6. Relire les informations comme un communiqué public et contrôler l'absence de données sensibles.
7. Publier **uniquement dans ce dépôt**, jamais par copie automatique du dépôt privé.

## Filtre de sécurité avant toute publication

Ne jamais inclure :

- Identités de personnes recherchées, données ou captures de dossiers d'investigation.
- Secrets, jetons, clés API, informations personnelles ou chemins WSL.
- Détails exploitables des vulnérabilités, démonstrations d'attaque et rapports confidentiels.
- SHAs du code privé, copies de bases, journaux internes ou informations d'infrastructure.
- Captures de l'application opérationnelle non autorisées pour diffusion.
- Promesses de certification, de sécurité complète, de conformité ou de disponibilité non vérifiées.

Aucun formulaire de collecte ni aucune recherche nominative ne doivent être ajoutés à cette vitrine sans décision distincte.

## Vérifications rapides

- JSON valide dans **data/progress.json**.
- Liens internes et ancres fonctionnels.
- Site lisible sur mobile et avec navigation clavier.
- FAQ accessible et texte clair sur l'accès fermé.
- Cohérence entre les états publics et les audits réellement acceptés.
- Aucun chargement de données privées depuis le navigateur.

Prévisualiser localement depuis un dossier contenant les fichiers du dépôt :

    python3 -m http.server 8080

Puis ouvrir http://127.0.0.1:8080/ ; les actualités proviennent de **data/progress.json** et nécessitent un serveur HTTP local.

L'ensemble peut être tenu à jour sans agent de développement coûteux ; la vérification humaine du contenu public reste indispensable.
