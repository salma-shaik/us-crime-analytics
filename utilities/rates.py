import pandas as pd
import  numpy as np

main_df = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/merge_files/Census_Crime_BEA_Spatial_Officers_Arrests_Incarceration.csv')
main_df['black_count_county'] = main_df[['blackmale_count_county', 'blackfemale_count_county']].sum(axis=1)
main_df['white_count_county'] = main_df[['whitemale_count_county', 'whitefemale_count_county']].sum(axis=1)
main_df['hispanic_count_county'] = main_df[['hispmale_count_county', 'hispfem_count_county']].sum(axis=1)

"""
Create rates for the below crime variables
    murder
    manslaughter
    rape
    robbery
    gun_robbery
    knife_robbery
    aggravated_assault
    gun_assault
    knife_assault
    simple_assault
    burglary
    larceny
    auto_theft
    officers_assaulted
    officers_killed_by_felony
    officers_killed_by_accident
    total_crime
    violent_crime
    property_crime
    crimes_against_officers

    population - crime pop
"""


def create_rates(var_list, pop_var=None, var_group=None):
    rate_multiplier = 10000
    if var_group == 'crime':
        rate_multiplier = 100000

    for rate_var in var_list:
        main_df[f'{rate_var}_rate'] = (main_df[f'{rate_var}']/main_df['population'])*rate_multiplier

# Create crime rates
crime_vars = ['murder', 'manslaughter', 'rape', 'robbery', 'gun_robbery', 'knife_robbery', 'aggravated_assault',
              'gun_assault', 'knife_assault', 'simple_assault','burglary', 'larceny', 'auto_theft', 'officers_assaulted',
              'officers_killed_by_felony','officers_killed_by_accident', 'total_crime', 'violent_crime','property_crime',
              'crimes_against_officers']

create_rates(crime_vars, 'population', 'crime')


"""
Create rates for the below arrests variables
    agg_assault_tot_arrests
    agg_assault_tot_black
    agg_assault_tot_white
    all_other_tot_arrests
    all_other_tot_black
    all_other_tot_white
    arson_tot_arrests
    arson_tot_black
    arson_tot_white
    burglary_tot_arrests
    burglary_tot_black
    burglary_tot_white
    mtr_veh_theft_tot_arrests
    mtr_veh_theft_tot_black
    mtr_veh_theft_tot_white
    murder_tot_arrests
    murder_tot_black
    murder_tot_white
    rape_tot_arrests
    rape_tot_black
    rape_tot_white
    robbery_tot_arrests
    robbery_tot_black
    robbery_tot_white
    sale_cannabis_tot_arrests
    sale_cannabis_tot_black
    sale_cannabis_tot_white
    sale_drug_total_tot_arrests
    sale_drug_total_tot_black
    sale_drug_total_tot_white
    weapons_tot_arrests
    weapons_tot_black
    weapons_tot_white
    poss_cannabis_tot_arrests
    poss_cannabis_tot_black
    poss_cannabis_tot_white
    poss_drug_total_tot_arrests
    poss_drug_total_tot_black
    poss_drug_total_tot_white
    disorder_arrests_tot_index
    disorder_arrests_black_index
    disorder_arrests_white_index
    larceny_theft_arrests_tot
    larceny_theft_arrests_black
    larceny_theft_arrests_white

arrests_vars = ['agg_assault_tot_arrests','agg_assault_tot_black','agg_assault_tot_white','all_other_tot_arrests','all_other_tot_black','all_other_tot_white',
                'arson_tot_arrests','arson_tot_black','arson_tot_white','burglary_tot_arrests','burglary_tot_black','burglary_tot_white','mtr_veh_theft_tot_arrests',
                'mtr_veh_theft_tot_black','mtr_veh_theft_tot_white','murder_tot_arrests','murder_tot_black','murder_tot_white','rape_tot_arrests','rape_tot_black',
                'rape_tot_white','robbery_tot_arrests','robbery_tot_black','robbery_tot_white','sale_cannabis_tot_arrests','sale_cannabis_tot_black','sale_cannabis_tot_white',
                'sale_drug_total_tot_arrests','sale_drug_total_tot_black','sale_drug_total_tot_white','weapons_tot_arrests','weapons_tot_black','weapons_tot_white',
                'poss_cannabis_tot_arrests','poss_cannabis_tot_black','poss_cannabis_tot_white','poss_drug_total_tot_arrests','poss_drug_total_tot_black',
                'poss_drug_total_tot_white','disorder_arrests_tot_index','disorder_arrests_black_index','disorder_arrests_white_index','larceny_theft_arrests_tot',
                'larceny_theft_arrests_black','larceny_theft_arrests_white']
"""

