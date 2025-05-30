# Importations
from tkinter import *
from datetime import datetime
from tkinter import ttk
from tkinter import messagebox
import json


# Fonctions utilitaires
def write_json(data, filename="data.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


def clear_frame():
    for widget in frm.winfo_children():
        widget.destroy()


def set_active_button(active_page):
    for button in nav_buttons:
        if button["text"] == active_page:
            button.config(bg="#0078D7", fg="blue")
        else:
            button.config(bg="SystemButtonFace", fg="black")


# Fonctions principales - Navigation
def show_home():
    clear_frame()
    set_active_button("Accueil")

    # Style personnalisé pour les boutons
    style = ttk.Style()
    style.configure(
        "Accueil.TButton",
        font=("Arial", 14, "bold"),
        padding=20,
        width=15,
        relief="solid",
        borderwidth=2,
    )

    # Cadre principal qui s'étire
    main_frame = ttk.Frame(frm)
    main_frame.grid(column=0, row=0, sticky="nsew", padx=50, pady=50)

    # Configuration du redimensionnement
    frm.columnconfigure(0, weight=1)
    frm.rowconfigure(0, weight=1)
    main_frame.columnconfigure(0, weight=1)
    for i in range(3):  # 3 lignes pour les boutons
        main_frame.rowconfigure(i, weight=1)

    # Boutons qui s'adaptent
    btn_add = ttk.Button(
        main_frame, text="Ajouter", command=open_add_page, style="Accueil.TButton"
    )
    btn_add.grid(column=0, row=0, sticky="nsew", padx=20, pady=10)

    btn_reserve = ttk.Button(
        main_frame, text="Réserver", command=open_reserve_page, style="Accueil.TButton"
    )
    btn_reserve.grid(column=0, row=1, sticky="nsew", padx=20, pady=10)

    btn_display = ttk.Button(
        main_frame, text="Afficher", command=open_display_page, style="Accueil.TButton"
    )
    btn_display.grid(column=0, row=2, sticky="nsew", padx=20, pady=10)

    # Adapter dynamiquement la taille de police
    def adjust_font(event):
        new_size = max(10, min(24, int(event.width / 40)))
        style.configure("Accueil.TButton", font=("Arial", new_size, "bold"))

    main_frame.bind("<Configure>", adjust_font)


# Fonctions pour la section Ajouter
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


def add_client(nom: str, prenom: str, mail: str, id=0, reservations=[]):
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
        }
        temp.append(y)
    write_json(data)


def add_new_client():
    clear_frame()
    set_active_button("Ajouter")
    ttk.Label(frm, text="Ajouter un nouveau client", font=("Arial", 14)).grid(
        column=0, row=0, pady=10, columnspan=2
    )
    ttk.Label(frm, text="Nom:").grid(column=0, row=1, pady=5, sticky=E)
    nom_entry = ttk.Entry(frm)
    nom_entry.grid(column=1, row=1, pady=5, sticky=W)
    ttk.Label(frm, text="Prénom:").grid(column=0, row=2, pady=5, sticky=E)
    prenom_entry = ttk.Entry(frm)
    prenom_entry.grid(column=1, row=2, pady=5, sticky=W)
    ttk.Label(frm, text="Adresse email:").grid(column=0, row=3, pady=5, sticky=E)
    email_entry = ttk.Entry(frm)
    email_entry.grid(column=1, row=3, pady=5, sticky=W)
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


def validate_client(nom, prenom, email):
    if not nom or not prenom or not email:
        messagebox.showerror("Erreur", "Tous les champs sont obligatoires")
    elif "@" not in email:
        messagebox.showerror("Erreur", "Adresse email invalide")
    else:
        add_client(str(nom), str(prenom), str(email))
        messagebox.showinfo("Succès", "Client ajouté avec succès")
        show_home()


