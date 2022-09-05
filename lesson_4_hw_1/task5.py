def word_1():
    w = 'beautiful'
    a = w[2]           # the third character of string.
    b = w[-2]          # penultimate character of string.
    c = w[0:5]         # the first five characters of string.
    d = w[:-2]         # the entire string except the last two characters.
    e = w[::2]         # all characters with even subscripts.
    f = w[1::2]        # all characters with odd subscripts.
    g = w[::-1]        # all characters are in reverse order.
    h = w[-1::-2]      # all characters of the string one by one in reverse order, starting with the last one.
    i = str(len(w))    # the length of this string.
    return a, b, c, d, e, f, g, h, i


print(' Answer for task 5 is:', word_1())
