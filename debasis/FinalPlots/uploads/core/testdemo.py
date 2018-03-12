
################yobin/ final+scatter+plot.py
import csv
import os.path
my_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
path = os.path.join(my_path, 'documents/Leadss.csv')
fpath = os.path.join(my_path, 'static/images/scatter')

import matplotlib
matplotlib.use('Agg')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import threading
data = path


def scatter(data):
    sep = ','
    #threading.thread()
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
    a = 0
    for col_name in first_col:
        if col_name != set_col:
            # for each png figure create fig separetely
            fig = plt.figure()
            plt.scatter(pp[set_col], pp[col_name])
            plt.xlabel(set_col)
            plt.ylabel(col_name)
            plt.title(set_col + ' vs ' + col_name)
            xx = int_x
            yy = int_y
            plt.rcParams["figure.figsize"] = [xx, yy]
            #plt.show()
            #figure = set_col + ' vs ' + col_name
            fig.savefig(fpath+'\\'+'figure'+str(a)+'.png')
            a = a+1
            #fig.savefig(figure + '.png')
            plt.close()

            plt.close(fig)
            fig.clear()
            # plt.close()
#scatter(data)
# In[ ]:


# In[ ]:



