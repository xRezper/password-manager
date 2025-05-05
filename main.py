import customtkinter
import tkinter
from pass_main import init_variables

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


root = customtkinter.CTk()
root.geometry("600x600")


init_variables()

from pass_main import *

# Generate Password Button
button = customtkinter.CTkButton(master=root, text="Generate Password", command=gen_pass)
button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

# Checkbox for Numbers in Password

checkbox_1 = customtkinter.CTkCheckBox(root, text="Numbers", variable=check_var, onvalue=True, offvalue=False, command=check_numbers)
checkbox_1.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")

root.mainloop()
