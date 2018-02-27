
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

#D:\Book4.csv 
data = input('enter the data path ')
sep = input('enter the seperater ')
df = pd.read_csv(data,sep)

#select all non-num data
ap=df.select_dtypes(exclude=['number'])

#convert into array
df2=ap.as_matrix()

#numpy array
ap_2d = np.array(df2)

#list of all non-numerical col 
first_col = list(ap)
print(first_col)

#plot
for a in first_col:
    df.boxplot(by=a,figsize=(20,10))

