import pandas as pd

pd.set_option('display.max_columns', 100)
pd.set_option('display.max_colwidth', 500)
pd.set_option('display.width', 5000)
pd.set_option('display.max_rows', 100)


'''
['ORI', 'AGENCY', 'YEAR', 'POP100', 'White_count', 'Black_count', 'Hispanic_count', 'Pct_WYM', 'Pct_WYF', 'total_count_county', 
'population', 'murder', 'rape', 'robbery', 'aggravated_assault', 'simple_assault', 'burglary', 'larceny', 'auto_theft', 
'total_main_crime', 'violent_crime', 'property_crime', 'murder_tot_arrests', 'murder_tot_black', 'murder_tot_white', 
'rape_tot_arrests', 'rape_tot_black', 'rape_tot_white', 'robbery_tot_arrests', 'robbery_tot_black', 'robbery_tot_white', 
'agg_assault_tot_arrests', 'agg_assault_tot_white', 'agg_assault_tot_black', 'larceny_theft_arrests_tot', 'larceny_theft_arrests_black', 
'larceny_theft_arrests_white', 'burglary_tot_arrests', 'burglary_tot_black', 'burglary_tot_white', 'mtr_veh_theft_tot_arrests', 
'mtr_veh_theft_tot_black', 'mtr_veh_theft_tot_white', 'violent_arrests', 'property_arrests', 'total_main_arrests', 
'sale_drug_total_tot_arrests', 'sale_drug_total_tot_black', 'sale_drug_total_tot_white', 'drug_total_arrests', 
'drug_arrests_black', 'drug_arrests_white', 'poss_drug_total_tot_arrests', 'poss_drug_total_tot_black', 'poss_drug_total_tot_white', 
'disorder_arrests_tot_index', 'disorder_arrests_black_index', 'disorder_arrests_white_index', 'total_officers', 'prison_occupancy_count', 
'jail_occupancy_count', 'pci_white', 'pci_black', 'emp_total', 'emp_total_white', 'emp_total_black']
'''


def drop_numerical_outliers_iqr(df, var):

    # z-score
    var_out_z = df[((df[f'{var}'] - df[f'{var}'].mean()) / df[f'{var}'].std()).abs() > 3]

    var_out_z.to_csv(f'/Users/salma/Research/us-crime-analytics/data/analysis/outliers/{var}_z_out.csv',
                                            index=False)
    # iqr
    Q1 = df[f'{var}'].quantile(0.25)
    Q3 = df[f'{var}'].quantile(0.75)
    IQR = Q3 - Q1

    var_out_iqr = df[(df[f'{var}'] > 1.5 * IQR) | (df[f'{var}'] < -1.5 * IQR)]

    var_out_iqr.to_csv(
        f'/Users/salma/Research/us-crime-analytics/data/analysis/outliers/{var}_iqr_out.csv',
        index=False)


ini_core_counts_pos = pd.read_csv('/Users/salma/Research/us-crime-analytics/data/analysis/initial_core_counts_pos.csv')

num_cols = list(ini_core_counts_pos)[3:]

for col in num_cols:
    drop_numerical_outliers_iqr(ini_core_counts_pos, col)