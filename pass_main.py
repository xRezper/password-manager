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

    if len(chars) == 0:
        EOFError

    

    for x in range(20):
        password_gen += random.choice(chars)

    print(password_gen)


