def fibonacci(n):
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n - 2)


def main():
    res = fibonacci(20)
    print('The 20th number in fibonacchi line is', res)


def test_is_even():
    assert fibonacci(1) == 0, 'the 1st number of fibonacci sequence is 0'
    assert fibonacci(2) == 1, 'the 2nd number of fibonacci sequence is 1'
    assert fibonacci(5) == 3, 'the 5th number of fibonacci sequence is 3'
    assert fibonacci(10) == 34, 'the 10th number of fibonacci sequence is 34'
    assert fibonacci(15) == 377, 'the 15th number of fibonacci sequence is 377'


test_is_even()
main()
