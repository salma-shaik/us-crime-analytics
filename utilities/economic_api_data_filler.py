import pandas as pd

pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 1000)

econ_data = pd.read_csv('/Users/salma/Research/us-crime-analytics/data/econ_dec_90_15.csv')

'''
'ORI', 'AGENCY', 'CNTY' obtained from crime files since econ api data is merged right with crime data on state and
place fips to obtain these. So, under identity columns, only placename would have NaN values for the rows which don't
have economic data but had crime data
'''

#########
# So we need to fill placename with any of the non missing place values in the group
econ_data['placename'] = econ_data.groupby('ORI')['placename'].apply(lambda x: x.ffill().bfill())

#######
# Now to fill all NaNs in numeric columns in a particular group with respective means

num_cols = ['pci_total_pop', 'pci_white', 'pci_black', 'emp_total_male', 'emp_total_female', 'emp_total',
            'emp_total_male_white', 'emp_total_female_white', 'emp_total_male_black', 'emp_total_female_black',
            'pci_hisp', 'emp_total_male_hisp', 'emp_total_female_hisp']

econ_data[[x for x in num_cols]] = econ_data.groupby('ORI', as_index=False)[num_cols]\
                                                                      .transform(lambda x: x.fillna(x.mean()))

econ_data.to_csv('/Users/salma/Research/us-crime-analytics/data/econ_dec_90_15_missing_filled.csv', index=False)