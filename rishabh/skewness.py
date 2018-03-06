
# coding: utf-8

# In[18]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.tools.plotting import table

data = input('enter the path name')

def sk_kurt(data):
    header = None
    sep = ','
    empdf = pd.DataFrame()
    df = pd.read_csv(data,sep,header)   # C:\Users\yobin\Desktop\c.csv     Ecommerce Purchases
    c=0
    t=0
    df1 = df.skew()
    li = list(df1)
    ke = df1.keys()
    while(t<len(li)):
        if(li[t]>0):
            li[t]='positively skewed'
        elif(li[t]<0):
            li[t]='negatively skewed'
        else:
            li[t]='symmetric'
        t=t+1
        
    while(c<len(li)):
        empdf = empdf.append({'column_name':ke[c],'skewness':li[c]},ignore_index=True)
        c=c+1
    empdf
    ax = plt.subplot(111)         
    table(ax, empdf, loc='center')
    ax.set_axis_off()
    plt.savefig('skewness.png')
sk_kurt(data)

