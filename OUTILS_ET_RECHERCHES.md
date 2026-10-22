# Ce que SunTinel permettra de rechercher

*Bêta en développement. Les recherches réelles ne sont pas autorisées et aucune fonctionnalité de recherche n'est accessible au public.*

## Les recherches

| Recherche | Exemple simple | Situation |
| --- | --- | --- |
| **Nom et prénom** | Retrouver des mentions publiques d'un nom, puis vérifier les sources | Parcours testé avec des données fictives |
| **Pseudonyme** | Repérer le même nom d'utilisateur sur plusieurs sites | Outils spécialisés en test |
| **Entreprise ou association** | Consulter les informations publiques d'une structure | Source publique étudiée |
| **E-mail ou téléphone** | Rechercher d'éventuelles mentions accessibles légalement | À l'étude |
| **Photo ou site web** | Explorer une image ou des informations publiques sur un site | Piste future |

Ces recherches ne donnent pas accès à des comptes privés et ne prouvent pas automatiquement l'identité d'une personne.

## Quels outils existent ?

Nous utilisons ou étudions des outils tiers pour les tâches spécialisées :

- **[Sherlock](https://github.com/sherlock-project/sherlock) et [Maigret](https://github.com/soxoj/maigret)** : recherche de pseudonymes.
- **[Tavily](https://tavily.com/) et [DDGS](https://github.com/deedy5/ddgs)** : recherche de pages sur Internet.
- **[Recherche d'entreprises](https://recherche-entreprises.api.gouv.fr/docs/)** : informations publiques sur des entreprises françaises.

Ces outils ne sont **pas créés par SunTinel** et ne sont pas tous activés. Une intégration technique ne vaut pas autorisation de recherche réelle.

## Qu'avons-nous créé nous-mêmes ?

**SunTinel** est le logiciel qui doit relier les étapes : créer un dossier, organiser les résultats, retirer les doublons, garder les sources, permettre leur examen et préparer les rapports.

Les composants sont encore testés séparément. La plateforme entière n'est pas ouverte.

**Règle essentielle :** une ressemblance de nom ou de pseudonyme est une piste, pas une identité confirmée.

[Retour à la présentation](README.md) · [Voir l'avancement](ROADMAP.md)
