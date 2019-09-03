import pandas as pd
from datetime import datetime

pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 5000)

from utilities import fixed_columns_replicator as fcr
from utilities import year_replicator as yr

# replicate fixed columns into required number of times depending on year
# 2015 - 5; 2010, 2000 - 10; 1990 - 1

# fcr.replicate_fixed_cols(df= pd.read_csv('/Users/salma/Research/us-crime-analytics/data/econ_dec_90_15_missing_filled.csv'),
#                          cols_list=['ORI', 'AGENCY', 'placename', 'STATEFP', 'CNTY', 'YEAR'],
#                          op_fl_path='/Users/salma/Research/us-crime-analytics/data',
#                          dt_type='Economic')


# replicate year set from 90-15 unique ORI number of times
# yr.genereate_years_90_15(df = pd.read_csv(
#                                 '/Users/salma/Research/us-crime-analytics/data/Economic_Fixed_Cols_Replicated.csv'),
#                          repl_times = 14542,
#                          dt_type = 'Economic',
#                          op_fl_path='/Users/salma/Research/us-crime-analytics/data')


print("########## Start: ", datetime.now().time())

econ_data = pd.read_csv('/Users/salma/Research/us-crime-analytics/data/econ_dec_90_15_missing_filled.csv')

##### trying resampling method to get yearly frequency for every ORI
# since each ORI has data for 90, 00, 10, 15 redsampling considers all the years in between as missing and gives value NaNs
# let's first convert year column to april 1 year i.e in the format 4/1/2010 etc.. whose dtype would be objec t

econ_data.loc[:, 'YEAR'] = econ_data['YEAR'].apply(lambda x: '4/1/' + str(x))

# Next convert this date string to datetime format
econ_data.loc[:, 'cen_dt_yr'] = pd.to_datetime(econ_data['YEAR'])

#print(econ_data['cen_dt_yr'])
# set the datetime as index
econ_data.index = econ_data['cen_dt_yr']


# print(econ_data.head())
# Since we want to interpolate for each ORI separately, we need to group our data by ‘ORI’ before we can use the
# resample() function with the option ‘A’ to resample the data to an annual/yearly frequency.

econ_data = econ_data.groupby('ORI').resample('A').mean().reset_index()

econ_data_int = econ_data.interpolate()

# econ_data = econ_data.resample('A').mean().head(4)

# df = df.interpolate(method='time')

print("########## End: ", datetime.now().time())


econ_data_int.to_csv('/Users/salma/Research/us-crime-analytics/data/econ_int_groupby.csv', index=False)