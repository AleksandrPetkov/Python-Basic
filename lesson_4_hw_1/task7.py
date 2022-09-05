def sum_each_number():
    a = input("Enter your number: ")
    e = ord('0')
    b = ord(a[0]) - e
    c = ord(a[1]) - e
    d = ord(a[2]) - e
    return b + c + d


print(sum_each_number())
