import pandas as pd

pd.options.display.float_format = '{:20,.4f}'.format
pd.set_option('display.max_columns', 100)
pd.set_option('display.max_colwidth', 500)
pd.set_option('display.width', 5000)


def get_ini_core_counts(initial_core_df):
    initial_core_counts = initial_core_df.loc[:, ['ORI', 'AGENCY', 'YEAR', 'POP100', 'White_count', 'Black_count',
                                               'Hispanic_count','Pct_WYM', 'Pct_WYF','total_count_county', 'population',
                                               'murder', 'rape', 'robbery', 'aggravated_assault',
                                               'simple_assault', 'burglary', 'larceny', 'auto_theft',
                                               'total_main_crime', 'violent_crime', 'property_crime',
                                               'murder_tot_arrests', 'murder_tot_black', 'murder_tot_white',
                                               'rape_tot_arrests', 'rape_tot_black', 'rape_tot_white',
                                               'robbery_tot_arrests', 'robbery_tot_black', 'robbery_tot_white',
                                               'agg_assault_tot_arrests', 'agg_assault_tot_white', 'agg_assault_tot_black',
                                               'larceny_theft_arrests_tot', 'larceny_theft_arrests_black','larceny_theft_arrests_white',
                                               'burglary_tot_arrests', 'burglary_tot_black', 'burglary_tot_white',
                                               'mtr_veh_theft_tot_arrests', 'mtr_veh_theft_tot_black','mtr_veh_theft_tot_white',
                                               'violent_arrests', 'property_arrests', 'total_main_arrests',
                                               'sale_drug_total_tot_arrests', 'sale_drug_total_tot_black','sale_drug_total_tot_white',
                                               'drug_total_arrests', 'drug_arrests_black', 'drug_arrests_white',
                                               'poss_drug_total_tot_arrests', 'poss_drug_total_tot_black','poss_drug_total_tot_white',
                                               'disorder_arrests_tot_index','disorder_arrests_black_index', 'disorder_arrests_white_index',
                                               'total_officers','prison_occupancy_count','jail_occupancy_count', 'pci_white',
                                               'pci_black','emp_total','emp_total_white', 'emp_total_black']]

    initial_core_counts.to_csv('C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/analysis/initial_core_counts.csv', index=False)

    # get the records with atleast 1 negative value in any one column
    initial_core_counts_neg = initial_core_counts.loc[(initial_core_counts[['murder', 'rape', 'robbery', 'aggravated_assault',
                                                                            'simple_assault', 'burglary','larceny', 'auto_theft',
                                                                            'murder_tot_arrests', 'murder_tot_black', 'murder_tot_white',
                                                                            'rape_tot_arrests', 'rape_tot_black', 'rape_tot_white',
                                                                            'robbery_tot_arrests', 'robbery_tot_black', 'robbery_tot_white',
                                                                            'agg_assault_tot_arrests', 'agg_assault_tot_white', 'agg_assault_tot_black',
                                                                            'larceny_theft_arrests_tot', 'larceny_theft_arrests_black', 'larceny_theft_arrests_white',
                                                                            'burglary_tot_arrests', 'burglary_tot_black', 'burglary_tot_white',
                                                                            'mtr_veh_theft_tot_arrests', 'mtr_veh_theft_tot_black', 'mtr_veh_theft_tot_white',
                                                                            'sale_drug_total_tot_arrests', 'sale_drug_total_tot_black', 'sale_drug_total_tot_white',
                                                                            'drug_total_arrests', 'drug_arrests_black', 'drug_arrests_white',
                                                                            'poss_drug_total_tot_arrests', 'poss_drug_total_tot_black', 'poss_drug_total_tot_white',
                                                                            'disorder_arrests_tot_index', 'disorder_arrests_black_index', 'disorder_arrests_white_index',
                                                                            'total_officers', 'prison_occupancy_count', 'jail_occupancy_count']] < 0).any(axis=1)]
    initial_core_counts_neg.to_csv('C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/analysis/'
                                  'initial_core_counts_neg.csv', index=False)

    # get the df without the negative value records
    initial_core_counts_pos = initial_core_counts.merge(initial_core_counts_neg, how='left', indicator=True)
    initial_core_counts_pos = initial_core_counts_pos[initial_core_counts_pos['_merge'] == 'left_only']

    initial_core_counts_pos.drop(['_merge'], inplace=True, axis=1)

    initial_core_counts_pos.to_csv('C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/analysis/'
                                  'initial_core_counts_pos.csv',  index=False)


