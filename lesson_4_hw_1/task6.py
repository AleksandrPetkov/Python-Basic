def my_sum(*a, start=0):
    b = sum(*a)+start
    return b


print(my_sum((1, 2, 3)))
