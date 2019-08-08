import pandas as pd
import numpy as np

"""
    Find the list of ORIs commonly missing in all the 3 census years
"""


def common_missing_crime_cen():
    cen_90 = pd.read_csv(
        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/merge_files/census_crime/Crime_Unmatched_With_Census_1990.csv')
    cen_00 = pd.read_csv(
        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/merge_files/census_crime/Crime_Unmatched_With_Census_2000.csv')
    cen_10 = pd.read_csv(
        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/merge_files/census_crime/Crime_Unmatched_With_Census_2010.csv')

    # Missing in all 3 census files
    cen_msng_common_ori = set(cen_90['ORI']).intersection(set(cen_00['ORI']), set(cen_10['ORI']))
    missing_common_ori = pd.DataFrame(list(cen_msng_common_ori), columns=['ORI'])
    print('cen_msng_common_ori: ', cen_msng_common_ori.__len__())
    missing_common_ori.to_csv(
        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/merge_files/census_crime/Crime_Unmatched_With_Census_Common_ORI.csv',
        index=False)

    # Missing in 1990 and 2000
    cen_msng_ori_90_00 = set(cen_90['ORI']).intersection(set(cen_00['ORI']))
    missing_common_ori_90_00 = pd.DataFrame(list(cen_msng_ori_90_00), columns=['ORI'])
    print('missing_common_ori_90_00: ', missing_common_ori_90_00.__len__())
    missing_common_ori_90_00.to_csv(
        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/merge_files/census_crime/Crime_Unmatched_With_Census_90_00_ORI.csv',
        index=False)

    # Missing in 1990 and 2010
    cen_msng_ori_90_10 = set(cen_90['ORI']).intersection(set(cen_10['ORI']))
    missing_common_ori_90_10 = pd.DataFrame(list(cen_msng_ori_90_10), columns=['ORI'])
    print('missing_common_ori_90_10: ', missing_common_ori_90_10.__len__())
    missing_common_ori_90_10.to_csv(
        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/merge_files/census_crime/Crime_Unmatched_With_Census_90_10_ORI.csv',
        index=False)

    # Missing in 2000 and 2010
    cen_msng_ori_00_10 = set(cen_00['ORI']).intersection(set(cen_10['ORI']))
    missing_common_ori_00_10 = pd.DataFrame(list(cen_msng_ori_00_10), columns=['ORI'])
    print('missing_common_ori_00_10: ', missing_common_ori_00_10.__len__())
    missing_common_ori_00_10.to_csv(
        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/merge_files/census_crime/Crime_Unmatched_With_Census_00_10_ORI.csv',
        index=False)


# common_missing_crime_cen()


"""
Get placename from non empty years
1st attempt:
    placename for 1990 :- index-1
    placename for 2000/2010 :- index+1

2nd attempt: David's suggestion - 'Missing'
    placename for all missing census years - 'Missing'

For all the below census enter zeroes . (May be 1 single command like for all empty cells enter zero? like fillna(value=0))
    POP100
    White_count
    Black_count
    Hispanic_count
    Age1524_WhiteM
    White_Males_All
    Age1524_WhiteF
    White_Females_All
    Age1524_BlackM
    Black_Males_All
    Age1524_BlackF
    Black_Females_All
    Age1524_HispanicM
    Hispanic_Males_All
    Age1524_HispanicF
    Hispanic_Females_All
    Pct_WYM
    Pct_WYF
"""


def fill_empty_census(cen_df):
    """
    Use placename = 'NA' for the ORIs missing census in all the 3 years.

    1st attempt:
    placename for 1990 :- index-1
    placename for 2000/2010 :- index+1

    msng_ORIs = ['MI63315','LA01700','NM00903','TN06400','HI00200','TX15208','WI06815','MA00403','SC04215','NY00659','TN05402','NJ00266']
    cen_df.loc[cen_df['ORI'].isin(msng_ORIs), 'placename'] = 'NA'

    for row in cen_df.itertuples():
        if pd.isnull(row.placename):
            if row.YEAR == 1990:
                # Have null checks for future if needed
                cen_df.at[row.Index, 'placename'] = cen_df.iloc[row.Index - 1].placename
            else:
                cen_df.at[row.Index, 'placename'] = cen_df.iloc[row.Index + 1].placename
    """

    cen_df = cen_df.fillna({'placename': 'Missing'})
    cen_df.fillna(0, inplace=True)

    return cen_df


ini_cens_df = pd.read_csv(
    '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/census/Census_Updated_Glevels_From_Crime.csv')
#
census_df = fill_empty_census(ini_cens_df)
census_df.to_csv(
    '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/census/Census_Updated_Glevels_From_Crime_Missing_Census_Filled.csv',
    index=False)

