
# coding: utf-8

# In[6]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

data = input('enter the data path ')#'C:\Users\yobin\Desktop\Ecommerce Purchases.csv'
def box_plot(data):
    sep = ','
    header = 'None'
    df = pd.read_csv(data,header,sep)
    datatype= df.dtypes

    #get only the numeric values of dataframe
    pp=df._get_numeric_data()

    #convert the pp to 2d array
    df1=pp.values
    np_2d = np.array(df1)
    #get columns list
    first_col = list(pp)
    print(first_col)
    path_name = os.path.expanduser('~\Downloads')
    for col_name in first_col:
        fig = plt.figure()
        plt.boxplot(pp[col_name])
        plt.title(col_name)
        plt.show()
        #fig.savefig(col_name + '.png')
        fig.savefig(path_name+'\\'+col_name+'.png')
box_plot(data)







# In[ ]:




# In[ ]:




# In[ ]:



