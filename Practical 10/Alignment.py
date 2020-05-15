# -*- coding: utf-8 -*-
"""
Created on Fri May 15 01:29:45 2020

@author: Dell
"""

# import libraries
import pandas as pd
import os
#change the working directory
os.chdir('E:/zheda/Anaconda/Files')
# define variables
mp=''; hp=''; rp=''; lib='ARNDCQEGHILKMFPSTWYVBZX'; score1=0; score2=0; score3=0;
edit_distance1=0; edit_distance2=0; edit_distance3=0
# open the files
mouseprotein=open('SOD2_mouse.fa')
humanprotein=open('SOD2_human.fa')
randomprotein=open('RandomSeq.fa')
blosum= pd.read_csv("BLOSUM62 matrix.csv")
# get genes in the files and store them in string variables
for line in mouseprotein:
    if not line.startswith('>'):
        mp+= line.strip()
for line in humanprotein:
    if not line.startswith('>'):
        hp+=line.strip()
for line in randomprotein:
    if not line.startswith('>'):
        rp+=line.strip()
# define a function to find the row of a amino acid
def find(a):
    for h in range (0,len(lib)):
        if lib[h]==a:
            return h
# for each amino acid, find its location in BLOSUM62 matrix.csv to get scores and add them up
# then print results
for i in range (0,len(mp)):
    score1+= (blosum.loc[find(mp[i]),hp[i]])
print('The final score between mousesequences and humansequences', score1)
for j in range (0,len(mp)):
    score2 += (blosum.loc[find(mp[j]),rp[j]])
print('The final score between mousesequences and randomsequences', score2)
for k in range (0,len(hp)):
    score3+=(blosum.loc[find(hp[k]),rp[k]])
print('The final score between randomsequences and humansequences', score3)
#set initial distance as zero
edit_distance = 0
#compare each amino acid
for i in range(len(hp)):
#add a score 1 if amino acids are different
    if hp[i]!=mp[i]:
        edit_distance1 += 1
    if hp[i]!=rp[i]:
        edit_distance2 +=1
    if rp[i]!=mp[i]:
        edit_distance3+= 1
# print results
print('The edit diatance between human sequences and mouse sequences:', edit_distance1)
print('The edit diatance between random sequences and human sequences:', edit_distance2)
print('The edit diatance between random sequences and mouse sequences:', edit_distance3)