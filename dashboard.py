import customtkinter as ctk
from PIL import Image
from dashboard_func import *


def open_dashboard(app):
    dashboard = ctk.CTkToplevel()
    dashboard.title("Password Manager")
    dashboard.geometry("800x600")

    label = ctk.CTkLabel(dashboard, text="")
    label.pack(pady=40)

# Frame start

    frame = ctk.CTkFrame(master=dashboard) 
    frame.place(x=0, y=0, relwidth=0.2, relheight=1) 
  
    logo_image = ctk.CTkImage(Image.open('images/passwortgen.png'), size=(100, 100))
        
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
    

    

    return dashboard
