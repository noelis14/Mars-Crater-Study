# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 12:46:13 2020

@author: MAHE
"""
import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib as plt


data=pd.read_csv('marscrater_pds.csv',low_memory=False)

pd.set_option('display.float_format', lambda x:'%f'%x)

dia=data[(data['DIAM_CIRCLE_IMAGE']>=10)&(data['DIAM_CIRCLE_IMAGE']<=100)]

print('No of rows in data frame for selected values:')
print(len(dia))
print('No of columns in data frame for selected values:')
print(len(dia.columns))

dia2=dia.copy()
dia3=dia.copy()

print('Counting the frequency of diameters above 10 km and below 100 km:')
diam_count=dia2['DIAM_CIRCLE_IMAGE'].value_counts(sort=False)
print(diam_count)

print('Making a series of craters by diameters')
diam=dia2['DIAM_CIRCLE_IMAGE']
diam.index=dia2['LATITUDE_CIRCLE_IMAGE']

print(diam)
diam_df=pd.DataFrame({'Latitude':diam.index,'Diameter':diam.values,'CraterID':dia['CRATER_ID']})
diam_df['Depth']=dia['DEPTH_RIMFLOOR_TOPOG']
print(diam_df)
print(diam_df.head(20))

print('Value Count of Depth:')
depth_count=diam_df['Depth'].value_counts(sort=False,dropna=False)
print(depth_count)
diam_df['Depth']=diam_df['Depth'].replace(np.nan,0)

print('Sorting by availability of depth:')
diam_df_depth=diam_df[diam_df['Depth']!=0]
print(diam_df_depth)

print('Adding Volume to DataFrame:')
diam_df_depth['Volume']=(1/8)*((diam_df_depth['Diameter'])**2)*3.14*diam_df_depth['Depth']
print(diam_df_depth)

# Plotting the Univariate bar graph
fig1=sb.distplot(diam_df_depth['Depth'].dropna(),kde=False)
fig1.set(xlabel='Depth of Crater',ylabel='Frequency',title='Frequency of craters by depth')
print(fig1)

fig2=sb.distplot(diam_df_depth['Diameter'].dropna(),kde=False)
fig2.set(xlabel='Diameter of Crater',ylabel='Frequency',title='Frequency of craters by diameter')
print(fig2)

fig3=sb.distplot(diam_df_depth['Latitude'].dropna(),kde=False)
fig3.set(xlabel='Latitude of Crater',ylabel='Frequency',title='Frequency of craters by Latitude')
print(fig3)

# Plotting the scatterplot between volume and latitude
fig4=sb.regplot(x='Latitude',y='Volume',fit_reg=False, data=diam_df_depth)
fig4.set(xlabel='Latitude of Crater',ylabel='Volume of Crater Impact',title='Latitude vs Volume plot')
print(fig4)

# Description of Depth,Latitude, Diameter and Volume statistics
print('Description of depth')
des_depth=diam_df_depth['Depth'].describe()
print(des_depth)

print('Description of diameter')
des_diameter=diam_df_depth['Diameter'].describe()
print(des_diameter)

print('Description of latitude')
des_latitude=diam_df_depth['Latitude'].describe()
print(des_latitude)

print('Description of Volume')
des_volume=diam_df_depth['Volume'].describe()
print(des_volume)

# Actual distributions
print('New Value count of depth:')
depth_count2=diam_df_depth['Depth'].value_counts(sort=False,dropna=False)
print(depth_count2)

print('Frequency distribution of depth:')
depth_freq2=diam_df_depth['Depth'].value_counts(sort=False,dropna=False,normalize=True)
print(depth_freq2)

print('Value count of Diameter:')
dia_count=diam_df_depth['Diameter'].value_counts(sort=False,dropna=False)
print(dia_count)

print('Frequency Distribution of Diameter:')
dia_count=diam_df_depth['Diameter'].value_counts(sort=False,dropna=False,normalize=True)
print(dia_count)

print('Value Count of latitude:')
lat_count=diam_df_depth['Latitude'].value_counts(sort=False,dropna=False)
print(lat_count)

print('Frequency Distribution of latitude:')
lat_freq=diam_df_depth['Latitude'].value_counts(sort=False,dropna=False,normalize=True)
print(lat_freq)



#%%
print('Replacing missing data with NaN')
dia3['DIAM_CIRCLE_IMAGE']=dia3['DIAM_CIRCLE_IMAGE'].replace(0,np.nan)

print('Counting the frequency of Diameters after replacing the missing values with NaN:')
diam_count2=dia3['DIAM_CIRCLE_IMAGE'].value_counts(sort=False,dropna=False)
print(diam_count2)
if len(diam_count) == len(diam_count2):
    print('There is no missing data in the dataframe.')
