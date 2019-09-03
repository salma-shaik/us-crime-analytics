import pandas as pd

yr_df = pd.DataFrame({'ORI': ['AK00101', 'AK00102']*25,'yr': [2015,2015,2015,2015,2015,2010,2010,2010,2010,2010,2010,2010,2010,2010,2010,2000,2000,2000,
                             2000,2000,2000,2000,2000,2000,2000] * 2})

# print(yr_df)

# yr_df['yr'] = yr_df.apply(lambda x : x-1 if x not in [2015, 2010,2000,1990] else x)
#
yr_df_upd = pd.DataFrame()

yr_df_grpd = yr_df.sort_values(['ORI', 'yr'], ascending=[True, False]).groupby('ORI',  as_index=False)

for grp_name, grp in yr_df_grpd:
    grp.reset_index(inplace=True)
    yr_dict = dict()
    for row_index, row in grp.iterrows():
        if row['yr'] in [2015, 2010, 2000, 1990]:
            if row['yr'] in yr_dict:
                grp.at[row_index, 'yr'] = ((grp.iloc[row_index - 1].yr) - 1)
            else:
                yr_dict.update({row['yr']: 1})
       # print(row_index, row.yr)
    yr_df_upd = pd.concat([yr_df_upd, grp], sort=False, ignore_index=True)
yr_df_upd.drop(['index'], axis=1 , inplace=True)
print(yr_df_upd)