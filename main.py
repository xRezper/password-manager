import customtkinter
from pass_main import *

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("600x600")




button = customtkinter.CTkButton(master=app, text="Generate Password", command=gen_pass)
button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)


app.mainloop()
