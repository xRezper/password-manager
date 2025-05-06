import tkinter.messagebox as tkmb 
import customtkinter as ctk 

def log(user_entry, user_pass, app): 
    username = "test"
    password = "test"
    
    if user_entry.get() == username and user_pass.get() == password:
        tkmb.showinfo(title="Login Successful", message="You have logged in Successfully") 
        
        # Neues Fenster erstellen (mit Parent, um Probleme zu vermeiden)
        new_window = ctk.CTkToplevel(app)  
        new_window.title("New Window") 
        new_window.geometry("350x150") 
        ctk.CTkLabel(new_window, text="GeeksforGeeks is best for learning ANYTHING !!").pack() 
        
        # Login-Fenster verstecken (statt zu zerstören)
        app.withdraw()  

        # Wenn das neue Fenster geschlossen wird, Programm beenden
        new_window.protocol("WM_DELETE_WINDOW", lambda: app.destroy())  
    
    elif user_entry.get() == username and user_pass.get() != password: 
        tkmb.showwarning(title='Wrong password', message='Please check your password') 
    elif user_entry.get() != username and user_pass.get() == password: 
        tkmb.showwarning(title='Wrong username', message='Please check your username') 
    else: 
        tkmb.showerror(title="Login Failed", message="Invalid Username and password")