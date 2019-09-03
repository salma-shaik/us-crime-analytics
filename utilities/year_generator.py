import pandas as pd


def generate_years(df, op_fl_path, dt_type):
    df_req_upd_yrs = pd.DataFrame()

    df_req_grpd = df.sort_values(['ORI', 'YEAR'], ascending=[True, False]).groupby('ORI', as_index=False)

    for grp_name, grp in df_req_grpd:
        grp.reset_index(inplace=True)
        yr_dict = dict()
        for row_index, row in grp.iterrows():
            if row['YEAR'] in [2015, 2010, 2000, 1990]:
                if row['YEAR'] in yr_dict:
                    grp.at[row_index, 'YEAR'] = (grp.iloc[row_index - 1].YEAR) - 1
                else:
                    yr_dict.update({row['YEAR']: 1})
        df_req_upd_yrs = pd.concat([df_req_upd_yrs, grp], sort=False, ignore_index=True)
        df_req_upd_yrs.drop('index', axis=1, inplace=True)

    df_req_upd_yrs.to_csv(f'{op_fl_path}/{dt_type}_Fixed_Cols_Replicated_Years_Assigned.csv', index=False)