#!/usr/bin/env python
# coding: utf-8

# In[127]:


import folium
from folium import plugins
from folium.plugins import MarkerCluster
import csv
import pandas as pd
import json
import matplotlib as pl


# In[188]:


#read data
states=pd.read_csv('C:/Users/Jimmy/Documents/states.csv')


# In[189]:


data=pd.DataFrame(states)
data


# In[246]:


#population
m = folium.Map(location=[38, -97], tiles='CartoDB dark_matter', zoom_start= 4.4)
for i in range(0,len(data)):
    folium.CircleMarker(
        location=[data.iloc[i]['usa_state_latitude'], 
                  data.iloc[i]['usa_state_longitude']],
        popup=data.iloc[i]['usa_state'],
        radius=data.iloc[i]['Percent of Total']*3,
        color='#007849',
        fill=True,
        fill_color='#007849'
    ).add_to(m)

m


# In[250]:


#electoral votes
m = folium.Map(location=[38, -97], tiles='CartoDB dark_matter', zoom_start= 4.4)
for i in range(0,len(data)):
    folium.CircleMarker(
        location=[data.iloc[i]['usa_state_latitude'], 
                  data.iloc[i]['usa_state_longitude']],
        popup=data.iloc[i]['Electoral Votes'],
        radius=int(data.iloc[i]['Electoral Percentage']*3),
        color='hotpink',
        fill=True,
        fill_color='hotpink'
    ).add_to(m)
m


# In[231]:


#Legend
m = folium.Map(location=[35, -130], tiles='CartoDB dark_matter', zoom_start= 4.4)
folium.CircleMarker(
        location=[25,-150],
        radius=[3],
        color='hotpink',
        fill=True,
        fill_color='hotpink'
    ).add_to(m)
folium.CircleMarker(
        location=[30,-150],
        radius=[9],
        color='hotpink',
        fill=True,
        fill_color='hotpink'
    ).add_to(m)
folium.CircleMarker(
        location=[36,-150],
        radius=[18],
        color='hotpink',
        fill=True,
        fill_color='hotpink'
    ).add_to(m)
folium.CircleMarker(
        location=[44,-150],
        radius=[36],
        color='hotpink',
        fill=True,
        fill_color='hotpink'
    ).add_to(m)

folium.CircleMarker(
        location=[25,-170],
        radius=[3],
        color='#007849',
        fill=True,
        fill_color='#007849'
    ).add_to(m)
folium.CircleMarker(
        location=[30,-170],
        radius=[9],
        color='#007849',
        fill=True,
        fill_color='#007849'
    ).add_to(m)
folium.CircleMarker(
        location=[36,-170],
        radius=[18],
        color='#007849',
        fill=True,
        fill_color='#007849'
    ).add_to(m)
folium.CircleMarker(
        location=[44,-170],
        radius=[36],
        color='#007849',
        fill=True,
        fill_color='#007849'
    ).add_to(m)
m


# In[249]:


m = folium.Map(location=[38, -97], tiles='CartoDB dark_matter', zoom_start= 4.4)
for i in range(0,len(data)):
    folium.CircleMarker(
        location=[data.iloc[i]['usa_state_latitude'], 
                  data.iloc[i]['usa_state_longitude']],
        popup=data.iloc[i]['Electoral Votes'],
        radius=int(data.iloc[i]['Electoral Percentage']*3),
        color='hotpink',
        fill=True,
        fill_color='hotpink'
    ).add_to(m)
for i in range(0,len(data)):
    folium.CircleMarker(
        location=[data.iloc[i]['usa_state_latitude'], 
                  data.iloc[i]['usa_state_longitude']],
        popup=data.iloc[i]['usa_state'],
        radius=data.iloc[i]['Percent of Total']*3,
        color='#007849',
        fill=True,
        fill_color='#007849'
    ).add_to(m)
m


# In[ ]:




