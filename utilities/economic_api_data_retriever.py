import pandas as pd
import requests
import json
import csv
import os


def get_economic_data_from_api(base_url, vars_str, fips_df,  op_file, geo_type=None, census_year=None):
    """
    :param base_url: Different base url for 2000 and 2010 years
    :param fips_df: df with state and county fips codes
    :param op_file: op file name to which the census data needs to be written
    :param census_year: year for which decennial census data
    :return:
    """
    # take a count variable to help distinguish 1st request from subsequent requests so that we take the variable
    # names only from the 1st call as the header names and skip varibale names from the subsequent calls.
    response = ''
    count = 0
    # open a new file with the required output file name
    with open(
            f'{op_file}', 'w') as file_wrtr:
        # take a csv writer object to write to this output file
        op_file_writer = csv.writer(file_wrtr)

        states_list = []
        # Iterate over each row in the state_county fips df
        for row in fips_df.itertuples():
            # create the rquest url for ecah state and fips code to get the data for all county subdivisions under it
            try:
                """ Use timer if needed """
                # if count in [500, 1000, 1500, 2000, 2500, 3000]:
                #     time.sleep(3600)

                st_fips = str(getattr(row, "state"))

                if census_year == 1990:
                    # county from county fips file was being read as float!?!!? so converting to int before converting to string
                    cnty_fips = str(int(getattr(row, "county")))
                else:
                    cnty_fips = str(getattr(row, "county"))

                if census_year != 2000:
                    # for 1990 and 2010, state and county fips need to of size 2 and 3 respectively. Hence prepend with zeroes as required
                    if st_fips.__len__() < 2:
                        st_fips = '0' + st_fips

                    if cnty_fips.__len__() < 3:
                        cnty_fips = ('0' * (3 - cnty_fips.__len__())) + cnty_fips

                # 2000 / 2010 codes
                # response = requests.get(f'{base_url}?get=NAME,P012001,P012A001,P012B001,P012H001,P012A006,P012A007,P012A008,P012A009,P012A010,P012A002,P012A030,P012A031,P012A032,P012A033,P012A034,P012A026,P012B006,P012B007,P012B008,P012B009,P012B010,P012B002,P012B030,P012B031,P012B032,P012B033,P012B034,P012B026,P012H002,P012H006,P012H007,P012H008,P012H009,P012H010,P012H030,P012H031,P012H032,P012H033,P012H034,P012H026&for=county%20subdivision:*&in=state:{st_fips}%20county:{cnty_fips}&key=d2b9b07dfed3cc16bbb93f03b445c16a4fed0c72')

                # appending each state fips to the states_list coz we need only unique st fips for places
                states_list.append(st_fips)

                if geo_type == 'county':
                    url = f'{base_url}?get={vars_str}&for=county:{cnty_fips}&in=state:{st_fips}&key=d2b9b07dfed3cc16bbb93f03b445c16a4fed0c72'
                elif geo_type == 'place':
                    # need to make only one call for each state fips to get all the places info under it. So making a request only if there is one entry for a given state fips in the states_list
                    if states_list.count(st_fips) == 1:
                        url = f'{base_url}?get={vars_str}&for=place:*&in=state:{st_fips}&key=aefa63e9ca460169068f42b9ebc3101db025882f'
                    else:
                        continue
                else:
                    url = f'{base_url}?get={vars_str}&for=county%20subdivision:*&in=state:{st_fips}%20county:{cnty_fips}&key=aefa63e9ca460169068f42b9ebc3101db025882f'

                print(f'url at count{count}: ', url)

                headers = requests.utils.default_headers()
                headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36'
                response = requests.get(url, headers=headers)

                """
                    White_count=P0100001;

                    Black_count=P0100002;

                    Hispan_allcount=sum(P0100006,P0100007,P0100008,P0100009,P0100010);

                    P0120001 to P0120124

                    P0130001 to P0130062       
                """

                # load the json in to python object which would be list of all entries in the json object
                resp = json.loads(response.content)
                # If this is the first call(count=0), then write the entire content so that the 1st row with the variable names is the header
                if count == 0:
                    # iterate over respone python object and write each row to the csv
                    for res in resp:
                        op_file_writer.writerow(res)
                else:
                    # skipping 1st row which are the variable names starting from 2nd calls.
                    for res in resp[1:]:
                        op_file_writer.writerow(res)

                count += 1

            except Exception as ex:
                op_file_writer.writerow([])
                print('Error code: ', response.status_code)
                print('Error Response: ', response.content)
                print('Exception: ', ex)
                print('Total API Calls: ', count)
                break


