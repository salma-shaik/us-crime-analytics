import pandas as pd
import numpy as np

"""
1. Subset the Census_Crime_All_Right_Sorted_Missing_Census_Filled df to get the fixed and YEAR columns
"""
nat_cen_all_sorted = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/census/Census_90-15_Final_Sorted.csv')
nat_cen_fixed_yr = nat_cen_all_sorted[['ORI', 'AGENCY', 'placename', 'Govt_level', 'place_fips', 'STATEFP', 'CNTY', 'YEAR']]

"""
Set the number of repetitions for each row depending on the YEAR column
"""
conditions = [
    nat_cen_fixed_yr['YEAR'] == 2015,
    nat_cen_fixed_yr['YEAR'] == 2010,
    nat_cen_fixed_yr['YEAR'] == 2000,
    nat_cen_fixed_yr['YEAR'] == 1990,
]

outputs = [
    5, 10, 10, 1
]

year_codes = np.select(conditions, outputs)

# new 'reps' column will be created and year_codes would be replicated required number of times to meet the length of nat_cen_fixed_yr
nat_cen_fixed_yr['reps'] = pd.Series(year_codes)

"""
Replicate each row based on the corresponding value from reps column
"""
nat_cen_fixed_yr = nat_cen_fixed_yr.loc[nat_cen_fixed_yr.index.repeat(nat_cen_fixed_yr.reps)].reset_index(drop=True)

# Drop reps and YEAR columns
nat_cen_fixed_yr = nat_cen_fixed_yr.drop(['reps', 'YEAR'], axis=1)

nat_cen_fixed_yr.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/census/Census_Fixed_Cols_Replicated.csv', index=False)

"""
###### nat_cen_fixed_yr --> final rows should be 385606(14831)
seems right coz in each year has 14542 rows. so 5*14542  + 20*14542  + 14542  = 378092 (72710 + 290840 + 14542) i.e 5 replications for 2015 row, 10 replications each for every 2000
    and 2010 row and 1 replication of each 1990 row.
"""