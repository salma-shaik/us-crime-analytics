import pandas as pd

def consolidate_all_census_files():

    # Finally, read all the years' census files to append together and form a consolidated census file with updated govt level, ORI from the 1990 final main file
    # nat_cen_90_df = pd.read_csv(
    #     '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/merge_files/census_crime/Census_1990_Crime_Merge_Right.csv')

    nat_cen_90_df = pd.read_csv(
        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/census/cen_90/census_cities_1990/new_census_variables/cen_90_ini_cnty_city_new_twnshp_glevels.csv')
    nat_cen_00_df = pd.read_csv(
        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/census/cen_00/Census_2000_Crime_Merge_Right.csv')
    nat_cen_10_df = pd.read_csv(
        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/census/cen_10/Census_2010_Crime_Merge_Right.csv')

    # Append all the census files together
    nat_cen_all = nat_cen_10_df.append([nat_cen_00_df, nat_cen_90_df], sort=False)

    nat_cen_all.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/merge_files/census_crime/Census_Crime_All_Right.csv', index=False)

    """
        Sort the df by 'ORI' and 'YEAR' to get the 3 occurences of each ORI together and then sort by YEAR(10,00,90)
    """
    nat_cen_all_sorted = nat_cen_all.sort_values(by=['ORI', 'YEAR'], ascending=[True, False])

    # ############## Check this out
    # Reset index after sorting so that it is in ascending order again and not trying to maintain the original index
    nat_cen_all_sorted = nat_cen_all_sorted.reset_index(drop=True)

    """
        Write the above sorted df to a csv for future use and reference
    """
    nat_cen_all_sorted.to_csv(
        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/census/Census_Updated_Glevels_From_Crime.csv',
        index=False)


consolidate_all_census_files()