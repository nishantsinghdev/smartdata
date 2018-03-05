
# coding: utf-8

# In[ ]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = input('enter the path name')

header = None
sep = ','
df = pd.read_csv(data,sep,header)   # C:\Users\yobin\Desktop\c.csv     Ecommerce Purchases
#to get table of a series use reset_index
arr = []
ap=df.select_dtypes(exclude=['number'])
first_col = list(ap)
n=0
str_arr = []
for cln in first_col:
    arr.append(np.array(ap.iloc[:,n]))
    n = n+1
print(type(arr))
indx_colno = 0
last_no = 0
ar_len = len(first_col) - 1 
print(ar_len)
i = 0

while i <= ar_len - 1:
    f_a = []
    j = 0
    f_a = arr[i]
    j = i+1
    while j <= ar_len:
        print(pd.crosstab(f_a,arr[j],rownames=['row'],colnames=['column']))
        print('\n\n')
        j = j + 1
    i = i + 1
        






# In[ ]:



