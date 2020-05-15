# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 12:16:02 2020

@author: Dell
"""

# I assume that the complexity O(n) should be (5/2)*(n!)**2
# import libraries
import re
import sys
import copy
# make variables defined
judge = True; c = float(); R = []; result = False; num_float = [];count = 0
origin = input('''Please input numbers to compute 24:(use ',' to divide them)
''')
# store input  numbers in a list
nums = re.split(',', origin)
# change the type of the items into float since devision part may return float
for item in nums:
    num_float.append(float(item))
# judge whether all input numbers are satisfactory
for n in range(len(nums)):
    if int(nums[n]) >= 24 or int(nums[n]) < 1:
        judge = False
if judge == False:
    print('The input numbers must be integers from 1 to 23')
else:
# an function is defined to calculate the result of an operation given
    def operation(a,b,op):
# global variables used in other parts
        global c,count
        if op == 1:
            c = a + b
        elif op == 2:
            c = a * b
# whether the result of this minus operation is positive or negative does not matter
# since some specific changes in other parts will make the results the same
# this means that we will not miss results even if we do not calculate (b-a) 
        elif op == 3:
            c = a - b
# devision part was devided to two cases to make it clearer when judging whether divisor is 0
        elif op == 4:
# if the divisor is 0, this calculation is meaningless and so are the subsequent recursions
# we should try to stop this branch of recursion, this may reduce unnecessary recusions
            if b == 0.0:
# str(1) is assigned to c in this situation to make it special and easy to be recognized
               c = str(1)
            else:
               c = a/b
        elif op == 5:
# similar to previous one
            if a == 0.0:
               c = str(1)
            else:
               c = b/a
# if 24 is worked out during the process using just some of the input numbers
# it is also okay and the program can be stopped
        if c == 24.0:
# when we get 24, this is also a recusion, use count to record
            count += 1
            print('Yes')
            print('Recursion times:',count)
            sys.exit()
        else:
            return c
# another function is defined to do the recursion of a list of numbers
    def cal(L):
# global variables used in other parts
        global c,count
# if the length of the list is 1, the number in it shoud be one of the recursion results
# assign them to list R
        if len(L) == 1:
            R.append(L[0])
        else:
# try to list out all the cases
         for i in range(0,len(L)-1):
          for j in range (i+1,len(L)):
# make a copy and make changes in the copy
            L_copy = copy.deepcopy(L)
            A = L[i]
            B = L[j]
            L_copy.remove(A)
            L_copy.remove(B)
# excecute all operations one by one
            for k in range(1,6):
# make a copy of the list in which A,B have already been removed to store result of the operation
                copyL_copy = copy.deepcopy(L_copy)
                Result = operation(A,B,k)
# use count to record recursion times, one operation contains one recursion
                count += 1
# if the content of c is str(1), this branch of recusion can be stopped
                if c == str(1):
# it may not be necessary to change the type of c back to float, but I want to keep the types consistent
                   c = float()
                else:
# append result to the second copy and return to the start
                 copyL_copy.append(Result)
                 cal(copyL_copy)
# run the function
    cal(num_float)
# now we have the results, we just need to know if 24 exists in the result
    for r in range(len(R)):
        if R[r] == 24:
            result = True
    if result == True:
        print('Yes')
    else:
        print('No')
# recursion times
    print('Recursion times:',count)
    
