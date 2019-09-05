import pandas as pd

'''
We need to create an YEAR column with all the years between 2015 to 2010, 2010 to 2000 and then between 2000 and 1990
'''


def replicate_years_90_15(df, repl_times, dt_type, op_fl_path):
    # Create a dataframe with 2015-1990 years and replicate it as many times required to fill up the existing dataframe length
    years = pd.DataFrame(
        {'YEAR': [2015, 2014, 2013, 2012, 2011, 2010, 2009, 2008, 2007, 2006, 2005, 2004, 2003, 2002, 2001,
                  2000, 1999, 1998, 1997, 1996, 1995, 1994, 1993, 1992, 1991, 1990]})


    # replicate the above year df 'repl_times'. stack the df along axis = 0 i.e stack repl_times
    years_rep = pd.concat([years]*repl_times, ignore_index=True) # 14542 records(ORIs) in each normalized census files. So all these years for each of the ORI. Total 378092

    # append the year column to df
    df_yr = pd.concat([df, years_rep], axis=1, sort=False)

    #print(df_yr)

    df_yr.to_csv(f'{op_fl_path}/{dt_type}_Fixed_Cols_Years_Replicated.csv', index=False)