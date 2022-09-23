"""
Function 'diff_min_max' randomly generated number range and
make a subtraction between maximum and minimum number in a range.
For define max and min value don't used built-in functions 'min' and 'max'
"""
import random


def diff_min_max_sorted(arg):
    sorted_user_range = sorted(arg)
    sub_numbers = sorted_user_range[-1] - sorted_user_range[0]
    return sub_numbers


def diff_min_max_2(arg):
    min_1 = None
    max_1 = None
    for item in arg:
        if min_1 is None or item < min_1:
            min_1 = item
        if max_1 is None or item > max_1:
            max_1 = item
    sub_numbers_2 = max_1 - min_1
    return sub_numbers_2


def main():
    num_limit, lower_bound, upper_bound = map(int, input('Please, enter how many numbers need to be generated'
                                                         ' by function and in what range(first, last number), '
                                                         'for example(10,1,40):').split(','))
    user_range = [random.randint(lower_bound, upper_bound) for _ in range(num_limit)]
    answer_1 = diff_min_max_sorted(user_range)
    answer_2 = diff_min_max_2(user_range)
    print('Your randomly generated list of numbers is: ', user_range)
    print('Subtraction of maximum and minimum value in your range used sorted method is: ', answer_1)
    print('Subtraction of maximum and minimum value in your range used "for" method is: ', answer_2)


def test_diff_min_max_sorted():
    assert diff_min_max_sorted([1, 5, 10, 2, 20]) == 19


def test_diff_min_max_2():
    assert diff_min_max_2([5, 8, 90, 52, 3, 48]) == 87


test_diff_min_max_sorted()
test_diff_min_max_2()
main()
