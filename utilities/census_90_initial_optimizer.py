import pandas as pd

"""
        # Clean up 1990 census file
 """
national_cens_90_df = pd.read_excel('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/cen_90/National_Census_1990_All.xlsx')

# drop the duplicates based on state and place fips
national_cens_90_df_unique = national_cens_90_df.drop_duplicates(['STATEFP', 'place_fips'])

# add YEAR column with 1990 value at 5th position
national_cens_90_df_unique.insert(5, 'YEAR', 1990)

# Rename Hispan columns to Hispanic
national_cens_90_df_unique.rename({'Hispan_allcount': 'Hispanic_count', 'Hispan_Males_All': 'Hispanic_Males_All', 'Age1524_HispanM': 'Age1524_HispanicM', 'Age1524_HispanF': 'Age1524_HispanicF', 'Hispan_Females_All': 'Hispanic_Females_All'}, inplace=True, axis=1)

# drop 'other' columns
national_cens_90_df_unique.drop(['Other_count', 'Other_Males_All', 'Age1524_OtherM', 'Age1524_OtherF', 'Other_Females_All'], inplace=True, axis=1)

national_cens_90_df_unique.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/cen_90/National_Census_1990_unique.csv', index=False)
