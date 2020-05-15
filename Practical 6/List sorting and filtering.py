# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 13:12:25 2020

@author: Dell
"""

# type in a list of gene lengths
gene_lengths=[9410,3944141,4442,105338,19149,76779,126550,36296,842,15981]
# use another variable to operate
G = gene_lengths
# first, sort
G = sorted(G)
G.sort()
# second, remove the first and the last
G.remove(G[0])
G.pop()
# import library
import matplotlib.pyplot as plt
# draw the plot
ax1 = plt.subplot()
ax1.set_title('List sorting and filtering')
ax1.boxplot(G, patch_artist=True)
plt.close