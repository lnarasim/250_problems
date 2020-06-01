'''This program has been written to find the roots of a quadratic equation'''
from fractions import Fraction
from pyproblems.utility import is_int
from pyproblems.utility import is_float
from pyproblems.class_complex import ComplexCustom

def quadratic_equation(a_x, b_y, c_c):
    '''
    This function finds the roots X and Y for the given input to a quadratic
    equation
    '''
    for i in (a_x, b_y, c_c):
        if not is_int(i) and not is_float(i):
            raise TypeError("unsupported format")
    discriminant = (b_y**2)-(4*a_x*c_c)
    if discriminant > 0:
        root_x = ((-b_y + (discriminant)**0.5)/(2*a_x))
        root_y = ((-b_y - (discriminant)**0.5)/(2*a_x))
        print("The roots are real and distinct")
        print(f'The roots are {str(Fraction(root_x))} and {str(Fraction(root_y))}')
        return root_x, root_y
    if discriminant == 0:
        root_x = root_y = -b_y / (2*a_x)
        print("The roots are real and equal")
        print(f'The roots are {str(Fraction(root_x))} and {str(Fraction(root_y))}')
        return root_x, root_y
    if discriminant < 0:
        root_x = root_y = -b_y / (2 * a_x)
        imaginary = ((discriminant)**0.5) / (2*a_x)
        root_x_1 = ComplexCustom(root_x + imaginary)
        root_x_2 = ComplexCustom(root_x - imaginary)
        print("The roots are complex")
        print(f'The roots are{root_x_1}and{root_x_2}')
        return root_x_1, root_x_2
    return None
