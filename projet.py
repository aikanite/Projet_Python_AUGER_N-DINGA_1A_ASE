from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import json


# Ecrire dans jason
def write_json(data, filename="data.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


# Fonction pour afficher la page d'accueil
def show_home():
    clear_frame()
    set_active_button("Accueil")
    ttk.Button(frm, text="Ajouter", command=open_add_page).grid(
        column=0, row=0, pady=10, padx=50
    )
    ttk.Button(frm, text="Réserver", command=open_reserve_page).grid(
        column=0, row=1, pady=10
    )
    ttk.Button(frm, text="Afficher", command=open_display_page).grid(
        column=0, row=2, pady=10
    )


# Fonction pour afficher la page Ajouter
def open_add_page():
    clear_frame()
    set_active_button("Ajouter")
    ttk.Button(frm, text="Ajouter un nouveau client", command=add_new_client).grid(
        column=0, row=0, pady=10, padx=50
    )
    ttk.Button(frm, text="Ajouter une nouvelle salle", command=add_new_room).grid(
        column=0, row=1, pady=10
    )
    ttk.Button(frm, text="Retour", command=show_home).grid(column=0, row=2, pady=10)


# Fonction pour ajouter un nouveau client


# Dans json
def add_client(nom: str, prenom: str, mail: str, id=0, reservations=[]):
    """ajouter un nouveau client"""

    with open("data.json") as json_file:
        data = json.load(json_file)
        temp = data["Clients"]
        y = {
            f"{nom} {prenom}": {
                "Nom": nom,
                "Prenom": prenom,
                "Mail": mail,
                "ID": id,
                "Reservations": reservations,
            }
        }  # temp +1 si pas de client 0
        temp.append(y)

    write_json(data)


# Visuellement
def add_new_client():
    clear_frame()
    set_active_button("Ajouter")

    # Titre
    ttk.Label(frm, text="Ajouter un nouveau client", font=("Arial", 14)).grid(
        column=0, row=0, pady=10, columnspan=2
    )

    # Champs de saisie
    ttk.Label(frm, text="Nom:").grid(column=0, row=1, pady=5, sticky=E)
    nom_entry = ttk.Entry(frm)
    nom_entry.grid(column=1, row=1, pady=5, sticky=W)

    ttk.Label(frm, text="Prénom:").grid(column=0, row=2, pady=5, sticky=E)
    prenom_entry = ttk.Entry(frm)
    prenom_entry.grid(column=1, row=2, pady=5, sticky=W)

    ttk.Label(frm, text="Adresse email:").grid(column=0, row=3, pady=5, sticky=E)
    email_entry = ttk.Entry(frm)
    email_entry.grid(column=1, row=3, pady=5, sticky=W)

    # Boutons
    ttk.Button(frm, text="Annuler", command=open_add_page).grid(
        column=0, row=4, pady=20, padx=5, sticky=E
    )
    ttk.Button(
        frm,
        text="Valider",
        command=lambda: validate_client(
            nom_entry.get(), prenom_entry.get(), email_entry.get()
        ),
    ).grid(column=1, row=4, pady=20, padx=5, sticky=W)


# Fonction pour valider l'ajout d'un client
def validate_client(nom, prenom, email):
    if not nom or not prenom or not email:
        messagebox.showerror("Erreur", "Tous les champs sont obligatoires")
    elif "@" not in email:
        messagebox.showerror("Erreur", "Adresse email invalide")
    else:
        add_client(str(nom), str(prenom), str(email))
        messagebox.showinfo("Succès", "Client ajouté avec succès")
        show_home()


# Fonction pour ajouter une nouvelle salle


# Dans json
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


# Visuellement
def add_new_room():
    clear_frame()
    set_active_button("Ajouter")

    # Titre
    ttk.Label(frm, text="Ajouter une nouvelle salle", font=("Arial", 14)).grid(
        column=0, row=0, pady=10, columnspan=2
    )

    # Champs de saisie
    ttk.Label(frm, text="Identifiant de la salle:").grid(
        column=0, row=1, pady=5, sticky=E
    )
    id_entry = ttk.Entry(frm)
    id_entry.grid(column=1, row=1, pady=5, sticky=W)

    ttk.Label(frm, text="Capacité:").grid(column=0, row=2, pady=5, sticky=E)
    capacity_var = StringVar(value="1")
    capacity_spin = Spinbox(
        frm, from_=1, to=10, textvariable=capacity_var, state="readonly"
    )
    capacity_spin.grid(column=1, row=2, pady=5, sticky=W)

    ttk.Label(frm, text="Type de salle:").grid(column=0, row=3, pady=5, sticky=E)
    room_type = StringVar()
    room_type_combobox = ttk.Combobox(
        frm, textvariable=room_type, values=["Standard", "Conference", "Informatique"]
    )
    room_type_combobox.grid(column=1, row=3, pady=5, sticky=W)
    room_type_combobox.current(0)

    # Mise à jour de la capacité en fonction du type
    def update_capacity(*args):
        salle_type = room_type.get()
        if salle_type == "Standard":
            capacity_spin.config(from_=1, to=4)
            capacity_var.set("1")
        elif salle_type == "Conférence":
            capacity_spin.config(from_=4, to=10)
            capacity_var.set("4")
        elif salle_type == "Informatique":
            capacity_spin.config(from_=1, to=4)
            capacity_var.set("1")

    room_type.trace_add("write", update_capacity)

    # Boutons
    ttk.Button(frm, text="Annuler", command=open_add_page).grid(
        column=0, row=4, pady=20, padx=5, sticky=E
    )
    ttk.Button(
        frm,
        text="Valider",
        command=lambda: validate_room(
            id_entry.get(), capacity_spin.get(), room_type.get()
        ),
    ).grid(column=1, row=4, pady=20, padx=5, sticky=W)


# Fonction pour valider l'ajout d'une salle
def validate_room(room_id, capacity, room_type):
    if not room_id:
        messagebox.showerror("Erreur", "L'identifiant de la salle est obligatoire")
    elif not capacity.isdigit() or int(capacity) < 1:
        messagebox.showerror("Erreur", "Capacité invalide")
    elif not room_type:
        messagebox.showerror("Erreur", "Type de salle invalide")
    else:
        add_salle(room_id, room_type, capacity)
        messagebox.showinfo("Succès", "Salle ajoutée avec succès")
        show_home()


# Fonction pour afficher la page Réserver
def open_reserve_page():
    clear_frame()
    set_active_button("Réserver")

    # Titre
    ttk.Label(frm, text="Réserver une salle", font=("Arial", 14)).grid(
        column=0, row=0, pady=10, columnspan=4
    )

    # Section Date et Heure de début
    ttk.Label(frm, text="Date de début:").grid(column=0, row=1, pady=5, sticky=E)
    start_date_entry = ttk.Entry(frm, width=10)
    start_date_entry.grid(column=1, row=1, pady=5, sticky=W)
    ttk.Label(frm, text="JJ/MM/AAAA").grid(column=2, row=1, sticky=W)

    ttk.Label(frm, text="Heure de début:").grid(column=0, row=2, pady=5, sticky=E)
    start_time_entry = ttk.Entry(frm, width=5)
    start_time_entry.grid(column=1, row=2, pady=5, sticky=W)
    ttk.Label(frm, text="HH:MM").grid(column=2, row=2, sticky=W)

    # Section Date et Heure de fin
    ttk.Label(frm, text="Date de fin:").grid(column=0, row=3, pady=5, sticky=E)
    end_date_entry = ttk.Entry(frm, width=10)
    end_date_entry.grid(column=1, row=3, pady=5, sticky=W)
    ttk.Label(frm, text="JJ/MM/AAAA").grid(column=2, row=3, sticky=W)

    ttk.Label(frm, text="Heure de fin:").grid(column=0, row=4, pady=5, sticky=E)
    end_time_entry = ttk.Entry(frm, width=5)
    end_time_entry.grid(column=1, row=4, pady=5, sticky=W)
    ttk.Label(frm, text="HH:MM").grid(column=2, row=4, sticky=W)

    # Section Client
    with open("data.json", "r") as f:
        data = json.load(f)

    clients = data["Clients"]
    liste_cles = [list(client.keys())[0] for client in clients]

    ttk.Label(frm, text="Client:").grid(column=0, row=5, pady=5, sticky=E)

    client_var = StringVar()
    client_combobox = ttk.Combobox(frm, textvariable=client_var, values=liste_cles)
    client_combobox.grid(column=1, row=5, pady=5, sticky=W, columnspan=2)
    client_combobox.set("Sélectionner un client")

    # Boutons
    ttk.Button(frm, text="Annuler", command=show_home).grid(
        column=0, row=6, pady=20, sticky=E, columnspan=2
    )
    ttk.Button(
        frm,
        text="Valider",
        command=lambda: validate_reservation(
            start_date_entry.get(),
            start_time_entry.get(),
            end_date_entry.get(),
            end_time_entry.get(),
            client_var.get(),
        ),
    ).grid(column=2, row=6, pady=20, sticky=W, columnspan=2)


def validate_reservation(start_date, start_time, end_date, end_time, client):
    def is_valid_date(date_str):
        try:
            day, month, year = map(int, date_str.split("/"))
            if len(date_str) != 10 or date_str[2] != "/" or date_str[5] != "/":
                return False
            return 1 <= day <= 31 and 1 <= month <= 12 and year == 2025
        except:
            return False

    def is_valid_time(time_str):
        try:
            hours, minutes = map(int, time_str.split(":"))
            return 0 <= hours <= 23 and 0 <= minutes <= 59 and len(time_str) == 5
        except:
            return False

    # Validation des champs
    errors = []
    if not start_date:
        errors.append("Date de début manquante")
    elif not is_valid_date(start_date):
        errors.append("Date début invalide (JJ/MM/2025 obligatoire)")

    if not start_time:
        errors.append("Heure de début manquante")
    elif not is_valid_time(start_time):
        errors.append("Heure début invalide (HH:MM)")

    if not end_date:
        errors.append("Date de fin manquante")
    elif not is_valid_date(end_date):
        errors.append("Date fin invalide (JJ/MM/2025 obligatoire)")

    if not end_time:
        errors.append("Heure de fin manquante")
    elif not is_valid_time(end_time):
        errors.append("Heure fin invalide (HH:MM)")

    if client == "Sélectionner un client":
        errors.append("Client non sélectionné")

    if errors:
        messagebox.showerror("Erreurs", "\n".join(errors))
    else:
        show_room_selection(start_date, start_time, end_date, end_time, client)


def show_room_selection(start_date, start_time, end_date, end_time, client):
    clear_frame()

    # Calcul de la durée
    def calculate_duration(start, end):
        start_h, start_m = map(int, start.split(":"))
        end_h, end_m = map(int, end.split(":"))
        total_min = (end_h * 60 + end_m) - (start_h * 60 + start_m)
        return f"{total_min // 60}h{total_min % 60:02d}"

    duration = calculate_duration(start_time, end_time)

    # Titre
    ttk.Label(frm, text="Réserver une salle : ", font=("Arial", 14)).grid(
        column=0, row=0, pady=10, columnspan=4
    )

    # Affichage des informations
    ttk.Label(frm, text="Client:", font=("Arial", 10, "bold")).grid(
        column=0, row=1, sticky=E
    )
    ttk.Label(frm, text=client).grid(column=1, row=1, sticky=W, columnspan=3)

    ttk.Label(frm, text="Début:", font=("Arial", 10, "bold")).grid(
        column=0, row=2, sticky=E
    )
    ttk.Label(frm, text=f"{start_date} {start_time}").grid(column=1, row=2, sticky=W)

    ttk.Label(frm, text="Fin:", font=("Arial", 10, "bold")).grid(
        column=2, row=2, sticky=E
    )
    ttk.Label(frm, text=f"{end_date} {end_time}").grid(column=3, row=2, sticky=W)

    ttk.Label(frm, text="Durée:", font=("Arial", 10, "bold")).grid(
        column=0, row=3, sticky=E
    )
    ttk.Label(frm, text=duration).grid(column=1, row=3, sticky=W)

    # Séparation
    ttk.Separator(frm, orient=HORIZONTAL).grid(
        column=0, row=4, columnspan=4, pady=10, sticky="ew"
    )

    # Section Sélection de salle
    ttk.Label(frm, text="Sélectionnez une salle:", font=("Arial", 12)).grid(
        column=0, row=5, columnspan=4, pady=5
    )

    # Type de salle
    ttk.Label(frm, text="Type de salle:").grid(column=0, row=6, sticky=E)
    room_type = StringVar()
    room_type_combobox = ttk.Combobox(
        frm,
        textvariable=room_type,
        values=["Standard", "Conference", "Informatique"],
        state="readonly",
    )
    room_type_combobox.grid(column=1, row=6, sticky=W)
    room_type_combobox.current(0)

    # Bouton pour afficher les salles disponibles
    ttk.Button(
        frm,
        text="Voir salles disponibles",
        command=lambda: show_available_rooms(room_type.get()),
    ).grid(column=2, row=6, columnspan=2, sticky=W)

    # Liste des salles disponibles
    rooms_listbox = Listbox(frm, height=4, selectmode=SINGLE)
    rooms_listbox.grid(column=0, row=7, columnspan=4, pady=10, sticky="ew")

    # Boutons
    ttk.Button(frm, text="Retour", command=open_reserve_page).grid(
        column=0, row=8, pady=20, sticky=E, columnspan=2
    )
    ttk.Button(
        frm,
        text="Confirmer",
        command=lambda: finalize_reservation(
            client,
            f"{start_date} {start_time}",
            f"{end_date} {end_time}",
            rooms_listbox.get(ACTIVE),
        ),
    ).grid(column=2, row=8, pady=20, sticky=W, columnspan=2)

    # Fonction pour afficher les salles disponibles
    def show_available_rooms(selected_type):
        with open("data.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        salles = data["Salles"]
        liste_cles_salles = [list(salle.keys())[0] for salle in salles]

        # Dictionnaire pour stocker les salles triées par catégorie
        categories = {"Informatique": [], "Conference": [], "Standard": []}

        for salle in salles:
            for nom_salle, infos in salle.items():
                cat = infos.get("Type")
                if cat in categories:
                    categories[cat].append(nom_salle)
                else:
                    categories["Standard"].append(
                        nom_salle
                    )  # Par défaut si catégorie inconnue

        rooms_listbox.delete(0, END)
        # Exemple de données
        available_rooms = categories
        for room in available_rooms.get(selected_type, []):
            rooms_listbox.insert(END, room)

    # Initialisation
    show_available_rooms(room_type.get())


def finalize_reservation(client, start, end, room):
    if not room:
        messagebox.showerror("Erreur", "Veuillez sélectionner une salle")
    else:
        messagebox.showinfo(
            "Succès",
            f"Réservation confirmée pour:\n"
            f"Client: {client}\n"
            f"Salle: {room}\n"
            f"Du {start} au {end}",
        )
        show_home()


# Fonction pour afficher la page Afficher
def open_display_page():
    clear_frame()
    set_active_button("Afficher")
    ttk.Label(frm, text="Contenu de la page Afficher").grid(column=0, row=0, pady=10)
    ttk.Button(frm, text="Retour", command=show_home).grid(column=0, row=1, pady=10)


# Fonction pour nettoyer le contenu du cadre principal
def clear_frame():
    for widget in frm.winfo_children():
        widget.destroy()


# Fonction pour mettre à jour le bouton actif avec une couleur bleue
def set_active_button(active_page):
    for button in nav_buttons:
        if button["text"] == active_page:
            button.config(bg="#0078D7", fg="blue")  # Fond bleu pour le bouton actif
        else:
            button.config(
                bg="SystemButtonFace", fg="black"
            )  # Couleur par défaut pour les autres boutons


# Fenêtre principale
root = Tk()
root.title("MeetingPro")
root.geometry("800x600")  # Taille adaptée
root.configure(bg="lightgray")  # Couleur d'arrière-plan pour distinguer la fenêtre

# Barre de navigation horizontale
nav_frame = Frame(root, bg="white")
nav_frame.pack(side=TOP, fill=X)

# Boutons de navigation
nav_buttons = []
nav_buttons.append(
    Button(nav_frame, text="Accueil", command=show_home, width=15, relief=FLAT)
)
nav_buttons.append(
    Button(nav_frame, text="Ajouter", command=open_add_page, width=15, relief=FLAT)
)
nav_buttons.append(
    Button(nav_frame, text="Réserver", command=open_reserve_page, width=15, relief=FLAT)
)
nav_buttons.append(
    Button(nav_frame, text="Afficher", command=open_display_page, width=15, relief=FLAT)
)

# Afficher les boutons dans la barre de navigation
for button in nav_buttons:
    button.pack(side=LEFT, padx=5, pady=5)

# Cadre principal pour le contenu
frm = ttk.Frame(root, padding=20)
frm.pack(expand=True)

# Centrer les widgets du cadre
frm.columnconfigure(0, weight=1)
frm.columnconfigure(1, weight=1)
for i in range(5):
    frm.rowconfigure(i, weight=1)

# Afficher la page d'accueil par défaut
show_home()

root.mainloop()
