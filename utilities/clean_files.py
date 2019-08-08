import pandas as pd
import re
from utilities import files_metadata as fm


"""
Helper function to remove unwanted columns from a csv.
Can either return the modified df or write it to a file
"""


def remove_unused_cols(file_path, file_out_path, out_type, drop_cols, enc_type='utf-8'):
    initial_file = pd.read_excel(file_path, encoding=enc_type)
    initial_file_df = pd.DataFrame(initial_file)

    initial_file_req_df = initial_file_df.drop(drop_cols, axis=1)

    if out_type == 'file':
        initial_file_req_df.to_csv(file_out_path, encoding='utf-8', index=False)
    elif out_type == 'df':
        return initial_file_req_df


# Removing Byrne, LLEB, WEED, GOT_COPS, HIRING_TOT2, HIRING_RATE columns from main file which won't be used.
'''
remove_unused_cols(file_path='C:/Users/sshaik2/Criminal_Justice/Projects/main_census_merge/data/Final_Main_1990_2001.xlsx',
                   enc_type="ISO-8859-1", file_out_path='C:/Users/sshaik2/Criminal_Justice/Projects/main_census_merge/data/Final_Main_Var_1990_2001.csv',
                   drop_cols=['BYRNE_DISCRET_580', 'LLEBG_592', 'WEED_AND_SEED_595', 'GOT_COPS', 'HIRING_TOT2', 'HIRING_RATE'], out_type='file')
'''


"""
Remove 2nd column header row i.e Id, Id2, Geography etc..
Rename 
"""


def remove_unused_rows(file_path):
    initial_df = pd.DataFrame(pd.read_csv(file_path, encoding='utf-8'))
    # Dropping the 1st row which has Id, Id2, Geography etc.. values below the 1st column headers. drop() returns a new df
    reduced_df = initial_df.drop(initial_df.index[0])
    return reduced_df


"""
- renames 'GEO.display-label'column to 'placename'
- strip ',' and state name from placename value
"""


def remove_state_from_placename(pl_name, ptrn):
    pattern = re.compile(ptrn)
    match = pattern.search(pl_name)
    if match:
        return pl_name[:match.start()]
    else:
        return pl_name


"""
    extracts the corresponding 'P**' string from the filename and prefixes it to each of the column headers
"""


def update_census_file_headers(df_obj, file_path):
    # rename 'GEO.display-label' col
    df_obj.rename(columns={'GEO.display-label': 'placename'}, inplace=True)

    """
        Remove statename from placename variable
        Ex: Remove ",Alaska" from Anchorage municipality, Alaska
    """

    ############### To-Do: See if you can just split at , instead of using regex ###################
    df_obj['placename'] = df_obj['placename'].apply(remove_state_from_placename, args=('\,',))

    # extract file name from the file path
    file_name = file_path.split('/')[-1]

    # extract the corresponding 'P**' string from the filename
    file_type = file_name.split('_')[3]

    # get the list of column headers
    col_headers = list(df_obj)

    # create new list of column headers by appending correpsonding P*** string to the existing column headers
    new_col_headers = col_headers[:3]+list(file_type+x for x in col_headers[3:])
    df_obj.columns = new_col_headers
    return df_obj


"""
Write the modified df to modified_files folder
"""


def write_updated_df_file(updated_df, out_path):
    updated_df.to_csv(out_path, encoding='utf-8', index=False)


"""
Iterates over each directory(cities 00/10, counties 00/10) and then works on each census file within that directory
Uses remove_unused_rows, update_all_census_files functions to modify census files to have required headers with corresponding P*** prefixes
"""

if __name__ == '__main__':
    # get the list of input and output file path tuples
    file_paths_list = fm.find_files_path('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data',
                            ori_files_folder_name='reduced_census_files', mod_files_folder_name='updated_col_headers')


    # for every tuple of inp and out file paths, perform the reqd operations
    for f_paths in file_paths_list:
        ip_file, op_file = f_paths
        df1 = remove_unused_rows(ip_file)
        updated_df = update_census_file_headers(df1, ip_file)
        write_updated_df_file(updated_df, op_file)