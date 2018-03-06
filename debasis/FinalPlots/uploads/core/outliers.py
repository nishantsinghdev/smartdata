import os.path

my_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
filepath = os.path.join(my_path, 'documents//Ecommerce.csv')

fpath = os.path.join(my_path, 'static/images/outliers')
import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

from pandas.tools.plotting import table

def outliers(filepath):
    newDF = pd.DataFrame()
    df = pd.read_csv(filepath)
    # get only the numeric values of dataframe
    pp = df._get_numeric_data()
    pp.fillna(0, inplace=True)
    first_col = list(pp)
    sha = pp.shape
    no_rows = sha[0]
    # calculating quantiles
    s = pp[first_col[0]].quantile([0.25, 0.5, 0.75])

    i = 1
    while (i < len(first_col)):
        s = s.append(pp[first_col[i]].quantile([0.25, 0.5, 0.75]))
        i = i + 1

    r = s.tolist()
    # done calc quantiles
    # variables int
    i = 0
    cols = []
    q = np.zeros(len(first_col))
    a = []
    b = []
    c = []
    d = []
    low = []
    high = []
    k = 0
    j = 0

    # putting quantiles in respective lists
    while (i < len(r)):
        if (i % 3 == 0):
            a.append(r[i])
        elif (i % 3 == 1):
            b.append(r[i])
        else:
            c.append(r[i])
        i = i + 1
    # end
    # calculating 1.5IQR
    while ((k * 3) < len(r)):
        d.append(1.5 * (c[k] - a[k]))
        k = k + 1
    # end

    # calc boundry values
    while ((j * 3) < len(r)):
        low.append(a[j] - d[j])
        high.append(b[j] + d[j])
        j = j + 1
    coun = 0
    # end calc boundry values
    # counting outliers
    while (coun < len(first_col)):
        for z in first_col:
            g = 0
            while (g <= (pp[z].size - 1)):
                if ((pp[z][g]) > high[coun] or (pp[z][g]) < low[coun]):
                    q[coun] = q[coun] + 1
                g = g + 1
            coun = coun + 1
            # end counting outliers
    # printing percentage and column name
    k = 0
    while (k < len(first_col)):
        q[k] = (q[k] / no_rows) * 100
        newDF = newDF.append({'col_name': first_col[k], '% outliers': str(q[k])}, ignore_index=True)
        k = k + 1
    ax = plt.subplot(111)

    table(ax, newDF, loc='center')

    ax.set_axis_off()
    plt.savefig(fpath + '\\' + 'outliers.png')
    #plt.savefig('outliers.png')
    # end printing
    # function end


#outliers(filepath)

