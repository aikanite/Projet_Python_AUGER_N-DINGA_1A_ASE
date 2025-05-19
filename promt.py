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


add_salle("911", "informatique", 4)