"""
    Get 1990 economic census data - 3006 calls
"""

# st_cnty_fips_90 = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/helper_files/st_cnty_fips_1990.csv')

# 1. Get the county level data. Geo: state› county. All counties in a state
# get_economic_data_from_api(base_url='https://api.census.gov/data/1990/sf3', vars_str='ANPSADPI,P114A001,P115A001,P115A002,P0700001,P0700002,P0720001,P0720002,P0700005,P0700006,P0710001,P0710002,P0710005,P0710006,P0710009,P0710010,P0710013,P0710014', fips_df=st_cnty_fips_90, op_file='eco_cen_90_cnty_initial', geo_type='county', census_year=1990)


"""
   Get 2000 economic census data - 3139 calls
"""

# st_cnty_fips_00 = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/helper_files/st_cnty_fips_2000.csv')

# 1. Get the county level data. Geo: state› county. All counties in a state - 3007 calls
# get_economic_data_from_api(base_url='https://api.census.gov/data/2000/sf3', vars_str='NAME,P043001,P082001,P157A001,P157I001,P157B001,P157H001,P043004,P043006,P043011,P043013,P150A004,P150A006,P150A011,P150A013,P150B004,P150B006,P150B011,P150B013,P150I004,P150I006,P150I011,P150I013,P150H004,P150H006,P150H011,P150H013', fips_df=st_cnty_fips_00, op_file='eco_cen_00_cnty_initial', geo_type='county', census_year=2000)


"""
   Get 2010 economic census data - 2012 acs data centered on 2010
"""

# st_cnty_fips_10 = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/helper_files/st_cnty_fips_2010.csv')


# 2. Get the place level data. Geo: state› place. All places in a state
# till B23001_093E
# get_economic_data_from_api(base_url='https://api.census.gov/data/2012/acs/acs5', vars_str='NAME,B19301_001E,B19301A_001E,B19301B_001E,B19301H_001E,B19301I_001E,B23001_005E,B23001_012E,B23001_019E,B23001_026E,B23001_033E,B23001_040E,B23001_047E,B23001_054E,'
#                                                                                      'B23001_061E,B23001_068E,B23001_007E,B23001_014E,B23001_021E,B23001_028E,B23001_035E,B23001_042E,B23001_049E,B23001_056E,B23001_063E,B23001_070E,B23001_075E,B23001_080E,'
#                                                                                      '.=B23001_085E,B23001_091E,B23001_098E,B23001_105E,B23001_112E,B23001_119E,B23001_126E,B23001_133E,B23001_140E,B23001_147E,B23001_154E,B23001_093E', fips_df=st_cnty_fips_10, op_file='eco_cen_10_place_initial', geo_type='place', census_year=2010)


# from B23001_100E
# get_economic_data_from_api(base_url='https://api.census.gov/data/2012/acs/acs5', vars_str='NAME,B23001_100E,B23001_107E,B23001_114E,B23001_121E,B23001_128E,B23001_135E,B23001_142E,B23001_149E,B23001_156E,B23001_161E,B23001_166E,B23001_171E,C24010_002E,B23001_001E,'
#                                                                                          'C23002H_005E,C23002H_007E,C23002H_012E,C23002H_018E,C23002H_020E,C23002H_025E,C23002A_005E,C23002A_007E,C23002A_012E,C23002A_018E,C23002A_020E,C23002A_025E,'
#                                                                                          'C23002B_005E,C23002B_007E,C23002B_012E,C23002B_018E,C23002B_020E,C23002B_025E,C23002I_005E,C23002I_007E,C23002I_012E,C23002I_018E,C23002I_020E,C23002I_025E', fips_df=st_cnty_fips_10, op_file='eco_cen_10_place_4mB23001_100E_initial', geo_type='place', census_year=2010)



