import pandas as pd

# Read the 1990 econ crime merged file
econ_90 = pd.read_csv('C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/economic/new_eco_cen/merged_with_crime/economic_data_1990_crime_merged.csv')
# add YEAR column with value 1990
econ_90['YEAR'] = 1990

# Read the 1990 econ crime merged file
econ_00 = pd.read_csv('C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/economic/new_eco_cen/merged_with_crime/economic_data_2000_crime_merged.csv')
# add YEAR column with value 2000
econ_00['YEAR'] = 2000

# Read the 1990 econ crime merged file
econ_10 = pd.read_csv('C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/economic/new_eco_cen/merged_with_crime/economic_data_2010_crime_merged.csv')
# add YEAR column with value 2010
econ_10['YEAR'] = 2010

# Read the 1990 econ crime merged file
econ_15 = pd.read_csv('C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/economic/new_eco_cen/merged_with_crime/economic_data_2015_crime_merged.csv')
# add YEAR column with value 2015
econ_15['YEAR'] = 2015

econ_dec_acs = pd.concat([econ_90, econ_00, econ_10, econ_15 ], sort=False, ignore_index=True)

econ_dec_acs.sort_values(by=['ORI', 'YEAR'], ascending=[True, False], inplace=True)

# ############## Check this out
# Reset index after sorting so that it is in ascending order again and not trying to maintain the original index
econ_dec_acs = econ_dec_acs.reset_index(drop=True)

# replace any  negative value with zero
# Accessing the private _get_numeric_data() of the dataframe. Private method, so changes reflected in the original df
num = econ_dec_acs._get_numeric_data()
num[num < 0] = 0
econ_dec_acs.to_csv('C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/economic/new_eco_cen/econ_dec_90_15.csv', index=False)

