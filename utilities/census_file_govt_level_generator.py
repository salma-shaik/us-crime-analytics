import pandas as pd

pd.options.mode.chained_assignment = None


def get_final_main_cgovtype_ori_agency(file_path):
    """
        Obtain ORI, AGENCY, CGOVTYPE, FIPS_STATE, FIPS_PLACE from final main(90-01) file
    """
    final_main_df = pd.read_csv(file_path)
    final_main_fips_ori_agency = final_main_df[['ORI', 'AGENCY', 'CGOVTYPE', 'FIPS_STATE', 'FIPS_PLACE']]

    """
    1. Obtain only unique records from the final main file - key: fips place + fips state
    """
    final_main_fips_ori_agency_unique = final_main_fips_ori_agency.drop_duplicates(['FIPS_STATE', 'FIPS_PLACE']) # --> 11,602 rows

    """
    2. Rename CGOVTYPE, FIPS_STATE, FIPS_PLACE to Govt_level, 'STATEFP', 'place_fips' to match national census file
    """
    final_main_fips_ori_agency_unique = final_main_fips_ori_agency_unique.rename(
        {'CGOVTYPE': 'Govt_level', 'FIPS_STATE': 'STATEFP', 'FIPS_PLACE': 'place_fips'}, axis='columns')

    """
    3. Get only those records from 90 final main file whose cgovtype is 1,2 or 3
    """
    final_main_fips_ori_agency_unique = final_main_fips_ori_agency_unique.loc[final_main_fips_ori_agency_unique['Govt_level'].isin([1, 2, 3])]

    return final_main_fips_ori_agency_unique


def get_glevel_ori_agency(county_cens_file, crime_df, filename, cens_year, city_cens_file=False):

    """
        Merge CGOVTYPE, ORI, AGENCY from final main file into census files based on state and place fips.
    """

    """
    1. Append cities census file to counties census file
    """
    national_census_df = pd.read_csv(county_cens_file)

    """
        Checking for city census file coz we need to first append city census file to the bottom of county census file for 2000 and 2010.
        And city census file is passed only for 2000 and 2010 since for 1990 city and county census data is already together.
    """
    if city_cens_file:
        cities_df = pd.read_csv(city_cens_file)
        national_census_df = national_census_df.append([cities_df])

    # Drop duplicates
    national_census_df = national_census_df.drop_duplicates(['STATEFP', 'place_fips'])
    national_census_df.to_csv(f'/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/cen_00/Census_{cens_year}_Unique.csv', index=False)


    """
    2.
    Merge census unique files with Crime_Major_Gov_Fips to get the correct cgovtype, CNTY based on fips state, fips place. 
    Also obtain ORI, Agency columns from crime file. 
    """
    national_census_df = national_census_df.merge(crime_df, on=['STATEFP', 'place_fips'], how='right')


    """
    3. Create final Govt_level = Govt_level_y column which has govt_level values from crime file and get rid of _x and _y columns 
    """
    national_census_df['Govt_level'] = national_census_df['Govt_level_y']
    national_census_df['CNTY'] = national_census_df['CNTY_y']
    national_census_df.drop(['Govt_level_x', 'Govt_level_y', 'CNTY_x', 'CNTY_y'], axis=1, inplace=True)

    """
    Add the year column to have year for even the missing census rows for certain ORIs
    """
    national_census_df['YEAR'] = cens_year

    """
    4. Rearrange columns so that ORI, AGENCY, Govt_level are at the beginning
    """
    cols = list(national_census_df.columns.values)
    cols.pop(cols.index('ORI'))
    cols.pop(cols.index('AGENCY'))
    cols.pop(cols.index('Govt_level'))
    cols.pop(cols.index('CNTY'))
    cols.pop(cols.index('YEAR'))

    national_census_df = national_census_df[['ORI', 'AGENCY', 'Govt_level', 'CNTY', 'YEAR'] + cols]
    #national_census_df = national_census_df[['ORI', 'AGENCY', 'YEAR'] + cols]

    # write the final df with updated govt_level, ori, agency etc. to a csv
    national_census_df.to_csv(f'/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/cen_00/{filename}.csv', index=False)


def merge_cen_final_main():
    """
        Use the Crime_National_UCR_offenses_1990_2015_Req_Vars_Unique_Crosswalk_Merged_CGOVTYPE123.csv
    """
    crime_major = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/crime/Crime_Crswlk_Major_Merged_Inner.csv')

    crime_major_gov_fips = crime_major[['ORI', 'AGENCY', 'Govt_level', 'place_fips', 'STATEFP', 'CNTY']]
    crime_major_gov_fips.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/crime/Crime_Major_Gov_Fips.csv', index=False)

    # Create the final national census 2000 file by combining 2000 cities and counties. Then merge it with crime main df on place and state fips
    counties_00_file = '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/cen_00/census_county_2000/new_census_variables/new_vars_census_county_2000.csv'
    cities_00_file = '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/cen_00/census_cities_2000/new_census_variables/new_census_cities_townships_00_new_vars.csv'
    #get_glevel_ori_agency(county_cens_file=counties_00_file, city_cens_file=cities_00_file, crime_df=crime_major_gov_fips, filename='Census_2000_Crime_Merge_Right', cens_year = 2000)


    # Create the final national census 2010 file by merging combining 2010 cities and counties.
    counties_10_file = '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/cen_10/census_county_2010/new_census_variables/new_vars_census_county_2010.csv'
    cities_10_file = '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/cen_10/census_cities_2010/new_census_variables/new_census_cities_townships_10_new_vars.csv'
    # get_glevel_ori_agency(county_cens_file=counties_10_file, city_cens_file=cities_10_file, crime_df=crime_major_gov_fips, filename='Census_2010_Crime_Merge_Right', cens_year = 2010)

    # Create the final 1990 census file by merging with 90 final main file
    get_glevel_ori_agency(county_cens_file = '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/cen_90/National_Census_1990_unique.csv', crime_df = crime_major_gov_fips, filename = 'Census_1990_Crime_Merge_Right', cens_year = 1990)





"""
   Merge each of the final 90, 00 and 10 the census files with final main file to get correct govt level values
   """
# merge_cen_final_main()


"""
    Consolidate all the final census files with the updated ORIs together
"""
# consolidate_all_census_files()