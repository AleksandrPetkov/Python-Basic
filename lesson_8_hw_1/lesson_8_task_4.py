"""
Function 'random password' generated random 8 symbol password, which always include minimum 1 uppercase letter,
1 lowercase letter and 1 number,  also password can include symbol '_'.
"""
import random


def random_password():
    upper_letter = 'ABCDEFGHIGKLMNOPQRSTUVWXYZ'
    lower_letter = 'abcdefghijklmnopqrstuvwxyz'
    numbers = '0123456789'
    symbol = '_'
    all_in_one = upper_letter+lower_letter+numbers+symbol
    password = ''.join(random.sample(all_in_one, 8))
    while True:
        if (any(i in upper_letter for i in password) and any(i in lower_letter for i in password)
                and any(i in numbers for i in password)):
            return password
        else:
            password = ''.join(random.sample(all_in_one, 8))
            continue
    return password


def main():
    print(random_password())


main()
