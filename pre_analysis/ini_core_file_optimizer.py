import pandas as pd
import os
import numpy as np

pd.set_option('display.max_columns', 100)


# drop places with less than 1000 population
def drop_pop_1000(fl_path):
    file_name = os.path.basename(fl_path).split('.')[0]

    df = pd.read_csv(fl_path)

    df = df.query('POP100 >= 1000')

    df.to_csv(f'/Users/salma/Research/us-crime-analytics/data/pre_analysis/{file_name}_pop_1000.csv', index=False)
    return df


# replace negatives with blanks
def replace_neg_with_blanks(fl_path):
    file_name = os.path.basename(fl_path).split('.')[0]

    df = pd.read_csv(fl_path)

    df_non_neg = df.where(df > 0, np.nan)

    df_non_neg.to_csv(f'/Users/salma/Research/us-crime-analytics/data/pre_analysis/{file_name}_neg_rplcd.csv', index=False)


###### for initial_core file ######
# drop places with less than 1000 population from initial core file
drop_pop_1000('/Users/salma/Research/us-crime-analytics/data/pre_analysis/initial_core.csv')

# replace negatives in initial_core_pop_1000.csv file with blanks/nans
replace_neg_with_blanks('/Users/salma/Research/us-crime-analytics/data/pre_analysis/initial_core_pop_1000.csv')


###### for initial_core_counts file ######
# drop places with less than 1000 population from initial core file
drop_pop_1000('/Users/salma/Research/us-crime-analytics/data/pre_analysis/initial_core_counts.csv')

# replace negatives in initial_core_pop_1000.csv file with blanks/nans
replace_neg_with_blanks('/Users/salma/Research/us-crime-analytics/data/pre_analysis/initial_core_counts_pop_1000.csv')


###### for initial_core_rates file ######
# drop places with less than 1000 population from initial core file
drop_pop_1000('/Users/salma/Research/us-crime-analytics/data/pre_analysis/initial_core_rates.csv')

# replace negatives in initial_core_pop_1000.csv file with blanks/nans
replace_neg_with_blanks('/Users/salma/Research/us-crime-analytics/data/pre_analysis/initial_core_rates_pop_1000.csv')