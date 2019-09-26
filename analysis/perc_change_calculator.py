import pandas as pd
import numpy as np


def calc_perc_change(df, var_type):
    #df_grpd = df.groupby('ORI').apply(lambda x: x/)
    # lets sort the df by ori and year so that each ori has data starting from 90-15 not from 15-90
    # df.sort_values(['ORI', 'YEAR'], ascending=[True, True], inplace=True)
    # print(df.head())

   # df = 100 * (1 - df.iloc[0]/df)
    df_grpd = df.groupby('ORI')
    df_grpd_pct = df_grpd._get_numeric_data().apply(lambda x: x.div(x.iloc[0]).subtract(1).mul(100))

    print(df_grpd_pct.head())
    # row.POP100 + (5 * (row.POP100 - cen_90_00_10.iloc[row.Index - 1].POP100) / 10
    #
    # df.groupby('ORI').apply(lambda x: x.div(x.iloc[0]).subtract(1).mul(100))

    # If already ordered by year in each possible grouping

# def pct_change(df):
#     return df._get_numeric_data().apply(axis=0, x.div(x.iloc[0]).subtract(1).mul(100))

ini_df = pd.read_csv('C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/analysis/initial_core_counts_pos.csv')
ini_df_grpd = ini_df.groupby('ORI')
calc_perc_change(ini_df, var_type='counts')

