import pandas as pd

# getting only the main columns for initial trend lines
def get_top_level_vars(fnl_main):
    initial_core_df = fnl_main.loc[:, ['ORI', 'AGENCY', 'placename', 'Govt_level', 'place_fips', 'STATEFP', 'CNTY',
                                       'YEAR', 'POP100','White_count', 'Black_count', 'Hispanic_count',
                                       'Age1524_WhiteM','White_Males_All', 'Age1524_WhiteF', 'White_Females_All',
                                       'Age1524_BlackM','Black_Males_All', 'Age1524_BlackF','Black_Females_All',
                                       'Hispanic_Males_All','Age1524_HispanicM', 'Age1524_HispanicF',
                                       'Hispanic_Females_All', 'Pct_WYM','Pct_WYF', 'total_count_county',
                                       'population', 'murder', 'rape', 'robbery', 'aggravated_assault',
                                       'simple_assault', 'burglary', 'larceny', 'auto_theft', 'violent_crime',
                                       'property_crime','total_main_crime','murder_rate', 'rape_rate',
                                       'robbery_rate','aggravated_assault_rate','simple_assault_rate',
                                       'burglary_rate', 'larceny_rate','auto_theft_rate','violent_crime_rate',
                                       'property_crime_rate','total_main_crime_rate','violent_arrests',
                                       'property_arrests', 'total_main_arrests', 'violent_arrests_rates','property_arrests_rates',
                                       'total_main_arrests_rates', 'sale_drug_total_tot_arrests_rate',
                                       'poss_drug_total_tot_arrests_rate', 'disorder_arrests_tot_index_rate',
                                       'pci_total_pop','pci_white', 'pci_black', 'pci_hisp', 'emp_total',
                                       'emp_total_male','emp_total_female','emp_total_male_white',
                                       'emp_total_female_white','emp_total_male_black', 'emp_total_female_black',
                                       'emp_total_male_hisp','emp_total_female_hisp', 'emp_total_white', 'emp_total_black',
                                       'emp_total_hisp', 'PRIMARY_LATITUDE', 'PRIMARY_LONGITUDE', 'total_officers',
                                       'total_officers_rate', 'perc_felonies', 'perc_misdemeanors','prison_occupancy_count',
                                       'jail_occupancy_count', 'icspr_rep_code']]


    initial_core_df.to_csv('C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/analysis/initial_core_file.csv', index=False)

    return initial_core_df


# Create weighted averages
def create_weighted_avgs(df, avg_name, weight_name):
    d = df[avg_name]
    w = df[weight_name]
    try:
        return (d * w).sum() / w.sum()
    except ZeroDivisionError:
        return d.mean()


# Create graphs for trends
# def graph_trends(trend_vars, title, xlbl, ylbl):
#     for trend_var, pop_var in trend_vars.items():
#         print(trend_var, ":", pop_var)
#         plt_var = final_df.groupby("YEAR").apply(create_weighted_avgs, f'{trend_var}', f'{pop_var}')
#         plt.plot(plt_var, label=f'{trend_var}')
#         plt.legend()
#         plt.title(f'{title}')
#         plt.xlabel(f'{xlbl}')
#         plt.ylabel(f'{ylbl}')
#     plt.show()


get_top_level_vars(pd.read_csv('C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/analysis/final_main_ncrp_incarc_rep_code_enhanced.csv'))