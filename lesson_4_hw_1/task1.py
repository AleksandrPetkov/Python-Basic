import math


def degrees2radians(a):
    cos_a = a * (math.pi / 180)
    return cos_a


print('The answers for task are:\n' '-cos60 is', round(degrees2radians(60), 3), ';')
print('-cos45 is', round(degrees2radians(45), 3), ';\n' '-cos40 is', round(degrees2radians(40), 3), '.')
