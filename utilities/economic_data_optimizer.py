import pandas as pd

bea_census = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/economic/bea_census_all_1990_2015.csv')

"""
    Obtaining the subset of columns from whitemale_count to percap_income to append county at the end of the corresponding column name
    If we don't want to rely on indexes to subset columns like this, then the other way would be to rename each column explicitly
"""
bea_census_std = bea_census[['geoname', 'year', 'fips_state', 'fips_county', 'stco_fips','county_short', 'county_pop_final']]
bea_census_count = bea_census[bea_census.columns[5:31]]

bea_census_count_col_updated = bea_census_count.rename(columns=lambda x: x+'_county')

"""
Add the updated column names back to the original bea df
"""
bea_census_updated = pd.concat([bea_census_std, bea_census_count_col_updated], axis=1)

bea_census_updated.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/economic/bea_census_all_1990_2015_cols_updated_county_suffix.csv', index=False)

# bea_census.drop_duplicates(subset=['stco_fips'], inplace=True)
#
# print(bea_census.shape[0]) #3118