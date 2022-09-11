"""
Function 'diff_odd_even' randomly generated number range and
make a subtraction between sum of even and sum of odd numbers in a range.
"""

import random


def diff_odd_even(arg):
    sum_even = sum([num for num in arg if num % 2 == 0])
    sum_odd = sum([num for num in arg if num % 2 != 0])
    sub_num = sum_even - sum_odd
    return sub_num


def main():
    num_limit, lower_bound, upper_bound = map(int, input('Please, enter how many numbers need to be '
                                                         ' by function and in what range(first, last number), '
                                                         'for example(10,1,40):').split(','))
    user_range = [random.randint(lower_bound, upper_bound) for _ in range(num_limit)]
    answer_1 = diff_odd_even(user_range)
    print('Your randomly generated list of numbers is: ', user_range)
    print('Subtraction of sum of even numbers and sum of odd numbers in your range is: ', answer_1)


def test_diff_odd_even():
    assert diff_odd_even([1, 3, 5, 4, 8, 9, 10]) == 4


test_diff_odd_even()
main()
