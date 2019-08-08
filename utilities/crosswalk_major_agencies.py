import pandas as pd

crswlk_df = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/crosswalk/crosswalk_improved_2006.csv')

########## TO-DO:  Use UPOPCOV ##########
# Get the records where UPOPCOV != 99999999 or != 0
crswlk_df = crswlk_df[crswlk_df.UPOPCOV != 9999999]
crswlk_df = crswlk_df[crswlk_df.UPOPCOV != 0]

# Drop the records with blank ORIs or blank UPOPCOV
crswlk_df.dropna(subset=['ORI', 'UPOPCOV'], inplace=True)

#### TO-DO: Remove the ones with 0 UPOCOV
# Get only those crswlk file records whose cgovtype is 1,2,3
crswlk_123 = crswlk_df.loc[crswlk_df['CGOVTYPE'].isin([1, 2, 3])]

"""
    Sort by state and place fips and then by population(descending) - to identify major agencies. 
    Keep the record with highest population - THESE SHOULD BE UNIQUE
"""
crswlk_123.sort_values(by=['fips_state', 'fips_place', 'UPOPCOV'], ascending=[True, True, False], inplace=True)

# Drop duplicates so that only the highest population record is retained for a given agency.
crswlk_major = crswlk_123.drop_duplicates(subset=['fips_state', 'fips_place'])
crswlk_major.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/crosswalk/crosswalk_major_agencies.csv',index=False)