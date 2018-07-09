# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 16:20:40 2018

@author: Darko
"""

import pandas as pd
import matplotlib.pyplot as plt

filename = '../desktop/blossom/influenza.xlsx'
column = [1,2,3,4,6,8,9]
data = pd.read_excel(filename, na_values= None, usecols = column)
data = data.dropna()

'''print(len(data))'''

sum_year = []
sum_quartilea = []
sum_quartileb = []
sum_quartilec = []
sum_quartiled = []
sum_yeara = []
sum_yearb = []
sum_yearc = []

years = []


def year_sum(year,col):
    total = sum(data[(data['YEAR'])== year][col])
    return total


for i in range(1997,2018):
    sum_year.append(year_sum(i,'AGE 0-4'))
    years.append(i)

for i in range(1997,2018):
    sum_yeara.append(year_sum(i,'AGE 5-24'))
    
    
for i in range(1997,2018):
    sum_yearb.append(year_sum(i,'AGE 25-64'))
    

for i in range(1997,2018):
    sum_yearc.append(year_sum(i,'AGE 65'))
    
# calculating quarterly cases    
def quartile_sum(week,col):
    total = sum(data[(data['WEEK'])== week][col])
    return total
    
firstquartile = []
for i in range(1,14):
    # loop through week column and sum them per week
    sum_quartilea.append(quartile_sum(i,'AGE 0-4'))    
# sum content of list to get sum for quarter
firstquartile.append(sum(sum_quartilea))

for i in range(1,14):
    sum_quartileb.append(quartile_sum(i,'AGE 5-24'))
firstquartile.append(sum(sum_quartileb))    
    
for i in range(1,14):
    sum_quartilec.append(quartile_sum(i,'AGE 25-64'))
firstquartile.append(sum(sum_quartilec))    

for i in range(1,14):
    sum_quartiled.append(quartile_sum(i,'AGE 65'))
firstquartile.append(sum(sum_quartiled))

firstquartile_df = pd.DataFrame(firstquartile)     

df = pd.DataFrame(sum_year)
dfb = pd.DataFrame(sum_yeara)
dfc = pd.DataFrame(sum_yearb)
dfd = pd.DataFrame(sum_yearc)



fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(df,  label ='AGE 0-4')
ax.plot(dfb,  label ='AGE 5-24')
ax.plot(dfc,  label ='AGE 25-64')
ax.plot(dfd,  label ='AGE 65')
ax.legend(loc='best' )
ax.set_xlabel('YEARS')
ax.set_ylabel('NO OF CASES')
plt.title('yearly influenza cases grouped by age group ')
ticks = ax. set_xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21])
labels = ax. set_xticklabels([1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017],rotation=90, fontsize='small' )
plt.savefig('yearly influenza ')

print(firstquartile)

fig =  plt. figure(); bx = fig.add_subplot(1, 1, 1)
firstquartile_df.plot(kind= 'bar')

