#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[2]:


from bs4 import BeautifulSoup
import requests


# In[3]:


webpage=requests.get("https://presidentofindia.nic.in/former-presidents.htm a")
webpage


# In[4]:


soup=BeautifulSoup(webpage.content)
soup


# In[32]:


titles=[]


# In[35]:


for i in soup.find_all('h3', class_='presidentListing'):
    titles.append(i.text)


# In[36]:


titles


# In[37]:


termsofoffice=[]


# In[38]:


for i in soup.find_all('p', class_='terms'):
    termsofoffice.append(i.text)


# In[39]:


termsofoffice


# In[40]:


import pandas as pd


# In[41]:


df=pd.DataFrame({'h3','p'})


# In[42]:


df


# In[ ]:




