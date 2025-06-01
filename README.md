# Projet_Python_AUGER_N-DINGA_1A_ASE

Projet python de N'DINGA Albin et AUGER Kévin (2025)

### Résumé de la démarche et répartition des tâches

Notre projet consistait à développer une application Python avec une interface graphique pour la gestion des réservations de salles de coworking pour l'entreprise MeetingPro. Nous avons adopté une approche modulaire en séparant le projet en deux parties principales :

Partie Interface Graphique : Pris en charge par Ndinga Albin, qui a conçu et implémenté toutes les interfaces utilisateur (menus, formulaires, affichages) en utilisant Tkinter.
Partie Données : Pris en charge par Kevin, qui a géré la modélisation des données (clients, salles, réservations), la persistance des données dans un fichier JSON, et la logique métier (validation des créneaux, gestion des réservations).
Cette répartition nous a permis de travailler en parallèle tout en assurant une bonne cohérence entre les fonctionnalités et leur affichage.

### Fonctionnement général de l'application

L'application permet aux utilisateurs de :

1. Ajouter des clients et des salles :
Les clients sont enregistrés avec leur nom, prénom, email et un identifiant unique.
Les salles sont classées par type (Standard, Conférence, Informatique) avec des capacités spécifiques.
2. Réserver des salles :
Un client sélectionne un créneau horaire (date et heure de début/fin).
Le système vérifie la disponibilité des salles et propose celles compatibles.
3. Afficher des informations :
Consultation des listes de clients, de salles, et des réservations par client.
Visualisation des salles disponibles pour un créneau donné.
L'interface est intuitive, avec un menu principal et des sous-menus pour chaque fonctionnalité. Les données sont sauvegardées dans un fichier JSON pour assurer la persistance.

### Partie Interface; N'DINGA Albin :

L'interface graphique de l'application a été développée avec `tkinter`, offrant une expérience utilisateur intuitive et responsive. Elle est structurée autour de quatre onglets principaux accessibles depuis une barre de navigation :

1. **Accueil** : Point d'entrée avec des boutons pour accéder aux fonctionnalités clés (Ajouter, Réserver, Afficher).
2. **Ajouter** : Permet d'ajouter un nouveau client ou une nouvelle salle avec des formulaires de saisie et des validations.
3. **Réserver** : Guide l'utilisateur à travers la réservation d'une salle (sélection de créneau, choix de salle, confirmation).
4. **Afficher** : Affiche les listes de salles, de clients, les réservations par client, et les salles disponibles pour un créneau.

### Fonctionnalités Graphiques
- **Styles Personnalisés** : Utilisation de `ttk.Style` pour une apparence moderne (boutons, arrière-plans, polices).
- **Validation des Données** : Contrôles des saisies (dates, emails, capacités) avec messages d'erreur explicites.
- **Affichage Tabulaire** : Tables interactives (`ttk.Treeview`) pour les listes de salles, clients et réservations, avec barres de défilement.
- **Adaptabilité** : Redimensionnement dynamique des éléments pour s'adapter à la taille de la fenêtre.

### Exemples d'Écrans
- **Formulaire de Réservation** : Sélection de créneau avec vérification des conflits.
- **Confirmation** : Récapitulatif visuel après une réservation réussie.
- **Tableaux** : Tri et affichage clair des données (ex : salles disponibles par type).


### Partie données; AUGER Kévin :

Pour cette partie j'ai dû apprendre à me servir de json et structurer les données pour convenir à nos besoins. 
### Structure d'un client : 
{
            "AUGER Kevin": {
                "Nom": "AUGER",
                "Prenom": "Kevin",
                "Mail": "kevin.auger@uha.fr",
                "ID": "0000",
                "Reservations": []
            }
}


### Structure d'une salle :
{
            "Salle 0": {
                "Type": "Informatique",
                "Capacite": 1,
                "Date d'indisponibilite": []
                }
}

Il a ensuite fallu penser aux réservations qui ont été plus dures a penser puisque les tableaux de "AFFICHER" ne montrent pas le même type de données.

### Reservation client : 
{
    "Salle": "Salle 20",
    "Type": "Standard",
    "Capacite": "3",
    "DateDebut": "12/02/2025 \n 08:00",
    "DateFin": "12/02/2025 \n 09:00",
    "Duree": 1.0
}

### Reservation Salle :
{
    "DateDebut": "12/02/2025 \n 07:30",
    "DateFin": "12/02/2025 \n 08:30",
     "Duree": 1.0
}

Apres avoir implémenté les fonctions mettant en oeuvre ce systeme de stockage il suffisait de les utiliser dans les fonctions que mon collegue a utilisé pour les boutons correspondants.


### Problèmes rencontrés et solutions

### Problème majeur : Compatibilité entre macOS et Windows

Description : Albin travaillant sur macOS et Kevin sur Windows, nous avons rencontré des différences dans le rendu des interfaces graphiques (Tkinter). Par exemple, les polices et les tailles des widgets n'étaient pas toujours cohérentes entre les deux systèmes.
Solution : Nous avons standardisé les styles en utilisant des configurations explicites (tailles fixes, polices communes) et testé l'application sur les deux systèmes pour ajuster les détails.
Autres problèmes :

Gestion des dates/heures : La validation des créneaux horaires (durée minimale de 30 min) a été complexe. Nous avons utilisé le module datetime pour comparer les heures et calculer les durées.
Persistance des données : L'écriture/lecture du fichier JSON posait parfois des problèmes de format. Nous avons ajouté des vérifications d'intégrité et des messages d'erreur clairs.
Ressources utilisées

Pour mener à bien le projet, nous avons utilisé :

1. Fichier fourni : Le PDF du projet a servi de référence pour les consignes et les attentes fonctionnelles.
2. Outils en ligne :
Google : Pour rechercher des solutions techniques (ex : utilisation de Tkinter, gestion des dates).
GitHub Copilot : Pour générer des snippets de code et accélérer le développement.
Documentation Python : La fonction help() et les docs officielles (Tkinter, JSON) nous ont aidés à comprendre les modules.
Vidéos sur le MVC : Les liens YouTube fournis dans le sujet nous ont éclairés sur l'architecture Model-View-Controller.

### Conclusion

Ce projet nous a permis d'appliquer nos compétences en Python et en travail collaboratif. Malgré les défis techniques, nous avons livré une application fonctionnelle et intuitive. La répartition des tâches était équilibrée, avec une bonne communication pour intégrer nos parties respectives.

### Contributeurs :

Ndinga Albin (Interface Graphique)
Kevin (Gestion des Données)
Date de rendu : 1 juin 2025