"""
Create rates for the below arrests total variables

    agg_assault_tot_arrests
    all_other_tot_arrests
    arson_tot_arrests
    burglary_tot_arrests
    mtr_veh_theft_tot_arrests
    murder_tot_arrests
    rape_tot_arrests
    robbery_tot_arrests
    sale_cannabis_tot_arrests
    sale_drug_total_tot_arrests
    weapons_tot_arrests
    poss_cannabis_tot_arrests
    poss_drug_total_tot_arrests
    disorder_arrests_tot_index
    larceny_theft_arrests_tot
"""
arrests_total_vars = ['agg_assault_tot_arrests','all_other_tot_arrests','arson_tot_arrests','burglary_tot_arrests','mtr_veh_theft_tot_arrests',
                      'murder_tot_arrests','rape_tot_arrests','robbery_tot_arrests','sale_cannabis_tot_arrests','sale_drug_total_tot_arrests',
                      'weapons_tot_arrests','poss_cannabis_tot_arrests','poss_drug_total_tot_arrests','disorder_arrests_tot_index','larceny_theft_arrests_tot']

create_rates(arrests_total_vars)


"""
Create rates for the below arrests black variables

    agg_assault_tot_black
    all_other_tot_black
    arson_tot_black
    burglary_tot_black
    mtr_veh_theft_tot_black
    murder_tot_black
    rape_tot_black
    robbery_tot_black
    sale_cannabis_tot_black
    sale_drug_total_tot_black
    weapons_tot_black
    poss_cannabis_tot_black
    poss_drug_total_tot_black
    disorder_arrests_black_index
    larceny_theft_arrests_black
"""
main_df['drug_arrests_black'] = main_df[['sale_drug_total_tot_black', 'poss_drug_total_tot_black']].sum(axis=1)
arrests_black_vars = ['agg_assault_tot_black','all_other_tot_black','arson_tot_black','burglary_tot_black','mtr_veh_theft_tot_black',
                      'murder_tot_black','rape_tot_black','robbery_tot_black','drug_arrests_black','sale_cannabis_tot_black','sale_drug_total_tot_black',
                      'weapons_tot_black','poss_cannabis_tot_black','poss_drug_total_tot_black','disorder_arrests_black_index','larceny_theft_arrests_black']

# create_rates(arrests_black_vars, 'Black_count')


"""
Create rates for the below arrests white variables

    agg_assault_tot_white
    all_other_tot_white
    arson_tot_white
    burglary_tot_white
    mtr_veh_theft_tot_white
    murder_tot_white
    rape_tot_white
    robbery_tot_white
    sale_cannabis_tot_white
    sale_drug_total_tot_white
    weapons_tot_white
    poss_cannabis_tot_white
    poss_drug_total_tot_white
    disorder_arrests_white_index
    larceny_theft_arrests_white
"""
main_df['drug_arrests_white'] = main_df[['sale_drug_total_tot_white', 'poss_drug_total_tot_white']].sum(axis=1)
arrests_white_vars = ['agg_assault_tot_white','all_other_tot_white','arson_tot_white','burglary_tot_white','mtr_veh_theft_tot_white',
                      'murder_tot_white','rape_tot_white','robbery_tot_white','drug_arrests_white','sale_cannabis_tot_white','sale_drug_total_tot_white',
                      'weapons_tot_white','poss_cannabis_tot_white','poss_drug_total_tot_white','disorder_arrests_white_index','larceny_theft_arrests_white']

# create_rates(arrests_white_vars, 'White_count')


"""
Create rates for the below incarceration variables
    total_jail_pop

    black_jail_pop
    latino_jail_pop
    white_jail_pop

    total_prison_pop

    black_prison_pop
    latino_prison_pop
    white_prison_pop
"""

#incarc_tot_vars = ['total_jail_pop', 'total_prison_pop']
# create_rates(incarc_tot_vars, 'county_pop_final')

#incarc_black_vars = ['black_jail_pop', 'black_prison_pop']
# create_rates(incarc_black_vars, 'black_count_county')

#incarc_white_vars = ['white_jail_pop', 'white_prison_pop']
# create_rates(incarc_white_vars, 'white_count_county')

#incarc_hispanic_vars = ['latino_jail_pop', 'latino_prison_pop']
# create_rates(incarc_hispanic_vars, 'hispanic_count_county')

# some populations are zero so divide by zero gets infinity so replace them with 0
main_df.replace(np.inf, 0, inplace=True)
main_df.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/analysis/final_main_rates.csv', index=False)
