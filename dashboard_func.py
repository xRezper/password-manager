import customtkinter as ctk 
from PIL import Image

def open_add_entry_window():
    add_window = ctk.CTkToplevel()
    add_window.title("Neuer Eintrag")
    add_window.geometry("400x300")

    label_platform = ctk.CTkLabel(add_window, text="Plattform")
    label_platform.pack(pady=5)
    entry_platform = ctk.CTkEntry(add_window)
    entry_platform.pack(pady=5)

    label_username = ctk.CTkLabel(add_window, text="Username/Email")
    label_username.pack(pady=5)
    entry_username = ctk.CTkEntry(add_window)
    entry_username.pack(pady=5)

    label_password = ctk.CTkLabel(add_window, text="Passwort")
    label_password.pack(pady=5)
    entry_password = ctk.CTkEntry(add_window, show="*")
    entry_password.pack(pady=5)

    def save_entry():
        platform = entry_platform.get()
        username = entry_username.get()
        password = entry_password.get()
        # Hier: Eintrag speichern (z.B. in Datenbank oder Datei)
        # Beispiel: print(platform, username, password)
        add_window.destroy()

    save_button = ctk.CTkButton(add_window, text="Speichern", command=save_entry)
    save_button.pack(pady=10)


def open_overview_window():
    overview_window = ctk.CTkToplevel()
    overview_window.title("Übersicht")
    overview_window.geometry("600x400")

    # Hier: Daten laden, z.B. aus einer Liste oder Datenbank
    # Beispiel mit Dummy-Daten:
    entries = [
        {"Plattform": "Gmail", "Username": "user@gmail.com", "Passwort": "*****"},
        {"Plattform": "Facebook", "Username": "user@fb.com", "Passwort": "*****"}
    ]

    for entry in entries:
        entry_text = f"{entry['Plattform']} | {entry['Username']} | {entry['Passwort']}"
        label = ctk.CTkLabel(overview_window, text=entry_text)
        label.pack(pady=2)
