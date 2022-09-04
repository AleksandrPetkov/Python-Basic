import math


def cone_s_v():
    a = float(input('Enter the value for cone radius: '))
    b = float(input('Enter the value for cone height: '))
    cone_sq = math.pi * a * math.sqrt(a**2 + b**2)
    cone_vol = 1/3 * math.pi * (a**2) * b
    return cone_sq, cone_vol


res_cone_sq, res_cone_vol = cone_s_v()
print('The answers for task are:\n' '-cone square is', round(res_cone_sq, 3), ';')
print('-cone volume is', round(res_cone_vol, 3), '.')
