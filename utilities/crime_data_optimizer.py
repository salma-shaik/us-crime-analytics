import pandas as pd

# Default=warn (about working with a copy). To disable SettingWithCopyWarning
pd.options.mode.chained_assignment = None

"""
        1. Get the data only from 1990.
"""
def get_req_crime_data_from1990(file_path):

     # Had to use encoding = "ISO-8859-1" to handle the below encoding error
     # UnicodeDecodeError: 'utf-8' codec can't decode byte 0x9f in position 14: invalid start byte

    ini_crime_df = pd.read_csv(file_path, encoding = "ISO-8859-1")

    ini_crime_df_from1990 = ini_crime_df[ini_crime_df.year >= 1990]
    # Write the crime data from 1990 to a csv.
    ini_crime_df_from1990.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/cleaned_files/crime/Crime_1990_2015.csv', index=False)

    crime_req_vars_df = ini_crime_df_from1990[['state',
                                                'ori_code',
                                                'group_number',
                                                'division',
                                                'year',
                                                'city_number',
                                                'months_reported',
                                                'agency_name',
                                                'agency_state',
                                                'zip_code',
                                                'murder',
                                                'manslaughter',
                                                'rape',
                                                'robbery',
                                                'gun_robbery',
                                                'knife_robbery',
                                                'aggravated_assault',
                                                'gun_assault',
                                                'knife_assault',
                                                'simple_assault',
                                                'burglary',
                                                'larceny',
                                                'auto_theft',
                                                'officers_assaulted',
                                                'officers_killed_by_felony',
                                                'officers_killed_by_accident',
                                                'sub_group']]

    # Create population column by summing up population_1, population_2 and population_3 columns
    crime_req_vars_df['population'] = ini_crime_df_from1990[['population_1', 'population_2', 'population_3']].sum(axis=1)

    # Remove the 0  alabama  ALAST00  ...       NaN        0.0 entry coz population is zero - CHECK
    crime_df = crime_req_vars_df[1:]
    #  Write this df with required variables to a csv.
    crime_df.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/cleaned_files/crime/Crime_1990_2015_Req_Vars.csv', index=False)

    # Drop the duplicate ORIs
    crime_df_uniq_ori = crime_df.drop_duplicates(subset=['ori_code'])
    crime_df_uniq_ori.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/cleaned_files/crime/Crime_1990_2015_Req_Vars_Unique.csv', index=False)
    # Initial crime data req vars file rows: 522355, Unique file rows:  22542

# Read the original crime file Crime_National_UCR_offenses_1960_2015.csv
get_req_crime_data_from1990('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/crime/Crime_National_UCR_offenses_1960_2015.csv')


