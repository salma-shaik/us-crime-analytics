import pandas as pd

# rates_df = pd.read_csv('C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/pre-analysis/initial_core_rates_pop_1000_neg_rplcd.csv')
#
# #print(rates_df.head())
# rates_df_grpd = rates_df.groupby('YEAR').aggregate('mean').reset_index()
#
# rates_df_grpd.to_csv('C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/rates_df_grpd.csv', index=False)
# #print(rates_df_grpd.head())

# final_df = pd.read_csv('C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/crime/Crime_1990_2015.csv')
# print(pd.crosstab(final_df['year'], final_df['months_reported']))
# print(list(final_df))
# final_df_robbery = final_df.loc[:, ['ORI', 'year', 'population', 'robbery', 'murder', 'aggravated_assault']]

#print(final_df[final_df['robbery'] == 100280])
#
# #final_df_robbery_grpd = /
# print(final_df_robbery.groupby('year').aggregate('sum').reset_index())

#print(final_df['murder'].describe())

#final_df_robbery_grpd.to_csv('C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/final_df_robbery_grpd.csv', index=False)

# print('1993 rec: ', final_df[final_df['year'] == 1993].shape[0])
# print('1992 rec: ', final_df[final_df['year'] == 1992].shape[0])
#
# print()


final_df = pd.read_csv('C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/crime/Crime_National_UCR_offenses_1960_2015.csv', encoding = "ISO-8859-1")



final_df_robbery = final_df[(final_df.months_reported == "Dec last reported") |
                                            (final_df.months_reported == "December is the last month reported")]

final_df_robbery = final_df_robbery.loc[:, ['ORI', 'year', 'population', 'robbery', 'aggravated_assault']]

final_df_robbery_dec_rep = final_df_robbery.query('year >= 1990')
# print(final_df_robbery_dec_rep.groupby('year').aggregate({'robbery': 'sum', 'aggravated_assault': 'sum'}).reset_index())

print(final_df_robbery_dec_rep.groupby('year').size())

