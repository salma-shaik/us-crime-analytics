import pandas as pd
import os


def demean_vars(fl_path):
    file_name = os.path.basename(fl_path).split('.')[0]
    df = pd.read_csv(fl_path)

    # don't need to .reset_index() since we wan't the 0 based index obtained as part of the grouping & broadcasting operation
    df_grpd = df.groupby('ORI').transform(lambda x: x - x.mean())

    # drop YEAR and Govt_level col so that it isn't demeaned.
    df_grpd.drop(['YEAR', 'Govt_level'], inplace=True, axis=1)

    # append _dm to the demeaned columns
    df_grpd.columns = ['dm_' + str(col) for col in df_grpd.columns]

    # get id columns from original df
    df_id = df.loc[:, ['ORI', 'AGENCY', 'YEAR', 'Govt_level', 'POP100']]

    df_demeaned = pd.concat([df_id, df_grpd], axis=1)

    df_demeaned.to_csv(f'C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/pre-analysis/{file_name}_dm.csv', index=False)


# demean num vars for counts file
# demean_vars('/Users/salma/Research/us-crime-analytics/data/pre_analysis/outliers/initial_core_counts_pop_1000_neg_rplcd_out_repl.csv')

# demean num vars for rates file
demean_vars('C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/pre-analysis/outliers/initial_core_rates_pop_1000_neg_rplcd_incrc_cnts_rates_out_repl.csv')
