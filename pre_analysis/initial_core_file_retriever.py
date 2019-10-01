import pandas as pd


# getting only the main columns for initial trend lines
def get_top_level_vars(fnl_main):

    initial_core_df = fnl_main.loc[:, ['ORI', 'AGENCY', 'placename', 'Govt_level', 'place_fips', 'STATEFP', 'CNTY',
                                       'YEAR', 'crime_year', 'POP100','White_count', 'Black_count', 'Hispanic_count',
                                       'Age1524_WhiteM','White_Males_All', 'Age1524_WhiteF', 'White_Females_All',
                                       'Age1524_BlackM','Black_Males_All', 'Age1524_BlackF','Black_Females_All',
                                       'Hispanic_Males_All','Age1524_HispanicM', 'Age1524_HispanicF',
                                       'Hispanic_Females_All', 'Pct_WYM','Pct_WYF', 'total_count_county',
                                       'population', 'murder', 'rape', 'robbery', 'aggravated_assault',
                                       'simple_assault', 'burglary', 'larceny', 'auto_theft', 'violent_crime',
                                       'property_crime','total_main_crime','murder_rate', 'rape_rate',
                                       'robbery_rate','aggravated_assault_rate','simple_assault_rate', 'property_arrests_rates',
                                       'burglary_rate', 'larceny_rate','auto_theft_rate','violent_crime_rate','total_crime_rate',
                                       'property_crime_rate','total_main_crime_rate',

                                       'murder_tot_arrests', 'murder_tot_black', 'murder_tot_white',
                                       'rape_tot_arrests', 'rape_tot_black','rape_tot_white',
                                       'robbery_tot_arrests','robbery_tot_black', 'robbery_tot_white',
                                       'agg_assault_tot_arrests', 'agg_assault_tot_white', 'agg_assault_tot_black',
                                       'larceny_theft_arrests_tot', 'larceny_theft_arrests_black', 'larceny_theft_arrests_white',
                                       'burglary_tot_arrests', 'burglary_tot_black', 'burglary_tot_white',
                                       'mtr_veh_theft_tot_arrests', 'mtr_veh_theft_tot_black', 'mtr_veh_theft_tot_white',
                                       'violent_arrests','property_arrests','total_main_arrests',
                                       'sale_drug_total_tot_arrests', 'sale_drug_total_tot_black','sale_drug_total_tot_white',
                                       'drug_total_arrests', 'drug_arrests_black', 'drug_arrests_white',
                                       'poss_drug_total_tot_arrests','poss_drug_total_tot_black','poss_drug_total_tot_white',
                                       'disorder_arrests_tot_index','disorder_arrests_black_index', 'disorder_arrests_white_index',

                                       'murder_tot_arrests_rate', 'murder_tot_black_rate', 'murder_tot_white_rate',
                                       'rape_tot_arrests_rate', 'rape_tot_black_rate', 'rape_tot_white_rate',
                                       'robbery_tot_arrests_rate', 'robbery_tot_black_rate', 'robbery_tot_white_rate',
                                       'agg_assault_tot_arrests_rate', 'agg_assault_tot_white_rate', 'agg_assault_tot_black_rate',
                                       'larceny_theft_arrests_tot_rate', 'larceny_theft_arrests_black_rate', 'larceny_theft_arrests_white_rate',
                                       'burglary_tot_arrests_rate', 'burglary_tot_black_rate', 'burglary_tot_white_rate',
                                       'mtr_veh_theft_tot_arrests_rate', 'mtr_veh_theft_tot_black_rate', 'mtr_veh_theft_tot_white_rate',
                                       'violent_arrests_rates', 'property_arrests_rates', 'total_main_arrests_rates',
                                       'sale_drug_total_tot_arrests_rate', 'sale_drug_total_tot_black_rate', 'sale_drug_total_tot_white_rate',
                                       'drug_total_arrests_rate', 'drug_arrests_black_rate', 'drug_arrests_white_rate',
                                       'poss_drug_total_tot_arrests_rate', 'poss_drug_total_tot_black_rate','poss_drug_total_tot_white_rate',
                                       'disorder_arrests_tot_index_rate', 'disorder_arrests_black_index_rate','disorder_arrests_white_index_rate',
                                       'prison_occupancy_count_rate', 'jail_occupancy_count_rate',

                                       'pci_total_pop','pci_white', 'pci_black', 'pci_hisp', 'emp_total',
                                       'emp_total_male','emp_total_female','emp_total_male_white',
                                       'emp_total_female_white','emp_total_male_black', 'emp_total_female_black',
                                       'emp_total_male_hisp','emp_total_female_hisp', 'emp_total_white', 'emp_total_black',
                                       'emp_total_hisp', 'total_officers',
                                       'total_officers_rate', 'perc_felonies', 'perc_misdemeanors','prison_occupancy_count',
                                       'jail_occupancy_count', 'ncrp_incarc_rep_code']]



    initial_core_df.to_csv('C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/pre-analysis/initial_core.csv', index=False)


get_top_level_vars(pd.read_csv('C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/pre-analysis/final_main_ncrp_incarc_rep_code_enhanced.csv'))