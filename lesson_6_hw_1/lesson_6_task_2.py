"""
Function 'diff_min_max' randomly generated number range and
make a subtraction between maximum and minimum number in a range.
For define max and min value used built-in functions 'min' and 'max'
"""
import random


def diff_min_max(arg):
    sub_numbers = max(arg) - min(arg)
    return sub_numbers


def main():
    num_limit, lower_bound, upper_bound = map(int, input('Please, enter how many numbers need to be generated'
                                                         ' by function and in what range(first, last number), '
                                                         'for example(10,1,40):').split(','))
    user_range = [random.randint(lower_bound, upper_bound) for _ in range(num_limit)]
    answer_1 = diff_min_max(user_range)
    print('Your randomly generated list of numbers is: ', user_range)
    print('Subtraction of maximum and minimum value in your range is: ', answer_1)


def test_diff_min_max():
    assert diff_min_max([1, 5, 10, 2, 20]) == 19


test_diff_min_max()
main()
