# SunTinel — Types de recherche et outils

**Projet en bêta fermée : aucune recherche réelle n'est ouverte ou autorisée.** Toutes les possibilités ci-dessous sont décrites au futur ou dans un cadre de tests fictifs.

## Les recherches envisagées

| Recherche | Exemple simple | Statut |
| --- | --- | --- |
| Identité | Chercher des mentions d'un nom et prénom et examiner les sources | Parcours testé avec données fictives |
| Pseudonyme | Voir si le même nom d'utilisateur apparaît sur plusieurs sites | Outils spécialisés en développement |
| Entreprise / association | Retrouver une structure dans des données publiques françaises | Source publique étudiée |
| Adresse e-mail ou téléphone | Examiner d'éventuelles mentions publiques et licites | Projet futur, non disponible |
| Photo / image | Explorer une recherche d'image inversée | Piste future non intégrée |
| Site ou domaine | Examiner des informations publiques associées à un site | Piste future à qualifier |

Une même appellation peut correspondre à plusieurs personnes. **SunTinel ne devra jamais confirmer automatiquement une identité à partir d'un seul indice.**

## Les outils externes connus

| Outil | À quoi sert-il ? | Place dans SunTinel |
| --- | --- | --- |
| [Sherlock](https://github.com/sherlock-project/sherlock) | Chercher un pseudonyme sur différents sites | Adaptation travaillée et testée dans des périmètres limités |
| [Maigret](https://github.com/soxoj/maigret) | Chercher des profils associés à un pseudonyme | Collecteur travaillé ; pas d'activation réelle automatique |
| [Tavily](https://tavily.com/) | Rechercher des pages du Web | Connecteur étudié et testé dans des périmètres limités |
| [DDGS](https://github.com/deedy5/ddgs) | Réunir des résultats de moteurs de recherche | Collecteur travaillé, utilisation réelle soumise à validation |
| [Recherche d'entreprises](https://recherche-entreprises.api.gouv.fr/docs/) | Consulter les données ouvertes d'entreprises françaises | Connexion à la source publique travaillée |

Ces outils appartiennent à leurs éditeurs ou communautés respectives. **Ils n'ont pas été créés par SunTinel.** Leur présence dans le projet ne signifie pas qu'ils sont actuellement activés ou approuvés pour des recherches réelles.

## Ce que nous avons développé nous-mêmes

**SunTinel est le logiciel créé pour coordonner le travail.** Il comprend des composants de préparation d'investigations, de gestion des dossiers et autorisations, de tri des résultats, de suppression des doublons, de conservation des sources, de revue humaine et de rapports.

Des journaux permettent de retracer les opérations importantes. Les exports de rapports ont été testés sur des données fictives. Plusieurs fonctions restent à vérifier ou à améliorer avant l'ouverture du produit.

## Ce que SunTinel ne fera pas

- Accéder par magie à des comptes privés ou à des fichiers protégés.
- Transformer une ressemblance en identité prouvée.
- Ouvrir des recherches sur des personnes à tout visiteur.
- Remplacer la décision humaine ou le respect du droit.

[Retour à la présentation](README.md) · [Sécurité et cadre légal](SECURITE_ET_DROIT.md)
