"""
Function 'circles_intersect' the function determines if the circles intersect:
x1,y1,x2,y2 - center coordinates of circles
r1, r2 - radiuses of circles.
Function the main receives values (x1, y1, r1, x2, y2, r2) from the user and
launch the function 'circles_intersect' with user's parametres and then output the answer.
"""
import math


def circles_intersect(x1, y1, r1, x2, y2, r2):
    distance = (math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))
    sub_r = int(r2 - r1)
    sum_r = int(r1 + r2)
    if sub_r < distance < sum_r:
        return True
    else:
        return False


def main():
    x1, y1, r1, x2, y2, r2 = map(float, input('Please enter the values (x1,y1,r1,x2,y2,r2):').split(','))
    res = circles_intersect(x1, y1, r1, x2, y2, r2)
    if res is True:
        return print('The circles intersect')
    else:
        return print('The circles don\'t intersect')


def test_circles_intersect():
    assert circles_intersect(1, 2, 3, 4, 5, 6) is True, 'def circles_intersect has a mistake'
    assert circles_intersect(4, 10, 4, 2, 3, 7) is True, 'def circles_intersect has a mistake'


test_circles_intersect()
main()
