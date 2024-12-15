# -*- coding: utf-8 -*-
"""
Given three points (x1, y1), (x2, y2) and (x3, y3),
 write a program to check if all the three points fall on one straight line.
"""

p1 = input("Enter x1,y1 ").split(',')
p2 = input("Enter x2,y2 ").split(',')
p3 = input("Enter x3,y3 ").split(',')

def distance(p1,p2):
    if p1[0] == p2[0]:
        slope = 0
    else:
        slope = (float(p1[1])-float(p2[1]))/(float(p1[0])-float(p2[0]))
        
    return slope

if distance(p1, p2) == distance(p2,p3):
    print('colinear')

else:
    print('Non colinear')