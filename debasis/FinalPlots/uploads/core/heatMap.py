
import os.path
my_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..'))
filepath = os.path.join(my_path, 'documents/Leads.csv')
fpath = os.path.join(my_path, 'static/images/hitmap')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



def heat_map(filepath):
    sep=','
    df = pd.read_csv(filepath,sep,index_col=False)


    #get only the numeric values of dataframe
    pp=df._get_numeric_data()
    cor=pp.corr()
    plt.figure(figsize = (10,10))
    sns_img=sns.heatmap(cor,linewidths=0.10)
    #plt.show()
    s=sns_img.get_figure()
    f=0
    s.savefig(fpath + '\\' + 'hitmap' + str(f) + '.png')
#heat_map(filepath)