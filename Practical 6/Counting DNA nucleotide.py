# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 11:41:35 2020

@author: Dell
"""
# get numbers of nucleotides
A = int(input('number of A:'))
G = int(input('number of G:'))
C = int(input('number of C:'))
T = int(input('number of T:'))
L = A + T + C + G
# make a dictionary to store information
my_dict = {}
nucleotides={'A':A, 'T':T, 'C':C, 'G':G}
print(nucleotides)
# get data for sizes
A1 = A/L*100
T1 = T/L*100
C1 = C/L*100
G1 = G/L*100
# import and draw the plot
import matplotlib.pyplot as plt
labels = "A","T","C","G"
sizes = [A1,T1,C1,G1]
explode = (0,0,0,0) 
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90)
plt.axis('equal')
plt.show()
plt.close