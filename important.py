import tkinter.messagebox as tkmb 
import customtkinter as ctk 
from dashboard import open_dashboard


def log(user_entry, user_pass, app, open_dashboard): 
    username = "test"
    password = "test"
    
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