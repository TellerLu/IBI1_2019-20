# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 12:16:02 2020

@author: Dell
"""

# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
# define variables
beta = 0.3; gamma = 0.05
# make array of all susceptible population
population = np.zeros((100 , 100))
# choose the point that outbreak happens
outbreak = np.random.choice(range(100),2)
population[outbreak[0],outbreak[1]] = 1
# loop 100 times
for j in range(100):
# find infected points
  infectedIndex = np.where(population==1)
# loop through all infected points
  for i in range(len(infectedIndex[0])):
    # get x, y coordinates for each point
    x = infectedIndex[0][i]
    y = infectedIndex[1][i]
# recover
    population[x,y]=np.random.choice(range(1,3),1,p=[1-gamma,gamma])[0]
    # infect each neighbour with probability beta
    # infect all 8 neighbours (this is a bit finicky, is there a better way?):
    for xNeighbour in range(x-1,x+2):
        for yNeighbour in range(y-1,y+2):
            # don't infect yourself! (Is this strictly necessary?)
            # recovery process is in previous part, so this is strictly necessary
            # In 
            if (xNeighbour,yNeighbour) != (x,y):
                # make sure I don't fall off an edge
                if xNeighbour != -1 and yNeighbour != -1 and xNeighbour!=100 and yNeighbour!=100:
                    # only infect neighbours that are not already infected!
                    if population[xNeighbour,yNeighbour]==0:
                        population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-beta,beta])[0]
# show the figure
  plt.figure(figsize = (6,4), dpi =150)
  plt.imshow(population, cmap='viridis', interpolation= 'nearest')
  plt.show
  plt.close