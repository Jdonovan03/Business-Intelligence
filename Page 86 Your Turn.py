#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')

names = ['Bob','Jessica','Mary','John','Mel']
absences = [3,0,1,0,8]
detentions = [2,1,0,0,1]
warnings= [2,1,5,1,2]

GradeList =zip(names,absences,detentions,warnings)
columns=['Names','Absences','Detentions','Warnings']
df = pd.DataFrame(data = GradeList, columns=columns)

df

df['TotalDemerits'] = df['Absences'] + df['Detentions'] + df['Warnings']
df

plt.pie(df['TotalDemerits'])
plt.pie(df['TotalDemerits'],
       labels=df['Names'],
       explode=(0,0,0,0.25,0),
       startangle=150,
       autopct='%1.1f%%',)

plt.axis('equal')

df


# In[ ]:




