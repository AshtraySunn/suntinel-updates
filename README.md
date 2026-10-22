# SunTinel — Rechercher avec méthode

**SunTinel** est un logiciel privé d'aide à l'investigation en sources ouvertes, aussi appelées **OSINT**. L'idée est simple : réunir des pistes trouvées sur Internet dans un même dossier, les comparer et préparer un rapport, sans affirmer trop vite qu'elles concernent une personne.

> **Au 22 octobre 2026 : bêta 0.1 en développement, accès fermé.** Le site ne permet pas de rechercher des personnes. Les tests récents utilisent des données fictives.

**[Découvrir le site SunTinel](https://ashtraysunn.github.io/suntinel-updates/)**

## Quelles recherches sont envisagées ?

| Point de départ | À quoi cela pourrait servir | Situation |
| --- | --- | --- |
| Nom et prénom | Retrouver des mentions publiques et comparer les sources | Parcours bêta testé avec données fictives |
| Pseudonyme | Chercher un nom d'utilisateur sur différents sites | Collecteurs spécialisés travaillés en développement |
| Entreprise ou association | Consulter des informations publiques sur une structure | Connecteur de données publiques étudié |
| E-mail ou téléphone | Rechercher, si c'est légalement autorisé, des mentions publiques de cet indice | Envisagé, non disponible |
| Photo, domaine ou autre indice | Explorer des pistes et des liens entre sources | À l'étude, non intégré à la bêta |

**Important :** un résultat possible n'est pas une preuve d'identité. Les fonctions présentées ne sont pas ouvertes à des recherches réelles.

## Quels outils utilisons-nous ?

**Ce que nous développons nous-mêmes : SunTinel.** C'est le logiciel qui relie les étapes : dossiers, préparation des recherches, rapprochement et tri des observations, conservation des sources, revue humaine, historique des actions et rapports. Les composants sont encore en test et en stabilisation.

**Les outils externes travaillés :**

- **Sherlock et Maigret** : chercher des pseudonymes sur des sites publics.
- **Tavily et DDGS** : trouver des pages et des informations sur le Web.
- **Recherche d'entreprises** : consulter des informations publiques sur des structures françaises.

Certains composants existent dans le projet sans être autorisés pour des recherches réelles. La présence d'un outil **ne signifie pas qu'il est actif**, disponible ou certifié.

## Comment une investigation devrait-elle se dérouler ?

1. Ouvrir un dossier et définir le but de la recherche.
2. Préparer les critères et vérifier les autorisations nécessaires.
3. Rassembler les observations en gardant leurs sources.
4. Comparer les résultats et retirer les doublons.
5. Examiner les pistes et expliquer les décisions.
6. Produire un rapport avec les réserves utiles.

Ce chemin décrit **l'objectif du produit**, pas un service aujourd'hui disponible.

## Comment protégeons-nous les informations ?

L'accès sera limité aux comptes approuvés, avec des droits distincts pour chaque dossier.

- **Chiffrement :** rendre une information illisible sans la clé permettant de la lire. La protection des échanges, du stockage et des sauvegardes fait partie des exigences ; sa couverture complète reste à valider.
- **Historique d'audit :** garder une trace des actions et des décisions importantes. Des composants existent, mais l'export complet de ces traces reste à qualifier.
- **Rapports exportables :** des exports PDF, texte et données structurées ont été testés sur des scénarios fictifs ; ils ne sont pas encore qualifiés pour un usage réel.
- **Durée de conservation :** ne garder les informations que le temps justifié. Les règles définitives ne sont pas encore arrêtées.

**SunTinel n'est pas présenté comme déjà certifié ou totalement sécurisé.** Voir les [explications simples sur la sécurité et le droit](SECURITE_ET_DROIT.md).

## RGPD et législation

Les informations publiées en ligne restent susceptibles d'être des données personnelles. Les utiliser impose un but légitime, une base juridique adaptée, une collecte proportionnée et des protections appropriées.

Selon le contexte, le **RGPD**, la **loi Informatique et Libertés** ou les règles spécifiques **« Police-Justice »** peuvent s'appliquer. Les conditions doivent être examinées avant tout usage réel ; aucune conformité globale n'est revendiquée à ce stade.

## Qui pourra utiliser SunTinel ?

Le projet vise des enquêteurs et des structures associatives d'investigation identifiés. La future admission sera **manuelle**, sans création automatique de compte. Les comptes approuvés auront les mêmes fonctionnalités, mais **pas accès automatiquement aux dossiers des autres**.

Aucun formulaire d'inscription n'est actuellement ouvert.

## Avancement et transparence

- [Feuille de route](ROADMAP.md) : ce qui est évalué, en cours de revue ou prévu.
- [Journal public](CHANGELOG.md) : dernières étapes annoncées.
- [FAQ](FAQ.md) : réponses en langage simple.
- [Sécurité et droit](SECURITE_ET_DROIT.md) : protections, limites et sources officielles.

**Point d'étape :** un correctif de sécurité ciblé a été accepté après audit indépendant avec réserves. En revanche, le dernier parcours de revue doit encore être corrigé sur ses rapports. Une acceptation partielle ne donne jamais l'autorisation de déployer ou d'effectuer des recherches réelles.

## À propos de ce dépôt

Ce dépôt public héberge **uniquement la vitrine**. Il ne contient ni code privé d'investigation, ni dossier, ni donnée personnelle, ni secret, ni rapport de sécurité confidentiel.

SunTinel est un projet indépendant ; il n'est pas présenté comme un service officiel ou homologué d'une administration. La publication de cette vitrine n'accorde aucune licence sur le code applicatif privé.
