#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 16:22:17 2017

@author: nicholasf
"""

# A regular polygon has n number of sides. Each side has length s.
# The area of a regular polygon is: 0.25∗n∗s2tan(π/n)
# The perimeter of a polygon is: length of the boundary of the polygon
# Write a function called polysum that takes 2 arguments, n and s. This function should sum the area and square of the perimeter of the regular polygon. The function returns the sum, rounded to 4 decimal places.


from math import pi
import numpy as np

def polysum(n,s):
    perimeter = n*s
    area = (0.25*n*s*s)/np.tan(pi/n)
    square_perimeter = perimeter*perimeter
    total_value = square_perimeter + area
    return float(str(round(total_value,4)))
    


