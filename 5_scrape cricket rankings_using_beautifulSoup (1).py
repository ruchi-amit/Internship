#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[4]:


from bs4 import BeautifulSoup
import requests


# In[5]:


webpage=requests.get("https://www.icc-cricket.com/rankings/mens/team-rankings/t20i")


# In[6]:


webpage


# In[7]:


Soup=BeautifulSoup(webpage.content)


# In[8]:


Soup


# In[69]:


first_data=Soup.find("div",attrs={"data-cricket-scope":"odi"}).find("div",class_="rankings-block__top-player").get_text(strip=True,separator=" ").split(" ")

other_data=Soup.find("div",attrs={"data-cricket-scope":"odi"}).find_all("tr",class_="table-body")

final_lst=[]
final_lst.append(first_data)

for i in data:
    split_lst=i.get_text(strip=True,separator=" ").split(" ")
    final_lst.append(split_lst)


# In[9]:


first_data=Soup.find("span",class_="u-hide-phablet")
first_data


# In[10]:


first_data.text


# In[11]:


team=[]
for i in Soup.find_all('span',class_="u-hide-phablet"):
    team.append(i.text)


# In[35]:


team[0:10]


# In[37]:


first_data=Soup.find("td",class_="rankings-block__banner--matches") #,"rankings-block__banner--points","rankings-block__banner--rating u-text-right")
first_data


# In[38]:


first_data.text


# In[82]:


match=[]      
for i in Soup.find('tr',class_="table-body").find_all('td',class_="table-body__cell u-center-text"):
     match.append(i.text)


# In[83]:


match[0:30]


# In[91]:


rating=[]
        
for i in Soup.find_all('tr',class_="table-body").find_all('td',class_="table-body__cell u-center-text"):
     rating.append(i.text)


# In[92]:


rating


# In[ ]:





# In[93]:


import pandas as pd


# In[99]:


df=pd.DataFrame({'team','match','rating'})


# In[100]:


df


# In[ ]:




