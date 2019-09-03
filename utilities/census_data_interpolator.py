import pandas as pd

from utilities import fixed_columns_replicator as fcr
from utilities import year_replicator as yr

# replicate fixed columns into required number of times depending on year
# 2015 - 5; 2010, 2000 - 10; 1990 - 1

fcr.replicate_fixed_cols(df = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/us_crime_analytics/data/census/Census_90-15_Final_Sorted.csv'),
                         cols_list=['ORI', 'AGENCY', 'placename', 'Govt_level', 'place_fips', 'STATEFP', 'CNTY', 'YEAR'],
                         op_fl_path='/Users/salma/Studies/Research/Criminal_Justice/us_crime_analytics/data/census',
                         dt_type='Census')


# replicate year set from 90-15 unique ORI number of times
yr.genereate_years_90_15(df = pd.read_csv(
                                '/Users/salma/Studies/Research/Criminal_Justice/us_crime_analytics/data/census/Census_Fixed_Cols_Replicated.csv'),
                         repl_times = 14542,
                         dt_type = 'Census',
                         op_fl_path='/Users/salma/Studies/Research/Criminal_Justice/us_crime_analytics/data/census')
