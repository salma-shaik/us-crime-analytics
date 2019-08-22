import pandas as pd
import numpy as np

final_df = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/merge_files/final_main_race_counts.csv')

"""
    1. 
        Get only the required crime columns for years 98-08
"""
crime_req = final_df[['ORI', 'AGENCY','Govt_level', 'POP100', 'place_fips', 'placename', 'STATEFP', 'CNTY', 'YEAR', 'murder', 'manslaughter', 'rape', 'robbery', 'aggravated_assault', 'burglary', 'larceny',
                         'simple_assault', 'auto_theft']]
crime_years = [1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008]
crime_req_yrs = crime_req.loc[crime_req['YEAR'].isin(crime_years)]

"""
    2. 
        Create tot major offences by adding up all the crime vars to only consider records with non-zero crime.   
"""
crime_req_yrs['tot_major_offenses_agency'] = crime_req_yrs[['murder', 'manslaughter', 'rape', 'robbery', 'aggravated_assault', 'burglary', 'larceny',
                                                            'simple_assault', 'auto_theft']].sum(axis=1)
crime_req_yrs['tot_felonies_agency'] = crime_req_yrs[['murder', 'manslaughter', 'rape', 'robbery',
                                                    'aggravated_assault', 'burglary', 'auto_theft']].sum(axis=1)
crime_req_yrs['tot_misdemeanors_agency'] = crime_req_yrs[['larceny', 'simple_assault']].sum(axis=1)

crime_req_yrs.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/merge_files/final_main_race_counts_crime_totals_98_08.csv', index=False)


"""
    3. 
        Some ORIs don't have data for 98-08 but do for some years out of this range
        Identify non zero and zero ones
        Get only those records which have non-zero total offense count
        Get the list of ORIs which have zero tot offense count for all the yrs between 98-08
"""

# Get only those records whose tot_major_offenses_agency value is > 0
crime_98_08_1st_rep_yr = crime_req_yrs.query('tot_major_offenses_agency > 0')

# Sort by ORI and ascending year and get the 1st available year record for each jurisdiction
crime_98_08_1st_rep_yr.sort_values(['ORI', 'YEAR'], inplace=True)

# drop duplicates so that the 1st record, in this case the record for the first reported year is retained.
crime_98_08_1st_rep_yr.drop_duplicates(subset=['ORI'], inplace=True)
crime_98_08_1st_rep_yr.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/merge_files/crime_98_08_tot_non_zero.csv', index=False)


# Getting the ORIs which don't have data for any of the years between 1998-2008
crime_98_08_tot_zero = crime_req_yrs[~crime_req_yrs.ORI.isin(crime_98_08_1st_rep_yr['ORI'])]
zero_oris = set(crime_98_08_tot_zero['ORI'])

# Write the zero ORIs to output file
ori_list_df = pd.DataFrame(zero_oris, columns=['ORI'])
ori_list_df.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/merge_files/oris_zero_totals_98_08.csv', index=False)


"""
    3.
        Group the data frame by fips state and fips county and then calculate the sum of each crime column
        The groupby output will have an index or multi-index on rows corresponding to your chosen grouping variables. 
        To avoid setting this index, pass “as_index=False” to the groupby operation.
"""

# creating new representative column for each crime to hold the total counts
crime_req_yrs_cnty_totals = crime_98_08_1st_rep_yr.assign(
    murder_cnty_total = crime_98_08_1st_rep_yr['murder'],
    manslaughter_cnty_total = crime_98_08_1st_rep_yr['manslaughter'],
    rape_cnty_total = crime_98_08_1st_rep_yr['rape'],
    robbery_cnty_total = crime_98_08_1st_rep_yr['robbery'],
    aggravated_assault_cnty_total = crime_98_08_1st_rep_yr['aggravated_assault'],
    burglary_cnty_total = crime_98_08_1st_rep_yr['burglary'],
    larceny_cnty_total = crime_98_08_1st_rep_yr['larceny'],
    simple_assault_cnty_total = crime_98_08_1st_rep_yr['simple_assault'],
    auto_theft_cnty_total = crime_98_08_1st_rep_yr['auto_theft']
).groupby(
   ['STATEFP', 'CNTY'], as_index=False
).agg(
    {
        'murder_cnty_total':'sum',
        'manslaughter_cnty_total': 'sum',
        'rape_cnty_total': 'sum',
        'robbery_cnty_total':'sum',
        'aggravated_assault_cnty_total': 'sum',
        'burglary_cnty_total': 'sum',
        'larceny_cnty_total': 'sum',
        'simple_assault_cnty_total':'sum',
        'auto_theft_cnty_total': 'sum'
    }
).reset_index()  #initially reset_index(drop=True). shouldn't make a diff since we want STATEFP and CNTY to remain as columns.
# or may be check the index initially in the previous case and this case. IF it was adding 0 index initially also coz as_index= False might infact not be adding statefp and cnty as indices
#################### CHECK ####################


