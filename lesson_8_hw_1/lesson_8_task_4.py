"""
Function 'random password' generated random 8 symbol password, which always include minimum 1 uppercase letter,
1 lowercase letter and 1 number,  also password can include symbol '_'.
"""
from random import choice
from random import shuffle
from string import ascii_lowercase
from string import ascii_uppercase
from string import digits


def random_password():
    symbol = '_'
    all_in_one = ascii_uppercase + ascii_lowercase + digits + symbol
    password_part = [choice(all_in_one) for _ in range(5)]
    password_part.append(choice(ascii_uppercase))
    password_part.append(choice(ascii_lowercase))
    password_part.append(choice(digits))
    shuffle(password_part)
    for idx in range(len(password_part) - 1):
        while password_part[idx] == password_part[idx + 1]:
            shuffle(password_part)
    password = ''.join(password_part)
    return password


def main():
    print(random_password())


if __name__ == "__main__":
    main()
