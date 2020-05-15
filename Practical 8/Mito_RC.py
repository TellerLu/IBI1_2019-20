# -*- coding: utf-8 -*-
"""
Created on Fri May 15 01:10:46 2020

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
# get a user-specified filename for the new file
fname = input('Please type in a name for the new file:')
# define a function to get RC sequence
def RC(a):
  sequence = str();RC = str()
  seq = a
  for i in range (len(seq)):
    sequence += seq[len(seq)-1-i]
  for i in range(len(sequence)):
    if sequence[i] == 'A':
        RC += 'T'
    elif sequence[i] == 'T':
        RC += 'A'
    elif sequence[i] == 'C':
        RC += 'G'
    else:
        RC += 'C'
  return RC
for line in DNA:
# get gene names and count the number of DNA
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
# append the last genesequence
g.append(s)
# create a new file
xfile=open(fname,'w')
for i in range(count):
# find mito genes and write the RC sequence to the file
    if ':Mito:' in x[i]:
        a = n[i] + '  ' + str(len(g[i])) + '\n' + RC(g[i]) + '\n'
        xfile.write(a)
DNA.close
xfile.close