
# coding: utf-8

# In[21]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import platform
#import os

data = input('enter the data path ')#'C:\Users\yobin\Desktop\Ecommerce Purchases.csv'
def scatter(data):
    sep = ','
    header = 'None'
    df = pd.read_csv(data,header,sep)
    datatype= df.dtypes

    #get only the numeric values of dataframe
    pp=df._get_numeric_data()

    #convert the pp to 2d array
    df1=pp.values
    #print(df1)
    
    #get columns list
    first_col = list(pp)
        
    #print(first_col)
    #set_col = first_col[1]
    col_len = len(first_col)
    ar_len = col_len-1

    int_x = 10
    int_y = 10

    #get the path of Downloads
    #path_name = os.path.expanduser('~\Downloads')
    a = 0
    i=0
    for col_name in first_col:
        indx_colno = first_col.index(col_name)
        last_no = indx_colno+1
        while last_no <= ar_len :
            next_col = first_col[last_no]
            #print(col_name + ' vs ' + next_col)
            last_no = last_no + 1
            #for each png figure create fig separetely
            fig = plt.figure()
            plt.scatter(pp[col_name],pp[next_col])
            plt.xlabel(next_col)
            plt.ylabel(col_name)
            plt.title( col_name + ' vs ' + next_col)
            xx = int_x
            yy = int_y
            plt.rcParams["figure.figsize"] = [xx,yy]
            plt.show()
            #figure = set_col + ' vs ' + col_name
            #fig.savefig(path_name+'\\'+figure+'.png')
            fig.savefig('figure'+str(a)+'.png')
            a = a+1
scatter(data)


    



        
    
    
    







# In[ ]:




# In[ ]:



