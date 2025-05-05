import random
import tkinter


chars = []
check_var = None


# globalis check_var variable - sets check_var to false

def init_variables():
    global check_var
    check_var = tkinter.BooleanVar(value=False)

# Set Numbers into chars list

def check_numbers():
    if check_var.get():
        chars.extend(["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"])
        print(chars)
    else:
        pass

# generate password from chars list

def gen_pass():
    

    password = ''

    for x in range(20):
        password += random.choice(chars)

    print(password)


