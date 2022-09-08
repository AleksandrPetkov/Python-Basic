"""
Function sing() help to determine the sign of number which was entered by user
"""


def sign(x):
    if x < 0:
        return -1
    elif x > 0:
        return 1
    else:
        return 0


user_num = float(input('Please, enter your number to determine the result of function sign(x):'))
sign(user_num)
if sign(user_num) == -1:
    print('sign('+str(user_num)+') = -1')
elif sign(user_num) == 1:
    print('sign('+str(user_num)+') = 1')
else:
    print('sign('+str(user_num)+') = 0')
