
# coding: utf-8

# In[14]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import platform
import os

data = input('enter the data path ')#'C:\Users\yobin\Desktop\Ecommerce Purchases.csv'
def scatter(data):
    sep = ','
    header = 'None'
    df = pd.read_csv(data,header,sep)
    datatype= df.dtypes
    print(df.head())
    print(datatype)

    #get only the numeric values of dataframe
    pp=df._get_numeric_data()
    print(pp)

    #convert the pp to 2d array
    df1=pp.values
    print(df1)
    #get columns list
    first_col = list(pp)
    print(first_col)
    set_col = first_col[1]

    int_x = 10
    int_y = 10
    arry_no = first_col.index(set_col)
    print(arry_no)

    #convert the array df1 into numpy array
    np_2d = np.array(df1)

    #select all rows of s column
    dep_col = np_2d[:,arry_no]

    #find the 2nd element of shape array which is column length
    len = np_2d.shape[1]
    print(len)
    a = 0

    #get the path of Downloads
    path_name = os.path.expanduser('~\Downloads')


    def plot_rest(a):
        var = 1
        while var ==1:
            #for each png figure create fig separetely
            fig = plt.figure()

            #a chages the column
            a=a+1
            #skip the plooting with its self
            if a==arry_no:
                continue
            #return when the a is equals to length of column
            if a==len:
                return 0
            z = np_2d[:,a]
            plt.scatter(dep_col,z)
            plt.xlabel(set_col)
            plt.ylabel(first_col[a])
            plt.title('plot '+str(a))
            xx = int_x
            yy = int_y
            plt.rcParams["figure.figsize"] = [xx,yy]
            plt.show()
            figure = set_col + ' vs ' + first_col[a]
            fig.savefig(path_name+'\\'+figure+'.png')
    #except 0 till end column will be plotted
    if arry_no==0:
        plot_rest(a)

    #from column 0 till end plot
    else:
        #plot graph for 0 column as it will be skipped in plot_rest function
        fig = plt.figure()
        q = np_2d[:,a]
        plt.scatter(dep_col,q)
        plt.xlabel(set_col)
        plt.ylabel(first_col[a])
        plt.title('plot '+str(a))
        #we get exact value
        xxx = int_x
        yyy = int_y
        plt.rcParams["figure.figsize"] = [xxx,yyy]
        plt.show()
        fig_0 = set_col + " vs " + first_col[a]
        fig.savefig(path_name+'\\'+fig_0+'.png')
    #for rest of the plotting call plot_rest
        plot_rest(a)
scatter(data)


    



        
    
    
    







# In[ ]:




# In[ ]:



