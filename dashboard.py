import customtkinter as ctk
from PIL import Image
from dashboard_func import *
import os
import sys
from pass_main import get_entries  # Import hinzufügen


def open_dashboard(app):
    dashboard = ctk.CTkToplevel()
    dashboard.title("Password Manager")
    dashboard.geometry("800x600")

    label = ctk.CTkLabel(dashboard, text="")
    label.pack(pady=40)

    def resource_path(relative_path):
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    # Frame start
    frame = ctk.CTkFrame(master=dashboard) 
    frame.place(x=0, y=0, relwidth=0.2, relheight=1) 
  
    logo_image = ctk.CTkImage(Image.open(resource_path('images/passwortgen.png')), size=(100, 100))
    
    logo_label = ctk.CTkLabel(master=frame, text="", image=logo_image)
    logo_label.pack(pady=12, padx=10)

    logout_button = ctk.CTkButton(frame, text="Logout", command=lambda: [dashboard.destroy(), app.deiconify()])
    logout_button.place(relx=0, rely=1, x=10, y=-10, anchor="sw")

    start_button = ctk.CTkButton(frame, text="Startseite")
    start_button.pack(pady=12, padx=12, fill="x")

    add_button = ctk.CTkButton(frame, text="Neuer Entry", command=lambda: open_add_entry_window())
    add_button.pack(pady=12, padx=12, fill="x")

    view_button = ctk.CTkButton(frame, text="Übersicht", command=lambda: open_overview_window())
    view_button.pack(pady=12, padx=12, fill="x")

    # MainFrame1 - Anzahl der gespeicherten Passwörter
    main_frame1 = ctk.CTkFrame(master=dashboard, width=200, height=150)
    main_frame1.place(x=180, y=50, relx = 0, rely = 0)
    
    entries = get_entries()
    count_label = ctk.CTkLabel(main_frame1, text=f"Gespeicherte Passwörter: {len(entries)}", font=("Arial", 16))
    count_label.pack(pady=20, padx=20)
    
    # MainFrame2 - Stärke der Passwörter
    main_frame2 = ctk.CTkFrame(master=dashboard, width=300, height=150)
    main_frame2.place(x=500, y=50, relx=0, rely=0)
    
    # Funktion zur Bewertung der Passwortstärke
    def evaluate_password_strength():
        if not entries:
            return "Keine Passwörter gespeichert"
            
        strengths = []
        for entry in entries:
            password = entry['password']
            score = 0
            
            # Bewertungskriterien
            if len(password) >= 8: score += 1
            if any(c.isdigit() for c in password): score += 1
            if any(c.islower() for c in password): score += 1
            if any(c.isupper() for c in password): score += 1
            if any(not c.isalnum() for c in password): score += 1
            
            strengths.append(score)
        
        avg_strength = sum(strengths) / len(strengths) if strengths else 0
        
        if avg_strength >= 4:
            return "Sehr stark"
        elif avg_strength >= 3:
            return "Stark"
        elif avg_strength >= 2:
            return "Mittel"
        else:
            return "Schwach"
    
    strength_label = ctk.CTkLabel(main_frame2, text=f"Durchschnittliche Passwortstärke:\n{evaluate_password_strength()}", 
                                 font=("Arial", 16), justify="left")
    strength_label.pack(pady=20, padx=20)

    return dashboard