def add_salle(roomid: str, type: str, C: int, reservations=[]):
    with open("data.json") as json_file:
        data = json.load(json_file)
        temp = data["Salles"]
        y = {
            f"Salle {roomid}": {
                "Room Id": roomid,
                "Type": type,
                "Capacite": C,
                "Date d'indisponibilite": reservations,
            }
        }
        temp.append(y)
    write_json(data)


def add_new_room():
    clear_frame()
    set_active_button("Ajouter")
    ttk.Label(frm, text="Ajouter une nouvelle salle", font=("Arial", 14)).grid(
        column=0, row=0, pady=10, columnspan=2
    )
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


# Fonctions pour la section Réserver
def open_reserve_page():
    clear_frame()
    set_active_button("Réserver")
    ttk.Label(frm, text="Réserver une salle", font=("Arial", 14)).grid(
        column=0, row=0, pady=10, columnspan=4
    )
    ttk.Label(frm, text="Date de début:").grid(column=0, row=1, pady=5, sticky=E)
    start_date_entry = ttk.Entry(frm, width=10)
    start_date_entry.grid(column=1, row=1, pady=5, sticky=W)
    ttk.Label(frm, text="JJ/MM/AAAA").grid(column=2, row=1, sticky=W)
    ttk.Label(frm, text="Heure de début:").grid(column=0, row=2, pady=5, sticky=E)
    start_time_entry = ttk.Entry(frm, width=5)
    start_time_entry.grid(column=1, row=2, pady=5, sticky=W)
    ttk.Label(frm, text="HH:MM").grid(column=2, row=2, sticky=W)
    ttk.Label(frm, text="Date de fin:").grid(column=0, row=3, pady=5, sticky=E)
    end_date_entry = ttk.Entry(frm, width=10)
    end_date_entry.grid(column=1, row=3, pady=5, sticky=W)
    ttk.Label(frm, text="JJ/MM/AAAA").grid(column=2, row=3, sticky=W)
    ttk.Label(frm, text="Heure de fin:").grid(column=0, row=4, pady=5, sticky=E)
    end_time_entry = ttk.Entry(frm, width=5)
    end_time_entry.grid(column=1, row=4, pady=5, sticky=W)
    ttk.Label(frm, text="HH:MM").grid(column=2, row=4, sticky=W)
    ttk.Label(frm, text="Client:").grid(column=0, row=5, pady=5, sticky=E)

    with open("data.json", "r") as f:
        data = json.load(f)
    clients = data["Clients"]
    liste_cles = [list(client.keys())[0] for client in clients]
    client_var = StringVar()
    client_combobox = ttk.Combobox(frm, textvariable=client_var, values=liste_cles)
    client_combobox.grid(column=1, row=5, pady=5, sticky=W, columnspan=2)
    client_combobox.set("Sélectionner un client")
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

    def calculate_duration(start, end):
        start_h, start_m = map(int, start.split(":"))
        end_h, end_m = map(int, end.split(":"))
        total_min = (end_h * 60 + end_m) - (start_h * 60 + start_m)
        return f"{total_min // 60}h{total_min % 60:02d}"

    duration = calculate_duration(start_time, end_time)
    ttk.Label(frm, text="Réserver une salle : ", font=("Arial", 14)).grid(
        column=0, row=0, pady=10, columnspan=4
    )
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
    ttk.Separator(frm, orient=HORIZONTAL).grid(
        column=0, row=4, columnspan=4, pady=10, sticky="ew"
    )
    ttk.Label(frm, text="Sélectionnez une salle:", font=("Arial", 12)).grid(
        column=0, row=5, columnspan=4, pady=5
    )
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
    ttk.Button(
        frm,
        text="Voir salles disponibles",
        command=lambda: show_available_rooms(room_type.get()),
    ).grid(column=2, row=6, columnspan=2, sticky=W)
    rooms_listbox = Listbox(frm, height=4, selectmode=SINGLE)
    rooms_listbox.grid(column=0, row=7, columnspan=4, pady=10, sticky="ew")
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

    def show_available_rooms(selected_type):
        with open("data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        salles = data["Salles"]
        liste_cles_salles = [list(salle.keys())[0] for salle in salles]
        categories = {"Informatique": [], "Conference": [], "Standard": []}
        for salle in salles:
            for nom_salle, infos in salle.items():
                cat = infos.get("Type")
                if cat in categories:
                    categories[cat].append(nom_salle)
                else:
                    categories["Standard"].append(nom_salle)
        rooms_listbox.delete(0, END)
        available_rooms = categories
        for room in available_rooms.get(selected_type, []):
            rooms_listbox.insert(END, room)

    show_available_rooms(room_type.get())


def show_reservation_confirmation(
    client, start, end, duration, room, room_type, capacity
):
    clear_frame()
    ttk.Label(frm, text="Réservation Validée!", font=("Arial", 16, "bold")).grid(
        column=0, row=0, pady=20, columnspan=2
    )
    ttk.Label(frm, text="Client:", font=("Arial", 12, "bold")).grid(
        column=0, row=1, sticky=E, pady=5
    )
    ttk.Label(frm, text=client, font=("Arial", 12)).grid(
        column=1, row=1, sticky=W, pady=5
    )
    ttk.Label(frm, text="Début:", font=("Arial", 12)).grid(
        column=0, row=2, sticky=E, pady=5
    )
    ttk.Label(frm, text=start).grid(column=1, row=2, sticky=W, pady=5)
    ttk.Label(frm, text="Fin:", font=("Arial", 12)).grid(
        column=0, row=3, sticky=E, pady=5
    )
    ttk.Label(frm, text=end).grid(column=1, row=3, sticky=W, pady=5)
    ttk.Label(frm, text="Durée:", font=("Arial", 12)).grid(
        column=0, row=4, sticky=E, pady=5
    )
    ttk.Label(frm, text=duration).grid(column=1, row=4, sticky=W, pady=5)
    ttk.Label(frm, text="Salle:", font=("Arial", 12, "bold")).grid(
        column=0, row=5, sticky=E, pady=5
    )
    ttk.Label(frm, text=room, font=("Arial", 12)).grid(
        column=1, row=5, sticky=W, pady=5
    )
    ttk.Label(frm, text="Type:", font=("Arial", 12)).grid(
        column=0, row=6, sticky=E, pady=5
    )
    ttk.Label(frm, text=room_type).grid(column=1, row=6, sticky=W, pady=5)
    ttk.Label(frm, text="Capacité:", font=("Arial", 12)).grid(
        column=0, row=7, sticky=E, pady=5
    )
    ttk.Label(frm, text=capacity).grid(column=1, row=7, sticky=W, pady=5)
    ttk.Button(frm, text="Menu principal", command=show_home).grid(
        column=0, row=8, columnspan=2, pady=20
    )
    frm.columnconfigure(0, weight=1)
    frm.columnconfigure(1, weight=1)


def finalize_reservation(client, start, end, room):
    if not room:
        messagebox.showerror("Erreur", "Veuillez sélectionner une salle")
    else:
        with open("data.json", "r") as f:
            data = json.load(f)
            room_info = None
            for salle in data["Salles"]:
                if room in salle:
                    room_info = salle[room]
                    break

        if room_info:
            start_dt = datetime.strptime(start, "%d/%m/%Y %H:%M")
            end_dt = datetime.strptime(end, "%d/%m/%Y %H:%M")
            duration = end_dt - start_dt
            hours = duration.seconds // 3600
            minutes = (duration.seconds % 3600) // 60
            duration_str = f"{hours}h{minutes:02d}"
            show_reservation_confirmation(
                client=client,
                start=start,
                end=end,
                duration=duration_str,
                room=room,
                room_type=room_info["Type"],
                capacity=room_info["Capacite"],
            )


# Fonctions pour la section Afficher
def open_display_page():
    clear_frame()
    set_active_button("Afficher")
    ttk.Label(frm, text="Afficher les informations", font=("Arial", 14)).grid(
        column=0, row=0, pady=20, columnspan=2
    )
    ttk.Button(
        frm,
        text="Afficher liste des salles",
        command=display_rooms_list,
        width=30,
    ).grid(column=0, row=1, pady=10, padx=10, columnspan=2)
    ttk.Button(
        frm,
        text="Afficher liste des clients",
        command=display_clients_list,
        width=30,
    ).grid(column=0, row=2, pady=10, padx=10, columnspan=2)
    ttk.Button(
        frm,
        text="Afficher les salles disponibles pour un créneau",
        command=display_available_slots,
        width=30,
    ).grid(column=0, row=3, pady=10, padx=10, columnspan=2)
    ttk.Button(
        frm,
        text="Afficher les réservations d'un client",
        command=display_client_reservations,
        width=30,
    ).grid(column=0, row=4, pady=10, padx=10, columnspan=2)
    ttk.Button(frm, text="Retour", command=show_home).grid(
        column=0, row=5, pady=20, columnspan=2
    )
    frm.columnconfigure(0, weight=1)
    frm.columnconfigure(1, weight=1)


def display_rooms_list():
    clear_frame()
    set_active_button("Afficher")
    ttk.Label(frm, text="Liste des salles", font=("Arial", 14)).grid(
        column=0, row=0, pady=10, columnspan=3, sticky="n"
    )
    table_frame = ttk.Frame(frm)
    table_frame.grid(column=0, row=1, columnspan=3, pady=10, sticky="nsew")
    scrollbar = ttk.Scrollbar(table_frame)
    scrollbar.pack(side=RIGHT, fill=Y)
    style = ttk.Style()
    style.configure(
        "Treeview",
        rowheight=25,
        background="white",
        fieldbackground="white",
        font=("Arial", 10),
    )
    style.configure(
        "Treeview.Heading", font=("Arial", 10, "bold"), background="#f0f0f0"
    )
    style.map("Treeview", background=[("selected", "#0078D7")])
    columns = ("identifiant", "type", "capacite")
    tree = ttk.Treeview(
        table_frame,
        columns=columns,
        show="headings",
        yscrollcommand=scrollbar.set,
        height=10,
    )
    tree.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.config(command=tree.yview)
    tree.heading("identifiant", text="Identifiant")
    tree.heading("type", text="Type")
    tree.heading("capacite", text="Capacité")
    tree.column("identifiant", width=150, anchor=CENTER)
    tree.column("type", width=150, anchor=CENTER)
    tree.column("capacite", width=100, anchor=CENTER)

    try:
        with open("data.json", "r") as f:
            data = json.load(f)
            rooms = data.get("Salles", [])
            for room_data in rooms:
                for room_name, room_info in room_data.items():
                    tree.insert(
                        "",
                        END,
                        values=(
                            room_name,
                            room_info.get("Type", ""),
                            str(room_info.get("Capacite", "")),
                        ),
                    )
    except FileNotFoundError:
        messagebox.showerror("Erreur", "Fichier de données introuvable")
    except json.JSONDecodeError:
        messagebox.showerror("Erreur", "Fichier JSON invalide")

    ttk.Button(frm, text="Retour", command=open_display_page).grid(
        column=0, row=2, pady=20, columnspan=3
    )
    frm.grid_rowconfigure(1, weight=1)
    for i in range(6):
        frm.grid_columnconfigure(i, weight=1)


def display_clients_list():
    clear_frame()
    set_active_button("Afficher")
    ttk.Label(frm, text="Liste des clients", font=("Arial", 14)).grid(
        column=0, row=0, pady=10, columnspan=4, sticky="n"
    )
    table_frame = ttk.Frame(frm)
    table_frame.grid(column=0, row=1, columnspan=4, pady=10, sticky="nsew")
    scrollbar = ttk.Scrollbar(table_frame)
    scrollbar.pack(side=RIGHT, fill=Y)
    style = ttk.Style()
    style.configure(
        "Treeview",
        rowheight=25,
        background="white",
        fieldbackground="white",
        font=("Arial", 10),
    )
    style.configure(
        "Treeview.Heading", font=("Arial", 10, "bold"), background="#f0f0f0"
    )
    style.map("Treeview", background=[("selected", "#0078D7")])
    columns = ("nom", "prenom", "email", "id")
    tree = ttk.Treeview(
        table_frame,
        columns=columns,
        show="headings",
        yscrollcommand=scrollbar.set,
        height=10,
    )
    tree.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.config(command=tree.yview)
    tree.heading("nom", text="Nom")
    tree.heading("prenom", text="Prénom")
    tree.heading("email", text="Adresse email")
    tree.heading("id", text="ID")
    tree.column("nom", width=120, anchor=W)
    tree.column("prenom", width=120, anchor=W)
    tree.column("email", width=200, anchor=W)
    tree.column("id", width=80, anchor=CENTER)

    try:
        with open("data.json", "r") as f:
            data = json.load(f)
            clients = data.get("Clients", [])
            for client_data in clients:
                for client_key, client_info in client_data.items():
                    tree.insert(
                        "",
                        END,
                        values=(
                            client_info.get("Nom", ""),
                            client_info.get("Prenom", ""),
                            client_info.get("Mail", ""),
                            str(client_info.get("ID", "")),
                        ),
                    )
    except FileNotFoundError:
        messagebox.showerror("Erreur", "Fichier de données introuvable")
    except json.JSONDecodeError:
        messagebox.showerror("Erreur", "Fichier JSON invalide")

    ttk.Button(frm, text="Retour", command=open_display_page).grid(
        column=0, row=2, pady=20, columnspan=4
    )
    frm.grid_rowconfigure(1, weight=1)
    for i in range(4):
        frm.grid_columnconfigure(i, weight=1)


def display_client_reservations():
    clear_frame()
    set_active_button("Afficher")
    ttk.Label(
        frm, text="Rechercher les réservations d'un client ", font=("Arial", 14)
    ).grid(column=0, row=0, pady=20, columnspan=2)

    try:
        with open("data.json", "r") as f:
            data = json.load(f)
            clients = [list(client.keys())[0] for client in data.get("Clients", [])]
    except FileNotFoundError:
        clients = []
        messagebox.showerror("Erreur", "Fichier de données introuvable")

    ttk.Label(frm, text="Client:").grid(column=0, row=1, pady=10, sticky="e")
    client_var = StringVar()
    client_combobox = ttk.Combobox(frm, textvariable=client_var, values=clients)
    client_combobox.grid(column=1, row=1, pady=10, sticky="ew")
    client_combobox.set("Sélectionner un client")
    button_frame = ttk.Frame(frm)
    button_frame.grid(column=0, row=2, columnspan=2, pady=20)
    ttk.Button(button_frame, text="Annuler", command=open_display_page).pack(
        side=LEFT, padx=10
    )
    ttk.Button(
        button_frame,
        text="Valider",
        command=lambda: show_reservations_table(client_var.get()),
    ).pack(side=LEFT, padx=10)
    frm.columnconfigure(1, weight=1)


def show_reservations_table(client_name):
    if not client_name or client_name == "Aucun client disponible":
        messagebox.showwarning("Erreur", "Veuillez sélectionner un client valide")
        return

    clear_frame()
    set_active_button("Afficher")
    ttk.Label(
        frm, text=f"Réservations du client : {client_name}", font=("Arial", 14)
    ).grid(column=0, row=0, pady=10, columnspan=6)
    table_frame = ttk.Frame(frm)
    table_frame.grid(column=0, row=1, columnspan=6, pady=10, sticky="nsew")
    scrollbar = ttk.Scrollbar(table_frame)
    scrollbar.pack(side=RIGHT, fill=Y)
    columns = ("salle", "type", "capacite", "date_debut", "date_fin", "duree")
    tree = ttk.Treeview(
        table_frame,
        columns=columns,
        show="headings",
        yscrollcommand=scrollbar.set,
        height=10,
    )
    tree.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.config(command=tree.yview)

    for col in columns:
        tree.heading(col, text=col.replace("_", " ").title())
        tree.column(col, width=100, anchor=CENTER)

    try:
        with open("data.json", "r") as f:
            data = json.load(f)
            reservations = []
            for client in data.get("Clients", []):
                if client_name in client:
                    reservations = client[client_name].get("Reservations", [])
                    break

            if not reservations:
                ttk.Label(
                    frm, text="Aucune réservation trouvée", font=("Arial", 12)
                ).grid(column=0, row=2, pady=20, columnspan=6)
            else:
                for resa in reservations:
                    tree.insert(
                        "",
                        END,
                        values=(
                            resa.get("Salle", "N/A"),
                            resa.get("Type", "N/A"),
                            str(resa.get("Capacité", "N/A")),
                            resa.get("DateDébut", "N/A"),
                            resa.get("DateFin", "N/A"),
                            resa.get("Durée", "N/A"),
                        ),
                    )
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur de chargement: {str(e)}")

    ttk.Button(frm, text="Retour", command=display_client_reservations).grid(
        column=0, row=3, pady=20, columnspan=6
    )
    frm.grid_rowconfigure(1, weight=1)
    for i in range(6):
        frm.grid_columnconfigure(i, weight=1)


def display_available_slots():
    clear_frame()
    set_active_button("Afficher")
    ttk.Label(
        frm, text="Afficher les salles disponibles pour un créneau", font=("Arial", 14)
    ).grid(column=0, row=0, pady=20, columnspan=2)
    ttk.Label(frm, text="Date de début:").grid(column=0, row=1, pady=10, sticky=E)
    start_date_entry = ttk.Entry(frm, width=10)
    start_date_entry.grid(column=1, row=1, pady=10, sticky=W)
    ttk.Label(frm, text="JJ/MM/AAAA").grid(column=2, row=1, sticky=W)
    ttk.Label(frm, text="Heure de début:").grid(column=0, row=2, pady=10, sticky=E)
    start_time_entry = ttk.Entry(frm, width=5)
    start_time_entry.grid(column=1, row=2, pady=10, sticky=W)
    ttk.Label(frm, text="HH:MM").grid(column=2, row=2, sticky=W)
    ttk.Label(frm, text="Date de fin:").grid(column=0, row=3, pady=10, sticky=E)
    end_date_entry = ttk.Entry(frm, width=10)
    end_date_entry.grid(column=1, row=3, pady=10, sticky=W)
    ttk.Label(frm, text="JJ/MM/AAAA").grid(column=2, row=3, sticky=W)
    ttk.Label(frm, text="Heure de fin:").grid(column=0, row=4, pady=10, sticky=E)
    end_time_entry = ttk.Entry(frm, width=5)
    end_time_entry.grid(column=1, row=4, pady=10, sticky=W)
    ttk.Label(frm, text="HH:MM").grid(column=2, row=4, sticky=W)
    button_frame = ttk.Frame(frm)
    button_frame.grid(column=0, row=5, columnspan=3, pady=20)
    ttk.Button(button_frame, text="Annuler", command=open_display_page).pack(
        side=LEFT, padx=10
    )
    ttk.Button(
        button_frame,
        text="Valider",
        command=lambda: validate_slot_selection(
            start_date_entry.get(),
            start_time_entry.get(),
            end_date_entry.get(),
            end_time_entry.get(),
        ),
    ).pack(side=LEFT, padx=10)
    frm.columnconfigure(1, weight=1)


def validate_slot_selection(start_date, start_time, end_date, end_time):
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

    if errors:
        messagebox.showerror("Erreurs", "\n".join(errors))
    else:
        show_available_rooms_table(
            f"{start_date} {start_time}", f"{end_date} {end_time}"
        )


def show_available_rooms_table(start_datetime, end_datetime):
    clear_frame()
    set_active_button("Afficher")

    try:
        start_dt = datetime.strptime(start_datetime, "%d/%m/%Y %H:%M")
        end_dt = datetime.strptime(end_datetime, "%d/%m/%Y %H:%M")
        duration = end_dt - start_dt
        duration_hours = duration.total_seconds() / 3600
        duration_str = f"{duration_hours:.1f}h"
    except ValueError:
        messagebox.showerror("Erreur", "Format de date/heure invalide")
        return

    ttk.Label(frm, text="Salles disponibles pour le créneau", font=("Arial", 14)).grid(
        column=0, row=0, pady=10, columnspan=3
    )
    ttk.Label(frm, text=f"Début: {start_datetime}").grid(
        column=0, row=1, pady=5, sticky=W
    )
    ttk.Label(frm, text=f"Fin: {end_datetime}").grid(column=0, row=2, pady=5, sticky=W)
    ttk.Label(frm, text=f"Durée: {duration_str}").grid(
        column=0, row=3, pady=5, sticky=W
    )
    table_frame = ttk.Frame(frm)
    table_frame.grid(column=0, row=4, columnspan=3, pady=10, sticky="nsew")
    scrollbar = ttk.Scrollbar(table_frame)
    scrollbar.pack(side=RIGHT, fill=Y)
    columns = ("salle", "type", "capacite")
    tree = ttk.Treeview(
        table_frame,
        columns=columns,
        show="headings",
        yscrollcommand=scrollbar.set,
        height=10,
    )
    tree.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.config(command=tree.yview)

    for col in columns:
        tree.heading(col, text=col.replace("_", " ").title())
        tree.column(col, width=100, anchor=CENTER)

    try:
        with open("data.json", "r") as f:
            data = json.load(f)
            all_rooms = data.get("Salles", [])
            reservations = []
            for client in data.get("Clients", []):
                for client_name, client_data in client.items():
                    reservations.extend(client_data.get("Reservations", []))

            available_rooms = []
            for room_data in all_rooms:
                for room_name, room_info in room_data.items():
                    is_available = True
                    for resa in reservations:
                        if resa.get("Salle") == room_name:
                            resa_start = datetime.strptime(
                                resa.get("DateDébut"), "%d/%m/%Y %H:%M"
                            )
                            resa_end = datetime.strptime(
                                resa.get("DateFin"), "%d/%m/%Y %H:%M"
                            )
                            if not (end_dt <= resa_start or start_dt >= resa_end):
                                is_available = False
                                break

                    if is_available:
                        available_rooms.append(
                            (
                                room_name,
                                room_info.get("Type", "N/A"),
                                str(room_info.get("Capacite", "N/A")),
                            )
                        )

            if not available_rooms:
                ttk.Label(
                    frm,
                    text="Aucune salle disponible pour ce créneau",
                    font=("Arial", 12),
                ).grid(column=0, row=5, pady=20, columnspan=3)
            else:
                for room in available_rooms:
                    tree.insert("", END, values=room)

    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur de chargement: {str(e)}")

    ttk.Button(frm, text="Retour", command=display_available_slots).grid(
        column=0, row=6, pady=20, columnspan=3
    )
    frm.grid_rowconfigure(4, weight=1)
    for i in range(3):
        frm.grid_columnconfigure(i, weight=1)


# Initialisation de l'application
root = Tk()
root.title("MeetingPro")
root.geometry("1000x800")
root.minsize(1000, 800)
root.configure(bg="lightgray")  # Fond en lightgray

# Configurer le style global
style = ttk.Style()
style.theme_use("clam")  # Ou 'default', 'alt', 'clam', 'classic'
style.configure("TFrame", background="lightgray")

# Barre de navigation
nav_frame = Frame(root, bg="white")
nav_frame.pack(side=TOP, fill=X)
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

for button in nav_buttons:
    button.pack(side=LEFT, padx=5, pady=5)

# Cadre principal
frm = ttk.Frame(root, padding=200)
frm.pack(expand=True)
frm.columnconfigure(0, weight=1)
frm.columnconfigure(1, weight=1)
for i in range(5):
    frm.rowconfigure(i, weight=1)

# Lancement de l'application
show_home()
root.mainloop()
