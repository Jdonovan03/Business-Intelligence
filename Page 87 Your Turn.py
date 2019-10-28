#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
get_ipython().magic(u'matplotlib inline')
Location= "gradedata.csv"
df = pd.read_csv(Location)

plt.scatter(df['hours'], df['grade'])


# In[ ]:




