#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[ ]:


#load csv file from local path


# In[3]:


matches = pd.read_csv("C:\\Users\\rahul\\Downloads\\matches.csv", index_col=0) 


# In[4]:


matches.head()


# In[5]:


matches.shape


# In[7]:


matches["team"].value_counts()


# In[ ]:


#Checking datatypes of values


# In[9]:


matches.dtypes


# In[ ]:


#changing datatype from object to datetime


# In[10]:


matches["date"]= pd.to_datetime(matches["date"])


# In[11]:


matches.dtypes


# In[ ]:


#creating new columns
#machine learning can only be done with numeric datatypes so creating new columns havinng changed datatypes 


# In[12]:


matches["venue_code"]= matches["venue"].astype("category").cat.codes


# In[13]:


matches.dtypes


# In[15]:


matches["opp_code"]=matches["opponent"].astype("category").cat.codes


# In[16]:


#converting time (hour:minutes) to only hours
matches["hour"]=matches["time"].str.replace(":.+", "", regex = True).astype("int")


# In[17]:


matches["day_code"]=matches["date"].dt.dayofweek


# In[18]:


matches


# In[19]:


matches["target"] = (matches["result"] == "W").astype("int")


# In[20]:


matches