"""
    4. Create the below indexes
        o	tot_felonies_cnty  : murder, manslaughter, rape, robbery (the measure with all the robberies together), aggravated assault, burglary, auto theft
        o	tot_minor_offences_cnty : simple assault + larceny
            tot_major_offences_cnty : tot_felonies_cnty + tot_minor_offences_cnty 
"""

crime_req_yrs_cnty_totals['tot_felonies_cnty'] = crime_req_yrs_cnty_totals[['murder_cnty_total', 'manslaughter_cnty_total', 'rape_cnty_total', 'robbery_cnty_total',
                                                                          'aggravated_assault_cnty_total', 'burglary_cnty_total', 'auto_theft_cnty_total']].sum(axis=1)
crime_req_yrs_cnty_totals['tot_misdemeanors_cnty'] = crime_req_yrs_cnty_totals[['larceny_cnty_total', 'simple_assault_cnty_total']].sum(axis=1)
crime_req_yrs_cnty_totals['tot_major_offenses_cnty'] = crime_req_yrs_cnty_totals[['tot_felonies_cnty', 'tot_misdemeanors_cnty']].sum(axis=1)

crime_req_yrs_cnty_totals.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/merge_files/final_main_race_counts_crime_totals_98_08_1st_rep_yr_cnty_totals_groupby.csv', index=False)

# merge the county totals group by df with the crime_98_08_1st_rep_yr on state and cnty fips so that county level totals
# are assigned to each agency based on state and county fips
crime_non_zero_totals = pd.merge(crime_98_08_1st_rep_yr, crime_req_yrs_cnty_totals, on=['STATEFP', 'CNTY'])
crime_non_zero_totals['perc_felonies'] = (crime_non_zero_totals['tot_felonies_agency']/crime_non_zero_totals['tot_felonies_cnty'])*100
crime_non_zero_totals['perc_misdemeanors'] = (crime_non_zero_totals['tot_misdemeanors_agency']/crime_non_zero_totals['tot_misdemeanors_cnty'])*100

crime_non_zero_totals.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/merge_files/agency_1st_rep_yr_fel_misd_pcts_98_08.csv', index=False)







"""
    After groupby - 3036 statefp and cnty combinations (crime_req_yrs_cnty_totals)

    But in crime_98_08_1st_rep_yr:
    2729 counties, 7848 cities(2), 1415 townships(3)

    So apparently some county jurisdictions didn't fall under major agencies.

    Get the list of state and cnty fips combinations which are different between crime_non_zero_totals and crime_req_yrs_cnty_totals_groupby.
"""


