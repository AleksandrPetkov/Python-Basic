import math


def cone_square_and_volume():
    radius = float(input('Enter the value for cone radius: '))
    height = float(input('Enter the value for cone height: '))
    cone_sq = math.pi * radius * (radius + math.sqrt(radius**2 + height**2))
    cone_vol = 1/3 * math.pi * (radius**2) * height
    return cone_sq, cone_vol


res_cone_sq, res_cone_vol = cone_square_and_volume()
print('The answers for task are:\n' '-cone square is', round(res_cone_sq, 3), ';')
print('-cone volume is', round(res_cone_vol, 3), '.')
