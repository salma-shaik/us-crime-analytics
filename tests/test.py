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

# df1 = pd.DataFrame({'a': [1, 1, 1, 2, 2]})
# df2 = pd.DataFrame({'a': [1, 2], 'b':['a_replicated', 'b_replicated']})
#
# df = df1.merge(df2, on='a')
# print(df)

import numpy as np
import operator

raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
        'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'],
        'age': [42, 52, 36, 24, 73],
        'preTestScore': [-19, -999, -34534, 2, 1],
        'postTestScore': [2, 2, -100, 2, -999]}
df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'preTestScore', 'postTestScore'])

# Accessing the private _get_numeric_data() of the dataframe. Private method, so changes reflected in the original df
# int_df_num = int_df._get_numeric_data()
# int_df_num[int_df_num < 0] = 0

#df_num = df._get_numeric_data()

#df_num[df_num < 0] = 0
# r'[^-\d]', ""
# df[df.postTestScore < 0] = np.nan

#df[df.postTestScore < 0] = 'NaN'

#df.replace('', np.nan, inplace=True)

# Replace values where the condition is False.
# data_frame = df.where(df > 0, np.nan)
#
#
# df_num = df._get_numeric_data()
# df_num[df_num < 0] = np.nan
#
# print(df)
# print()
# print(df.dtypes)
# print()
# print(df.preTestScore.mean())
# print()
# print(df.postTestScore.mean())


#modDfObj = df.apply(lambda x: x + 10)
pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 5000)

data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy', 'Roger', 'Ryan'],
        'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze', 'Ben', 'Olsen'],
        'age': [42, 52, 36, 24, 1007389, 797809, 3456788],
        'preTestScore': [19, 999, 345348, 946578,23456, 2, 1],
        'postTestScore': [2, 2, 100, 2, 99956, 34567, 2345678]}
df_out_test = pd.DataFrame(data, columns = ['first_name', 'last_name', 'age', 'preTestScore', 'postTestScore'])

#print(df_out_test, '\n')
#mod_df = df_out_test.select_dtypes(include=[np.number]).apply(lambda x: ((x - x.mean())/x.std()).abs()>2, np.nan)

#
# def repl_outliers(ser):
#
#         if ((ser-ser.mean())/ser.std()) > 2:
#                 return np.nan
#         else:
#                 return ser

#print(df_out_test.loc[:, 'age':])
df_num = df_out_test.loc[:, 'age':]

df_num_out_repl = df_num.mask(df_num.sub(df_num.mean()).div(df_num.std()).abs().gt(2))

print(df_num_out_repl)

# df_num_out_repl = df_num.apply(repl_outliers)
#
# print(df_num_out_repl)

# df_num_z = df_num.apply(lambda x: ((x - x.mean())/x.std()).abs())
#
# print(df_num_z, '\n')
#
# df_num = df_num.apply(lambda x: np.nan if ((((x - x.mean())/x.std()).abs()) > 2).any() else x)
# print(df_num, '\n')
#
# df_num = np.where(fake_abalone2['Rings']<10, 'K', fake_abalone2['Sex'])

#
# # mod_df = df_out_test.iloc[:, 2:].apply(lambda x: np.nan if operator.gt((((x - x.mean())/x.std()).abs()), 2) else x)
#
# print(df_num, '\n')

# df_out_test_merged = df_out_test.iloc[:,:2].merge(mod_df, left_index=True, right_index=True)
# print(df_out_test_merged, '\n')

#
# df.loc[:,~df.columns.str.startswith('Test')]
#
#
# df_out_test_merged = df_out_test_merged.loc[:,~df_out_test_merged.columns.str.endswith('_x')]
# print(df_out_test_merged)
#
# df_out_test_merged.columns = df_out_test_merged.columns.str.rstrip('_y')
#initial_core_counts_pos = initial_core_counts.merge(initial_core_counts_neg, how='left', indicator=True)
# initial_core_counts_pos = initial_core_counts_pos[initial_core_counts_pos['_merge'] == 'left_only']