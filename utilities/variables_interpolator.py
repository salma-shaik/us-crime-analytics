import pandas as pd

pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 5000)


def interpolate_vars(df, dt_type, op_fl_path):
    """
    trying resampling method to get yearly frequency for every ORI
    since each ORI has data for dec years, re-sampling considers all the years in between as missing and fills with NaNs
    let's first convert year column to april 1 year i.e in the format 4/1/2010 etc.. whose dtype would be object
    """

    df.loc[:, 'YEAR'] = df['YEAR'].apply(lambda x: '4/1/' + str(x))

    # Next convert this date string to datetime format
    # df.loc[:, 'cen_dt_yr'] = pd.to_datetime(df.loc[:, 'YEAR'])
    df['cen_dt_yr'] = pd.to_datetime(df['YEAR'])

    # set the datetime as index
    df.index = df['cen_dt_yr']
    del df['cen_dt_yr']

    '''
    Since we want to interpolate for each ORI separately, we need to group our data by ‘ORI’ before we can use the
    resample() function with the option ‘A’ to resample the data to an annual/yearly frequency.
    '''
    df = df.groupby('ORI').resample('A').mean()

    df_int = df.interpolate()

    # creates multi-index with ORI and YEAR so resetting that and getting back ORI and cen_dt_yr as columns
    df_int.reset_index(inplace=True)

    # retrieve only year from cen_dt_yr and create a new YEAR column with those values
    df_int['YEAR'] = df_int['cen_dt_yr'].dt.year

    df_int.drop(['cen_dt_yr'], axis=1, inplace=True)
    # just to be sure sort by ORI and year
    df_int.sort_values(['ORI', 'YEAR'], ascending=[True, False], inplace=True)

    # write to a csv
    df_int.to_csv(f'{op_fl_path}/{dt_type}_Vars_Interpolated.csv', index=False)