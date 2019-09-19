import pandas as pd
import os
import numpy as np
from openpyxl import load_workbook

pd.set_option('display.max_columns', 500)
pd.set_option('max_colwidth', 5000)

incarc_df = pd.DataFrame()

os.chdir('C:/Users/sshaik2/Downloads/ICPSR_37021-V1/ICPSR_37021/Incarc_Data')

files_metadata_xl_path = r'C:/Users/sshaik2/projects/criminal_justice/us-crime-analytics/data/ICPSR_37021/incarc_files_metadata.xlsx'

files_metadata_book = load_workbook(files_metadata_xl_path)
writer = pd.ExcelWriter(files_metadata_xl_path, engine='openpyxl')
writer.book = files_metadata_book


def get_states_list():
    for fle in os.listdir():
        df = pd.read_csv(fle, sep='\t')
        f_name = fle.split('/')[-1]
        states = set(df['STATE'])
        print('file_name: ', f_name, '\n', 'states: ', states, '\n', 'records: ', df.shape[0], '\n')


def get_yrs_reported():
    for fle in os.listdir():
        df = pd.read_csv(fle, sep='\t')
        f_name = fle.split('/')[-1]
        if 'RPTYEAR' in list(df):
            print('file_name: ', f_name, ':', df['RPTYEAR'].unique(), '\n')


# get the set of reported years from each type of file
# get_yrs_reported()
def get_states_by_year():

    for fle in os.listdir():
        df = pd.read_csv(fle, sep='\t')

        if 'RPTYEAR' in list(df):

            # get the unique states list
            df_grpd = df.groupby(['RPTYEAR'])['STATE'].unique().apply(list).reset_index()
            df_grpd['ncrp_incarc_st_count'] = df_grpd['STATE'].apply(len)

            # write each df as a separate sheet to files metadata excel
            df_grpd.to_excel(writer, sheet_name=os.path.basename(f'{fle}_states'), index=False)
            writer.save()
            writer.close()

# get_states_by_year()


def get_years_by_state():

    for fle in os.listdir():
        df = pd.read_csv(fle, sep='\t')

        if 'RPTYEAR' in list(df):

            # get the unique states list
            df_grpd = df.groupby(['STATE'])['RPTYEAR'].unique().apply(list).reset_index()
            df_grpd['ncrp_incarc_yr_count'] = df_grpd['RPTYEAR'].apply(len)

            # write each df as a separate sheet to files metadata excel
            df_grpd.to_excel(writer, sheet_name=os.path.basename(f'{fle}_yrs'), index=False)
            writer.save()
            writer.close()

get_years_by_state()