#!/usr/bin/env python
# coding: utf-8

# In[4]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[11]:


#importing the required library 
from bs4 import BeautifulSoup


# In[13]:


import requests


# In[14]:


#send get request to web server to get page content data
webpage=requests.get("https://en.wikipedia.org/wiki/Main_Page")


# In[15]:


webpage


# In[18]:


soup=BeautifulSoup(webpage.content)


# In[19]:


soup


# In[30]:


All_titles = soup.find_all(['h1','h2','h3','h4'])


# In[31]:


All_titles


# In[33]:


import pandas as pd


# In[34]:


df=pd.DataFrame({'h1','h2','h3','h4'})


# In[35]:


df


# In[ ]:




