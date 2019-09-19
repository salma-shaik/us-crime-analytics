import pandas as pd
import numpy as np

pd.set_option('display.max_columns', 500)
pd.set_option('max_colwidth', 5000)


'''
create icspr yrs reported flag variables
    yr_count < 20 : 0
    20 <= yr_count <26 : 1
    yr_count = 26: 2 
'''
def create_icspr_flags(fnl_main_df):
    # read the incarc_files_metadata file
    icspr_meta_df = pd.read_excel('C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/ICPSR_37021/incarc_files_metadata.xlsx',
                                  sheet_name='prison_admissions_st_yrs')

    icspr_meta_df = icspr_meta_df.loc[:,['STATE', 'ncrp_incarc_yr_count']]

    # get the icspr_yr_count col into final main file
    final_df = pd.merge(fnl_main_df, icspr_meta_df, left_on='STATEFP', right_on='STATE', how='left')
    final_df['ncrp_incarc_rep_code'] = final_df.ncrp_incarc_yr_count.apply(lambda x: 0 if x < 20 else(2 if x == 26 else 1))

    final_df.to_csv('C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/analysis/final_main_ncrp_incarc_rep_code.csv', index=False)


def update_final_main_vars(main_df):
    main_df.drop(['violent_crime'], axis=1, inplace=True)

    main_df['violent_crime'] = main_df[['murder', 'rape', 'robbery', 'aggravated_assault']].sum(axis=1)
    main_df['total_main_crime'] = main_df[['violent_crime', 'property_crime']].sum(axis=1)
    main_df['total_main_crime_rate'] = main_df[['violent_crime_rate', 'property_crime_rate']].sum(axis=1)

    main_df['total_officers_rate'] = (main_df['total_officers'] / main_df['population']) * 1000

    main_df['violent_arrests'] = main_df[['murder_tot_arrests', 'agg_assault_tot_arrests','rape_tot_arrests',
                                          'robbery_tot_arrests']].sum(axis=1)
    main_df['property_arrests'] = main_df[['burglary_tot_arrests', 'larceny_theft_arrests_tot',
                                           'mtr_veh_theft_tot_arrests', 'arson_tot_arrests']].sum(axis=1)
    main_df['total_main_arrests'] = main_df[['murder_tot_arrests', 'agg_assault_tot_arrests','rape_tot_arrests',
                                          'robbery_tot_arrests', 'burglary_tot_arrests', 'larceny_theft_arrests_tot',
                                           'mtr_veh_theft_tot_arrests', 'arson_tot_arrests']].sum(axis=1)

    main_df['violent_arrests_rates'] = (main_df['violent_arrests']/main_df['population']) * 10000
    main_df['property_arrests_rates'] = (main_df['property_arrests'] / main_df['population']) * 10000
    main_df['total_main_arrests_rates'] = main_df[['violent_arrests_rates', 'property_arrests_rates']].sum(axis=1)

    main_df['emp_total_white'] = main_df[['emp_total_male_white', 'emp_total_female_white']].sum(axis=1)
    main_df['emp_total_black'] = main_df[['emp_total_male_black', 'emp_total_female_black']].sum(axis=1)
    main_df['emp_total_hisp'] = main_df[['emp_total_male_hisp', 'emp_total_female_hisp']].sum(axis=1)

    main_df['drug_total_arrests'] = main_df[['sale_drug_total_tot_arrests', 'poss_drug_total_tot_arrests']].sum(axis=1)
    main_df['drug_total_arrests_rate'] = main_df[['sale_drug_total_tot_arrests_rate', 'poss_drug_total_tot_arrests_rate']].sum(axis=1)

    main_df.replace(np.inf, 0, inplace=True)

    main_df.to_csv('C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/analysis/final_main_ncrp_incarc_rep_code_enhanced.csv',
                         index=False)


#create_icspr_flags(pd.read_csv('C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/analysis/final_main.csv'))

update_final_main_vars(pd.read_csv('C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/analysis/final_main_ncrp_incarc_rep_code.csv'))

