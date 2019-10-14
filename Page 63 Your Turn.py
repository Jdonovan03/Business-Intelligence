#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
Location = "gradedata.csv"
df = pd.read_csv(Location)

def gen_to_num(x):
    if x == 'female':
        return 1
    if x == 'male':
        return 0

df['gender_val']= df['gender'].apply(gen_to_num)

df.head()


# In[7]:


import statsmodels.formula.api as sm
result = sm.ols(formula='grade~exercise+hours', data=df).fit()
result.summary()


# In[ ]:




