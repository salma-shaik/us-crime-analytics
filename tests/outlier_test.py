from scipy import stats
import numpy as np
import pandas as pd

from numpy.random import seed
from numpy.random import randn
from numpy import mean
from numpy import std

# seed the random number generator
seed(1)

# generate univariate observations
test_df = pd.DataFrame({'a': [10,12,12,13,12,11,14,13,15,10,10,10,100,12,14],
                        'b': [12,10,10,11,12,15,12,13,12,11,14,150,13,10,15]})

# summarize
# print('mean: ', test_df.mean(),'\n', 'std: ', test_df.std())

def drop_numerical_outliers(df, z_thresh=3):
    # Constrains will contain `True` or `False` depending on if it is a value below the threshold.
    # non_outliers = df.select_dtypes(include=[np.number]).apply(lambda x: np.abs(stats.zscore(x)) < z_thresh,
    #                                                            result_type='reduce').all(axis=1)
    # # Drop (inplace) values set to be rejected
    # df.drop(df.index[~non_outliers], inplace=True)
    # return df

    outliers = df.select_dtypes(include=[np.number]).apply(lambda x: np.abs(stats.zscore(x)) > z_thresh, result_type='reduce').any(axis=1)
    #df.drop(df.index[outliers], inplace=True)

    return df.loc[df.index[outliers]]


non_outlier_test_df = drop_numerical_outliers(test_df)

print(non_outlier_test_df)