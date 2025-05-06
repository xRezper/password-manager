import customtkinter as ctk


def open_dashboard(app):
    dashboard = ctk.CTkToplevel()
    dashboard.title("Dashboard")
    dashboard.geometry("800x600")

    label = ctk.CTkLabel(dashboard, text="Dashboard")
    label.pack(pady=40)

    logout_button = ctk.CTkButton(dashboard, text="Logout", command=lambda: [dashboard.destroy(), app.deiconify()])
    logout_button.pack(pady=20)

    return dashboard