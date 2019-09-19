# base_url = 'https://api.census.gov/data/2000/sf3'
# list1 = 'P043001,P082001,PCT035001,PCT035002,PCT035003,PCT035010,PCT035017'
#
# # print(f'list o fvars is {list1}')
#
#
# url = f'{base_url}?get={list1},NAME&for=county:001&in=state:01&key=d2b9b07dfed3cc16bbb93f03b445c16a4fed0c72' # 3140 calls
# response = requests.get(url)
#
# resp = json.loads(response.content)
#
# print(resp)

#print(type(23))

# if ~ isinstance('s', str):
#     print('Not a string')
#
# # print(len(123)) - doesn't work

import pandas as pd
# from utilities import df_cleaner
#
# df = pd.DataFrame({'a': [1,2,3]})
#
# a = df['a'].astype(str)
# print(a.dtype)

# print(str(3))

# final_df = pd.read_csv('C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/merge_files/final_main_race_counts_incarc_counts.csv')
# print(set(final_df['ORI']).__len__())

########## Check fo rany place fips that have a code equal to or greater than 99001
# econ = pd.read_csv('C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/economic/new_eco_cen/2015/cnty_subd/eco_15_cnty_subd.csv')
#
# econ_above = econ[econ.place_fips > 99001]
# print(econ_above)

# 90
# econ_df = pd.read_csv('C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/economic/new_eco_cen/1990/eco_1990.csv')

# 00
#econ_df = pd.read_csv('C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/economic/new_eco_cen/2000/eco_2000.csv')

# 10
# econ_df = pd.read_csv('C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/economic/new_eco_cen/2010/eco_2010.csv')
#
# print('Duplicate records: ')
# econ_df_dup = econ_df[econ_df.duplicated(subset=['STATEFP', 'place_fips'])]
# #econ_df_dup = pd.concat(g for _, g in econ_df.groupby(['STATEFP', 'place_fips']) if len(g) > 1)
# print(econ_df_dup)


# df1 = pd.DataFrame({'a': [1, 2, 3]})
# df2 = pd.DataFrame({'a': [4, 2, 3]})
#
# # df1_new = df1.merge(df2)
# df1_new = pd.concat([df1, df2], ignore_index=True)
# #print(df1)
#
# print(df1_new)

# year = 2015
# yr_str = '4/1/' + str(year)
# yr_str_dt = pd.to_datetime(yr_str)
# print(yr_str_dt.year)

df1 = pd.DataFrame({'a': [1, 1, 1, 2, 2]})
df2 = pd.DataFrame({'a': [1, 2], 'b':['a_replicated', 'b_replicated']})

df = df1.merge(df2, on='a')
print(df)