"""
    Get df with only required govt level
"""
def get_glevel_crime(g_level):
    if g_level == 'cnty':
        # Get the df with only county level non-zero totals
       # crime_non_zero_totals = crime_98_08_1st_rep_yr[crime_98_08_1st_rep_yr.Govt_level == 1].merge(crime_req_yrs_cnty_totals, on=['STATEFP', 'CNTY'], how='left')
        crime_non_zero_totals = pd.merge(crime_98_08_1st_rep_yr[crime_98_08_1st_rep_yr.Govt_level == 1], crime_req_yrs_cnty_totals, on=['STATEFP', 'CNTY'], how='left')

    else:
        # Get the df with city and township level non-zero totals
       # crime_non_zero_totals = crime_98_08_1st_rep_yr[(crime_98_08_1st_rep_yr.Govt_level == 2) | (crime_98_08_1st_rep_yr.Govt_level == 3)].merge(crime_req_yrs_cnty_totals, on=['STATEFP', 'CNTY'], how='left')
        crime_non_zero_totals = pd.merge(crime_98_08_1st_rep_yr[(crime_98_08_1st_rep_yr.Govt_level == 2) | (crime_98_08_1st_rep_yr.Govt_level == 3)], crime_req_yrs_cnty_totals, on=['STATEFP', 'CNTY'], how='left')

        # multiple cities and townships can have same st_cnty_fips and only differ by place fips so need to drop duplciates with st and cnty fips
        crime_non_zero_totals.sort_values(['STATEFP', 'CNTY'], inplace=True)
        crime_non_zero_totals.drop_duplicates(subset=['STATEFP', 'CNTY'], inplace=True)

    """
        Create the felony and misdemeanor percentages based on POP100
    """
    # crime_non_zero_totals['tot_cnty_prisons_pct'] = crime_non_zero_totals['tot_felonies_cnty'] / crime_non_zero_totals['POP100'] * 100
    # crime_non_zero_totals['tot_cnty_jails_pct'] = crime_non_zero_totals['tot_misdemeanors_cnty'] / crime_non_zero_totals['POP100'] * 100

    # POP100 is zero for some ORIs that is census missing for some ORIs. Hence replacing inf with 0
    crime_non_zero_totals.replace(np.inf, 0, inplace=True)
    crime_non_zero_totals.to_csv(f'/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/analysis/crime_{g_level}_98_08_totals_pcts.csv', index=False)


    # Get only the 'STATEFP', 'CNTY', 'tot_cnty_prisons_pct', 'tot_cnty_jails_pct' columns
    crime_totals = crime_non_zero_totals[['STATEFP', 'CNTY', 'ORI', 'Govt_level','placename','POP100','tot_felonies_cnty', 'tot_misdemeanors_cnty', 'tot_major_offenses_cnty']]
    crime_totals.to_csv(f'/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/analysis/crime_{g_level}_98_08_crime_totals.csv', index=False)


# Get the df with only county level non-zero totals
#get_glevel_crime('cnty')

# Get the df with city and township level non-zero totals
#get_glevel_crime('non_cnty')


# Just need to get the city and township records which dont match with the cnty records based on st_cnty_fips string
def get_nonmatching_non_cnty():
    cnty_pct_df = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/analysis/crime_cnty_98_08_crime_totals.csv')
    non_cnty_pct_df = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/analysis/crime_non_cnty_98_08_crime_totals.csv')

    cnty_pct_df = cnty_pct_df.assign(st_cnty_fips=[str(x) + str(y) for x, y in zip(cnty_pct_df['STATEFP'], cnty_pct_df['CNTY'])]).reset_index(drop=True)
    #cnty_pct_df.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/analysis/crime_cnty_98_08_incarc_pcts_stcnty.csv', index=False)

    non_cnty_pct_df = non_cnty_pct_df.assign(st_cnty_fips=[str(x) + str(y) for x, y in zip(non_cnty_pct_df['STATEFP'], non_cnty_pct_df['CNTY'])]).reset_index(drop=True)
    #non_cnty_pct_df.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/analysis/crime_non_cnty_98_08_incarc_pcts_stcnty.csv', index=False)

    non_cnty_nonmatching = non_cnty_pct_df[~non_cnty_pct_df.st_cnty_fips.isin(cnty_pct_df['st_cnty_fips'])]
    #crime_98_08_tot_zero = crime_req_yrs[~crime_req_yrs.ORI.isin(crime_98_08_1st_rep_yr['ORI'])]

    non_cnty_nonmatching.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/analysis/crime_98_08_crime_totals_non_cnty_nonmatching.csv', index=False)

    # Finally append all the census files together
    crime_totals_98_08 = cnty_pct_df.append([non_cnty_nonmatching], sort=False)
    crime_totals_98_08.sort_values(['st_cnty_fips', 'Govt_level'], inplace=True)
    crime_totals_98_08.drop_duplicates(subset=['st_cnty_fips', 'Govt_level'], inplace=True)
    crime_totals_98_08.drop(['ORI', 'placename', 'Govt_level','POP100'], axis=1, inplace=True)
    crime_totals_98_08.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/analysis/agency_crime_totals_98_08.csv', index=False)
#
#get_nonmatching_non_cnty()