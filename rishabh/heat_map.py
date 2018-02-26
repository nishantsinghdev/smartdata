
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().magic('matplotlib inline')

def heat_map(filepath):
    sep=','
    df = pd.read_csv(filepath,sep,index_col=False)


    #get only the numeric values of dataframe
    pp=df._get_numeric_data()

    plt.figure(figsize = (10,10))
    sns_img=sns.heatmap(pp,linewidths=0.10)
    plt.show()
    s=sns_img.get_figure()
    s.savefig('D:\imgg.png')
heat_map(filepath)

