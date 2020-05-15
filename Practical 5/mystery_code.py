# What does this piece of code do?
# Answer: For each click, it can find one prime number.(May be repeated)

# Import libraries
# randint allows drawing a random number, 
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

p=False
while p==False:
    p=True
# n is a integer and 1<=n<=99
    n = randint(1,100)
    u = ceil(n**(0.5))
# check if n can be divided by numbers from 2 to u+1
# if it cannot be divided by these numbers, it cannot be divided by all numbers but 1
    for i in range(2,u+1):
        if n%i == 0:
# if n is not the number we are finding, return to while loop
            p=False


# print out the number we find in this loop
print(n)
