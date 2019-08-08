import pandas as pd
import requests
import json
import csv
import os


def get_census_data_from_api(base_url, fips_df, op_file, census_year=None):
    """
    :param base_url: Different base url for 2000 and 2010 years
    :param fips_df: df with state and county fips codes
    :param op_file: op file name to which the census data needs to be written
    :param census_year: year for which decennial census data
    :return:
    """
    # take a count variable to help distinguish 1st request from subsequent requests so that we take the variable
    # names only from the 1st call as the header names and skip varibale names from the subsequent calls.
    count = 0
    # open a new file with the required output file name
    with open(
            f'/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/census_cities_1990/twnshps_api/{op_file}.csv',
            'w') as file_wrtr:
        # take a csv writer object to write to this output file
        op_file_writer = csv.writer(file_wrtr)

        # Iterate over each row in the state_county fips df
        for row in fips_df.itertuples():
            # create the rquest url for ecah state and fips code to get the data for all county subdivisions under it
            try:
                print('count: ', count)

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

                # 1990 codes
                # 1st call
                # url = f'{base_url}?get=ANPSADPI,STUSAB,P0100001,P0100002,P0100006,P0100007,P0100008,P0100009,P0100010,P0120001,P0120002,P0120003,P0120004,P0120005,P0120006,' \
                #       f'P0120007,P0120008,P0120009,P0120010,P0120011,P0120012,P0120013,P0120014,P0120015,P0120016,P0120017,P0120018,P0120019,P0120020,P0120021,' \
                #       f'P0120022,P0120023,P0120024,P0120025,P0120026,P0120027,P0120028,P0120029,P0120030,P0120031,P0120032,P0120033,P0120034,P0120035&for=county%20subdivision:*&' \
                #       f'in=state:{st_fips}%20county:{cnty_fips}&key=d2b9b07dfed3cc16bbb93f03b445c16a4fed0c72'

                # 2nd call
                # url = f'{base_url}?get=ANPSADPI,STUSAB,P0120036,P0120037,P0120038,P0120039,P0120040,P0120041,P0120042,P0120043,P0120044,P0120045,P0120046,P0120047,' \
                #       f'P0120048,P0120049,P0120050,P0120051,P0120052,P0120053,P0120054,P0120055,P0120056,P0120057,P0120058,P0120059,P0120060,P0120061,P0120062,P0120063,' \
                #       f'P0120064,P0120065,P0120066,P0120067,P0120068,P0120069,P0120070&for=county%20subdivision:*&' \
                #       f'in=state:{st_fips}%20county:{cnty_fips}&key=d2b9b07dfed3cc16bbb93f03b445c16a4fed0c72'

                # 3RD
                # url = f'{base_url}?get=ANPSADPI,STUSAB,P0120071,P0120072,P0120073,P0120074,P0120075,P0120076,P0120077,P0120078,P0120079,P0120080,P0120081,P0120082,P0120083,' \
                #       f'P0120084,P0120085,P0120086,P0120087,P0120088,P0120089,P0120090,P0120091,P0120092,P0120093,P0120094,P0120095,P0120096,P0120097,P0120098,P0120099,' \
                #       f'P0120100,P0120101,P0120102,P0120103,P0120104,P0120105,P0120106,P0120107,P0120108,P0120109,P0120110&for=county%20subdivision:*&' \
                #       f'in=state:{st_fips}%20county:{cnty_fips}&key=d2b9b07dfed3cc16bbb93f03b445c16a4fed0c72'

                # 4th
                # url = f'{base_url}?get=ANPSADPI,STUSAB,P0120111,P0120112,P0120113,P0120114,P0120115,P0120116,P0120117,P0120118,P0120119,P0120120,P0120121,P0120122,P0120123,' \
                #       f'P0120124,P0130001,P0130002,P0130003,P0130004,P0130005,P0130006,P0130007,P0130008,P0130009,P0130010,P0130011,P0130012,P0130013,P0130014,P0130015,' \
                #       f'P0130016,P0130017,P0130018,P0130019,P0130020,P0130021,P0130022,P0130023,P0130024&for=county%20subdivision:*&in=state:{st_fips}%20county:{cnty_fips}&' \
                #       f'key=d2b9b07dfed3cc16bbb93f03b445c16a4fed0c72'

                # 5th
                # url = f'{base_url}?get=ANPSADPI,STUSAB,P0130025,P0130026,P0130027,P0130028,P0130029,P0130030,P0130031,P0130032,P0130033,P0130034,P0130035,P0130036,P0130037,' \
                #       f'P0130038,P0130039,P0130040,P0130041,P0130042,P0130043,P0130044,P0130045,P0130046,P0130047,P0130048,P0130049,P0130050,P0130051,P0130052,P0130053,P0130054,' \
                #       f'P0130055,P0130056,P0130057,P0130058,P0130059,P0130060,P0130061,P0130062&for=county%20subdivision:*&in=state:{st_fips}%20county:{cnty_fips}&' \
                #       f'key=d2b9b07dfed3cc16bbb93f03b445c16a4fed0c72'

                # 6th - total persons
                url = f'{base_url}?get=P0010001&for=county%20subdivision:*&in=state:{st_fips}%20county:{cnty_fips}&key=d2b9b07dfed3cc16bbb93f03b445c16a4fed0c72'

                print(f'url at count{count}: ', url)
                response = requests.get(url)

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
                print('Error code: ', response.status_code)
                print('Error Response: ', response.content)
                print('Exception: ', ex)
                print('Total API Calls: ', count)
                break


# Get 2000 township census data
# st_cnty_fips_00 = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/helper_files/st_cnty_fips_2000.csv')
# get_census_data_from_api('https://api.census.gov/data/2000/sf1', st_cnty_fips_00, 'new_census_townships_00_initial') # 3141 calls

# Get 2010 township census data
# st_cnty_fips_10 = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/helper_files/st_cnty_fips_10_temp.csv')
# get_census_data_from_api('https://api.census.gov/data/2010/dec/sf1', st_cnty_fips_10, 'new_census_townships_10_initial_16th', 2010)

# Get 1990 township census data
fips_90 = pd.read_csv(
    '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/helper_files/st_cnty_fips_1990.csv')
# st_cnty_fips_90 = fips_90[fips_90['county'].isnull]
# get_census_data_from_api('https://api.census.gov/data/1990/sf1', fips_90, 'new_census_for_tships_90_total_pop', 1990)

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


final_df = create_final_twnshp_file(
    '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/census_cities_1990/twnshps_api',
    '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/census_cities_1990/new_census_townships_90_initial.csv')

# sort the final df by state, county and then county subdivision to make sure they are in required ascending order. Default is ascending
final_df_sorted = final_df.sort_values(by=['state', 'county', 'county subdivision'])

# write the final df to a csv
final_df_sorted.to_csv(
    '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/census_cities_1990/new_census_townships_90.csv',
    index=False)