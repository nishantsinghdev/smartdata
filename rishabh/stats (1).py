
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = input('enter the data path ')#'C:\Users\yobin\Desktop\Ecommerce Purchases.csv'
sep = input('enter the seperater ')
df = pd.read_csv(data,sep)
#get only the numeric values of dataframe
pp=df._get_numeric_data()


pp2=pp.describe()
pp2.to_csv("new.csv")

