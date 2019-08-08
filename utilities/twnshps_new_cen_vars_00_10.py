
#import utilities
"""

    Create new variables for township census similar to cities and counties

    Govt_level	                    Add default value 3
    place_fips	                    rename county subdivision col to place_fips
    placename	                    NAME column. Rename NAME col to placename
    CNTY	                        Curernt cities files doesn’t have county fips so leave this blank? CHECK. If not, rename county to CNTY
    STATEFP	                        Rename state col to STATEFP
    YEAR                            Add a new YEAR col with default value of 2000 or 2010 depending on which file we are working with
    POP100	                        P012001

    White_count	                    P012A001
    Black_count	                    P012B001
    Hispanic_count	                P012H001
    Age1524_WhiteM	                P012A006, P012A007, P012A008, P012A009, P012A010
    White_Males_All	                P012A002
    Age1524_WhiteF	                P012A030, P012A031, P012A032, P012A033, P012A034
    White_Females_All	            P012A026
    Age1524_BlackM	                P012B006, P012B007, P012B008, P012B009, P012B010
    Black_Males_All	                P012B002
    Age1524_BlackF	                P012B030, P012B031, P012B032, P012B033, P012B034
    Black_Females_All	            P012B026
    Hispanic_Males_All	            P012H002
    Age1524_HispanicM	            P012H006, P012H007, P012H008, P012H009, P012H010
    Age1524_HispanicF	            P012H030, P012H031, P012H032, P012H033, P012H034
    Hispanic_Females_All	        P012H026
    Pct_WYM	                        Age1524_WhiteM/White_Males_All
    Pct_WYF	                        Age1524_WhiteF/White_Females_All

"""
import pandas as pd


"""
    Govt_level	                    Add default value 3
    place_fips	                    rename county subdivision col to place_fips
    placename	                    NAME column. Rename NAME col to placename
    CNTY	                        Curernt cities files doesn’t have county fips so leave this blank? CHECK. If not, rename county to CNTY
    STATEFP	                        Rename state col to STATEFP
    YEAR                            Add a new YEAR col with default value of 2000 or 2010 depending on which file we are working with
    POP100	                        P012001
"""


def create_fixed_columns(twnshp_df, new_df, cen_year):
    new_df['place_fips'] = twnshp_df['county subdivision']
    new_df['placename'] = twnshp_df['NAME']
    new_df['CNTY'] = ''
    new_df['STATEFP'] = twnshp_df['state']
    new_df['POP100'] = twnshp_df['P012001']
    # If I place constant value columns at the beginning they are getting set to NaN. dtype conversion?
    new_df['Govt_level'] = 3
    new_df['YEAR'] = cen_year
    return new_df


"""
    White_count	                    P012A001
    Black_count	                    P012B001
    Hispanic_count	                P012H001
    Age1524_WhiteM	                P012A006, P012A007, P012A008, P012A009, P012A010
    White_Males_All	                P012A002
    Age1524_WhiteF	                P012A030, P012A031, P012A032, P012A033, P012A034
    White_Females_All	            P012A026
    Age1524_BlackM	                P012B006, P012B007, P012B008, P012B009, P012B010
    Black_Males_All	                P012B002
    Age1524_BlackF	                P012B030, P012B031, P012B032, P012B033, P012B034
    Black_Females_All	            P012B026
    Hispanic_Males_All	            P012H002
    Age1524_HispanicM	            P012H006, P012H007, P012H008, P012H009, P012H010
    Age1524_HispanicF	            P012H030, P012H031, P012H032, P012H033, P012H034
    Hispanic_Females_All	        P012H026
"""


