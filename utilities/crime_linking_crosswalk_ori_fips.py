import pandas as pd


"""
 1. Merge Crime Nat 1960-15 file with crosswalk improved 2006 file by ORI. 
    Get CGOVTYPE, fips codes, st, cnty, pl from crosswalk file for all the matching entries
"""


def merge_crime_crswlk(crswlk_fl, crime_fl):
    # Read the linking crosswalk file
    crswlk_major = pd.read_csv(crswlk_fl)

    # Get only the required columns from crosswalk_major_agencies df
    crswlk_major_reqd_vars = crswlk_major[['ORI', 'CGOVTYPE', 'fips_place', 'fips_state', 'fips_county']]
    crswlk_major_reqd_vars.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/cleaned_files/crosswalk/crosswalk_major_agencies_req_vars.csv', index=False)

    # Read Crime_National_UCR_offenses_1990_2015_Req_Vars_Unique.csv file
    crime_unique = pd.read_csv(crime_fl)

    # crime file = ori_code; crswlk_file = ORI
    crime_unique_crswlk_major_merged = crime_unique.merge(crswlk_major_reqd_vars, left_on='ori_code', right_on='ORI')

    # drop ORI corresponding to crosswalk coz both ori_code and ORI columns are retained after the merge but we only want ori from crime file
    crime_unique_crswlk_major_merged.drop(['ORI'], axis=1, inplace=True)

    # Rearrange columns such that ORI, CGOVTYPE, fips_place, fips_county, fips_state are at the beginning
    cols = list(crime_unique_crswlk_major_merged.columns.values)
    cols.pop(cols.index('ori_code'))
    cols.pop(cols.index('agency_name'))
    cols.pop(cols.index('CGOVTYPE'))
    cols.pop(cols.index('fips_place'))
    cols.pop(cols.index('fips_county'))
    cols.pop(cols.index('fips_state'))

    merged_crime_file_cgovtype_df_arranged = crime_unique_crswlk_major_merged[
        ['ori_code', 'agency_name', 'CGOVTYPE', 'fips_place', 'fips_county', 'fips_state'] + cols]

    # Rename 'CGOVTYPE', 'fips_place', 'fips_county', 'fips_state' columns to match the names in census files.
    # Also year to crime_year to differentiate from census year. ###### Address later when merging crime and census together. ######
    merged_crime_file_cgovtype_df_arranged = merged_crime_file_cgovtype_df_arranged.rename(
        {'ori_code':'ORI','CGOVTYPE': 'Govt_level', 'fips_place': 'place_fips', 'fips_state': 'STATEFP', 'fips_county': 'CNTY',
         'year': 'crime_year', 'agency_name': 'AGENCY'}, axis='columns')

    merged_crime_file_cgovtype_df_arranged = merged_crime_file_cgovtype_df_arranged.sort_values(by=['ORI'])

    # Reset index after sorting so that it is in ascending order again and not trying to maintain the original index
    merged_crime_file_cgovtype_df_arranged = merged_crime_file_cgovtype_df_arranged.reset_index(drop=True)
    print('merged_crime_file_cgovtype_df_arranged ', merged_crime_file_cgovtype_df_arranged.shape[0])

    merged_crime_file_cgovtype_df_arranged.to_csv(
        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/crime_data/Crime_Crswlk_Major_Merged_Inner.csv',
        index=False)


merge_crime_crswlk(crswlk_fl='/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/cleaned_files/crosswalk/crosswalk_major_agencies.csv', crime_fl='/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/cleaned_files/crime/Crime_1990_2015_Req_Vars.csv')

#major_agencies = merge_crime_crswlk(crswlk_fl='/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/cleaned_files/crosswalk/crosswalk_major_agencies.csv', crime_fl='/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/cleaned_files/crime/Crime_1990_2015_Req_Vars.csv')
# Obtain only those records from the initial crime file whose ORIs are present in this list of major agencies.

# ini_crime_df = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/cleaned_files/crime/Crime_1990_2015_Req_Vars.csv')
# crime_major_rec = ini_crime_df[ini_crime_df.ori_code.isin(major_agencies['ORI'])]
# crime_major_rec.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/crime_data/crime_major_agencies_records.csv', index=False)

