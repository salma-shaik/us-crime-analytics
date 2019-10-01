import pandas as pd
import os

pd.set_option('display.max_columns', 100)
pd.set_option('display.max_colwidth', 500)
pd.set_option('display.width', 5000)
pd.set_option('display.max_rows', 100)


def calc_perc_change(fl_path):
    file_name = os.path.basename(fl_path).split('.')[0]

    df = pd.read_csv(fl_path)
    # lets sort the df by ori and year so that each ori has data starting from 90-15 not from 15-90
    df.sort_values(['ORI', 'YEAR'], ascending=[True, True], inplace=True)

   # ((x-x[0])/x[0]) * 100
    df_grpd_pct = df.groupby('ORI').transform(lambda x: x.div(x.iloc[0]).subtract(1).mul(100))

    # drop YEAR and Govt_level col so that it isn't demeaned.
    df_grpd_pct.drop(['YEAR', 'Govt_level'], inplace=True, axis=1)

    # append _dm to the demeaned columns
    df_grpd_pct.columns = ['pc_' + str(col) for col in df_grpd_pct.columns]

    # get id columns from original df
    df_id = df.loc[:, ['ORI', 'AGENCY', 'YEAR', 'Govt_level', 'POP100']]

    df_pc = pd.concat([df_id, df_grpd_pct], axis=1)

    df_pc.to_csv(f'C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/pre-analysis/{file_name}_pc.csv', index=False)


    # row.POP100 + (5 * (row.POP100 - cen_90_00_10.iloc[row.Index - 1].POP100) / 10
    #
    # df.groupby('ORI').apply(lambda x: x.div(x.iloc[0]).subtract(1).mul(100))

    # If already ordered by year in each possible grouping

# def pct_change(df):
#     return df._get_numeric_data().apply(axis=0, x.div(x.iloc[0]).subtract(1).mul(100))

# pc for counts
#calc_perc_change('/Users/salma/Research/us-crime-analytics/data/pre_analysis/outliers/initial_core_counts_pop_1000_neg_rplcd_out_repl.csv')


# pc for rates
calc_perc_change('C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/pre-analysis/outliers/initial_core_rates_pop_1000_neg_rplcd_incrc_cnts_rates_out_repl.csv')