def get_ini_core_counts_neg(initial_core_counts):
    initial_core_counts_neg = initial_core_counts[(initial_core_counts['murder'] < 0) | (initial_core_counts['rape'] < 0)
                                                | (initial_core_counts['robbery'] < 0) | (initial_core_counts['aggravated_assault'] < 0)
                                                | (initial_core_counts['simple_assault'] < 0) | (initial_core_counts['burglary'] < 0)
                                                | (initial_core_counts['larceny'] < 0) | (initial_core_counts['auto_theft'] < 0)
                                                | (initial_core_counts['murder_tot_arrests'] < 0) | (initial_core_counts['murder_tot_black'] < 0) | (initial_core_counts['murder_tot_white'] < 0)
                                                | (initial_core_counts['rape_tot_arrests'] < 0) | (initial_core_counts['rape_tot_black'] < 0) | (initial_core_counts['rape_tot_white'] < 0)
                                                | (initial_core_counts['robbery_tot_arrests'] < 0) | (initial_core_counts['robbery_tot_black'] < 0) | (initial_core_counts['robbery_tot_white'] < 0)
                                                | (initial_core_counts['agg_assault_tot_arrests'] < 0) | (initial_core_counts['agg_assault_tot_white'] < 0) | (initial_core_counts['agg_assault_tot_black'] < 0)
                                                | (initial_core_counts['larceny_theft_arrests_tot'] < 0) | (initial_core_counts['larceny_theft_arrests_black'] < 0) | (initial_core_counts['larceny_theft_arrests_white'] < 0)
                                                | (initial_core_counts['burglary_tot_arrests'] < 0) | (initial_core_counts['burglary_tot_black'] < 0) | (initial_core_counts['burglary_tot_white'] < 0)
                                                | (initial_core_counts['mtr_veh_theft_tot_arrests'] < 0) | (initial_core_counts['mtr_veh_theft_tot_black'] < 0) | (initial_core_counts['mtr_veh_theft_tot_white'] < 0)
                                                | (initial_core_counts['sale_drug_total_tot_arrests'] < 0) | (initial_core_counts['sale_drug_total_tot_black'] < 0) | (initial_core_counts['sale_drug_total_tot_white'] < 0)
                                                | (initial_core_counts['drug_total_arrests'] < 0) | (initial_core_counts['drug_arrests_black'] < 0) | (initial_core_counts['drug_arrests_white'] < 0)
                                                | (initial_core_counts['poss_drug_total_tot_arrests'] < 0) | (initial_core_counts['poss_drug_total_tot_black'] < 0) | (initial_core_counts['poss_drug_total_tot_white'] < 0)
                                                | (initial_core_counts['disorder_arrests_tot_index'] < 0) | (initial_core_counts['disorder_arrests_black_index'] < 0) | (initial_core_counts['disorder_arrests_white_index'] < 0)
                                                | (initial_core_counts['total_officers'] < 0) | (initial_core_counts['prison_occupancy_count'] < 0) | (initial_core_counts['jail_occupancy_count'] < 0)]


    initial_core_counts_neg.to_csv('C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/analysis/'
                                  'initial_core_counts_neg.csv', index=False)


