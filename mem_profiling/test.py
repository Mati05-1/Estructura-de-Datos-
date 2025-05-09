'''
Mem profiling test.
'''


from memory_profiler import profile
from copy import deepcopy
import pandas as pd


@profile
def memtest():

    # df = pd.read_csv('test_csv.csv')
    # print(df.shape)

    # df_2 = df
    # print(df_2)

    # df_3 = deepcopy(df)
    # print(df_3)

    # df_3['Column_11'] = df_3['Column_1'] + df_3['Column_2']
    # df_3['Column_11'] = df_3['Column_11'][5:]

    # df_4 = df.drop((['Column_1', 'Column_2']), axis=1, inplace=True)
    # print(df_4.shape)

    arr = [1, 0] * 100000
    arr_2 = arr
    arr_3 = deepcopy(arr)
    arr_4 = deepcopy(arr_3)

memtest()
