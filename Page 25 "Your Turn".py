#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,-2,77,78,101]

Gradelist = zip(names,grades)
df = pd.DataFrame(data = Gradelist,
    columns=['Names','Grades'])  
df.loc[(df['Grades'] <=0, 'Grades')] = 0
df


# In[ ]:




