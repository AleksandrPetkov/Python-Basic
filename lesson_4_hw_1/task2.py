import math


def triangle_s_p():
    a = float(input('Enter the value for first leg: '))
    b = float(input('Enter the value for second leg: '))
    tr_sq = 0.5 * a * b
    tr_per = math.sqrt(a**2 + b**2) + a + b
    return tr_sq, tr_per


res_tr_sq, res_tr_per = triangle_s_p()
print('The answers for task are:\n' '-triangle square is', round(res_tr_sq, 3), ';')
print('-triangle perimetr is', round(res_tr_per, 3), '.')
