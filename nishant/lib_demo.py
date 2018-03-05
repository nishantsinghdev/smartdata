import pandas as pd
import numpy as np
import seaborn as sns
import math
import matplotlib

import matplotlib.pyplot as plt
matplotlib.use('Agg')

import threading
data = path

import csv
import os

my_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..'))
path = os.path.join(my_path, 'documents/Ecommerce_Purchases.csv')
fpath1 = os.path.join(my_path, 'static/images/boxplot')
fpath2 = os.path.join(my_path, 'static/images/dist')
fpath3 = os.path.join(my_path, 'static/images/scatter')


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
        fig.savefig(fpath1 + '\\' + num + '.png')
        plt.close()


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
        fig.savefig(fpath2 + '\\' + num + '.png')
        plt.close()
        #fig.savefig(num+'.png')


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
            figure = set_col + ' vs ' + col_name
            fig.savefig(fpath3+'\\'+figure+'.png')
            #fig.savefig(figure + '.png')
            plt.close()

            plt.close(fig)
            fig.clear()
            # plt.close()


'''
# For calling the functions :
histo(data)
scatter(data)
box(data)
'''
