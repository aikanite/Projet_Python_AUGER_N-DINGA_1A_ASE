from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Interface")
root.geometry("400x300")  # Taille raisonnable pour voir les boutons

# Centrer les widgets dans le cadre avec du padding raisonnable
frm = ttk.Frame(root, padding=20)
frm.grid(column=0, row=0, sticky="nsew")

# Assurer que le frame et la fenêtre s'adaptent au centrage
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
frm.columnconfigure(0, weight=1)

# Ajouter les boutons
ttk.Button(frm, text="Ajouter").grid(column=0, row=0, pady=5)
ttk.Button(frm, text="Réserver").grid(column=0, row=1, pady=5)
ttk.Button(frm, text="Afficher").grid(column=0, row=2, pady=5)

root.mainloop()
