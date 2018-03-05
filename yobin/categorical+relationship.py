
# coding: utf-8

# In[7]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = input('enter the path name')

def cat_relation(data):
    header = None
    sep = ','
    df = pd.read_csv(data,sep,header)   # C:\Users\yobin\Desktop\c.csv     Ecommerce Purchases
    #to get table of a series use reset_index
    arr = []
    #ap=df.select_dtypes(exclude=['number'])
    first_col = list(df)
    n=0
    str_arr = []
    for cln in first_col:
        arr.append(np.array(df.iloc[:,n]))
        n = n+1
    #print(type(arr))
    indx_colno = 0
    last_no = 0
    ar_len = len(first_col) - 1 
    #print(ar_len)
    i = 0

    while i <= ar_len - 1:
        f_a = []
        j = 0
        f_a = arr[i]
        j = i+1
        while j <= ar_len:
            fig = plt.figure()
            ct = pd.crosstab(f_a,arr[j],rownames=['row'],colnames=['col'])
            print('\n\n')
            # now stack and reset
            stacked = ct.stack().reset_index().rename(columns={0:'value'})
            # plot grouped bar chart
            lb = sns.barplot(x=stacked.row, y=stacked.value, hue=stacked.col)
            #label in seaborn
            lb.set(xlabel=first_col[i],ylabel=first_col[j])
            #title
            lb.set_title(first_col[i] + ' vs ' + first_col[j])
            plt.show()
            fig.savefig('PIC ' + str(i)+str(j) +'.png')
            j = j + 1
        i = i + 1
cat_relation(data)  






# In[ ]:



