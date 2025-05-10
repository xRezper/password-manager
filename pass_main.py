import random
import tkinter
import string


chars = []
check_var = None
check_let = None
check_let_up = None
check_spe = None


# globalis check_var variable - sets check_var to false

def init_variables():
    global check_var
    global check_let
    global check_let_up
    global check_spe
    check_var = tkinter.BooleanVar(value=False)
    check_let = tkinter.BooleanVar(value=False)
    check_let_up = tkinter.BooleanVar(value=False)
    check_spe = tkinter.BooleanVar(value=False)




# Set Numbers into chars list

def check_numbers():
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    if check_var.get():
        chars.extend(numbers)
        print(chars)

    else:
        for x in numbers:
            while x in chars:
                chars.remove(x)
        
password_gen = ''
# generate password from chars list

def gen_pass():
    global password_gen

    if not chars:  # Check if chars list is empty
        raise ValueError("Keine Zeichen zum Generieren des Passworts ausgewählt! Bitte wählen Sie mindestens eine Zeichenkategorie aus.")

    for x in range(20):
        password_gen += random.choice(chars)

    print(password_gen)
    password_gen = ''


def check_letters():
    small_letters = list(string.ascii_lowercase)
    if check_let.get():
        chars.extend(small_letters)
        print(chars)
    else:
        for x in small_letters:
            while x in chars:
                chars.remove(x)

def check_letters_up():
    upper_letters = list(string.ascii_uppercase)
    if check_let_up.get():
        chars.extend(upper_letters)
        print(chars)
    else:
        for x in upper_letters:
            while x in chars:
                chars.remove(x)


def check_special():
    special = ["!", "?", "§", "$", "%", "&", "/", "(", ")", "=", "-", ".", ";", ":", "_", "#", "*", "+"]
    if check_spe.get():
        chars.extend(special)
        print(special)
    else:
        for x in special:
            while x in chars:
                chars.remove(x)

    











