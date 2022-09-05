import math


def triangle_square_and_perimeter():
    leg_1 = float(input('Enter the value for first leg: '))
    leg_2 = float(input('Enter the value for second leg: '))
    tr_sq = 0.5 * leg_1 * leg_2
    tr_per = math.sqrt(leg_1**2 + leg_2**2) + leg_1 + leg_2
    return tr_sq, tr_per


res_tr_sq, res_tr_per = triangle_square_and_perimeter()
print('The answers for task are:\n' '-triangle square is', round(res_tr_sq, 3), ';')
print('-triangle perimetr is', round(res_tr_per, 3), '.')
