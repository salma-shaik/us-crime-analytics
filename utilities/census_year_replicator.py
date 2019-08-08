import pandas as pd

"""
We need to create an YEAR column with all the years between 2010 to 2000 and then between 2000 and 1990
Create a dataframe with 2010-1990 years and replicate it as many times required to fill up the existing dataframe length
"""

"""
Read the Census_Agency_Replicated.csv to append YEAR column to it
"""
nat_cen_constant_vars = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/census/Census_Fixed_Cols_Replicated.csv')

years = pd.DataFrame({'YEAR': [2015, 2014, 2013, 2012, 2011, 2010, 2009, 2008, 2007, 2006, 2005, 2004, 2003, 2002, 2001,
                         2000, 1999, 1998, 1997, 1996, 1995, 1994, 1993, 1992, 1991, 1990]})

years_rep = pd.concat([years]*14542, ignore_index=True) # 14542 records(ORIs) in each normalized census files. So all these years for each of the ORI. Total 378092

nat_cen_fixed_rows_yr = pd.concat([nat_cen_constant_vars, years_rep], axis=1)

nat_cen_fixed_rows_yr.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/census/Census_Fixed_Cols_Years_Replicated.csv', index=False)
