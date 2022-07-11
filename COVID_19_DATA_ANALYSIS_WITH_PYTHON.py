#!/usr/bin/env python
# coding: utf-8

# # THIS IS THE DATA ANALYSISI ON COVID 19 USING PYTHON

# In[3]:


## IMPORTING THE MODULES
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[9]:


## IMPORTING THE COVID 19 DATASET
## TO GET THE FIRST 5 DATA

corona_dataset = pd.read_csv("datasets/covid19_Confirmed_dataset.csv")
corona_dataset.head()


# In[21]:


## TO DELETE THE USELESS COLUMNS IN THE ABOVE DATASET 
## THEIR IS A SPECIAL METHOD CALLED DROP
## AND AXIS IS USED BEACAAUSE TO DELETE THE ROWS WITHE THE NAMES HERE LAT AND LONG BUT THEIR ARE NO NAMES SO AXIS IS 1
## BUT DEFAULT THE AXIS IS 0

corona_dataset.drop(["Lat","Long"],axis=1)
corona_dataset.head()


# In[86]:


## TO DELETE THE PROVINCE/STATE COLUMN AND MARKING THE INDEX TO START WITH A COUNTRY
## AND CHECKING THE SHAPE

corona_dataset.drop(["Province/State"],axis=1)
corona_dataset.set_index("Country/Region")


# In[42]:


## LET US CHECK THE SHAPE OF THE DATASET

df = corona_dataset.groupby("Country/Region").sum()
df.shape


# In[44]:


## VISUALIZING THE DATA RELATED TO THE PARTICULAR COUNTRY 
## LET US CONSIDER THE COUNTRY AS INDIA

df.loc["India"]


# In[45]:


## LET US PLOT A GRAPH OF INDIA

df.loc["India"].plot()


# In[52]:


## LET US COMPARE THE 2 GRAPHS BY TAKING 2 COUNTRIES
## THE FIRST COUNTRY IS INDIA AND THE OTHER IS ITALY
## THE GRAPH IS SHOWN
## BUT THE GRAPH DIDNOT INDICATES WHICH LINE REFERS TO THE INDIA AND WHICH LINE REFERS TO THE ITALY
## SO WE HAVE USED A FUNCTION CALLED LEGEND()

df.loc["India"].plot()
df.loc["Italy"].plot()
plt.legend()


# In[53]:


## CALCULATING THE GOOD MEASURE OF THE COUNTRY INDIA

df.loc["India"].plot()


# In[58]:


## LET US CONSDIDER THE FIRST 15 DATES OF THE PANDEMIC

df.loc["India"][:15].plot()


# In[59]:


## TO KNOW THE INFECTION RATE 

df.loc["India"][:15].diff().plot()


# In[62]:


## TO KNOW THE MAXIMUM INFECTION RATE OF INDIA

df.loc["India"][:15].diff().max()


# In[64]:


## TO KNOW THE MAXIMUM INFECTION RATE OF China

df.loc["China"][:15].diff().max()


# In[71]:


## TO KNOW THE MAXIMUM INFECTION RATE OF THE ALL THE COUNTRIES

countries = list(df.index)
max_infection_rate=[]
for c in countries:
    max_infection_rate.append(df.loc[c].diff().max())
max_infection_rate


# In[72]:


## TO ADD THE COLUMN IN THE DATASET ON MAXIMUM INFECTION RATE

df["Maximum_Infection_Rate"] = max_infection_rate
df.head()


# In[197]:


## TO GET ONLY THE COUNTRY AND THE MAXIMUM INFECTION RATE ONLY SO WE CAN CREATE A NEW DATAFRAME

df["Maximum_Infection_Rate"]=max_infection_rate
df.head()


# In[192]:


## IMPOERTING THE WORLD HAPPINESS REPORT 

df2=pd.read_csv("datasets/worldwide_happiness_report.csv")
df2.head()


# In[193]:


## DELETE THE SOME THE USELESS COLUMNS

columns_useless = ["Overall rank","Score","Generosity","Perceptions of corruption"]
pjmh = df2.drop(columns_useless,axis=1)
pjmh.head()


# In[194]:


## WORLDWIDE HAPPINESS REPORT DATASET

pjmh.shape


# In[195]:


## CORONA DATASET SHAPE

df.shape


# In[202]:


pjmh143 = corona_dataset.join(pjmh,how='inner')


# In[203]:


## FINDING THE CORRELATION MATRIX

pjmh143.corr()


# In[209]:


## LET US MAKE THIS RESULTS WITH MORE UNDERSTANDING

x=pjmh143["GDP per capita"]
y=pjmh143["Social support"]
sns.scatterplot(x,np.log(y))


# In[210]:


sns.regplot(x,np.log(y))

