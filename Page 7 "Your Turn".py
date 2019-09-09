#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd 
Location = "http://censusdata.ire.org/12/all_040_in_12.P1.csv"
# to add headers as we load the data...
df=pd.read_csv(Location, names=['Names','Value'])
# To add header to a dataframe
df.columns=['Names','Values']


# In[17]:


df.head()