def get_ini_core_rates(initial_core_df):
    initial_core_rates = initial_core_df.loc[:, ['ORI', 'AGENCY', 'YEAR', 'POP100', 'White_count', 'Black_count',
                                                 'Hispanic_count','Pct_WYM', 'Pct_WYF','total_count_county', 'population',
                                                 'murder_rate', 'rape_rate', 'robbery_rate', 'aggravated_assault_rate',
                                                 'simple_assault_rate','burglary_rate','larceny_rate','auto_theft_rate',
                                                 'total_main_crime_rate','violent_crime_rate','property_crime_rate',
                                                 'murder_tot_arrests_rate','murder_tot_black_rate','murder_tot_white_rate',
                                                 'rape_tot_arrests_rate','rape_tot_black_rate','rape_tot_white_rate',
                                                 'robbery_tot_arrests_rate','robbery_tot_black_rate','robbery_tot_white_rate',
                                                 'agg_assault_tot_arrests_rate','agg_assault_tot_white_rate','agg_assault_tot_black_rate',
                                                 'larceny_theft_arrests_tot_rate','larceny_theft_arrests_black_rate','larceny_theft_arrests_white_rate',
                                                 'burglary_tot_arrests_rate','burglary_tot_black_rate','burglary_tot_white_rate',
                                                 'mtr_veh_theft_tot_arrests_rate','mtr_veh_theft_tot_black_rate','mtr_veh_theft_tot_white_rate',
                                                 'violent_arrests_rates','property_arrests_rates','total_main_arrests_rates',
                                                 'sale_drug_total_tot_arrests_rate','sale_drug_total_tot_black_rate','sale_drug_total_tot_white_rate',
                                                 'drug_total_arrests_rate','drug_arrests_black_rate','drug_arrests_white_rate',
                                                 'poss_drug_total_tot_arrests_rate','poss_drug_total_tot_black_rate','poss_drug_total_tot_white_rate',
                                                 'disorder_arrests_tot_index_rate','disorder_arrests_black_index_rate','disorder_arrests_white_index_rate',
                                                 'total_officers_rate','prison_occupancy_count','jail_occupancy_count', 'pci_white',
                                                 'pci_black','emp_total','emp_total_white', 'emp_total_black'
                                                 ]]

    initial_core_rates.to_csv('C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/analysis/initial_core_rates.csv', index=False)

    # get the records with atleast 1 negative value in any one column
    initial_core_rates_neg = initial_core_rates.loc[(initial_core_rates[['murder_rate', 'rape_rate', 'robbery_rate', 'aggravated_assault_rate',
                              'simple_assault_rate', 'burglary_rate', 'larceny_rate', 'auto_theft_rate',
                              'murder_tot_arrests_rate', 'murder_tot_black_rate', 'murder_tot_white_rate',
                              'rape_tot_arrests_rate', 'rape_tot_black_rate', 'rape_tot_white_rate',
                              'robbery_tot_arrests_rate', 'robbery_tot_black_rate', 'robbery_tot_white_rate',
                              'agg_assault_tot_arrests_rate', 'agg_assault_tot_white_rate', 'agg_assault_tot_black_rate',
                              'larceny_theft_arrests_tot_rate', 'larceny_theft_arrests_black_rate', 'larceny_theft_arrests_white_rate',
                              'burglary_tot_arrests_rate', 'burglary_tot_black_rate', 'burglary_tot_white_rate',
                              'mtr_veh_theft_tot_arrests_rate', 'mtr_veh_theft_tot_black_rate', 'mtr_veh_theft_tot_white_rate',
                              'sale_drug_total_tot_arrests_rate', 'sale_drug_total_tot_black_rate', 'sale_drug_total_tot_white_rate',
                              'drug_total_arrests_rate', 'drug_arrests_black_rate', 'drug_arrests_white_rate',
                              'poss_drug_total_tot_arrests_rate', 'poss_drug_total_tot_black_rate', 'poss_drug_total_tot_white_rate',
                              'disorder_arrests_tot_index_rate', 'disorder_arrests_black_index_rate','disorder_arrests_white_index_rate',
                              'total_officers_rate', 'prison_occupancy_count', 'jail_occupancy_count']] < 0).any(axis=1)]

    initial_core_rates_neg.to_csv('C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/analysis/'
                                   'initial_core_rates_neg.csv', index=False)

    # get the df without the negative value records
    initial_core_rates_pos = initial_core_rates.merge(initial_core_rates_neg, how='left', indicator=True)
    initial_core_rates_pos = initial_core_rates_pos[initial_core_rates_pos['_merge'] == 'left_only']

    # drop _merge column
    initial_core_rates_pos.drop(['_merge'], inplace=True, axis=1)

    initial_core_rates_pos.to_csv('C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/analysis/'
                                   'initial_core_rates_pos.csv', index=False)


