"""
Function 'solve_quadratic_equation()' solve the quadratic equation like "ax^2+bx+c=0"
with parameters a, b, c entered by user. And the program output to user the roots of equation.
"""
import math


def solve_quadratic_equation(a, b, c):
    discriminant = b**2 - 4 * a * c
    if a == 0 or discriminant < 0:
        root1 = None
        root2 = None
    elif discriminant == 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = None
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    return root1, root2


def test_solve_quadratic_equation():
    assert solve_quadratic_equation(1, 0, -4) == (2, -2), 'function "solve_quadratic_equation" has a mistake.'


test_solve_quadratic_equation()
value_1, value_2, value_3 = map(float, input('Please, enter the value of a,b,c: ').split(','))
x1, x2 = solve_quadratic_equation(value_1, value_2, value_3)
if x1 is None and x2 is None:
    print('This equation hasn\'t a solution ')
elif x1 is not None and x2 is None:
    print('The solution of this equation is x =', round(x1, 2))
else:
    print('The solutions of this equation is:\n' 'x1 =', round(x1, 2), '\nx2 =', round(x2, 2))
