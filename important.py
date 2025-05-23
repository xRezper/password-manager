import tkinter.messagebox as tkmb 
import customtkinter as ctk 
from dashboard import open_dashboard
import json
import os

CONFIG_FILE = "config.json"

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    return {"master_username_set": False, "master_username": "", "master_password": ""}

def save_config(config):
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f)

def set_master_credentials(app, open_dashboard):
    set_window = ctk.CTkToplevel(app)
    set_window.title("Master Credentials Setup")
    set_window.geometry("600x500")

    label = ctk.CTkLabel(set_window, text="Setzen Sie Ihr Master-Passwort und Master-Username")
    label.pack(pady=20)

    label_username = ctk.CTkLabel(set_window, text="Master-Username")
    label_username.pack()
    entry_username = ctk.CTkEntry(set_window)
    entry_username.pack(pady=5)

    label_password = ctk.CTkLabel(set_window, text="Master-Passwort")
    label_password.pack()
    entry_password = ctk.CTkEntry(set_window, show="*")
    entry_password.pack(pady=5)

    label_confirm = ctk.CTkLabel(set_window, text="Bestätigen Sie das Master-Passwort")
    label_confirm.pack()
    entry_confirm = ctk.CTkEntry(set_window, show="*")
    entry_confirm.pack(pady=5)

    def save_master_credentials():
        username = entry_username.get()
        password = entry_password.get()
        confirm = entry_confirm.get()

        if not username or not password or not confirm:
            tkmb.showerror("Fehler", "Bitte füllen Sie alle Felder aus.")
            return

        if password != confirm:
            tkmb.showerror("Fehler", "Die Passwörter stimmen nicht überein.")
            return

        config = {
            "master_username_set": True,
            "master_username": username,
            "master_password": password
        }
        save_config(config)
        set_window.destroy()
        app.withdraw()
        open_dashboard(app)

    button = ctk.CTkButton(set_window, text="Speichern", command=save_master_credentials)
    button.pack(pady=20)

def log(user_entry, user_pass, app, open_dashboard): 
    config = load_config()

    if not config["master_username_set"]:
        set_master_credentials(app, open_dashboard)
        return

    username = config["master_username"]
    password = config["master_password"]
    
    if user_entry.get() == username and user_pass.get() == password:
        tkmb.showinfo(title="Login Successful", message="You have logged in Successfully") 
        app.withdraw() 
        open_dashboard(app) 
    elif user_entry.get() == username and user_pass.get() != password: 
        tkmb.showwarning(title='Wrong password', message='Please check your password') 
    elif user_entry.get() != username and user_pass.get() == password: 
        tkmb.showwarning(title='Wrong username', message='Please check your username') 
    else: 
        tkmb.showerror(title="Login Failed", message="Invalid Username and password")