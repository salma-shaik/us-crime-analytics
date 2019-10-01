import pandas as pd

rates_ol = pd.read_csv('C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/pre-analysis/initial_core_rates_pop_1000_neg_rplcd.csv')
rates_ol['prison_occupancy_count_rate'] = (rates_ol['prison_occupancy_count']/rates_ol['total_count_county']) * 10000
rates_ol['jail_occupancy_count_rate'] = (rates_ol['jail_occupancy_count']/rates_ol['total_count_county']) * 10000
rates_ol.to_csv('C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/pre-analysis/initial_core_rates_pop_1000_neg_rplcd_incrc_cnts_rates.csv', index=False)
