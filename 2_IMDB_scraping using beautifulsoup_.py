#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[3]:


#importing the required library 
from bs4 import BeautifulSoup
import requests


# In[4]:


#send get request to web server to get page content data
webpage=requests.get("https://www.imdb.com/list/ls055386972/")
webpage


# In[5]:


webpage


# In[6]:


soup=BeautifulSoup(webpage.content)


# In[7]:


soup


# In[22]:


#scraping multiple movie title
titles=[] #empty list to store the data


# In[19]:


for i in soup.find_all('a', class_='href'):
    titles.append(i.text)


# In[106]:


titles


# In[20]:


rating=[]

for i in soup.find_all('div',class_='ipl-rating-star small'):
    rating.append(i.text)


# In[21]:


rating


# In[10]:


year=[]

for i in soup.find_all('span',class_='lister-item-year text-muted unbold'):
    year.append(i.text)


# In[85]:


year


# In[11]:


import pandas as pd


# In[22]:


df=pd.DataFrame({'a','span'})


# In[23]:


df


# In[ ]:




