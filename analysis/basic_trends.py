import pandas as pd

# cnts_pc = pd.read_csv('/Users/salma/Research/us-crime-analytics/data/pre_analysis/initial_core_counts_pop_1000_neg_rplcd_out_repl_pc.csv')
# print(cnts_pc.head())


import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt


# Create weighted averages
def create_weighted_avgs(df, avg_name, weight_name):
    d = df[avg_name]
    w = df[weight_name]
    try:
        return (d * w).sum() / w.sum()
    except ZeroDivisionError:
        return d.mean()


# Create graphs for trends
def graph_trends(df, trend_vars, title, xlbl, ylbl):
    for trend_var, pop_var in trend_vars.items():
        plt_var = df.groupby("YEAR").apply(create_weighted_avgs, f'{trend_var}', f'{pop_var}')
        plt.plot(plt_var, label=f'{trend_var}')
        plt.legend()
        plt.title(f'{title}')
        plt.xlabel(f'{xlbl}')
        plt.ylabel(f'{ylbl}')
    plt.show()


def rates_trends():
    rates_df = pd.read_csv('C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/pre-analysis/initial_core_rates_pop_1000_neg_rplcd_incrc_cnts_rates.csv')
    """
    Violent crimes, property crimes
    """
    # graph_trends(rates_df, {'violent_crime_rate':'population', 'property_crime_rate':'population'},
    #              title='Major Crime Trends',
    #               xlbl='Year', ylbl='Crime Rate')

    """
    prison occupancy counts, jail occupancy counts
    """
    graph_trends(rates_df, {'prison_occupancy_count_rate': 'total_count_county', 'jail_occupancy_count_rate': 'total_count_county'},
                 title='Incarceration Trends',
                 xlbl='Year', ylbl='Incarceration Rate')


def rates_without_ol_trends():
    rates_df = pd.read_csv('C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/pre-analysis/outliers/initial_core_rates_pop_1000_neg_rplcd_incrc_cnts_rates_out_repl.csv')
    """
    Violent crimes, property crimes
    """
    graph_trends(rates_df, {'violent_crime_rate':'population', 'property_crime_rate':'population'},
                 title='Major Crime Trends',
                  xlbl='Year', ylbl='Crime Rate')

    """
    prison occupancy counts, jail occupancy counts
    """
    graph_trends(rates_df, {'prison_occupancy_count_rate': 'total_count_county', 'jail_occupancy_count_rate': 'total_count_county'},
                 title='Incarceration Trends',
                 xlbl='Year', ylbl='Incarceration Rate')


def rates_without_ol_dm_trends():
    dm_df = pd.read_csv(
        'C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/pre-analysis/initial_core_rates_pop_1000_neg_rplcd_incrc_cnts_rates_out_repl_dm.csv')
    """
    Violent crimes, property crimes
    """
    graph_trends(dm_df, {'dm_violent_crime_rate': 'dm_population', 'dm_property_crime_rate': 'dm_population'},
                 title='Major Crime Trends',
                 xlbl='Year', ylbl='Crime Rate(dm)')

    """
    prison occupancy counts, jail occupancy counts
    """
    graph_trends(dm_df, {'dm_prison_occupancy_count_rate': 'dm_total_count_county',
                            'dm_jail_occupancy_count_rate': 'dm_total_count_county'},
                 title='Incarceration Trends',
                 xlbl='Year', ylbl='Incarceration Rate')


def rates_without_ol_pc_trends():
    pc_df = pd.read_csv(
        'C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/pre-analysis/initial_core_rates_pop_1000_neg_rplcd_incrc_cnts_rates_out_repl_pc.csv')
    """
    Violent crimes, property crimes
    """
    graph_trends(pc_df, {'pc_violent_crime_rate': 'pc_population', 'pc_property_crime_rate': 'pc_population'},
                 title='Major Crime Trends',
                 xlbl='Year', ylbl='Crime Rate(pc)')

    """
    prison occupancy counts, jail occupancy counts
    """
    graph_trends(pc_df, {'pc_prison_occupancy_count_rate': 'pc_total_count_county',
                            'pc_jail_occupancy_count_rate': 'pc_total_count_county'},
                 title='Incarceration Trends',
                 xlbl='Year', ylbl='Incarceration Rate(pc)')

# rates_trends()
rates_without_ol_trends()
# rates_without_ol_dm_trends()
# rates_without_ol_pc_trends()

"""
    1. Drug Arrests Trend By Race (Sale + Possession)
"""
# graph_trends({'drug_arrests_white':'White_count', 'drug_arrests_black':'Black_count'}, title='Drug Arrests Trend By Race', xlbl='Year', ylbl='Drug Arrests Rate')


"""
    2. Drug Sale Arrests Trend By Race
"""
# graph_trends({'sale_drug_total_tot_white_rate':'White_count', 'sale_drug_total_tot_black_rate':'Black_count'}, title='Drug Sale Arrests Trend By Race', xlbl='Year', ylbl='Drug Sale Arrests Rate')


"""
    3. Drug Possession Arrests Trend By Race
"""
# graph_trends({'poss_drug_total_tot_white_rate':'White_count', 'poss_drug_total_tot_black_rate':'Black_count'}, title='Drug Possession Arrests Trend By Race', xlbl='Year', ylbl='Drug Possession Arrests Rate')


"""
    4. Drug Possession Arrests Trend By Officers Rate
"""
# graph_trends({'poss_drug_total_tot_white_rate':'White_count', 'poss_drug_total_tot_black_rate':'Black_count'}, title='Drug Possession Arrests Trend By Race', xlbl='Year', ylbl='Drug Possession Arrests Rate')


"""
    5. Disorder Arrests Trend By Race
"""
# graph_trends({'disorder_arrests_white_index_rate':'White_count', 'disorder_arrests_black_index_rate':'Black_count'}, title='Disorder Arrests Trend By Race', xlbl='Year', ylbl='Disorder Arrests Rate')


