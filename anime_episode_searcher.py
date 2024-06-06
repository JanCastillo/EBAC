#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup as bs
import os


# In[35]:


anime_name = input('Captura el nombre del anime que quieres buscar: ')


# In[36]:


response_API = requests.get(f'https://www.animenewsnetwork.com/encyclopedia/reports.xml?id=155&type=anime&name={anime_name}')


# In[37]:


soup_anime = bs(response_API.text, 'lxml')


# In[52]:


search_results = soup_anime.select('item')


# In[64]:


result_list = []

for result in search_results:
    anime_id = result.select('id')[0].get_text()
    anime_name = result.select('name')[0].get_text()
    anime_release = result.select('vintage')[0].get_text()

    result_list.append({'id': anime_id, 'name': anime_name, 'release_date': anime_release})


# In[68]:


for r in result_list:
    print(r)


# In[69]:


anime_id_query = input('Captura el id del anime que quieres buscar: ')


# In[70]:


response_query = requests.get(f'https://cdn.animenewsnetwork.com/encyclopedia/api.xml?anime={anime_id_query}')


# In[71]:


soup_query = bs(response_query.text, 'lxml')


# In[73]:


episodes = soup_query.select('episode')


# In[94]:


for ep in episodes:
    print(ep['num'] + ' ' + ep.select('title')[0].get_text())


# In[ ]:




