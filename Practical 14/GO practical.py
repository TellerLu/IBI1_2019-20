# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 12:16:02 2020

@author: Dell
"""

# import libraries
import xml.dom.minidom
import pandas as pd
import os
# change the working directory
os.chdir('E:/zheda/Anaconda/Files')
# define variables
ID1 = []; Name1 = []; Defstr1 = []; Is_a1 = []; CN=[]; count = 0; childnodes_number = []
# read the file and get list of elements
DOMTree = xml.dom.minidom.parse("go_obo.xml")
collection = DOMTree.documentElement
terms = collection.getElementsByTagName("term")
# define a function to count the number of child nodes
def count_childnodes(a):
    global count
    C = {}
# for every time of recursion, add 1 to count
    for term in terms:
# get is_a information
        childnodes = term.getElementsByTagName('is_a')
        c = childnodes.length
# if it has ids in is_a
        if c !=0:
           for i in range(c):
# get ids in is_a and use a dictionary to store
               child = term.getElementsByTagName('is_a')[i]
               C[i] = child.childNodes[0].data
# if input id exists in is_a of this term, count and regress
               if C[i].find(a) != -1:
                    ID = term.getElementsByTagName('id')[0]
                    IDc = ID.childNodes[0].data
                    count += 1
                    count_childnodes(IDc)
    return(count) # count is the real number of child nodes
for term in terms:
# get other information in the term
       ID = term.getElementsByTagName('id')[0]
       Name = term.getElementsByTagName('name')[0]
       Defstr = term.getElementsByTagName('defstr')[0]
# if autophagosome can be found in defstr of the term, append informatin to lists
       if Defstr.childNodes[0].data.find('autophagosome') != -1:
          I = ID.childNodes[0].data
          N = Name.childNodes[0].data
          D = Defstr.childNodes[0].data
          ID1.append(I)
          Name1.append(N)
          Defstr1.append(D)
# return count to 0 and start to count childnodes of current term
          count = 0
          count_childnodes(I)
          childnodes_number.append(count)
# output
my_dict = {}
information = {'id':ID1, 'names':Name1, 'definition':Defstr1, 'childnodes':childnodes_number}
df = pd.DataFrame.from_dict(information)
df.to_excel("GO task.xls")


