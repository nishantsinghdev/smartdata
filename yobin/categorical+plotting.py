
# coding: utf-8

# In[4]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = input('enter the path name')
def catg(data):
    header = None
    sep = ','
    df = pd.read_csv(data,sep,header)   # C:\Users\yobin\Desktop\c.csv     Ecommerce Purchases
    #to get table of a series use reset_index
    #select all non-num data
    ap=df.select_dtypes(exclude=['number'])
    #print(ap)
    #list of all non-numerical col 
    first_col = list(ap)
    print(first_col)
    a = 0
    for col_n in first_col:
        fig = plt.figure()
        #get the total number of repitition of values in a column with the key value pairs of a series
        s = ap.groupby(col_n).size()
        s.plot.bar()
        plt.show()
        fig.savefig('img' + str(a) + '.png')
        a = a+1
catg(data)




# In[ ]:



