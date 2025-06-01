# Projet_Python_AUGER_N-DINGA_1A_ASE

READMME a regarder dans code sinon la mise en page est pas jolie.

Bonjour

Projet python de N'DINGA Albin et AUGER Kévin (2025)

Résumé du projet : 
Une entreprise nous a contacté et donné un cahier des charges pour une application de réservation de salles. Il y a 3 types de salles : Informatique, Conférence et Standard.
On doit pouvoir ajouter clients et salles, réserver des salles, voir les réservation etc...


Partie Interface; N'DINGA Albin :














Partie données; AUGER Kévin :

Pour cette partie j'ai dû apprendre à me servir de json et structurer les données pour convenir à nos besoins. 
Structure d'un client : 
{
            "AUGER Kevin": {
                "Nom": "AUGER",
                "Prenom": "Kevin",
                "Mail": "kevin.auger@uha.fr",
                "ID": "0000",
                "Reservations": []
            }
}


Structure d'une salle :
{
            "Salle 0": {
                "Type": "Informatique",
                "Capacite": 1,
                "Date d'indisponibilite": []
                }
}

Il a ensuite fallu penser aux réservations qui ont été plus dures a penser puisque les tableaux de "AFFICHER" ne montrent pas le même type de données.

Reservation client : 
{
    "Salle": "Salle 20",
    "Type": "Standard",
    "Capacite": "3",
    "DateDebut": "12/02/2025 \n 08:00",
    "DateFin": "12/02/2025 \n 09:00",
    "Duree": 1.0
}

Reservation Salle :
{
    "DateDebut": "12/02/2025 \n 07:30",
    "DateFin": "12/02/2025 \n 08:30",
     "Duree": 1.0
}

Apres avoir implémenté les fonctions mettant en oeuvre ce systeme de stockage il suffisait de les utiliser dans les fonctions que mon collegue a utilisé pour les boutons correspondants.
Le principal défi était les nouveaux modules à apprendre.


