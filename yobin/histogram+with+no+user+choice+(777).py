
# coding: utf-8

# In[14]:




# In[5]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = input('enter the data path ')#'C:\Users\yobin\Desktop\Ecommerce Purchases.csv'
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


#press shift + tab for backing all selected by 1 tab and press tab only for selected things to move forward
a = 1
for num in first_col:
    bins = round(2*n**(1/3))
    plt.hist(pp[num],bins,label='histogram '+str(a))
    plt.xlabel('bins '+str(a))
    plt.ylabel(num)
    plt.legend()
    plt.show()
    a = a+1


# In[3]:

type(pp)


# In[ ]:



