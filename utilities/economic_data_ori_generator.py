import pandas as pd
import os
from utilities import df_cleaner

# Get the required crime df with info of major agencies
crime_major_gov_fips = pd.read_csv(
    'C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/crime/Crime_Major_Gov_Fips.csv')

# Dropping Govt_level coz it's already present in the merged census files so don't need in economic files again
crime_df = crime_major_gov_fips.drop(['Govt_level'], axis=1)


# Merge each of the economic files with the crime df on state and place fips to get the ori and agency names.
# Later, the new econ data wil be merged with rest of the data based on ori
def merge_econ_crime(econ_df, cr_df, fl_name):
    # drop CNTY col since we will get it from the crime file
    econ_df.drop(['CNTY'], axis=1, inplace=True)
    # Merging right on crime so that we retain all the ORIs from crime file.
    # This way can know which major agencies are missing econ data

    econ_df.drop_duplicates(['STATEFP', 'place_fips'], inplace=True)

    econ_df_merged = econ_df.merge(cr_df, on=['STATEFP', 'place_fips'], how='right')

    econ_df_merged.sort_values(['STATEFP', 'CNTY', 'place_fips'],  inplace=True)


    econ_df_merged_arngd = df_cleaner.rearrange_cols(econ_df_merged, ['ORI', 'AGENCY', 'placename', 'STATEFP', 'CNTY', 'place_fips'])

    econ_df_merged_arngd.to_csv(
        f'C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/economic/new_eco_cen/merged_with_crime/{fl_name}_crime_merged.csv',
        index=False)


# change into new_vars dir so that can loop through all the years' files and merge each one with crime
new_vars_dir_path = 'C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/economic/new_eco_cen/new_vars'
os.chdir(new_vars_dir_path)

# loop through each year econ file
for fl in os.listdir():
    if fl != '.DS_Store':
        fl_path = new_vars_dir_path + '/' + fl
        merge_econ_crime(
            pd.read_csv(fl_path), crime_df, fl.split('.')[0])
