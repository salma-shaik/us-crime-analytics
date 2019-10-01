from scipy import stats
import numpy as np
import pandas as pd

from numpy.random import seed
from numpy.random import randn
from numpy import mean
from numpy import std

pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 5000)
# seed the random number generator
seed(1)

# generate univariate observations
test_df = pd.DataFrame({'a': [10,12,12,13,12,11,14,13,15,10,10,10,100,12,14],
                        'b': [12,10,10,11,12,15,12,13,12,11,14,150,13,10,15]})

# summarize
# print('mean: ', test_df.mean(),'\n', 'std: ', test_df.std())


def get_outliers(df, z_thresh=3):
    df_num = df.loc[:, 'POP100':]

    # 3 z
    # df_num_out_repl = df_num.mask(df_num.sub(df_num.mean()).div(df_num.std()).abs().gt(3)) --> worked
    #df_num_out_repl = df.mask(df_num.sub(df_num.mean()).div(df_num.std()).abs().gt(3))

    # if we don't take only numeric, then NaNs on char cells
    df_num_out_repl = df.where(((df_num - df_num.mean()) / df_num.std()).abs() < 3, np.nan)

    # 2 z

    print(df_num_out_repl.head())

    # df_num_out_repl_merged = df.loc[:, :'Govt_level'].merge(df_num_out_repl, left_index=True, right_index=True)
    #
    # return df_num_out_repl_merged


df = pd.read_csv('/Users/salma/Research/us-crime-analytics/data/pre_analysis/initial_core_counts_pop_1000_neg_rplcd.csv')
outlier_test_df = get_outliers(df)

#outlier_test_df.to_csv('/Users/salma/Research/us-crime-analytics/data/tests/outlier_test_df_3z1.csv', index=False)










#
# print(outlier_test_df.shape[0])


# df_num_out_repl = df_num.mask(df_num.sub(df_num.mean()).div(df_num.std()).abs().gt(2))

# df_num_out_repl = df_num.mask(df_num.sub(df_num.mean()).div(df_num.std()).abs().gt(3))
#
# # mask() is the inverse boolean operation of where.
# df.mask(df.sub(df.mean()).div(df.std()).abs().gt(2))
#
# df_num_out_repl = df_num.mask(df_num.sub(df_num.mean()).div(df_num.std()).abs().gt(2))
#
# # mod_df_out_repl_merged = df.loc[:, :'Govt_level'].merge(df_num_out_repl, left_index=True, right_index=True)
# # print(mod_df_out_repl_merged.head())

# df_num_out_repl = df_num.where(((df_num - df_num.mean())/df_num.std()).abs() < 3, np.nan)

'''
df_num_out_repl = df.mask(df.sub(df.mean()).div(df.std()).abs().gt(3))
print(df_num_out_repl)
return df_num_out_repl
'''
# return df.loc[df.index[outliers]]