import pandas as pd


def calculate_incarc_counts(df):
    df['prison_occupancy_count'] = (df['perc_felonies'] * df['total_prison_pop']) / 100
    df['jail_occupancy_count'] = (df['perc_misdemeanors'] * df['jail_interp']) / 100

    return df
