import pandas as pd

final_rates = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/merge_files/Census_Crime_BEA_Spatial_Officers_Arrests_Incarceration.csv')


def calc_percent():
    race_cols_df = final_rates[['White_count', 'Black_count', 'Hispanic_count', 'Age1524_WhiteM', 'White_Males_All', 'Age1524_WhiteF',
                                'White_Females_All','Age1524_BlackM', 'Black_Males_All', 'Age1524_BlackF', 'Black_Females_All', 'Age1524_HispanicM',
                                'Hispanic_Males_All', 'Age1524_HispanicF', 'Hispanic_Females_All']]

    race_cols = list(race_cols_df)

    for race_col in race_cols:

        final_rates[f'{race_col}_cen_pop_pct'] = final_rates[race_col]/final_rates['POP100']*100
        final_rates[f'{race_col}_crime_pop'] = final_rates['population']*(final_rates[f'{race_col}_cen_pop_pct']/100)


calc_percent()

final_rates.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/merge_files/Census_Crime_BEA_Spatial_Officers_Arrests_Incarceration_Race_Counts.csv', index=False)