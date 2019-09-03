import pandas as pd


def calculate_incarc_counts():
    final_main_race_counts_crime_totals['prison_occupancy_count'] = (final_main_race_counts_crime_totals['perc_felonies'] * final_main_race_counts_crime_totals['total_prison_pop']) / 100
    final_main_race_counts_crime_totals['jail_occupancy_count'] = (final_main_race_counts_crime_totals['perc_misdemeanors'] * final_main_race_counts_crime_totals['jail_interp']) / 100
