import math


def degrees2radians():
    cos_a = a * (math.pi / 180)
    cos_b = b * (math.pi / 180)
    cos_c = c * (math.pi / 180)
    return cos_a, cos_b, cos_c


a = float(input('Enter the value for "cos_a": '))
b = float(input('Enter the value for "cos_b": '))
c = float(input('Enter the value for "cos_c": '))
res_cos_a, res_cos_b, res_cos_c = degrees2radians()
print('The answers for task are:\n' '-cos60 is', round(res_cos_a, 3), ';')
print('-cos45 is', round(res_cos_b, 3), ';\n' '-cos40 is', round(res_cos_c, 3), '.')
