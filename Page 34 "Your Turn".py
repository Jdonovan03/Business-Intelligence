#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd

Location = "gradedata.csv"
df = pd.read_csv(Location)

bins = [0,80,100]
status_names = ['Fail','Pass']
df['status']=pd.cut(df['grade'], bins, labels=status_names)

df.head()


# In[ ]:




