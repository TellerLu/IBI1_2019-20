# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 15:06:01 2020

@author: Dell
"""
# import the number x
x = 4352453
# use another variable in loop
y = x
# variable to store result
a = str()
# variable to keep record
b = 0
# loop
while y >= 2:
    if y%2 == 0:
        b = b + 1
# add to result
    else:
        a = "+" + "2**" + str(b) + str(a)
        b = b + 1
# get next number
    y = (y-y%2)/2
# get last b
a = "2**" + str(b) + str(a)
# print
print(x,"is",str(a))