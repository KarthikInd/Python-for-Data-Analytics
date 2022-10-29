#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import pandas as pd


# In[6]:


df = pd.read_excel (r'Desktop\Insurance.xlsx')
print (df)


# In[3]:


df.head()


# In[4]:


df.head(10)


# In[9]:


df.columns


# In[11]:


df.drop(columns='Region')


# In[13]:


len(df)


# In[14]:


df.iloc[0:5,0:4]


# In[18]:


df.loc[[0,2,4],['Policy','Expiry','Location']]


# In[19]:


df.dtypes


# In[21]:


df.sample(n=20)


# In[23]:


df.Column1.unique()


# In[24]:


df.Column1.nunique()


# In[31]:


df.replace('Karthik A','Karthik')


# In[32]:


df.rename(columns={"Column1":"Name"})


# In[39]:


df.groupby(["State","Location"])["InsuredValue"].sum()


# In[42]:


pd.crosstab(df['Region'],df['Location'])


# In[43]:


df['InsuredValue'].describe()


# In[44]:


df.nlargest(5,"InsuredValue")


# In[45]:


df.nsmallest(5,"InsuredValue")


# In[46]:


df.explode('Construction')


# In[47]:


arr=[]
n=int(input())
for i in range(n):
    v=int(input())
    arr.append(v)
a=np.array(arr)


# In[48]:


print(a)


# In[50]:


print(np.zeros(2*2))


# In[52]:


print(np.ones(2*2))


# In[54]:


df.drop_duplicates("Column1")


# In[73]:


df['Earthquake'] = df['Earthquake'].astype('category')


# In[74]:


df['Earthquake'] = df['Earthquake'].cat.rename_categories({'Y': "Yes", 'N': "No"})


# In[69]:


df.to_string("Flood")


# In[75]:


df


# In[76]:


df['Column1'].str.split(' ', expand=True)


# In[87]:


df['Column1'].str.capitalize()


# In[83]:


df


# In[88]:


df=df['Column1'].str.split(' ', expand=True)


# In[89]:


df


# In[91]:


d=df.rename(columns={0:"First_Name",1:"Last_Name"})


# In[7]:


df


# In[12]:


df["State"].sort_values(ascending = True)


# In[16]:


df.sort_values(by=["Policy", "State", "Region"],ascending=[True, True, False])


# In[17]:


s=df["State"].value_counts().sort_values(ascending=False).head(10)


# In[18]:


s


# In[19]:


import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns 
from matplotlib import style 
import datetime as dt
style.use("ggplot")


# In[20]:


s.plot.bar()
plt.xlabel("States")
plt.ylabel("Number of Policies")
plt.title("Number of Policies Provided by State")
plt.tight_layout()
plt.margins(0.05)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




