# Math library
# Author: Sébastien Combéfis
# Version: February 2, 2016

def fact(n):
    """Computes the factorial of a natural number.
    
    Pre: -
    Post: Returns the factorial of 'n'.
    Throws: ValueError if n < 0
    """

    try:

      if n== 0 or n==1:
        return 1

      elif n>1:
        return n * fact(n - 1)

      else:
         return print("Veuillez entrer un nombre entier positif")

    except:
        return print("Veuillez entrer un nombre correct")


def roots(a, b, c):
    """Computes the roots of the ax^2 + bx + x = 0 polynomial.
    
    Pre: -
    Post: Returns a tuple with zero, one or two elements corresponding
          to the roots of the ax^2 + bx + c polynomial.
    """
    try:
        delta = (b ** 2) - (4 * a * c)

        x1 = ((-b) + math.sqrt(delta)) / (2 * a)
        x2 = ((-b) - math.sqrt(delta)) / (2 * a)

        return (x1, x2)
    except:
        return "Ce polynôme n'a pas de racines"  # quand delta<0 et quand a=0

def integrate(function, lower, upper):
    """Approximates the integral of a fonction between two bounds
    
    Pre: 'function' is a valid Python expression with x as a variable,
         'lower' <= 'upper',
         'function' continuous and integrable between 'lower‘ and 'upper'.
    Post: Returns an approximation of the integral from 'lower' to 'upper'
          of the specified 'function'.
    """
    x = lower
    sum = 0
    while x <= upper:
        sum += eval(function) * 0.01
        x += 0.01

    return sum


if __name__ == '__main__':
    print(fact(5))
    print(roots(1, 0, 1))
    print(integrate('x ** 2 - 1', -1, 1))