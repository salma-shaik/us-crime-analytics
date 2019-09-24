import pandas as pd
import numpy as np


# Using pure vectorized Pandas/Numpy calls
def normalize_by_group(df, by):
    groups = df.groupby(by)
    # computes group-wise mean/std,
    # then auto broadcasts to size of group chunk
    mean = groups.transform(np.mean)
    std = groups.transform(np.std)
    return (df[mean.columns] - mean) / std

ini_core_counts_pos = pd.read_csv('/Users/salma/Research/us-crime-analytics/data/analysis/initial_core_counts_pos.csv')

#ini_core_counts_pos_grpd = normalize_by_group(ini_core_counts_pos, 'ORI')

## elegant but very slow; not good performance
ini_core_counts_pos_grpd = ini_core_counts_pos.groupby('ORI').transform(lambda x: x - x.mean())

ini_core_counts_pos_grpd.to_csv('/Users/salma/Research/us-crime-analytics/data/analysis/ini_core_counts_pos_demeaned.csv',
                                index=False)