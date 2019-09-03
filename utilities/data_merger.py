import pandas as pd
import numpy as np


def merge_census_crime():
    """
    Census Columns:
        ORI	AGENCY	placename	Govt_level	place_fips	STATEFP	CNTY	YEAR
        POP100	White_count	Black_count	Hispanic_count	Age1524_WhiteM	White_Males_All
        Age1524_WhiteF	White_Females_All	Age1524_BlackM	Black_Males_All	Age1524_BlackF
        Black_Females_All	Hispanic_Males_All	Age1524_HispanicM	Age1524_HispanicF	Hispanic_Females_All
        Pct_WYM	Pct_WYF

    US_Crime_Analysis Columns:
        state	ori_code	group_number	division	year
        city_number	months_reported
        agency_name	agency_state	zip_code	murder	manslaughter	rape	robbery
        gun_robbery	knife_robbery	aggravated_assault	gun_assault	knife_assault	simple_assault
        burglary	larceny	auto_theft	officers_assaulted	officers_killed_by_felony
        officers_killed_by_accident	sub_group	population
    """
    census_df = pd.read_csv(
        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/census/Census_Interpolated.csv')
    crime_df = pd.read_csv(
        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/crime/crime_with_updated_fbi_pop.csv')

    """
    Merge crime file with census file. Left merge for now to have all the ORIs and years from census file.
    Merging on ori and year
    """
    census_crime_merged = census_df.merge(crime_df, left_on=['ORI', 'YEAR'], right_on=['ORI', 'crime_year'], how='left')
    # cen_cr_df['state_abbr'] = cen_cr_df.ori_code

    # Some ORIs for some years are missing coz not all agencies have reported crime for all the years.
    # So need to bypass those using na_action='ignore' otherwise can't substring NA error
    census_crime_merged['state_abbr'] = census_crime_merged['ORI'].map(lambda ORI: ORI[:2], na_action='ignore')
    # cen_cr_df = cen_cr_df.rename({'year':'crime_year'}, axis='columns')

    """
        Create the below new crime columns for basic analysis
        total_crime = sum(murder,manslaughter,rape,robbery,gun_robbery,knife_robbery,aggravated_assault,gun_assault,knife_assault,simple_assault,burglary,larceny,auto_theft)
        violent_crime = sum(murder,manslaughter,rape,robbery,aggravated_assault)
        property_crime = sum(burglary,larceny,auto_theft)
        crimes_against_officers = sum(officers_assaulted, officers_killed_by_felony)
        officers_killed_by_accident - not considering a crime. Is that right? Does the homicide data include these stats as well? If yes, then all 3 or just the 1st 2?
    """
    census_crime_merged['total_crime'] = census_crime_merged[
        ['murder', 'manslaughter', 'rape', 'robbery', 'gun_robbery', 'knife_robbery', 'aggravated_assault',
         'gun_assault', 'knife_assault', 'simple_assault', 'burglary', 'larceny', 'auto_theft']].sum(axis=1)
    census_crime_merged['violent_crime'] = census_crime_merged[['murder', 'manslaughter', 'rape', 'robbery', 'aggravated_assault']].sum(
        axis=1)
    census_crime_merged['property_crime'] = census_crime_merged[['burglary', 'larceny', 'auto_theft']].sum(axis=1)
    census_crime_merged['crimes_against_officers'] = census_crime_merged[['officers_assaulted', 'officers_killed_by_felony']].sum(axis=1)

    census_crime_merged.to_csv(
        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/merge_files/Census_Crime.csv',
        index=False)


# merge_census_crime()


def merge_census_crime_bea():
    cen_cr_df = pd.read_csv(
        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/merge_files/Census_Crime.csv')
    bea_df = pd.read_csv(
        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/economic/bea_census_all_1990_2015_cols_updated_county_suffix.csv')

    """
        # left merge on cen_cr to have all the ORIs, census records and to identify missing economic data if needed
        # bea cols(right) = year	fips_state	fips_county; cen_cr columns(left) = STATEFP	CNTY	YEAR
    """
    cen_cr_bea_merge = cen_cr_df.merge(bea_df, left_on=['STATEFP', 'CNTY', 'YEAR'],
                                       right_on=['fips_state', 'fips_county', 'year'], how='left')
    cen_cr_bea_merge.drop(['fips_state', 'fips_county', 'year'], axis=1, inplace=True)
    cen_cr_bea_merge.to_csv(
        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/merge_files/Census_Crime_BEA.csv',
        index=False)


# merge_census_crime_bea()


def merge_cen_cr_bea_spatial():
    cen_cr_bea_df = pd.read_csv(
        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/merge_files/Census_Crime_BEA.csv')
    spatial_df = pd.read_csv(
        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/spatial/crime_coord_final_1990_2001.csv')

    # Get only the required columns from spatial df: ori, PRIMARY_LATITUDE	, PRIMARY_LONGITUDE, old_lat, old_long
    spatial_df_req_cols = spatial_df[['ori', 'PRIMARY_LATITUDE', 'PRIMARY_LONGITUDE', 'old_lat', 'old_long']]

    spatial_df_req_cols.drop_duplicates(subset=['ori'], inplace=True)

    # Left merge on ori to have all cen_cr_bea_df records.
    # on:- cen_cr_bea(left)- 'ORI_Census'; spatial(right) - 'ORI_Spatial';
    cen_cr_bea_spatial_merged = cen_cr_bea_df.merge(spatial_df_req_cols, left_on='ORI', right_on='ori', how='left')
    cen_cr_bea_spatial_merged.drop(['ori'], axis=1, inplace=True)
    cen_cr_bea_spatial_merged.to_csv(
        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/merge_files/Census_Crime_BEA_Spatial.csv',
        index=False)

    # Identify the agencies which don't have either PRIMARY or old or both spatial data
    cen_cr_bea_spatial_merged_missing = cen_cr_bea_spatial_merged[
        cen_cr_bea_spatial_merged.PRIMARY_LATITUDE.isnull() | cen_cr_bea_spatial_merged.PRIMARY_LONGITUDE.isnull() |
        cen_cr_bea_spatial_merged.old_lat.isnull() | cen_cr_bea_spatial_merged.old_long.isnull()]
    cen_cr_bea_spatial_merged_missing.to_csv(
        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/merge_files/Census_Crime_BEA_Spatial_SpatialMissing.csv',
        index=False)


# merge_cen_cr_bea_spatial()


def merge_cen_cr_bea_spatial_officers():
    cen_cr_bea_spatial = pd.read_csv(
        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/merge_files/Census_Crime_BEA_Spatial.csv')

    leoka_df = pd.read_excel(
        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/officers/leoka_all_1990_2015.xlsx')
    # get reqd cols
    leoka_req = leoka_df[['ori', 'agency', 'year', 'total_officers']]

    # write the df with req vars to file
    leoka_req.to_csv(
        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/officers/leoka_req_vars.csv',
        index=False)

    cen_cr_bea_spatial_officers_merged = cen_cr_bea_spatial.merge(leoka_req, left_on=['ORI', 'YEAR'],
                                                                  right_on=['ori', 'year'], how='left')

    # Drop duplicate ori, agency, year columns from officers file
    cen_cr_bea_spatial_officers_merged.drop(['ori', 'agency', 'year'], axis=1, inplace=True)
    cen_cr_bea_spatial_officers_merged.to_csv(
        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/merge_files/Census_Crime_BEA_Spatial_Officers.csv',
        index=False)


# merge_cen_cr_bea_spatial_officers()


def merge_cen_cr_bea_spatial_officers_arrests():
    cen_cr_bea_spatial_officers = pd.read_csv(
        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/merge_files/Census_Crime_BEA_Spatial_Officers.csv')
    arrests_df = pd.read_csv(
        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/arrests/Arrests_Req_Vars_Indexes.csv')
    cen_cr_bea_spatial_officers_merged = cen_cr_bea_spatial_officers.merge(arrests_df, left_on=['ORI', 'YEAR'],
                                                                           right_on=['ori', 'year'], how='left')

    cen_cr_bea_spatial_officers_merged.drop(['ori', 'year'], axis=1, inplace=True)
    cen_cr_bea_spatial_officers_merged.to_csv(
        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/merge_files/Census_Crime_BEA_Spatial_Officers_Arrests.csv',
        index=False)


# merge_cen_cr_bea_spatial_officers_arrests()


def merge_cen_cr_bea_spatial_officers_arrests_incarceration():
    cen_cr_bea_spatial_officers_arrests = pd.read_csv(
        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/merge_files/Census_Crime_BEA_Spatial_Officers_Arrests.csv')
    incarc_df = pd.read_csv(
        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/incarceration/incarc_req_vars_updated_fips.csv')

    cen_cr_bea_spatial_officers_arrests_incarc_merged = cen_cr_bea_spatial_officers_arrests.\
        merge(incarc_df,left_on=['STATEFP','CNTY','YEAR'], right_on=['STATEFP','CNTY','year'], how='left')

    cen_cr_bea_spatial_officers_arrests_incarc_merged['state'] = cen_cr_bea_spatial_officers_arrests_incarc_merged[
        'state_x']
    cen_cr_bea_spatial_officers_arrests_incarc_merged.drop(['state_x', 'state_y', 'year'], axis=1, inplace=True)
    cen_cr_bea_spatial_officers_arrests_incarc_merged.to_csv(
        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/merge_files/Census_Crime_BEA_Spatial_Officers_Arrests_Incarceration.csv',
        index=False)


# merge_cen_cr_bea_spatial_officers_arrests_incarceration()


def merge_final_main_race_rates_incarceration_pct():
    # Read the cnty crime totals file
    cnty_agency_totals_98_08 = pd.read_csv(
        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/merge_files/agency_1st_rep_yr_fel_misd_pcts_98_08.csv')
    cnty_agency_totals_98_08 = cnty_agency_totals_98_08[['ORI', 'perc_felonies', 'perc_misdemeanors']]
    # Read the final main race counts file
    final_main_race_counts = pd.read_csv(
        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/merge_files/final_main_race_counts.csv')

    # So here merging with agency_1st_rep_yr_fel_misd_pcts_98_08.csv file to have only those ORIs which have
    # reported data for all the years between 98-08
    final_main_race_counts_crime_totals = final_main_race_counts.merge(cnty_agency_totals_98_08, on=['ORI'])
    final_main_race_counts_crime_totals.replace(np.inf, 0, inplace=True)

    # final_main_race_counts_crime_totals['prison_occupancy_count'] = (final_main_race_counts_crime_totals['perc_felonies'] * final_main_race_counts_crime_totals['total_prison_pop']) / 100
    # final_main_race_counts_crime_totals['jail_occupancy_count'] = (final_main_race_counts_crime_totals['perc_misdemeanors'] * final_main_race_counts_crime_totals['jail_interp']) / 100

    final_main_race_counts_crime_totals.to_csv(
        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/merge_files/final_main_race_counts_incarc_counts.csv',
        index=False)


merge_final_main_race_rates_incarceration_pct()


def merge_final_main_race_counts_incarceration_pct_new_econ():
    # 1st del old econ data cols then merge with new econ data
    pass