import customtkinter as ctk 
from PIL import Image
from pass_main import *



def open_add_entry_window():
    init_variables()
    from pass_main import check_var, check_let, check_let_up, check_spe, add_entry

    add_window = ctk.CTkToplevel()
    add_window.title("Neuer Eintrag")
    add_window.geometry("800x600")

    label_platform = ctk.CTkLabel(add_window, text="Plattform")
    label_platform.pack(pady=5)
    entry_platform = ctk.CTkEntry(add_window)
    entry_platform.pack(pady=5)

    label_username = ctk.CTkLabel(add_window, text="Username/Email")
    label_username.pack()
    entry_username = ctk.CTkEntry(add_window)
    entry_username.pack(pady=5)

    number_checkbox = ctk.CTkCheckBox(add_window, text="Nummern", variable=check_var, command=check_numbers)
    number_checkbox.pack(pady=5)

    lowercase_checkbox = ctk.CTkCheckBox(add_window, text="Klein Buchstaben", variable=check_let, command=check_letters)
    lowercase_checkbox.pack(pady=5)

    uppercase_checkbox = ctk.CTkCheckBox(add_window, text="Groß Buchstaben", variable=check_let_up, command=check_letters_up)
    uppercase_checkbox.pack(pady=5)

    special_checkbox = ctk.CTkCheckBox(add_window, text="Sonderzeichen", variable=check_spe, command=check_special)
    special_checkbox.pack(pady=5)

    password_label = ctk.CTkLabel(add_window, text="")
    password_label.pack(pady=5)

    def handle_gen_pass():
        try:
            password_gen = gen_pass()  # Annahme: gen_pass() gibt das generierte Passwort zurück
            password_label.configure(text=f"Generiertes Passwort: {password_gen}")
            return password_gen
        except ValueError as e:
            error_label = ctk.CTkLabel(add_window, text=str(e), text_color="red")
            error_label.pack(pady=5)
            add_window.after(3000, error_label.destroy)
            return None

    generate_password_button = ctk.CTkButton(add_window, text="Generiere Passwort", command=handle_gen_pass)
    generate_password_button.pack(pady=5)

    def save_entry():
        platform = entry_platform.get()
        username = entry_username.get()
        password_gen = password_label.cget("text").replace("Generiertes Passwort: ", "")
        
        if not platform or not username or "Generiertes Passwort" not in password_label.cget("text"):
            error_label = ctk.CTkLabel(add_window, text="Bitte fülle alle Felder aus und generiere ein Passwort", text_color="red")
            error_label.pack(pady=5)
            add_window.after(3000, error_label.destroy)
            return
        
        add_entry(platform, username, password_gen)
        success_label = ctk.CTkLabel(add_window, text="Eintrag erfolgreich gespeichert!", text_color="green")
        success_label.pack(pady=5)
        add_window.after(3000, success_label.destroy)
        add_window.after(3000, add_window.destroy)

    save_button = ctk.CTkButton(add_window, text="Eintrag speichern", command=save_entry)
    save_button.pack(pady=10)


def open_overview_window():
    from pass_main import get_entries
    
    overview_window = ctk.CTkToplevel()
    overview_window.title("Übersicht")
    overview_window.geometry("1000x600")
    
    entries = get_entries()
    
    if not entries:
        ctk.CTkLabel(overview_window, text="Keine Einträge vorhanden").pack(pady=20)
        return
    
    frame = ctk.CTkScrollableFrame(overview_window)
    frame.pack(pady=20, padx=20, fill="both", expand=True)
    
    # Header
    ctk.CTkLabel(frame, text="Plattform", font=("Arial", 14, "bold")).grid(row=0, column=0, padx=10, pady=5)
    ctk.CTkLabel(frame, text="Username/Email", font=("Arial", 14, "bold")).grid(row=0, column=1, padx=10, pady=5)
    ctk.CTkLabel(frame, text="Passwort", font=("Arial", 14, "bold")).grid(row=0, column=2, padx=10, pady=5)
    ctk.CTkLabel(frame, text="Aktion", font=("Arial", 14, "bold")).grid(row=0, column=3, padx=10, pady=5)
    
    # Einträge mit Anzeige-Button
    for i, entry in enumerate(entries, start=1):
        ctk.CTkLabel(frame, text=entry['platform']).grid(row=i, column=0, padx=10, pady=5)
        ctk.CTkLabel(frame, text=entry['username']).grid(row=i, column=1, padx=10, pady=5)
        
        # Passwort-Label (initial zensiert)
        pass_label = ctk.CTkLabel(frame, text="••••••••")
        pass_label.grid(row=i, column=2, padx=10, pady=5)
        
        # "Anzeigen"-Button
        def toggle_password(label=pass_label, pwd=entry['password']):
            if label.cget("text") == "••••••••":
                label.configure(text=pwd)
            else:
                label.configure(text="••••••••")
                
        ctk.CTkButton(frame, 
                     text="Anzeigen", 
                     width=80,
                     command=toggle_password).grid(row=i, column=3, padx=10, pady=5)
