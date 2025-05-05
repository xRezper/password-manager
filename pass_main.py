import random

def gen_pass():
    chars = 'abcdefghijklmnopqrstuvawxyz1234567890?-.,+#!§$ % &/()="'

    password = ''

    for x in range(20):
        password += random.choice(chars)

    print(password)


