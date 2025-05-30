import json
import uuid


def write_json(data, filename="data.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


"""
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

reservation_dict = {
    "Salle": room,
    "Type": room_info["Type"],
    "Capacite": room_info["Capacite"],
    "Debut": start_dt,
    "Fin": end_dt,
    "Duree": duration,
}

# Ajout à la réservation du client "AUGER Kevin"
for client in data["Clients"]:
    if "AUGER Kevin" in client:
        client["AUGER Kevin"]["Reservations"].append(reservation_dict)

write_json(data)

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
"""

ID = str(uuid.uuid4())[:4]
print(ID)
