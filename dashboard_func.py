import customtkinter as ctk 
from PIL import Image
from pass_main import *



def open_add_entry_window():

    init_variables()
    from pass_main import check_var
    from pass_main import check_let
    from pass_main import check_let_up
    from pass_main import check_spe

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

    

    def handle_gen_pass():
        try:
            gen_pass()
            # Hier könntest du das generierte Passwort auch in einem Label anzeigen
            
            ctk.CTkLabel(add_window, text="Passwort generiert!").pack(pady=5)
        except ValueError as e:
            error_label = ctk.CTkLabel(add_window, text=str(e), text_color="red")
            error_label.pack(pady=5)
            # Entferne die Fehlermeldung nach 3 Sekunden
            add_window.after(3000, error_label.destroy)

    
    lowercase_checkbox = ctk.CTkCheckBox(add_window, text="Klein Buchstaben", variable=check_let, command=check_letters)
    lowercase_checkbox.pack(pady=5)

    uppercase_checkbox = ctk.CTkCheckBox(add_window, text="Groß Buchstaben", variable=check_let_up, command=check_letters_up)
    uppercase_checkbox.pack(pady=5)

    special_checkbox = ctk.CTkCheckBox(add_window, text="Sonderzeichen", variable=check_spe, command=check_special)
    special_checkbox.pack(pady=5)

    generate_password_button = ctk.CTkButton(add_window, text="Generiere Passwort", command=handle_gen_pass)
    generate_password_button.pack(pady=5)


def open_overview_window():
    overview_window = ctk.CTkToplevel()
    overview_window.title("Übersicht")
    overview_window.geometry("600x400")

    
