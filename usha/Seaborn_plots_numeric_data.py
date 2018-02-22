#SEABORN PLOTS FOR NUMERIC DATA OF ECOMMERCE DATASET
#
#

#DISTPLOT

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import seaborn as sns

data = input('enter the data path ')#'C:\Users\Usha\Downloads\Ecommerce Purchases.csv'
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
        sns.distplot(pp[num],bins,label='histogram '+str(a),kde=True,rug=True)
        plt.xlabel('bins '+str(a))
        plt.ylabel(num)
        plt.legend()
        plt.show()
        a = a+1
        #fig.savefig(path_name+'\\'+num+'.png')
        fig.savefig(num+'.png')
histo(data)

#
#
#



#BOXPLOT

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import platform
import os
import seaborn as sns
%matplotlib inline


data = input('enter the data path ')#'C:\Users\Usha\Downloads\Ecommerce Purchases.csv'
def box(data):
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
    set_col = first_col[1]

    int_x = 10
    int_y = 10

    #get the path of Downloads
    #path_name = os.path.expanduser('~\Downloads')

    a = 1
    for num in first_col:
        fig = plt.figure()
        sns.set_style("whitegrid")
        sns.boxplot(x=pp[num])
        
       
        plt.legend()
        plt.show()
        a = a+1
        #fig.savefig(path_name+'\\'+num+'.png')
        fig.savefig(num+'.png')
box(data)



#
#
#

#REGPLOT

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import platform
import os

data = input('enter the data path ')#'C:\Users\Usha\Downloads\Ecommerce Purchases.csv'
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
    set_col = first_col[1]

    int_x = 10
    int_y = 10

    #get the path of Downloads
    #path_name = os.path.expanduser('~\Downloads')

    for col_name in first_col:
        if col_name!=set_col:
            #for each png figure create fig separetely
            fig = plt.figure()
            sns.regplot(pp[set_col],pp[col_name],data=df,scatter=True, color="g")
            plt.xlabel(set_col)
            plt.ylabel(col_name)
            plt.title(set_col + ' vs ' + col_name)
            xx = int_x
            yy = int_y
            plt.rcParams["figure.figsize"] = [xx,yy]
            plt.show()
            figure = set_col + ' vs ' + col_name
            #fig.savefig(path_name+'\\'+figure+'.png')
            fig.savefig(figure+'.png')
            
scatter(data)
