#!/usr/bin/env python
# coding: utf-8

# In[5]:


arr=[]
n=int(input())

#for(i=0;i<n;i++)  value of i starts from 0 and ends at n-1
#arr=   1,2,3,4
#index= 0,1,2,3

for i in range(n): 
    x=int(input())
    arr.append(x)


# In[6]:


arr


# In[7]:


arr[0:2]


# In[8]:


arr[:]


# In[12]:


arr2=arr[::-1]


# In[11]:


arr


# In[14]:


arr==arr2


# In[15]:


arr.append(5)


# In[16]:


arr


# In[19]:


arr.insert(4,6)   #arr.insert(position, value)


# In[20]:


arr


# In[21]:


arr=[10,20,30,40]


# In[22]:


arr


# In[24]:


arr.append(50)  #arr.append(value)


# In[25]:


arr


# In[26]:


arr.remove(50) #arr.remove(value) 


# In[27]:


arr


# In[28]:


arr.insert(0,5)  #arr.insert(index/position, value)


# In[29]:


arr


# In[30]:


arr.reverse()


# In[31]:


arr


# In[33]:


arr.index(50)


# In[35]:


arr.append(20)


# In[36]:


arr.index(20)


# In[ ]:


# a=[10,20,30,40,50,60,20,70], find count of 20


# In[37]:


a=[10,20,30,40,50,60,20,70]


# In[42]:


count=0
for i in a:
    if i==20:
        count+=1   #count=count+1
print(count)


# In[43]:


a.sort()


# In[44]:


a


# In[45]:


a.remove(20)


# In[47]:


a


# In[53]:


multi=1
for karthik in a:
    multi=multi*karthik
print(multi)


# In[58]:


def multiplication(arr):
    sum=0
    for karthik in a:
        sum=sum+karthik
    return sum

a=[10, 20, 30, 40, 50, 60, 70]
print(multiplication(arr))    


# In[ ]:





# In[ ]:





# In[ ]:




