########################     usha/ssd_boxplot_seaborn.ipynb

import csv
import os.path
my_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..'))
path = os.path.join(my_path, 'documents/Ecommerce_Purchases.csv')
fpath = os.path.join(my_path, 'static/images/boxplot')

#print(my_path)


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import platform
import os
import seaborn as sns

  #'C:\\DJANGO_Projects\\file_upload\\simple-file-upload-master\\documents\\Ecommerce_Purchases.csv'
data = path

def box(data):
    sep = ','
    header = 'None'
    df = pd.read_csv(data, header, sep)
    datatype = df.dtypes
    # get only the numeric values of dataframe
    pp = df._get_numeric_data()

    # convert the pp to 2d array
    df1 = pp.values
    # print(df1)

    # get columns list
    first_col = list(pp)
    # print(first_col)
    set_col = first_col[1]

    int_x = 10
    int_y = 10

    # get the path of Downloads
    # path_name = os.path.expanduser('~\Downloads')

    a = 1
    for num in first_col:
        fig = plt.figure()
        sns.set_style("whitegrid")
        sns.boxplot(x=pp[num])

        #plt.legend()
        #plt.show()
        a = a + 1
        # fig.savefig(path_name+'\\'+num+'.png')
        #fig.savefig(num + '.png')
        fig.savefig(fpath + '\\' + num + '.png')
        plt.close()


box(data)