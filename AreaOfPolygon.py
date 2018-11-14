# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 23:53:10 2017

@author: Administrator
"""

def polysum (n,s):
    """
    Input: n = Number of Sides of a polygon
           s = Each side length
    Output: Return the sum = area of polygon + Square of perimeter, rounded to 4 decimal places.
    """
    import math #importing math library for tan and Pi 
    area_nr = 0.25 * n * (s**2) # calculating Numerator of Area
    area_dr = math.tan(math.pi/n) # Calculating Denominator of Area
    #Area Calculation
    area = area_nr/area_dr
    #Perimeter calculation
    perimeter = n * s
    #Sumation of Area and perimeter square
    sumi = area + (perimeter**2)
    # returns the sum, rounded to 4 decimal places.
    return(float("{0:.4f}".format(sumi)))