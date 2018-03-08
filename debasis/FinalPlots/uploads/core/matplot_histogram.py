import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import platform
from matplotlib.backends.backend_pdf import PdfPages

my_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

data = os.path.join(my_path + '\documents\Ecommerce_Purchases.csv')




def histo(data):
    sep = ','
    header = 'None'
    df = pd.read_csv(data, header, sep)
    datatype = df.dtypes

    # get only the numeric values of dataframe
    pp = df._get_numeric_data()

    # convert the pp to 2d array
    df1 = pp.values

    # get the first columns array
    first_col = list(pp)
    print(first_col)
    np_2d = np.array(df1)
    # get the number of rows in a file
    n = np_2d.shape[0]

    path_name = os.path.expanduser('~\Downloads')
    # press shift + tab for backing all selected by 1 tab and press tab only for selected things to move forward

    a = 1
    with PdfPages('histogram2.pdf') as pdf:
        for num in first_col:
            fig = plt.figure()
            bins = round(2 * n ** (1 / 3))
            print(bins)
            plt.hist(pp[num], bins, label=num)
            plt.xlabel('bins ' + str(a))
            plt.ylabel(num)
            plt.legend()
            plt.show()
            a = a + 1
            # fig.savefig(path_name+'\\'+num+'.png')
            pdf.savefig(fig)


#histo(data)