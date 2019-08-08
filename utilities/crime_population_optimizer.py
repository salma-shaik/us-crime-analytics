import pandas as pd
from datetime import datetime


# To get the counties that don't have crime data for all the years.
def get_incomplete_county_crime_years_ori(cr_df):

    crime_counties_ori_yr_grpd = {ORI: crime_year.tolist() for ORI, crime_year in cr_df.groupby('ORI')['crime_year']}

   # (pd.DataFrame(crime_counties_ori_yr_grpd)).to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/crime_data/Crime_ORI_Years.csv', index=False)

    req_yrs = [2015, 2014, 2013, 2012, 2011, 2010, 2009, 2008, 2007, 2006, 2005, 2004, 2003, 2002, 2001,
                         2000, 1999, 1998, 1997, 1996, 1995, 1994, 1993, 1992, 1991, 1990]

    incmplte_ori = pd.DataFrame(columns=['ORI'])

    ori_list = []

    # for col in final_main_subset_df.columns.tolist():
    for key, value in crime_counties_ori_yr_grpd.items():
        if all(elem in value for elem in req_yrs):
            pass
        else:
            ori_list.append(key)

    incmplte_ori = incmplte_ori.append(pd.Series(ori_list), ignore_index=True)

    return incmplte_ori


def get_crime_dec():
    crime_df = pd.read_csv(
        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/crime/Crime_Crswlk_Major_Merged_Inner.csv')

    crime_df = crime_df.drop(crime_df[(crime_df.ORI == 'CO00107') | (crime_df.ORI == 'VA07401')].index)

    # Get the list of all ORIs which have zero population for atleast one of the decennial crime_years
    crime_df_zero_dec_pop_ORIs = crime_df[(crime_df.population == 0) & ((crime_df.crime_year == 1990) | (crime_df.crime_year == 2000) | (crime_df.crime_year == 2010))]

    # Get the list of ORIs which don't have any entry for any of the census years
    # crime_df_msng_cen_entry = get_incomplete_county_crime_years_ori(crime_df)

    crime_counties_ori_yr_grpd = {ORI: crime_year.tolist() for ORI, crime_year in crime_df.groupby('ORI')['crime_year']}

    req_yrs = [2015, 2010, 2000, 1990]

    ori_list = []

    # for col in final_main_subset_df.columns.tolist():
    # crime_df_zero_dec_pop_ORIs canhave ORIs which have non zero population for atleast one of the decennial years.
    # But we want only those ORIs which have non zero population for all the decennial years and 2015
    # Hence get a list of ORIs which don't have data for all [2015, 2010, 2000, 1990]
    for key, value in crime_counties_ori_yr_grpd.items():
        if all(elem in value for elem in req_yrs):
            pass
        else:
            ori_list.append(key)

    # convert list to set coz there might be some duplicate ORIs which satisfy both the above conditions.
    ori_list_df = pd.DataFrame(set(ori_list), columns=['ORI'])

    all_msng_cen_cr = crime_df_zero_dec_pop_ORIs.append([ori_list_df], sort=False)

    all_msng_cen_cr['ORI'].to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/crime/crime_missing_decennial_pop_oris.csv', index=False)

    # Now subset the crime file without any records with the above ORIs
    crime_df_non_zero_dec_pop = crime_df[~crime_df.ORI.isin(all_msng_cen_cr['ORI'])]

    crime_df_zero_dec_pop = crime_df[crime_df.ORI.isin(all_msng_cen_cr['ORI'])]

    crime_df_zero_dec_pop.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/crime/crime_missing_decennial_pop.csv', index=False)

    crime_df_non_zero_dec_pop.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/crime/crime_without_missing_decennial_pop.csv', index=False)
    # There were 44 ORIs which had missing population in atleast one of the non-decennial crime_years
    # 454 agencies which don't have any entry for atleast one of the

    # Separate out county and city records based on Govt_level
    crime_counties = crime_df_non_zero_dec_pop[crime_df_non_zero_dec_pop.Govt_level == 1]
    # write to file to merge later with interpolated df
    crime_counties.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/crime/crime_counties.csv', index=False)

    # Get the decennial crime data for counties.
    crime_counties_dec = crime_counties[(crime_counties.crime_year == 1990) | (crime_counties.crime_year == 2000) | (
            crime_counties.crime_year == 2010) | (crime_counties.crime_year == 2015)]

    """
        Sort by ORI and crime_year to get the 4 occurrences of each ORI together
        and then sort by crime_year(15,10,00,90)
    """
    crime_counties_dec = crime_counties_dec.sort_values(by=['ORI', 'crime_year'], ascending=[True, False])
    crime_counties_dec.to_csv(
        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/crime/crime_counties_dec.csv',
        index=False)


    crime_cities = crime_df_non_zero_dec_pop[(crime_df_non_zero_dec_pop.Govt_level == 2) | (crime_df_non_zero_dec_pop.Govt_level == 3)]
    # write to file to merge later with interpolated df
    crime_cities.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/crime/crime_cities.csv', index=False)

    # Get the decennial crime data for cities.
    crime_cities_dec = crime_cities[(crime_cities.crime_year == 1990) | (crime_cities.crime_year == 2000) | (crime_cities.crime_year == 2010) | (crime_cities.crime_year == 2015)]

    """
    Sort by ORI and crime_year to get the 4 occurrences of each ORI together
    and then sort by crime_year(15,10,00,90)
    """
    crime_cities_dec = crime_cities_dec.sort_values(by=['ORI', 'crime_year'], ascending=[True, False])
    crime_cities_dec.to_csv(
        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/crime/crime_cities_dec.csv',
        index=False)


# Interpolate the population values between the decennial years and extrapolate beyond 2010 to 2015
def interpolate_population(crime_df, fl_name):
    print("########## Start: ", datetime.now().time())
    crime_dec = pd.read_csv(crime_df)

    # get the count of unique ORIs
    unique_ori = set(crime_dec['ORI']).__len__()
    print(unique_ori)
    # unique county ORIs: 2875
    # unique cities ORIs: 11589

    crime_pop = crime_dec[['ORI', 'crime_year', 'population']]
    crime_pop_int = pd.DataFrame(columns=crime_pop.columns)
    for row in crime_pop.itertuples():
        crime_pop_int = crime_pop_int.append(pd.Series(row[1:], index=crime_pop.columns), ignore_index=True)
        # append 4 rows after 2015 for 14, 13, 12, 11
        if row.crime_year == 2015:
            for i in range(4):
                crime_pop_int = crime_pop_int.append(pd.Series(), ignore_index=True)
        # append 9 empty rows if the year is != 1990 and 2015 coz we are interpolating till 1990.
        if row.crime_year != 1990 and row.crime_year != 2015:
            for i in range(9):
                crime_pop_int = crime_pop_int.append(pd.Series(), ignore_index=True)

    # ffill ORIs so that they are copied for in between decennial years
    crime_pop_int['ORI'] = crime_pop_int['ORI'].ffill()

    # Interpolate. This fills all the NaN rows between 2 given years that were added above.
    crime_pop_int = crime_pop_int.interpolate(method='linear', axis=0)
    print("########## End: ", datetime.now().time())

    crime_pop_int.drop(['crime_year'], axis=1, inplace=True)
    # Create all years between 90-15
    years = pd.DataFrame(
        {'crime_year': [2015, 2014, 2013, 2012, 2011, 2010, 2009, 2008, 2007, 2006, 2005, 2004, 2003, 2002, 2001,
                  2000, 1999, 1998, 1997, 1996, 1995, 1994, 1993, 1992, 1991, 1990]})

    crime_year = pd.concat([years] * unique_ori,ignore_index=True)  # 14831 records(ORIs) in each normalized census files. So all these years for each of the ORI. Total 385606

    crime_pop_int_geo_final = pd.concat([crime_pop_int, crime_year], axis=1)

    crime_pop_int_geo_final.to_csv(f'/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/crime/{fl_name}.csv',index=False)


def get_final_geo_crime_file(ini_fl, int_fl, op_file):
    crime_ini_df = pd.read_csv(ini_fl)
    crime_int_df = pd.read_csv(int_fl)
    crime_geo_final_df = crime_ini_df.merge(crime_int_df, on=['ORI', 'crime_year'],suffixes=['_original', '_interpolated'], how='left')

    crime_geo_final_df['population'] = crime_geo_final_df['population_interpolated']
    crime_geo_final_df.drop(['population_original', 'population_interpolated'], axis=1, inplace=True)

    crime_geo_final_df.to_csv(
        f'/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/crime/{op_file}.csv',
        index=False)


def append_crime_int_data():
    crime_counties_df = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/crime/crime_counties_pop_int_merged.csv')
    crime_cities_df = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/crime/crime_cities_pop_int_merged.csv')

    final_crime = crime_counties_df.append([crime_cities_df], sort=False)

    final_crime.drop(['AGENCY', 'Govt_level', 'place_fips', 'STATEFP', 'CNTY'], axis=1, inplace=True)

    final_crime_sorted = final_crime.sort_values(by=['ORI', 'crime_year'], ascending=[True, False])

    # ############## Check this out
    # Reset index after sorting so that it is in ascending order again and not trying to maintain the original index
    final_crime_sorted = final_crime_sorted.reset_index(drop=True)

    final_crime_sorted.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/crime/crime_with_updated_fbi_pop.csv', index=False)


# CO00107 - missing crime data for 1999 and 1998; VA07401 - missing crime data from 1994-1990


# 1. Get only the dec crime for interpolation
get_crime_dec()

# 2. Interpolate county population between census years
interpolate_population('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/crime/crime_counties_dec.csv', 'crime_counties_pop_int')

# 3. Interpolate city population between census years
interpolate_population('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/crime/crime_cities_dec.csv', 'crime_cities_pop_int')

# 4. merge int pop county with ini cnty
get_final_geo_crime_file('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/crime/crime_counties.csv',
                      '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/crime/crime_counties_pop_int.csv', 'crime_counties_pop_int_merged')

# 4. merge int pop city with ini city
get_final_geo_crime_file('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/crime/crime_cities.csv',
                        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/crime/crime_cities_pop_int.csv','crime_cities_pop_int_merged')


# 5. concat counties and cities with int pop
append_crime_int_data()


# get_incomplete_county_crime_years_ori('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/crime_data/crime_counties.csv')
#get_incomplete_county_crime_years_ori('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/crime_data/crime_cities.csv')
############### To-Do: for rates - create a new column with POP100 values for counties and population values for cities ###################