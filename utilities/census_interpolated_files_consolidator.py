import pandas as pd

from datetime import datetime
import numpy as np

pd.options.mode.chained_assignment = None

"""
Subset the nat_cen_all_sorted df to get the population variables' columns
"""

def interpolate_census_vars(fl_path):
    print("########## Start: ", datetime.now().time())

    nat_cen_all = pd.read_csv(fl_path)

    # Get the required columns from the national all census file.
    pop_vars = nat_cen_all[['ORI', 'YEAR', 'POP100', 'White_count', 'Black_count', 'Hispanic_count', 'Age1524_WhiteM', 'White_Males_All', 'Age1524_WhiteF',
                            'White_Females_All', 'Age1524_BlackM', 'Black_Males_All', 'Age1524_BlackF', 'Black_Females_All','Hispanic_Males_All',
                            'Age1524_HispanicM', 'Age1524_HispanicF', 'Hispanic_Females_All', 'Pct_WYM', 'Pct_WYF']]

    # Create an empty df to append the original rows and empty rows for every iteration of the original nat_cen_all df.
    pop_var_int = pd.DataFrame(columns = pop_vars.columns)

    for row in pop_vars.itertuples():
        # ????? ###
        pop_var_int = pop_var_int.append(pd.Series(row[1:], index=pop_vars.columns), ignore_index=True)
        # append 4 rows after 2015 for 14, 13, 12, 11
        if row.YEAR == 2015:
            for i in range(4):
                pop_var_int = pop_var_int.append(pd.Series(), ignore_index=True)
        # append 9 empty rows if the year is != 1990 and 2015 coz we are interpolating till 1990.
        if row.YEAR != 1990 and row.YEAR != 2015:
            for i in range(9):
                pop_var_int = pop_var_int.append(pd.Series(), ignore_index=True)

    # Drop the YEAR column
    # pop_var_int = pop_var_int.drop(['YEAR'], axis=1)


    # ffill ORIs so that they are copied for in between decennial years
    pop_var_int['ORI'] = pop_var_int['ORI'].ffill()

    # Interpolate. This fills all the NaN rows between 2 given years that were added above.
    pop_var_int = pop_var_int.interpolate(method='linear', axis=0)

    print("########## End: ", datetime.now().time()) # --> Process between line 11-line 38 takes around 2 hrs 3 minutes
    return pop_var_int


# call interpolate_census_vars() which returns a df with interpolated values of all variables
#interpolated_df = interpolate_census_vars('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/census/Census_90-15_Final_Sorted.csv')
# Write the df with interpolated values for all population variables to a csv
#interpolated_df.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/census/Census_Pop_Vars_Interpolated.csv', index=False)


"""
    After interpolation there are negative values in some rows.Because, some ORIs missing census data for 2010(Ex: AL05810). 
    So extrapolating from 2010 - 2015 yields negative results. In order to overcome this, after interpolation, replacing all negative values with 0
"""
def replace_negative_values():
    int_df = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/interpolated_files/Census_Vars_Interpolated.csv')
    # Accessing the private _get_numeric_data() of the dataframe. Private method, so changes reflected in the original df
    int_df_num = int_df._get_numeric_data()
    int_df_num[int_df_num < 0] = 0
    int_df.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/census/Census_Pop_Vars_Interpolated_Negative_Extrapolated_Pop_Zeroed.csv', index=False)


# replace_negative_values()


def write_final_intpltd_file():
    # Get the fixed columns and years file into a df
    fixed_rows_yr = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/census/Census_Fixed_Cols_Years_Replicated.csv')
    # Get the pop vars interpolated file into a df
    interpolated_df = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/census/Census_Pop_Vars_Interpolated_Negative_Extrapolated_Pop_Zeroed.csv')

    interpolated_df.drop(['YEAR'], axis=1, inplace=True)

    ############ To-Do: See if you can merge based on ORI instead ################
    # concatenate fixed columns, year and population variables together vertically
    # vars interpoalted file will have year column as a result of resampling. so can merge on ORI and year now
    #final_int_df = pd.concat([fixed_rows_yr, interpolated_df], axis=1)
    final_int_df = pd.merge(fixed_rows_yr, interpolated_df, on=['ORI', 'YEAR'])

    # Little tricky coz interpolated df doesn't have missing years filled in similar to the years replicated df
    # final_int_df = fixed_rows_yr.merge(interpolated_df, on=['ORI', 'YEAR'])

    # to add and update missing columns corresponding to the years that the census data is missing in
    final_int_df['missing_census_90'] = np.where(
        ((final_int_df['placename'] == 'Missing') & (final_int_df['YEAR'] == 1990)), True, False)
    final_int_df['missing_census_00'] = np.where(
        ((final_int_df['placename'] == 'Missing') & (final_int_df['YEAR'] == 2000)), True, False)
    final_int_df['missing_census_10'] = np.where(
        ((final_int_df['placename'] == 'Missing') & (final_int_df['YEAR'] == 2010)), True, False)


    # Write the final interpolated file to a csv
    final_int_df.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/census/Census_Interpolated.csv', index=False)


# write_final_intpltd_file()
