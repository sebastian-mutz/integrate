#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# About this script: 
# This script calculates the circumference and are of a circle with radius of 2 

import math                # import the math module

radius=2.0                 # set radius to 2.0 (float)
c=2*math.pi*radius         # calculate the circumference (c) of the circle 
a=math.pi*radius**2        # calculate the area (a) of the circle

# now display the circumference and area
print('circumference = ', str(c), 'area = ', str(a))

