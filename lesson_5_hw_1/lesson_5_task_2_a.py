"""
Function 'solve_quadratic_equation()' solve the quadratic equation like "ax^2+bx+c=0"
with complex parameters a, b, c entered by user.
This equation always will have a root, except when 'a' == 0.
"""
import cmath


def solve_quadratic_equation(a, b, c):
    discriminant = b**2 - 4 * a * c
    if a == 0:
        root1 = None
        root2 = None
    elif discriminant == 0:
        root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        root2 = None
    else:
        root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
    return root1, root2


value_1, value_2, value_3 = map(float, input('Please, enter the value of a,b,c: ').split(','))
x1, x2 = solve_quadratic_equation(value_1, value_2, value_3)
if x1 is None and x2 is None:
    print('This equation hasn\'t a solution ')
elif x1 is not None and x2 is None:
    print('The solution of this equation is x =', x1)
else:
    print('The solutions of this equation is:\n' 'x1 =', x1, '\nx2 =', x2)
