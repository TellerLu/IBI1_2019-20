# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 11:46:27 2020

@author: Dell
"""

# a is 3-digit number, b is 6-digit by writing a twice
a = 143
b = 143143
# check if b can be divided by 7
print("b%7","=",b%7)
print("b/7","=",b/7)
c = b/7
d = c/11
e = d/13
# compare e to a
if e > a :
    print("e",">","a")
elif e == a :
    print("e","=","a")
else :
    print("e","<","a")
# assign booleans to X and Y, also use X and Y to show Z
X = False ; Y = False
Z = (X	and	not	Y)	or	(Y	and	not	X)
print(Z)
W = X !=Y
print(Z == W)