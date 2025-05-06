 
import customtkinter as ctk 
import tkinter.messagebox as tkmb 
from important import log
from dashboard import open_dashboard
  
  
# Selecting GUI theme - dark, light , system (for system default) 
ctk.set_appearance_mode("dark") 
  
# Selecting color theme - blue, green, dark-blue 
ctk.set_default_color_theme("blue") 


  
app = ctk.CTk() 
app.geometry("400x400") 
app.title("Password Manager") 
  

  
  
label = ctk.CTkLabel(app,text="Login Page") 
  
label.pack(pady=20) 
  
  
frame = ctk.CTkFrame(master=app) 
frame.pack(pady=20,padx=40,fill='both',expand=True) 
  
label = ctk.CTkLabel(master=frame,text='Login') 
label.pack(pady=12,padx=10) 
  
  
user_entry= ctk.CTkEntry(master=frame,placeholder_text="Username") 
user_entry.pack(pady=12,padx=10) 
  
user_pass= ctk.CTkEntry(master=frame,placeholder_text="Password",show="*") 
user_pass.pack(pady=12,padx=10) 
  
  
button = ctk.CTkButton(master=frame,text='Login',command=lambda: log(user_entry, user_pass, app, open_dashboard)) 
button.pack(pady=12,padx=10) 
  
checkbox = ctk.CTkCheckBox(master=frame,text='Remember Me') 
checkbox.pack(pady=12,padx=10) 
  
  
app.mainloop()