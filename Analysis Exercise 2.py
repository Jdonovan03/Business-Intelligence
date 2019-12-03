#!/usr/bin/env python
# coding: utf-8

# In[88]:


import pandas as pd

Location = "axisdata.csv"
df = pd.read_csv(Location)
df.head()


# In[65]:


df['Cars Sold'].mean()


# In[7]:


df['Cars Sold'].max()


# In[8]:


df['Cars Sold'].min()


# In[9]:


pd.pivot_table(df, values=['Cars Sold'], index= ['Gender'])


# In[10]:


df[df['Cars Sold']>3]['Hours Worked'].mean()


# In[11]:


df['Years Experience'].mean()


# In[12]:


df[df['Cars Sold']>3]['Years Experience'].mean()


# In[16]:


pd.pivot_table (df,values=['Cars Sold'], index=['SalesTraining'])


# In[194]:


import matplotlib.pyplot as plt
import pandas as pd
get_ipython().magic(u'matplotlib inline')
Location = "axisdata.csv"
df = pd.read_csv(Location)
df.head()
df.hist()
df.hist(column="Years Experience")


# In[197]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')
Location = "axisdata.csv"
df = pd.read_csv(Location)
df.head()


# In[205]:


plt.scatter(df['Hours Worked'], df['Cars Sold']),

