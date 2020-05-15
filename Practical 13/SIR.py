# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 12:16:02 2020

@author: Dell
"""

# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
# define variables
S = 9999;I = 1; R = 0; beta = 0.3; gamma = 0.05; N = 10000; infected=0; recovered = 0;
Sr=[];Ir=[];Rr=[];Infected=[];Recovered=[]
# store initial data in lists
Sr.append(S)
Ir.append(I)
Rr.append(R)
# define a function to count something in list (count times of a in list b and assign it to c)
def count(a,b:list):
    Count = 0
    for i in range(len(b)):
        if b[i] == a:
            Count += 1
    return Count
# define a function to simulate one time of changing and record at the same time
def change_and_record():
  global S,I,R
# calculate proportion of infected people
  pr = I/N
# randomly choose people to be infected or recovered, 0 means unchanegd, 1 means changed
  Infected = np.random.choice(range(2),S,p=[1-beta*pr,beta*pr])
  Recovered = np.random.choice(range(2),I,p=[1-gamma,gamma])
# count 0 and 1 in the lists and use then to change the variables
  infected = count(1,Infected)
  recovered = count(1,Recovered)
  S = S - infected
  I = I + infected - recovered
  R = R + recovered
# store these changes in the lists
  Sr.append(S)
  Ir.append(I)
  Rr.append(R)

# use loop to simulate
for j in range(1000):
  change_and_record()
# time to plot
tx = np.arange(0,1001,1)
ty1 = Sr
ty2 = Ir
ty3 = Rr
ax1 = plt.plot(tx,ty1,label='susceptible')
ax2 = plt.plot(tx,ty2,label='infected')
ax3 = plt.plot(tx,ty3,label='recovered')
plt.legend(['susceptible','infected','recovered'])
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model')
plt.show
plt.close