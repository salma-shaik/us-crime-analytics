import pandas as pd
from datetime import datetime


print("########## Start: ", datetime.now().time())

arrests_df = pd.read_excel('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/arrests/Arrests_All_Race_1990_2016.xlsx')

"""
    Get only the required columns
"""

reqd_df = arrests_df[['ori', 'year', 'agency_name', 'agg_assault_tot_arrests', 'agg_assault_tot_black', 'agg_assault_tot_white', 'all_other_tot_arrests', 'all_other_tot_black',
                      'all_other_tot_white', 'arson_tot_arrests', 'arson_tot_black', 'arson_tot_white', 'burglary_tot_arrests', 'burglary_tot_black', 'burglary_tot_white',
                      'curfew_loiter_tot_arrests', 'curfew_loiter_tot_black', 'curfew_loiter_tot_white', 'disorder_cond_tot_arrests', 'disorder_cond_tot_black',
                      'disorder_cond_tot_white', 'drunkenness_tot_arrests', 'drunkenness_tot_black', 'drunkenness_tot_white', 'mtr_veh_theft_tot_arrests',
                      'mtr_veh_theft_tot_black', 'mtr_veh_theft_tot_white', 'murder_tot_arrests', 'murder_tot_black', 'murder_tot_white', 'prostitution_tot_arrests',
                      'prostitution_tot_black', 'prostitution_tot_white', 'rape_tot_arrests', 'rape_tot_black', 'rape_tot_white', 'robbery_tot_arrests', 'robbery_tot_black',
                      'robbery_tot_white', 'runaways_tot_arrests', 'runaways_tot_black', 'runaways_tot_white', 'sale_cannabis_tot_arrests', 'sale_cannabis_tot_black',
                      'sale_cannabis_tot_white','sale_drug_total_tot_arrests', 'sale_drug_total_tot_black', 'sale_drug_total_tot_white', 'stolen_prop_tot_arrests',
                      'stolen_prop_tot_black', 'stolen_prop_tot_white','theft_tot_arrests','theft_tot_black','theft_tot_white','vagrancy_tot_arrests','vagrancy_tot_black','vagrancy_tot_white',
                      'vandalism_tot_arrests','vandalism_tot_black', 'vandalism_tot_white', 'weapons_tot_arrests','weapons_tot_black','weapons_tot_white','poss_cannabis_tot_arrests',
                      'poss_cannabis_tot_black','poss_cannabis_tot_white','poss_drug_total_tot_arrests','poss_drug_total_tot_black','poss_drug_total_tot_white']]

# Write the df with req vars to a csv
reqd_df.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/arrests/Arrests_Req_Vars.csv', index=False)


"""
Create the required disadvantage indexes
"""


def create_disorder_arrests_index():
    reqd_df['disorder_arrests_tot_index'] = reqd_df[['curfew_loiter_tot_arrests','disorder_cond_tot_arrests','drunkenness_tot_arrests','runaways_tot_arrests','prostitution_tot_arrests','vagrancy_tot_arrests','vandalism_tot_arrests']].sum(axis=1)
    reqd_df['disorder_arrests_black_index'] = reqd_df[['curfew_loiter_tot_black','disorder_cond_tot_black','drunkenness_tot_black','runaways_tot_black','prostitution_tot_black','vagrancy_tot_black','vandalism_tot_black']].sum(axis=1)
    reqd_df['disorder_arrests_white_index'] = reqd_df[['curfew_loiter_tot_white','disorder_cond_tot_white','drunkenness_tot_white','runaways_tot_white','prostitution_tot_white','vagrancy_tot_white','vandalism_tot_white']].sum(axis=1)


def create_larceny_theft_arrests_index():
    reqd_df['larceny_theft_arrests_tot'] = reqd_df[['stolen_prop_tot_arrests','theft_tot_arrests']].sum(axis=1)
    reqd_df['larceny_theft_arrests_black'] = reqd_df[['stolen_prop_tot_black','theft_tot_black']].sum(axis=1)
    reqd_df['larceny_theft_arrests_white'] = reqd_df[['stolen_prop_tot_white','theft_tot_white']].sum(axis=1)


create_disorder_arrests_index()

create_larceny_theft_arrests_index()

def drop_unwanted_cols():
    # drop the non-required individual columns
    reqd_df.drop(['curfew_loiter_tot_arrests', 'disorder_cond_tot_arrests', 'drunkenness_tot_arrests','runaways_tot_arrests', 'prostitution_tot_arrests', 'vagrancy_tot_arrests', 'vandalism_tot_arrests', 'curfew_loiter_tot_black', 'disorder_cond_tot_black', 'drunkenness_tot_black',
                  'runaways_tot_black', 'prostitution_tot_black', 'vagrancy_tot_black', 'vandalism_tot_black', 'curfew_loiter_tot_white', 'disorder_cond_tot_white', 'drunkenness_tot_white',
                  'runaways_tot_white', 'prostitution_tot_white', 'vagrancy_tot_white', 'vandalism_tot_white', 'stolen_prop_tot_arrests', 'theft_tot_arrests', 'stolen_prop_tot_black', 'theft_tot_black', 'stolen_prop_tot_white', 'theft_tot_white'], axis=1, inplace=True)

    """
           total sales = sum of all individual drug sales.
           So just keep the total cols and drop the individual ones except for cannabis.
           (Cannabis is legalized in certain states. Need to think about this)
           
           total poss = sum of all individual drug possessions.
           So just keep the total cols and drop the individual ones except for cannabis.
           (Cannabis is legalized in certain states. Need to think about this)
    """

drop_unwanted_cols()

print("########## End: ", datetime.now().time())

# Write the final df with both req vars and indexes to a file
reqd_df.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/arrests/Arrests_Req_Vars_Indexes.csv', index=False)
