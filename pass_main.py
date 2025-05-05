import random
import tkinter


chars = []
check_var = None



def init_variables():
    global check_var
    check_var = tkinter.BooleanVar(value=False)

def check_numbers():
    if check_var.get():
        chars.extend(["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"])
        print(chars)
    else:
        pass

def gen_pass():
    

    password = ''

    for x in range(20):
        password += random.choice(chars)

    print(password)


