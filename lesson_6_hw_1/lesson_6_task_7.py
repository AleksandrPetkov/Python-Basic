"""
This program generate the random number from 1 to 10 and the user must guess it.
"""

import random

hidden_number = random.randint(1, 10)
user_number = int(input('Please enter your number from 1 to 10: '))
while hidden_number != user_number:
    if hidden_number < user_number:
        print('Ohh no, you loose, your number is bigger then guessed, try again!!!')
    elif hidden_number > user_number:
        print('Ohh no, you loose, your number is smaller then guessed, try again!!!')
    user_number = int(input('Please enter your number from 1 to 10: '))
else:
    print('Congratulations, you guessed the number!!!')
