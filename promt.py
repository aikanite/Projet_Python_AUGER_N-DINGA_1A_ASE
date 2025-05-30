import json


def write_json(data, filename="data.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


def add_salle(roomid: str, type: str, C: int, reservations=[]):
    """ajouter une nouvelle salle"""

    with open("data.json") as json_file:
        data = json.load(json_file)
        temp = data["Salles"]
        y = {
            f"Salle {roomid}": {
                "Room Id": roomid,
                "Type": type,
                "Capacite": C,
                "Date d'indisponibilite": reservations,  # ["date", ["heure+", "heure-"]]
            }
        }  # temp +1 si pas de salle 0
        temp.append(y)

    write_json(data)


with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

salles = data["Salles"]
liste_cles_salles = [list(salle.keys())[0] for salle in salles]
print(liste_cles_salles)


# Dictionnaire pour stocker les salles triées par catégorie
categories = {"Informatique": [], "Conférence": [], "Standard": []}

for salle in salles:
    for nom_salle, infos in salle.items():
        cat = infos.get("Type")
        if cat in categories:
            categories[cat].append(nom_salle)
        else:
            categories["Standard"].append(nom_salle)  # Par défaut si catégorie inconnue

print(categories)


# IDENTIFIANT CLIENT
import uuid


ID = uuid.bytes_()

str(ID)
print(ID)
