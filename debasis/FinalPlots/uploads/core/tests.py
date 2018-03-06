import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import collections
import math
# import tabulate
# from tabulate import tabulate
import os.path

my_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
data = os.path.join(my_path, 'documents/Ecommerce_Purchases.csv')

#data = input('enter the data path ')  # 'C:\Users\vidya bs\Desktop\Ecommerce Purchases.csv'


def miss(data):
    sep = ','
    header = None
    df = pd.read_csv(data, header, sep)
    first_col = list(df)
    datatype = df.dtypes
    np_2d = np.array(df)

    # to find length of row

    f = df.shape[0]
    # to find percentage
    ff = 100 / f

    # get position of empty cells in file
    position = np.nonzero(pd.isnull(np_2d))
    print(position)
    # position 1 indiscates in column finding unique val
    pos1 = position[1]
    a = np.unique(pos1)
    # print(a)
    emt_ary = []

    # get the names of columns dat have missinng values
    for ele in a:
        emt_ary.append(first_col[ele])
    # m=([len(path) for path in emt_ary])
    # l=max(m)
    l = 0
    print(emt_ary)
    l = max(len(path) for path in emt_ary)
    print(l)

    # y contains value with repetition
    y = collections.Counter(pos1)

    # to get prcentage of missing values in column
    b_ary = []
    i = 0
    for key in y:
        y[key] *= ff
    b_ary = list(y.values())
    # print(b_ary)
    # to get tabular form
    print('name' + ' ' * l + 'percentage')

    value_pos = []
    for each in emt_ary:
        value_pos = l + 1 - len(each)
        print(each + '    ' * value_pos + str(b_ary[i]))
        i = i + 1


miss(data)