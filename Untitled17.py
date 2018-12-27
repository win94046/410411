
# coding: utf-8

# In[32]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[33]:


# Warnings
import warnings
warnings.filterwarnings('ignore')


# In[34]:


# Style
sns.set(style='darkgrid')
plt.rcParams["patch.force_edgecolor"] = True


# In[35]:


import os
print(os.listdir("C:/Users/user/Desktop/BreadBasket_DMS_1_"))


# In[36]:


df = pd.read_csv("C:/Users/user/Desktop/BreadBasket_DMS_1_/BreadBasket_DMS_1_.csv")


# In[37]:


print('Dataset Information: \n')
print(df.info())


# In[38]:


print('Unique Items: ', df['Item'].nunique())
print( '\n', df['Item'].unique()) #列出每個項目


# In[39]:


print(df.isnull().sum().sort_values(ascending=False))


# In[40]:


print('First Ten Rows of the DataFrame: \n')
print(df.head(10))


# In[41]:


print('Unique Items: ', df['Item'].nunique())
print( '\n', df['Item'].unique())


# In[42]:


print(df.isnull().sum().sort_values(ascending=False)) #看數據有沒有遺漏直


# In[43]:


print(df[df['Item']=='NONE']) #找出數據集的none直


# In[44]:


df.drop(df[df['Item']=='NONE'].index, inplace=True) #消除NONE的數據


# In[45]:


print(df.info())


# In[48]:


#麵包店裡賣得最多的東西
most_sold = df['Item'].value_counts().head(15)

print('Most Sold Items: \n')
print(most_sold)

