import pandas as pd


def get_month_last_reported():
    initial_core = pd.read_csv('C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/pre-analysis/initial_core.csv')

    ini_crime = pd.read_csv('C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/crime/Crime_1990_2015.csv')
    ini_crime_req = ini_crime.loc[:, ['ori_code', 'year', 'months_reported']]

    initial_core_mnths_rep = pd.merge(initial_core, ini_crime_req, left_on=['ORI', 'YEAR'], right_on=['ori_code', 'year'], how='left')

    initial_core_mnths_rep_dec_rep = initial_core_mnths_rep[(initial_core_mnths_rep.months_reported == "Dec last reported") |
                                                            (initial_core_mnths_rep.months_reported == "December is the last month reported")]
    initial_core_mnths_rep_dec_rep.drop(['ori_code', 'year'], inplace=True, axis=1)

    initial_core_mnths_rep_dec_rep.to_csv('C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/pre-analysis/ini_core_dec_last_rep.csv', index=False)


# get_month_last_reported()


def check_93_data():
    dec_df = pd.read_csv('C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/pre-analysis/ini_core_dec_last_rep.csv')
    print(dec_df.groupby('YEAR').aggregate({'robbery': 'sum', 'aggravated_assault': 'sum'}))

    # get df only for 1993
    dec_df_93 = dec_df.query('YEAR == 1993')
    dec_df_93.to_csv('C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/pre-analysis/ini_core_dec_last_rep_93.csv', index=False)

check_93_data()