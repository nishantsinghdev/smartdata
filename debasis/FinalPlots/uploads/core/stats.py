import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.tools.plotting import table
import os.path
my_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..'))
data = os.path.join(my_path, 'documents/Ecommerce.csv')
fpath = os.path.join(my_path, 'static/images/statistics')

def stats(data):
    df = pd.read_csv(data)
    #get only the numeric values of dataframe
    pp=df._get_numeric_data()


    pp2=pp.describe()
    #pp2.to_csv("new.csv")
    ax = plt.subplot(111)

    table(ax, pp2, loc='center')

    ax.set_axis_off()

    f=0
    plt.savefig(fpath + '\\' + 'stat' + str(f) + '.png')

#stats(data)