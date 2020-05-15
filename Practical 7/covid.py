# -*- coding: utf-8 -*-
"""
Created on Fri May 15 01:32:43 2020

@author: Dell
"""

# import libraries
import matplotlib.pyplot as plt
import pandas as pd
import os
#change the working directory
os.chdir('E:/zheda/Anaconda/Files')
# import variables
l=[]; newcases=[]; world=[]; spain=[]
# read the file
covid_data = pd.read_csv("full_data.csv")
# show the rows and columns required
print(covid_data.iloc[0:18:3,:])
# use loop to find and append booleans to lists to record the locations
for i in range (0,int(covid_data.describe().iloc[0,0])):
    if covid_data.iloc[i,1]=='Afghanistan':       
        l.append(True)    
    else:
        l.append(False)
    if covid_data.iloc[i,1]=='World':       
        world.append(True)
    else:
        world.append(False)
    if covid_data.iloc[i,1]=='Spain':       
        spain.append(True) 
    else:
        spain.append(False)
# print total_cases for rows corresponding to Afghanistan and use describe to get mean and medium
print(covid_data.loc[l,'total_cases'])
print('The mean of new cases: ', (covid_data.describe().iloc[1,0]))
print('The median of new cases: ', (covid_data.describe().iloc[5,0]))
# get new cases
newcases=covid_data.loc[world,'new_cases']
# draw the boxplot
plt.boxplot(newcases,
            whis = 1.5,
            patch_artist = True,
            meanline = False,
            showbox = True,
            showcaps = True,
            showfliers = True,
            notch = False)
plt.title('Worldwide New Cases ')
plt.show()
plt.close
# use variebles to store information
world_dates=covid_data.loc[world , 'date']
world_new_cases=covid_data.loc[world ,'new_cases']
world_new_deaths=covid_data.loc[world,'new_deaths']
# draw other plots for different datas
# New cases
plt.plot(world_dates, world_new_cases, 'b+') # thses strings means color of the dots or lines!
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
plt.title('New Cases')
plt.ylabel('Number Of Cases')
plt.show()
plt.close
# New deaths
plt.plot(world_dates,world_new_deaths,'r+')
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
plt.title('New Deaths')
plt.ylabel('Number Of Deaths')
plt.show()
plt.close
# get information for Spain
spain_dates=covid_data.loc[spain,'date']
spain_new_cases=covid_data.loc[spain ,'new_cases']
spain_total_cases=covid_data.loc[spain ,'total_cases']
# Spanish tendency, new cases
plt.plot(spain_dates,spain_new_cases,'y+')
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
plt.title('Spainish Tendency')
plt.ylabel('Number Of New cases')
plt.show()
plt.close
# Spanish tendency, total cases
plt.plot(spain_dates,spain_total_cases,'g+')
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
plt.title('Spainish Tendency')
plt.ylabel('Number Of Total cases')
plt.show()
plt.close