# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 16:18:43 2020

@author: Dell
"""

# import library
import re
#import os
#change the working directory
#os.chdir('E:/zheda/Anaconda/Files')
# define variables
g=[]
n=[]
s=str()
count = 0
x=[]
# open the file
DNA = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
for line in DNA:
# get gene name and count the number of DNA
    if line.startswith('>'):
        if s != '':
            g.append(s)
        sta = re.findall(r'^>([0-9A-Z]+)',line)
        sta1 = str(sta)
        sta2 = sta1.strip('''['']''')
        n.append(sta2)
        s=''
        x.append(line)
        count += 1
# get gene sequence
    else:
        line = line.rstrip()
        s += str(line)
# append the last sequence
g.append(s)
# create a new file
xfile=open('mito_gene.fa','w')
for i in range(count):
# find mito genes and write their names and sequences to the file
    if ':Mito:' in x[i]:
        a = n[i] + '  ' + str(len(g[i])) + '\n'
        xfile.write(a)
DNA.close
xfile.close
# print lines in the file
yfile = open('mito_gene.fa')
for line in yfile:
    print(line)
yfile.close