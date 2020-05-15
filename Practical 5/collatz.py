# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 13:02:00 2020

@author: Dell
"""
# import positive integer n
import random
n = random.randint(1,100)
# loop
while n != 1:
# print
    print(n)
# get next n
    if n%2 == 0:
        n = n/2
    else:
        n = 3*n + 1
# print the last n
print(n)
    