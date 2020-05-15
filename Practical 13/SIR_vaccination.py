# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 12:16:02 2020

@author: Dell
"""

# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
# define variables
S = float();I = 1.0; R = 0.0; beta = 0.3; gamma = 0.05; N = 10000.0; infected=0.0; recovered = 0.0;
Sr=[];Ir=[];Irr=[];Rr=[];Infected=[];Recovered=[]; vaccination_rates=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
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
  Infected = np.random.choice(range(2),int(S),p=[1.0-beta*pr,beta*pr])
  Recovered = np.random.choice(range(2),int(I),p=[1.0-gamma,gamma])
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
# use loop to get result of situations with different vaccination rates
for v in range(len(vaccination_rates)):
    I = 1.0; R = 0.0;Sr=[];Ir=[];Rr=[];Infected=[];Recovered=[]
    R = N*vaccination_rates[v]
    S = N - I - R
    if S < 0:
       S = 0; I = 0
 # store initial data in lists
    Sr.append(S)
    Ir.append(I)
    Rr.append(R)
# use loop to simulate
    for j in range(1000):
       change_and_record()
    Irr.append(Ir)
# time to plot``
tx = np.arange(0,1001,1)
ty1,ty2,ty3,ty4,ty5,ty6,ty7,ty8,ty9,ty10,ty11 = Irr[0:len(Irr)]
ax1 = plt.plot(tx,ty1,label='0%')
ax2 = plt.plot(tx,ty2,label='10%')
ax3 = plt.plot(tx,ty3,label='20%')
ax4 = plt.plot(tx,ty4,label='30%')
ax5 = plt.plot(tx,ty5,label='40%')
ax6 = plt.plot(tx,ty6,label='50%')
ax7 = plt.plot(tx,ty7,label='60%')
ax8 = plt.plot(tx,ty8,label='70%')
ax9 = plt.plot(tx,ty9,label='80%')
ax10 = plt.plot(tx,ty10,label='90%')
ax11 = plt.plot(tx,ty11,label='100%')
plt.legend(['0%','10%','20%','30%','40%','50%','60%','70%','80%','90%','100%'])
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model with different vaccination rates')
plt.show
plt.close