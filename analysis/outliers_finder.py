import pandas as pd
import numpy as np

pd.set_option('display.max_columns', 100)
pd.set_option('display.max_colwidth', 500)
pd.set_option('display.width', 5000)
pd.set_option('display.max_rows', 100)


'''
Outliers for all the below variables
COUNTS:
['POP100', 'White_count', 'Black_count', 'Hispanic_count', 'Pct_WYM', 'Pct_WYF', 'total_count_county', 
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


RATES:
['murder_rate', 'rape_rate', 'robbery_rate', 'aggravated_assault_rate', 'simple_assault_rate', 'burglary_rate', 
'larceny_rate', 'auto_theft_rate', 'total_main_crime_rate', 'violent_crime_rate', 'property_crime_rate', 
'murder_tot_arrests_rate', 'murder_tot_black_rate', 'murder_tot_white_rate', 'rape_tot_arrests_rate', 
'rape_tot_black_rate', 'rape_tot_white_rate', 'robbery_tot_arrests_rate', 'robbery_tot_black_rate', 
'robbery_tot_white_rate', 'agg_assault_tot_arrests_rate', 'agg_assault_tot_white_rate', 'agg_assault_tot_black_rate', 
'larceny_theft_arrests_tot_rate', 'larceny_theft_arrests_black_rate', 'larceny_theft_arrests_white_rate', 
'burglary_tot_arrests_rate', 'burglary_tot_black_rate', 'burglary_tot_white_rate', 'mtr_veh_theft_tot_arrests_rate', 
'mtr_veh_theft_tot_black_rate', 'mtr_veh_theft_tot_white_rate', 'violent_arrests_rates', 'property_arrests_rates', 
'total_main_arrests_rates', 'sale_drug_total_tot_arrests_rate', 'sale_drug_total_tot_black_rate', 'sale_drug_total_tot_white_rate', 
'drug_total_arrests_rate', 'drug_arrests_black_rate', 'drug_arrests_white_rate', 'poss_drug_total_tot_arrests_rate', 
'poss_drug_total_tot_black_rate', 'poss_drug_total_tot_white_rate', 'disorder_arrests_tot_index_rate', 
'disorder_arrests_black_index_rate', 'disorder_arrests_white_index_rate', 'total_officers_rate', 'prison_occupancy_count', 
'jail_occupancy_count', 'pci_white', 'pci_black', 'emp_total', 'emp_total_white', 'emp_total_black']

'''


def drop_outliers_z_iqr_based(df, var, var_type):
    # z-score
    var_out_z = df[((df[f'{var}'] - df[f'{var}'].mean()) / df[f'{var}'].std()).abs() > 2]

    var_out_z.to_csv(f'C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/analysis/outliers/{var_type}/{var}_2z_out.csv',
                                            index=False)
    # iqr
    Q1 = df[f'{var}'].quantile(0.25)
    Q3 = df[f'{var}'].quantile(0.75)
    IQR = Q3 - Q1

    var_out_iqr = df[(df[f'{var}'] > 1.5 * IQR) | (df[f'{var}'] < -1.5 * IQR)]

    var_out_iqr.to_csv(
        f'C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/analysis/outliers/{var_type}/{var}_iqr_out.csv',
        index=False)


#### remove outliers from counts file
# ini_core_df = pd.read_csv('C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/analysis/initial_core_counts_pos.csv')
# num_cols = list(ini_core_df)[3:]


#### remove outliers from rates file
ini_core_df = pd.read_csv('C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/analysis/initial_core_rates_pos.csv')

# taking columns only from murder_rate
num_cols = list(ini_core_df)[11:]

for col in num_cols:
    # drop_outliers_z_iqr_based(df=ini_core_df, var=col, var_type='counts')
    drop_outliers_z_iqr_based(df=ini_core_df, var=col, var_type='rates')

# def drop_outliers_median_based(df, var_type='counts'):
#     # filt_df = filt_df.apply(lambda x: x[(x > quant_df.loc[low, x.name]) &
#     #                                     (x < quant_df.loc[high, x.name])], axis=0)
#     #
#     # filt_df.dropna(how='all', inplace=True)
#
#     outliers = df.select_dtypes(include=[np.number]).apply(lambda x: x > (3*np.median(x)))
#     print(outliers.head())
#
# drop_outliers_median_based(df=pd.read_csv('C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/analysis/initial_core_counts_pos.csv'),
#                            var_type='counts')
