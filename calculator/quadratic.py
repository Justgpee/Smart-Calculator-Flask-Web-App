import math

# This function solves the quadratic equation

def solve(a, b, c):
    d = b**2 - (4 * a *c)

    if d < 0:
        return None
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero.")
    
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)

    return (x1, x2)
