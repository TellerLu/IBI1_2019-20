# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 11:53:12 2020

@author: Dell
"""

#define variables
sequence = str();RC = str()
# use input function to get the sequence
seq = input('Type in sequence:')
# use loop to reverse
for i in range (len(seq)):
    sequence += seq[len(seq)-1-i]
# use loop to get complementary sequence
for i in range(len(sequence)):
    if sequence[i] == 'A':
        RC += 'T'
    elif sequence[i] == 'T':
        RC += 'A'
    elif sequence[i] == 'C':
        RC += 'G'
    else:
        RC += 'C'
# print results
print('Reverse complementary sequence','=',RC)