# -*- coding: utf-8 -*-
"""
If ages of Ram, Shyam and Ajay are input through the keyboard, 
write a program to determine the youngest of the three.
"""

ram = int(input("Enter Age of ram: "))
shyam = int(input("Enter Age of shyam : "))
ajay = int(input("Enter Age of ajay: "))

younger = ram
if shyam < younger:
    younger = shyam

if ajay < younger:
    younger = ajay

print(f"{younger} is youngest!")