"""
    Get 2015 economic census data - 2017 acs data centered on 2015
"""
# st_cnty_fips_10 = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/helper_files/st_cnty_fips_2010.csv')
# st_cnty_fips_2010 = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/helper_files/st_cnty_fips_2010_4mst51_cnty177.csv')
# # 1. Get the county level data. Geo: state› county. All counties in a state
# # till B23001_093E
# get_economic_data_from_api(base_url='https://api.census.gov/data/2017/acs/acs5',
#                            vars_str='NAME,B23001_100E,B23001_107E,B23001_114E,B23001_121E,B23001_128E,B23001_135E,B23001_142E,B23001_149E,B23001_156E,B23001_161E,B23001_166E,B23001_171E,C24010_002E,B23001_001E,'
#                                     'C23002H_005E,C23002H_007E,C23002H_012E,C23002H_018E,C23002H_020E,C23002H_025E,C23002A_005E,C23002A_007E,C23002A_012E,C23002A_018E,C23002A_020E,C23002A_025E,'
#                                     'C23002B_005E,C23002B_007E,C23002B_012E,C23002B_018E,C23002B_020E,C23002B_025E,C23002I_005E,C23002I_007E,C23002I_012E,C23002I_018E,C23002I_020E,C23002I_025E',
#                            fips_df=st_cnty_fips_2010,
#                            op_file='/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/economic/new_eco_cen_vars/2015/eco_cen_10_cnty_4mB23001_100E_initial_5.csv',
#                            geo_type='county',
#                            census_year=2015)



"""
    place level data from B23001_100E
"""
st_cnty_fips_2010 = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/helper_files/st_cnty_fips_2010_mod.csv')

get_economic_data_from_api(base_url='https://api.census.gov/data/2017/acs/acs5',
                           vars_str='NAME,B23001_100E,B23001_107E,B23001_114E,B23001_121E,B23001_128E,B23001_135E,B23001_142E,B23001_149E,B23001_156E,B23001_161E,B23001_166E,B23001_171E,'
                                     'C24010_002E,B23001_001E,C23002H_005E,C23002H_007E,C23002H_012E,C23002H_018E,C23002H_020E,C23002H_025E,C23002A_005E,C23002A_007E,C23002A_012E,C23002A_018E,'
                                     'C23002A_020E,C23002A_025E,C23002B_005E,C23002B_007E,C23002B_012E,C23002B_018E,C23002B_020E,C23002B_025E,C23002I_005E,C23002I_007E,C23002I_012E,C23002I_018E,'
                                     'C23002I_020E,C23002I_025E',
                           fips_df=st_cnty_fips_2010,
                           op_file='/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/economic/new_eco_cen_vars/2015/eco_cen_15_place_from B23001_100E_initial_1.csv',
                           geo_type='place',
                           census_year=2015)

"""
    16 files for 2010 census due to the limitations on # of API calls per hour.
    Hence need to iterate over the files in respective folder and concatenate all to the 1st file

    Almost 200 variables for 1990 but only 50 allowed in the request url. 
    So need to concatenate the individual files(corresponding to 50 vars) vertically.
"""


def create_final_twnshp_file(twnshp_dir, first_file):
    # Read the initial file
    twnshp_1st_file_df = pd.read_csv(first_file)

    # Change to the twnshp cen dir
    os.chdir(twnshp_dir)

    for f in os.listdir():
        if f != '.DS_Store' & f != first_file:
            # Read all the twnshp census files and append to the list
            df = pd.read_csv(f)
            # twnshp_1st_file_df = twnshp_1st_file_df.append([df])
            # check if list1 contains all elements in list2
            if all(elem in list(df) for elem in ['ANPSADPI', 'STUSAB']):
                df.drop(['ANPSADPI', 'STUSAB'], axis=1, inplace=True)

            twnshp_1st_file_df = twnshp_1st_file_df.merge(df, on=['state', 'county', 'county subdivision'])
            # twnshp_1st_file_df = pd.concat([twnshp_1st_file_df, df], axis=1)
    # return the final df
    return twnshp_1st_file_df


# final_df = create_final_twnshp_file(
#     '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/census_cities_1990/twnshps_api',
#     '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/census_cities_1990/new_census_townships_90_initial.csv')
#
# # sort the final df by state, county and then county subdivision to make sure they are in required ascending order. Default is ascending
# final_df_sorted = final_df.sort_values(by=['state', 'county', 'county subdivision'])
#
# # write the final df to a csv
# final_df_sorted.to_csv(
#     '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/census_cities_1990/new_census_townships_90.csv',
#     index=False)