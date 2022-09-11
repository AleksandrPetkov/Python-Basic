"""
Function 'sub_symbol_codes' calculate the sum of all code of Unicode symbols,
which are between those which were entered by user.
"""


def sum_symbol_codes(first, last):
    code_1 = ord(first)
    code_2 = ord(last)+1
    number_range = sum(range(code_1, code_2))
    return number_range


def main():
    x1, x2 = input('Please, enter two letters from "a" to "z":').split(',')
    print('The sum of numbers is: ', sum_symbol_codes(x1, x2))


def test_sum_symbol_codes():
    assert sum_symbol_codes('a', 'c') == 294


test_sum_symbol_codes()
main()
