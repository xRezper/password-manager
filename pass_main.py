import random
import tkinter
import string
import os
import json

entries = []
DATA_FILE = "password_entries.json"




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
    return password_gen


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

    


def save_entries():
    """Speichert die Einträge in einer JSON-Datei"""
    with open(DATA_FILE, 'w') as f:
        json.dump(entries, f)

def load_entries():
    """Lädt die Einträge aus der JSON-Datei"""
    global entries
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as f:
                file_content = f.read()
                if file_content.strip():  # Check if file is not empty
                    entries = json.loads(file_content)
                else:
                    entries = []
        except json.JSONDecodeError:
            # If file contains invalid JSON, start fresh
            entries = []
    else:
        entries = []

def add_entry(platform, username, password_gen):
    """Fügt einen neuen Eintrag hinzu"""
    entries.append({
        'platform': platform,
        'username': username,
        'password': password_gen
    })
    save_entries()

def get_entries():
    """Gibt alle Einträge zurück"""
    return entries

# Beim Start die Einträge laden
load_entries()








