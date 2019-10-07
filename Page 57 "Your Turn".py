#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel','Sam','Courtney','Jackie']
grades = [76,95,77,77,99,80,32,50]
hoursstudy = [11,5,5,3,0,3,2,1]

Gradelist = zip(names,grades,hoursstudy)
df= pd.DataFrame(data = Gradelist, columns=['Names', 'Grades', 'StudyHours'])
df ['Grades'].describe()


# In[ ]:




