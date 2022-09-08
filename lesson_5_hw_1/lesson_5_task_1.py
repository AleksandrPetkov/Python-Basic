"""
Function 'is_even(num)' determine if the number is even or not.
Function 'main()' take the number which enter the user, then launch
the 'is_even(num)' function and output to user the answer of question
"""


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


def main():
    num = int(input('Please enter the number:'))
    res = is_even(num)
    print('Is your number even?: ', res)


def test_is_even():
    assert is_even(4) is True, 'even number hasn\'t a reminder, when it divided by 2'
    assert is_even(10) is True, 'even number hasn\'t a reminder, when it divided by 2'


test_is_even()
main()
