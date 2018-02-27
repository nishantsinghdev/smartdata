############### usha/ssd_distplot_seaborn.ipynb

import csv
import os.path
my_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..'))
path = os.path.join(my_path, 'documents/Ecommerce_Purchases.csv')
fpath = os.path.join(my_path, 'static/images')

import pandas as pd
import numpy as np
import seaborn as sns
import math
import matplotlib

import matplotlib.pyplot as plt
matplotlib.use('Agg')

data = path #'C:\Users\Usha\Downloads\Ecommerce Purchases.csv'
def histo(data):
    print(data)
    sep = ','
    header = 'None'
    df = pd.read_csv(data,header,sep)
    datatype= df.dtypes

    #get only the numeric values of dataframe
    pp=df._get_numeric_data()

    #convert the pp to 2d array
    df1=pp.values
    print(pp.head(5))
    #get the first columns array
    first_col = list(pp)
    print(first_col)
    np_2d = np.array(df1)
    #get the number of rows in a file
    n = np_2d.shape[0]

    #path_name = os.path.expanduser('~\Downloads')
    #press shift + tab for backing all selected by 1 tab and press tab only for selected things to move forward
    a = 1
    d = 0
    for num in first_col:

        bins = round(2*n**(1/3))
        print(bins)
        distplot=sns.distplot(pp[num])
        print(distplot)
        fig=distplot.get_figure()
        #plt.xlabel('bins '+str(a))
        print(a)

        #plt.ylabel(num)


        #plt.legend()
        #fig.show()
        a = a+1
        #fig.savefig(num+'.png')
        fig.savefig(fpath + '\\' + 'image' + str(d) + '.png')
        d = d+1
        plt.close()
        #fig.savefig(num+'.png')
#histo(data)
