import pandas as pd


# utility function to rearrange columns as per the given list
def rearrange_cols(df, col_list):
    # Rearrange columns such that ORI, AGENCY, placename, 'STATEFP', 'CNTY', 'place_fips' are at the beginning
    cols = list(df.columns.values)

    for col in col_list:
        cols.pop(cols.index(col))

    df_arranged = df[col_list + cols]

    return df_arranged


# utility function to rename columns as per the given mapping
def rename_cols(ip_fl_path, mapping_dict):
    # Had to initialize here before using in try block coz was throwing variable used before initializing error
    df = pd.DataFrame()
    try:
        # using ISO-8859-1 to address some encode/decode issues
        df = pd.read_csv(ip_fl_path, encoding = "ISO-8859-1")
    except Exception as ex:
        print(ex)
        print('Error reading file: ', ip_fl_path)

    # rename df column names using mapping dict
    df_renamed = df.rename(columns=mapping_dict)

    return df_renamed


# utility function to update fips column values as per the required length
def update_fips_code_len(fips_code, fp_type):
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
