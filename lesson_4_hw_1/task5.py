def word_1():
    w = 'beautiful'
    a = w[2]
    b = w[-2]
    c = w[0:5]
    d = w[:-2]
    e = w[::2]
    f = w[1::2]
    g = w[::-1]
    h = w[-1::-2]
    i = str(len(w))
    return a, b, c, d, e, f, g, h, i


print(' Answer for task 5 is:', word_1())
