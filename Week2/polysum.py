# Write a function called polysum that takes 2 arguments, n and s. 
# This function should sum the area and square of the perimeter of the regular polygon. 
# The function returns the sum, rounded to 4 decimal places.

import math

def polygon_area(n, s):
    return (.25 * n * (s**2))/(math.tan(math.pi/n))

def polygon_perimeter(n, s):
    return n * s

def polysum(n, s):
    polysum = (polygon_area(n, s) + polygon_perimeter(n, s)**2)
    return float('{0:.4f}'.format(polysum))

assert polysum(59, 71) == 18942804.2883
assert polysum(60, 22) == 1880929.0524
assert polysum(18, 68) == 1616184.0321