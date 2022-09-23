"""
Function 'get_max_digit' define the maximum digit in randomly generated 12-digit number/
This function define the max digit on two ways: with using string and without it.
"""

import random


def get_max_digit(arg):
    max_number_var_1 = int(max(str(arg)))
    max_number_var_2 = 0
    while arg:
        arg, n = divmod(arg, 10)
        max_number_var_2 = max(max_number_var_2, n)
    return max_number_var_1, max_number_var_2


def main():
    random_number = random.randint(10 ** 11, 10 ** 12 - 1)
    x1, x2 = get_max_digit(random_number)
    print('Your randomly generated 12-digit number is: ', random_number)
    print('Maximum digit defined WITH "str" is:', f'{x1}.\n' 'Maximum digit defined WITHOUT "str" is:', f'{x2}.')


def test_get_max_digit():
    assert get_max_digit(478256231435) == (8, 8)


test_get_max_digit()
main()
