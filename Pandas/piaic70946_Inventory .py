#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[25]:


inventory = pd.read_csv('inventory.csv')
inventory.head(10)


# In[9]:


product_request = inventory[inventory['location'] == "Brooklyn"]
product_request


# In[26]:


inventory.dtypes


# In[27]:


seed_request = inventory[(inventory["location"] == "Brooklyn") & (inventory["product_type"] == "seeds")]


# In[28]:


seed_request


# In[29]:


inventory['in_stock'] = inventory['quantity'] > 0


# In[14]:


inventory


# In[20]:


inventory['total_value'] = inventory['price'] * inventory['quantity']


# In[21]:


combine_lambda = lambda row: '{} - {}'.format(row.product_type, row.product_description)


# In[22]:


combine_lambda


# In[23]:


inventory['full_description'] = inventory.apply(combine_lambda, axis=1) 



# In[24]:


inventory['full_description']


# In[30]:


inventory


# In[ ]:





# In[ ]:




