import pandas as pd

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 5000)
pd.options.display.float_format = '{:.2f}'.format

fnl_main_df = pd.read_csv('/Users/salma/Research/us-crime-analytics/data/pre_analysis/final_main_ncrp_incarc_rep_code_enhanced.csv')

incarc_df = fnl_main_df.loc[:, ['ORI', 'AGENCY', 'placename', 'YEAR', 'POP100', 'population', 'property_crime', 'total_officers',
                                'pci_total_pop', 'emp_total', 'violent_crime', 'total_main_crime', 'violent_arrests',
                                'property_arrests', 'total_main_arrests', 'drug_total_arrests', 'prison_occupancy_count',
                                'jail_occupancy_count', ]]

# incarc_df_grpd = incarc_df.groupby('YEAR').aggregate({'POP100': 'sum', 'population': 'sum', 'violent_crime': 'sum',
#                                                       'property_crime': 'sum', 'total_main_crime': 'sum',
#                                                       'total_officers': 'sum', 'violent_arrests': 'sum', 'property_arrests': 'sum',
#                                                       'total_main_arrests': 'sum', 'drug_total_arrests': 'sum', 'prison_occupancy_count': 'sum',
#                                                       'jail_occupancy_count': 'sum', 'emp_total': 'sum', 'pci_total_pop': 'sum', })
#
# incarc_df_grpd.to_csv('/Users/salma/Research/us-crime-analytics/data/pre_analysis/main_cr_arr_econ_incarc_counts.csv', index=False)



incarc_df = fnl_main_df.loc[:, ['ORI', 'AGENCY', 'placename', 'YEAR', 'POP100', 'population', 'property_crime_rate', 'total_officers_rate',
                                'violent_crime_rate', 'total_main_crime_rate', 'violent_arrests_rate',
                                'property_arrests_rate', 'total_main_arrests_rate', 'drug_total_arrests_rate',
                                'prison_occupancy_count_rate','jail_occupancy_count_rate']]

incarc_df_grpd = incarc_df.groupby('YEAR').aggregate({'violent_crime_rate': 'sum',
                                                      'property_crime_rate': 'sum', 'total_main_crime_rate': 'sum',
                                                      'total_officers_rate': 'sum', 'violent_arrests_rate': 'sum',
                                                      'property_arrests_rate': 'sum','total_main_arrests_rate': 'sum',
                                                      'drug_total_arrests_rate': 'sum', 'prison_occupancy_count_rate': 'sum',
                                                      'jail_occupancy_count_rate': 'sum'})

incarc_df_grpd.to_csv('/Users/salma/Research/us-crime-analytics/data/pre_analysis/main_cr_arr_econ_incarc_rates.csv', index=False)