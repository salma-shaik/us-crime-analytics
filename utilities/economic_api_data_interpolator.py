import pandas as pd

from datetime import datetime


pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 5000)

from utilities import fixed_columns_replicator as fcr
from utilities import year_replicator as yr

from utilities import variables_interpolator as vi
from utilities import year_generator as yg

# First, drop the records where pci_total is zero
'''
econ_df = pd.read_csv('C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/economic/new_eco_cen/econ_dec_90_15.csv')
econ_df = econ_df[(econ_df.pci_total_pop.notnull()) & (econ_df.pci_total_pop != 0)]
econ_df.to_csv('C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/economic/new_eco_cen/econ_dec_90_15_null_zero_pci_dropped.csv', index=False)
'''

#
# # replicate fixed columns into required number of times depending on year
# # 2015 - 5; 2010, 2000 - 10; 1990 - 1
#
"""
fcr.replicate_fixed_cols(df = pd.read_csv('C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/economic/new_eco_cen/econ_dec_90_15_null_zero_pci_dropped.csv'),
                         cols_list=['ORI', 'AGENCY', 'placename', 'STATEFP', 'CNTY', 'YEAR'],
                         op_fl_path='C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/economic/new_eco_cen/interpolated',
                         dt_type='Economic')
"""

# generate years between existing decennial years
"""
yg.generate_years(df = pd.read_csv(
                                'C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/economic/new_eco_cen/interpolated/Economic_Fixed_Cols_Replicated.csv'),
                         dt_type = 'Economic',
                         op_fl_path='C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/economic/new_eco_cen/interpolated')
"""

# interpolate variable values in between decennial years
"""
vi.interpolate_vars(df=pd.read_csv('C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/economic/new_eco_cen/econ_dec_90_15_null_zero_pci_dropped.csv'),
                    dt_type='Economic',
                    op_fl_path='C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/economic/new_eco_cen/interpolated')
"""

# merge fixed cols yr assigned file with pop vars interpolated file
fixed_df = pd.read_csv('C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/economic/new_eco_cen/interpolated/Economic_Fixed_Cols_Replicated_Years_Assigned.csv')
vars_df = pd.read_csv('C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/economic/new_eco_cen/interpolated/Economic_Vars_Interpolated.csv')
vars_df.drop(['STATEFP', 'CNTY'], axis=1, inplace=True)
econ_intpd = pd.merge(fixed_df, vars_df, on=['ORI', 'YEAR'])
econ_intpd.to_csv('C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/economic/new_eco_cen/interpolated/Economic_Interpolated.csv', index=False)