import pandas as pd
from utilities import files_metadata as fm

pd.options.mode.chained_assignment = None  # default='warn'
"""
TO BE IN SYNC WITH National_Census_1990_All FILE

Notes: Specify the correct index for county and city files respectively.
       Specify the year as needed to skip the 1st row.
       Specify code type as county when working with county files so that appropriate columns are created.
"""

# Every time a file is read get the census type and census year to be used across various functions

census_type = ''
census_year = ''


"""
Returns the census type of the current file being read
"""





# """
# Reads the original csv and returns it in a data-frame
# """
#
#
# def get_df(file_path):
#     init_df = pd.DataFrame(pd.read_csv(file_path))
#     # Removing the 2nd row with Id, Id2 etc ..
#     reduced_df = init_df.drop(init_df.index[0])
#     return reduced_df


"""
 Return GEO.id2 column as a series of strings to apply the split_geo_id2 function to each element of the column
"""


def get_geo_geo_id2_ser(ini_df):
    ini_df['GEO.id2'] = ini_df['GEO.id2'].astype(str)
    return pd.Series(ini_df['GEO.id2'])


"""
Helper function to split GEO.id2 column values
split_index is the position where place_fips code ends from the end(reverse) in GEO.id2
"""


def split_geo_id2(geo_id2, split_index, code_type=None):
    if code_type == 'place_fips' or code_type == 'CNTY':
        return geo_id2[split_index:]
    else:
        # if not place_fips/CNTY, then we need STATEFP from GEO.id2 which would be the indices before place_fips
        return geo_id2[:split_index]


"""
Helper function to prefix county fips value with zeroes as required so as to make all of them 3 chars long 
"""


def update_code_len(fips_code, fp_type):
    req_code_len = 0  # placeholder to assign required code length based on whether it is a city, county or state fips code.
                       # For now cnty and placefips ar of reqd len coz considered as strings. but can have below code for future use
    fp_code_len = fips_code.__len__()

    if fp_type == 'city':
        req_code_len = 5
    elif fp_type == 'county':
        req_code_len = 3
    elif fp_type == 'state':
        req_code_len = 2

    if fp_code_len < req_code_len:
        while fips_code.__len__() < req_code_len:
            fips_code = '0'*(req_code_len-fp_code_len) + fips_code
            return fips_code
    else:
        return fips_code


"""
Helper function to create a new column with constant value
"""


def create_new_col(df, new_col_list):
    for col_name, col_val in new_col_list.items():
        df[col_name] = col_val
    return df


"""
Helper function to move columns to the required locations
@Params:
    df = df in context whose columns need to be rearranged
    df_cols = list of columns of the df in context
    cols_dict = mapping of columns and their desired indexes
"""


def arrange_cols(df, df_cols, cols_dict):
    for ind, col in cols_dict.items():
        df_cols.insert(ind, df_cols.pop(df_cols.index(col)))
    return df.reindex(columns=df_cols)


"""
Create place_fips, CNTY and STATEFP columns
"""


def create_fips_cols(ini_df, geo_id2_ser):
    split_index = None # placeholder to set split_index based on the census type -> -3 for county and -5 for city

    """
    3) Create a new place_fips column by splitting the place_fips code value from GEO.id2 column
        Convert place_fips/CNTY column types back to int64 to be in sync with the column types in final main file.
    """
    if census_type == 'county':
        split_index = -3

        # split county code from geo id2
        ini_df['CNTY'] = geo_id2_ser.apply(split_geo_id2, args=(split_index, 'CNTY'))
        ini_df['place_fips'] = ['99'+x for x in ini_df['CNTY']]

        # create a Govt_level column with value 1 for county
        ini_df = create_new_col(ini_df, new_col_list={'Govt_level': 1})

    elif census_type == 'city':
        split_index = -5

        # get fips place code from geo id2
        ini_df['place_fips'] = geo_id2_ser.apply(split_geo_id2, args=(split_index, 'place_fips')) ###### TO-DO: May be we don't need 'place-fips' here. CHECk #########

        # create a blank CNTY column and Govt_level with value 3 for city census
        ini_df = create_new_col(ini_df,  new_col_list={'CNTY':'', 'Govt_level': 3})

    """
    4) Create a new STATEFP column by splitting the STATEFP code value from GEO.id2 column
    """
    # First get the state fips code from geo id2
    ini_df['STATEFP'] = geo_id2_ser.apply(split_geo_id2, args=(split_index, ))

    # Convert all state fips codes to be 2 chars long by prefixing with 0s as required
    fips_code_type = 'state'
    ini_df['STATEFP'] = ini_df['STATEFP'].apply(update_code_len, args=(fips_code_type, ))

    # Create a YEAR column with value = census_year obtained at the beginning while reading the file
    ini_df = create_new_col(ini_df, new_col_list={'YEAR': census_year})

    # dropping GEO.id, GEO.id2 columns as they no longer will be needed in the final national census all file
    ini_df = ini_df.drop(['GEO.id', 'GEO.id2'], axis=1)

    """
    6) Place Govt_level in 1st col, place_fips in 2nd col, placename in 3rd col, CNTY in 4th col and STATEFP in 5th col
    """
    df_cols = ini_df.columns.tolist()  # to get a list of columns

    ini_df = arrange_cols(ini_df, df_cols, {0:'Govt_level', 1:'place_fips', 2:'placename', 3:'CNTY', 4:'STATEFP', 5:'YEAR'})

    return ini_df


"""
To write final df to a csv
"""

#
# def create_updated_csv(fnl_df, file_path, enc='utf-8', ind_val=False, file_type=N):
#     fnl_df.to_csv(file_path, encoding=enc, index=ind_val)
#     fnl_df = pd.read_csv(file_path)


def get_updated_census_cols(file_path):
    """
    1) Obtain the original csv in an initial df
    """
    initial_df = pd.DataFrame(pd.read_csv(file_path))

    """
    2) convert GEO.id2 of int64 type to str type to split into fips state and fips place code respectively and get GEO.id2 column  
    """
    ############ To-Do: see if you can just do 1 liner without having to use a function like this ##############
    geo_id2_series = get_geo_geo_id2_ser(initial_df)

    """
    3) Create df with place_fips/CNTY, STATEFP, YEAR columns
    """
    mod_df = create_fips_cols(ini_df=initial_df, geo_id2_ser=geo_id2_series)

    return mod_df


############### TO-DO: Automate reading of files from the required directory so that all files are modified as required with single run of the program ######################

if __name__ == '__main__':
    # First obtain the paths to read input file and to write output file
    fp_list = fm.find_files_path('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data', 'updated_col_headers', 'new_fips_cols')

    for fp_elem in fp_list:
        inp_file_path, out_file_path = fp_elem
        # Second, obtain census_type and census_year values
        (census_type, census_year) = fm.get_census_type_year(inp_file_path)

        if census_year == '00':
            census_year = 2000
        elif census_year == '10':
            census_year = 2010

        # Get a new df with the required columns
        modified_df = get_updated_census_cols(inp_file_path)

        # Write the final modified df to an output csv
        modified_df.to_csv(out_file_path, index=False)
