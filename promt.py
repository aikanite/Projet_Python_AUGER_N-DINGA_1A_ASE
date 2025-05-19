import json


def write_json(data, filename="data.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


def add_client(nom: str, prenom: str, mail: str, id: str, reservations=[]):
    """ajouter un nouveau client"""

    with open("data.json") as json_file:
        data = json.load(json_file)
        temp = data["Clients"]
        y = {
            f"Client {len(temp)}": {
                "Nom": nom,
                "Prenom": prenom,
                "Mail": mail,
                "ID": id,
                "Reservations": reservations,
            }
        }  # temp +1 si pas de client 0
        temp.append(y)

    write_json(data)


def add_salle(type: str, C: int, reservations=[]):
    """ajouter une nouvelle salle"""

    with open("data.json") as json_file:
        data = json.load(json_file)
        temp = data["Salles"]
        y = {
            f"Salle {len(temp)}": {
                "Type": type,
                "Capacite": C,
                "Date d'indisponibilite": reservations,  # ["date", ["heure+", "heure-"]]
            }
        }  # temp +1 si pas de salle 0
        temp.append(y)

    write_json(data)