def get_ini_core_rates_neg(initial_core_rates):
    initial_core_rates_neg = initial_core_rates[(initial_core_rates['murder_rate'] < 0) | (initial_core_rates['rape_rate'] < 0)
                                                | (initial_core_rates['robbery_rate'] < 0) | (initial_core_rates['aggravated_assault_rate'] < 0)
                                                | (initial_core_rates['simple_assault_rate'] < 0) | (initial_core_rates['burglary_rate'] < 0)
                                                | (initial_core_rates['larceny_rate'] < 0) | (initial_core_rates['auto_theft_rate'] < 0)
                                                | (initial_core_rates['murder_tot_arrests_rate'] < 0) | (initial_core_rates['murder_tot_black_rate'] < 0) | (initial_core_rates['murder_tot_white_rate'] < 0)
                                                | (initial_core_rates['rape_tot_arrests_rate'] < 0) | (initial_core_rates['rape_tot_black_rate'] < 0) | (initial_core_rates['rape_tot_white_rate'] < 0)
                                                | (initial_core_rates['robbery_tot_arrests_rate'] < 0) | (initial_core_rates['robbery_tot_black_rate'] < 0) | (initial_core_rates['robbery_tot_white_rate'] < 0)
                                                | (initial_core_rates['agg_assault_tot_arrests_rate'] < 0) | (initial_core_rates['agg_assault_tot_white_rate'] < 0) | (initial_core_rates['agg_assault_tot_black_rate'] < 0)
                                                | (initial_core_rates['larceny_theft_arrests_tot_rate'] < 0) | (initial_core_rates['larceny_theft_arrests_black_rate'] < 0) | (initial_core_rates['larceny_theft_arrests_white_rate'] < 0)
                                                | (initial_core_rates['burglary_tot_arrests_rate'] < 0) | (initial_core_rates['burglary_tot_black_rate'] < 0) | (initial_core_rates['burglary_tot_white_rate'] < 0)
                                                | (initial_core_rates['mtr_veh_theft_tot_arrests_rate'] < 0) | (initial_core_rates['mtr_veh_theft_tot_black_rate'] < 0) | (initial_core_rates['mtr_veh_theft_tot_white_rate'] < 0)
                                                | (initial_core_rates['sale_drug_total_tot_arrests_rate'] < 0) | (initial_core_rates['sale_drug_total_tot_black_rate'] < 0) | (initial_core_rates['sale_drug_total_tot_white_rate'] < 0)
                                                | (initial_core_rates['drug_total_arrests_rate'] < 0) | (initial_core_rates['drug_arrests_black_rate'] < 0) | (initial_core_rates['drug_arrests_white_rate'] < 0)
                                                | (initial_core_rates['poss_drug_total_tot_arrests_rate'] < 0) | (initial_core_rates['poss_drug_total_tot_black_rate'] < 0) | (initial_core_rates['poss_drug_total_tot_white_rate'] < 0)
                                                | (initial_core_rates['disorder_arrests_tot_index_rate'] < 0) | (initial_core_rates['disorder_arrests_black_index_rate'] < 0) | (initial_core_rates['disorder_arrests_white_index_rate'] < 0)
                                                | (initial_core_rates['total_officers_rate'] < 0) | (initial_core_rates['prison_occupancy_count'] < 0) | (initial_core_rates['jail_occupancy_count'] < 0)]


    initial_core_rates_neg.to_csv('C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/analysis/'
                                  'initial_core_rates_neg.csv', index=False)


initial_core_df = pd.read_csv('C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/analysis/initial_core.csv')

get_ini_core_counts(initial_core_df)
get_ini_core_rates(initial_core_df)

