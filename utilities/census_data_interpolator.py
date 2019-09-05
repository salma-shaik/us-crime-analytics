import pandas as pd

from utilities import fixed_columns_replicator as fcr
from utilities import year_replicator as yr

from utilities import year_generator as yg
from utilities import variables_interpolator as vi
from utilities import census_interpolated_files_consolidator as cen_int_cons


# replicate fixed columns into required number of times depending on year
# 2015 - 5; 2010, 2000 - 10; 1990 - 1

fcr.replicate_fixed_cols(df = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/us_crime_analytics/data/census/Census_90-15_Final_Sorted.csv'),
                         cols_list=['ORI', 'AGENCY', 'placename', 'Govt_level', 'place_fips', 'STATEFP', 'CNTY', 'YEAR'],
                         op_fl_path='/Users/salma/Studies/Research/Criminal_Justice/us_crime_analytics/data/census',
                         dt_type='Census')


# replicate year set from 90-15 unique ORI number of times
yr.replicate_years_90_15(df = pd.read_csv(
                                '/Users/salma/Studies/Research/Criminal_Justice/us_crime_analytics/data/census/Census_Fixed_Cols_Replicated.csv'),
                         repl_times = 14542,
                         dt_type = 'Census',
                         op_fl_path='/Users/salma/Studies/Research/Criminal_Justice/us_crime_analytics/data/census')


# generate years between existing decennial years
'''
yg.generate_years(df=pd.read_csv(
                                '/Users/salma/Studies/Research/Criminal_Justice/us_crime_analytics/data/census/Census_Fixed_Cols_Replicated.csv'),
                         dt_type = 'Census',
                         op_fl_path='/Users/salma/Studies/Research/Criminal_Justice/us_crime_analytics/data/census')
'''

# interpolate variable values in between decennial years
vi.interpolate_vars(df=pd.read_csv('C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/economic/new_eco_cen/Census_90-15_Final_Sorted.csv'),
                    dt_type='Census_Pop_Vars',
                    op_fl_path='/Users/salma/Studies/Research/Criminal_Justice/us_crime_analytics/data/census')


# Merge the interpolateed files together by ORI and YEAR

''''
############## TO-DO ####################
do the below
'''
cen_int_cons.replace_negative_values()
cen_int_cons.write_final_intpltd_file()
# write_final_intpltd_file()