def create_race_cols(ini_df, new_df):
    new_df['White_count'] = ini_df.loc[:, 'P012A001']
    new_df['Black_count'] = ini_df.loc[:, 'P012B001']
    new_df['Hispanic_count'] = ini_df.loc[:, 'P012H001']

    new_df['Age1524_WhiteM'] = ini_df.loc[:, ['P012A006', 'P012A007', 'P012A008', 'P012A009', 'P012A010']].sum(axis=1)
    new_df['White_Males_All'] = ini_df.loc[:, 'P012A002']
    new_df['Age1524_WhiteF'] = ini_df.loc[:, ['P012A030', 'P012A031', 'P012A032', 'P012A033', 'P012A034']].sum(axis=1)
    new_df['White_Females_All'] = ini_df.loc[:, 'P012A026']

    new_df['Age1524_BlackM'] = ini_df.loc[:, ['P012B006', 'P012B007', 'P012B008', 'P012B009', 'P012B010']].sum(axis=1)
    new_df['Black_Males_All'] = ini_df.loc[:, 'P012B002']
    new_df['Age1524_BlackF'] = ini_df.loc[:, ['P012B030', 'P012B031', 'P012B032', 'P012B033', 'P012B034']].sum(axis=1)
    new_df['Black_Females_All'] = ini_df.loc[:, 'P012B026']

    new_df['Age1524_HispanicM'] = ini_df.loc[:, ['P012H006', 'P012H007', 'P012H008', 'P012H009', 'P012H010']].sum(axis=1)
    new_df['Hispanic_Males_All'] = ini_df.loc[:, 'P012H002']
    new_df['Age1524_HispanicF'] = ini_df.loc[:, ['P012H030', 'P012H031', 'P012H032', 'P012H033', 'P012H034']].sum(axis=1)
    new_df['Hispanic_Females_All'] = ini_df.loc[:, 'P012H026']

    return new_df

"""
    Pct_WYM	                        Age1524_WhiteM/White_Males_All
    Pct_WYF	                        Age1524_WhiteF/White_Females_All
"""
def create_white_perc_cols(new_df):
    new_df['Pct_WYM'] = new_df['Age1524_WhiteM'] / new_df['White_Males_All']
    new_df['Pct_WYF'] = new_df['Age1524_WhiteF'] / new_df['White_Females_All']
    return new_df


def write_final_df_csv(final_df, op_file):

    cols = list(final_df)
    cols.pop(cols.index('place_fips'))
    cols.pop(cols.index('placename'))
    cols.pop(cols.index('CNTY'))
    cols.pop(cols.index('STATEFP'))
    cols.pop(cols.index('POP100'))
    cols.pop(cols.index('Govt_level'))
    cols.pop(cols.index('YEAR'))

    # Arrange the columns in order similar to city and county census files
    final_df_arngd = final_df[['Govt_level', 'place_fips', 'placename', 'CNTY', 'STATEFP', 'YEAR', 'POP100'] + cols]

    # Write the final df with new vars to a csv
    final_df_arngd.to_csv(f'/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/wip_merge_files/{op_file}.csv',index=False)


"""
    Append township file to the bottom of the cities file
    national_census_df = national_census_df.append([cities_df])
"""


def append_city_twnshp(city_df, twnshp_df, op_file):
    city_df = city_df.append([twnshp_df], sort=False)
    city_df.to_csv(f'/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/cen_00/tnwshps_api/{op_file}.csv',index=False)


new_twnshp_df = pd.DataFrame()

"""
Create new vars for 2000 township file
"""
ini_twnshp_df = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/cen_00/tnwshps_api/new_census_townships_00_initial.csv')
new_twnshp_df = create_fixed_columns(ini_twnshp_df, new_twnshp_df, 2000)
new_twnshp_race_df = create_race_cols(ini_twnshp_df, new_twnshp_df)
new_twnshp_race_pct_df = create_white_perc_cols(new_twnshp_race_df)
write_final_df_csv(new_twnshp_race_pct_df, 'new_census_townships_00_new_vars')

# append new townships to city df
city_df = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/cen_00/census_cities_2000/new_census_variables/new_vars_census_cities_2000.csv')
append_city_twnshp(city_df, new_twnshp_race_pct_df, 'new_census_cities_townships_00_new_vars')

"""
Create new vars for 2010 township file
"""
# ini_twnshp_df = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/wip_merge_files/new_census_townships_10_initial.csv')
# new_twnshp_df = create_fixed_columns(ini_twnshp_df, new_twnshp_df, 2010)
# new_twnshp_race_df = create_race_cols(ini_twnshp_df, new_twnshp_df)
# new_twnshp_race_pct_df = create_white_perc_cols(new_twnshp_race_df)
# write_final_df_csv(new_twnshp_race_pct_df, 'new_census_townships_10_new_vars')
#
# city_df = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/census_cities_2010/new_census_variables/new_vars_census_cities_2010.csv')
# append_city_twnshp(city_df, new_twnshp_race_pct_df, 'new_vars_census_cities_townships_10')
