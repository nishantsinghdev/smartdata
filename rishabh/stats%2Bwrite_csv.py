
# coding: utf-8

# In[15]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sep=','
df = pd.read_csv('D:\Book2.csv',sep)
#get only the numeric values of dataframe
pp=df._get_numeric_data()


pp2=pp.describe()
pp2.to_csv("describe.csv")

