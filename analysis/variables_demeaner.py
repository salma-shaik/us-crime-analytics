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


def demean_vars(df, var_type):
    df_grpd = df.groupby('ORI').transform(lambda x: x - x.mean())
    df_grpd.to_csv(
        f'C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/analysis/ini_core_{var_type}_pos_demeaned.csv',
        index=False)

### Demean count vars
# ini_core_counts_pos_grpd = normalize_by_group(ini_core_counts_pos, 'ORI')

# demean_vars(pd.read_csv(
#         'C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/analysis/initial_core_counts_pos.csv'),
#         var_type='counts')

### Demean rate vars
# ini_core_counts_pos_grpd = normalize_by_group(ini_core_counts_pos, 'ORI')

demean_vars(pd.read_csv(
        'C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/analysis/initial_core_rates_pos.csv'),
        var_type='rates')
