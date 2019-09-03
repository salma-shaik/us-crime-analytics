import pandas as pd
import numpy as np


def replicate_fixed_cols(df, cols_list, op_fl_path, dt_type):
    # get only the reqd cols list =
    df_req = df[cols_list]

    """
    Set the number of repetitions for each row depending on the YEAR column
    """
    conditions = [
        df_req['YEAR'] == 2015,
        df_req['YEAR'] == 2010,
        df_req['YEAR'] == 2000,
        df_req['YEAR'] == 1990,
    ]

    outputs = [
        5, 10, 10, 1
    ]

    # define year_codes variable which will be generated based on the conditions and required outputs
    year_codes = np.select(conditions, outputs)

    # create new 'reps' column(= length of df) with year_codes values that would be assigned based on number of reps
    # required for each row for a given year (based on the conditions and output setup above)
    df_req.loc[:, 'reps'] = pd.Series(year_codes)


    """
    Replicate each row based on the corresponding value from reps column
    """
    df_req = df.loc[df.index.repeat(df.reps)].reset_index(drop=True)

    # Drop reps and YEAR columns
    df_req.drop(['reps', 'YEAR'], axis=1, inplace=True)

    df_req.to_csv(f'{op_fl_path}/{dt_type}_Fixed_Cols_Replicated.csv', index=False)

"""
###### nat_cen_fixed_yr --> final rows should be 385606(14831)
seems right coz in each year has 14542 rows. so 5*14542  + 20*14542  + 14542  = 378092 (72710 + 290840 + 14542) i.e 5 replications for 2015 row, 10 replications each for every 2000
    and 2010 row and 1 replication of each 1990 row.
"""