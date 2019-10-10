import pandas as pd
import xlrd

pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 5000)


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


def get_93_data_for_dec_last_reported():
    dec_df = pd.read_csv('C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/pre-analysis/ini_core_dec_last_rep.csv')
    print(dec_df.groupby('YEAR').aggregate({'robbery': 'sum', 'aggravated_assault': 'sum'}))

    # get df only for 1993
    dec_df_93 = dec_df.query('YEAR == 1993')
    dec_df_93.to_csv('C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/pre-analysis/ini_core_dec_last_rep_93.csv', index=False)

# get_93_data_for_dec_last_reported()


def crime_counts_diffs_ucr_cr_clnd_90_01():
    cr_ucr = pd.read_csv('/Users/salma/Research/us-crime-analytics/data/Crime_National_UCR_offenses_1960_2015.csv',
                         encoding = "ISO-8859-1")
    print('cr_ucr: ', list(cr_ucr))
    # get only the req vars
    cr_ucr_req = cr_ucr.loc[:, ['ori_code', 'year', 'murder', 'rape', 'robbery', 'aggravated_assault', 'simple_assault']]

    # get data from 1990
    cr_ucr_req = cr_ucr_req.query('year >= 1990')

    # get the crime cleaned file with crime sums
    fnl_main = pd.read_excel('/Users/salma/Research/us-crime-analytics/data/tests/93_disc_test/Crime_Predictors_Cleaned.xlsx')
    fnl_main_req = fnl_main.loc[:, ['ori', 'agency', 'year', 'murder_sum', 'rape_sum', 'robbery_sum', 'agg_assault_sum',
                                'simple_assault_sum']]

    cr_ucr_fnl_main_merge = pd.merge(fnl_main_req, cr_ucr_req, left_on = ['ori', 'year'], right_on= ['ori_code', 'year'])

    cr_ucr_fnl_main_merge['robbery_diff'] = cr_ucr_fnl_main_merge['robbery_sum'] - cr_ucr_fnl_main_merge['robbery']
    cr_ucr_fnl_main_merge['murder_diff'] = cr_ucr_fnl_main_merge['murder_sum'] - cr_ucr_fnl_main_merge['murder']
    cr_ucr_fnl_main_merge['rape_diff'] = cr_ucr_fnl_main_merge['rape_sum'] - cr_ucr_fnl_main_merge['rape']
    cr_ucr_fnl_main_merge['agg_assault_diff'] = cr_ucr_fnl_main_merge['agg_assault_sum'] - cr_ucr_fnl_main_merge['aggravated_assault']
    cr_ucr_fnl_main_merge['simple_assault_diff'] = cr_ucr_fnl_main_merge['simple_assault_sum'] - cr_ucr_fnl_main_merge['simple_assault']

    cr_ucr_fnl_main_merge.to_csv('/Users/salma/Research/us-crime-analytics/data/tests/93_disc_test/fnl_main_cr_ucr_diff.csv', index=False)


crime_counts_diffs_ucr_cr_clnd_90_01()


def get_ucr_crime_counts_year():
    # get the counts of 'murder', 'rape', 'robbery', 'aggravated_assault', 'simple_assault' from the ucr file
    # to compare with the ucr numbers online
    cr_ucr = pd.read_csv('/Users/salma/Research/us-crime-analytics/data/Crime_National_UCR_offenses_1960_2015.csv',
                           encoding="ISO-8859-1")

    cr_ucr_req = cr_ucr.loc[:, ['ori_code', 'year', 'population_1', 'population_2', 'population_3', 'murder', 'manslaughter',
                                'rape', 'force_rape', 'attempt_rape', 'robbery', 'aggravated_assault', 'simple_assault']]

    cr_ucr_req['murder_manslaughter'] = cr_ucr_req[['murder', 'manslaughter']].sum(axis=1)
    cr_ucr_req['population'] = cr_ucr_req[['population_1', 'population_2', 'population_3']].sum(axis=1)

    cr_ucr_req_90a = cr_ucr_req.query('year >= 1990')

    # to get the number of records/ORIs reported in each year
    cr_ucr_req_cr_sums = cr_ucr_req_90a.groupby('year').aggregate({'population': 'sum', 'murder_manslaughter': 'sum',
                                                                   'rape': 'sum','robbery': 'sum','aggravated_assault': 'sum',
                                                                   'simple_assault': 'sum'}).reset_index()

    cr_ucr_req_cr_sums.to_csv('/Users/salma/Research/us-crime-analytics/data/tests/93_disc_test/cr_ucr_90_15_major_counts.csv',
                              index=False)


# get_ucr_crime_counts_year()