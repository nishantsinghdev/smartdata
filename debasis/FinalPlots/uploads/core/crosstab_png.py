

import os.path
my_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..'))
data = os.path.join(my_path, 'documents\\Book4.csv')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.tools.plotting import table

#data = input('enter the path name')

def cross_tab(data):
    header = None
    sep = ','
    df = pd.read_csv(data, sep, header)  # C:\Users\Usha\Desktop\c.csv     Ecommerce Purchases
    # to get table of a series use reset_index
    arr = []
    ap = df.select_dtypes(exclude=['number'])
    first_col = list(ap)
    n = 0
    str_arr = []

    for cln in first_col:
        arr.append(np.array(ap.iloc[:, n]))
        n = n + 1
    print(type(arr))
    indx_colno = 0
    last_no = 0
    ar_len = len(first_col) - 1
    #print(ar_len)
    i = 0
    # with each column with other column with bigger index than it
    while i <= ar_len - 1:
        f_a = []
        j = 0
        f_a = arr[i]
        j = i + 1
        while j <= ar_len:
            ddf = pd.crosstab(f_a, arr[j], rownames=[first_col[i]], colnames=[first_col[j]])
            # print('\n\n')
            # print(ddf)
            ax = plt.subplot(111)
            fig = plt.figure(figsize=(9, 11))
            table(ax, ddf, loc='center')
            ax.set_axis_off()
            plt.savefig('img' + str(i) + str(j) + '.png', bbox_inches='tight', figsize=(9, 11))
            j = j + 1
        i = i + 1

#cross_tab(data)