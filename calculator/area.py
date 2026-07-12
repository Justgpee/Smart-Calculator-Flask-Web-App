"""
this calculates area functions
"""

from math import pi

def circle(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return pi * radius ** 2

def rectangle(length, width):
    if length < 0 or width < 0:
        raise ValueError("Length and width cannot be negative.")
    return length * width

def triangle(base, height):
    if base < 0 or height < 0:
        raise ValueError("Base and height cannot be negative.")
    return 0.5 * base * height

def square(side):

    if side < 0:
        raise ValueError("Side length cannot be negative.")
    else:
        return side ** 2