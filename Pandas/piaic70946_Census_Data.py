#!/usr/bin/env python
# coding: utf-8

# In[189]:


import numpy as np
import pandas as pd


# In[190]:


from os import listdir

filepaths = [f for f in listdir("./") if f.endswith('.csv')]
us_census = pd.concat(map(pd.read_csv, filepaths), ignore_index = True)


# In[201]:


filepaths


# In[204]:


us_census.head(80)


# In[205]:


us_census.drop(columns = ['Unnamed: 0'], inplace=True)


# In[206]:


us_census[['Male','Female']] = us_census.GenderPop.str.split("_",expand=True) 


# In[207]:


us_census.drop(columns = ['GenderPop'], inplace=True)


# In[208]:


us_census['Income'] = us_census.Income.str.strip('$')


# In[209]:


us_census = us_census.replace('%','', regex=True)


# In[210]:


us_census = us_census.replace('F','', regex=True)


# In[211]:


us_census = us_census.replace('M','', regex=True)


# In[212]:


us_census.loc[:,'Hispanic':'Income'] = round(us_census.loc[:,'Hispanic':'Income'].apply(pd.to_numeric),2)


# In[213]:


us_census['Male'] = us_census['Male'].astype(int)


# In[214]:


us_census.drop(columns = ['Female'], inplace=True)


# In[215]:


us_census['Female'] = us_census['TotalPop'] - us_census['Male']


# In[216]:


us_census.dtypes


# In[217]:


import matplotlib.pyplot as plt
plt.scatter(us_census['Female'],us_census['Income'])
plt.xlabel('Salary $', fontsize=18)
plt.ylabel('Female_Population', fontsize=16)
plt.show()


# In[218]:


us_census.duplicated()


# In[219]:


us_census.drop_duplicates(inplace= True)


# In[220]:


plt.scatter(us_census['Female'],us_census['Income'])
plt.xlabel('Salary $', fontsize=18)
plt.ylabel('Female_Population', fontsize=16)
plt.show()


# In[221]:


us_census.duplicated()


# ### ploting histograms for races 

# In[222]:


us_census


# In[223]:


us_census.describe()


# In[224]:


histo =  round(us_census.loc[:,'Hispanic':'Pacific'].apply(lambda x:x*us_census['TotalPop']/100))


# In[225]:


histo.head()


# In[226]:


histo.fillna(method='bfill', inplace = True)


# In[227]:


histo.astype(int)


# In[228]:


histo['total_pop'] =us_census['TotalPop']
histo['state'] = us_census['State']


# In[229]:


histo.hist(column='Hispanic')


# In[230]:


histo.hist(column='White')


# In[231]:


histo.hist(column='Black')


# In[232]:


histo.hist(column='Native')


# In[233]:


histo.hist(column='Asian')


# In[234]:


histo.hist(column='Pacific')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




