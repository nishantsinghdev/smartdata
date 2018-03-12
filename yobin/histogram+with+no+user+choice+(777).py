
# coding: utf-8

# In[21]:




# In[5]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import os
#import platform

data = input('enter the data path ')#'C:\Users\yobin\Desktop\Ecommerce Purchases.csv'
def histo(data):
    sep = ','
    header = 'None'
    df = pd.read_csv(data,header,sep)
    datatype= df.dtypes

    #get only the numeric values of dataframe
    pp=df._get_numeric_data()

    #convert the pp to 2d array
    df1=pp.values

    #get the first columns array
    first_col = list(pp)
    print(first_col)
    np_2d = np.array(df1)
    #get the number of rows in a file
    n = np_2d.shape[0]

    #path_name = os.path.expanduser('~\Downloads')
    #press shift + tab for backing all selected by 1 tab and press tab only for selected things to move forward
    a = 1
    for num in first_col:
        fig = plt.figure()
        bins = round(2*n**(1/3))
        print(bins)
        plt.hist(pp[num],bins,label='histogram '+str(a))
        plt.xlabel('bins '+str(a), fontsize = 20)
        plt.ylabel(num, fontsize = 20)
        plt.legend()
        plt.title(num,fontsize = 20)
        plt.show()
        a = a+1
        #fig.savefig(path_name+'\\'+num+'.png')
        fig.savefig(num+'.png')
histo(data)



# In[ ]:



