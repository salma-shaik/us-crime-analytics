import pandas as pd
import numpy as np

"""
Govt_level	        3 default
place_fips	        county subdivision
placename	        ANPSADPI
CNTY	            county
STATEFP	            state
YEAR	            1990 default
POP100	            P0010001

ANPSADPI
STUSAB
state
county
county subdivision
"""


def create_fixed_columns(twnshp_df, new_df, cen_year):
    new_df['place_fips'] = twnshp_df['county subdivision']
    new_df['placename'] = twnshp_df['ANPSADPI']
    new_df['CNTY'] = twnshp_df['county']
    new_df['STATEFP'] = twnshp_df['state']
    new_df['POP100'] = twnshp_df['P0010001']
    # If I place constant value columns at the beginning they are getting set to NaN. dtype conversion?
    new_df['Govt_level'] = 3
    new_df['YEAR'] = cen_year
    return new_df


"""
    White_count	            P0100001
    Black_count	            P0100002
    Hispanic_count	        sum(P0100006,P0100007,P0100008,P0100009,P0100010)
    Age1524_WhiteM	        sum(of P0120010 - P0120017)
    White_Males_All         sum(of P0120001 - P0120031);
    Age1524_WhiteF          sum(of P0120041 - P0120048);
    White_Females_All       sum(of P0120032 - P0120062);
    Age1524_BlackM          sum(of P0120072-P0120079);
    Black_Males_All         sum(of P0120063-P0120093);
    Age1524_BlackF          sum(of P0120103-P0120110);
    Black_Females_All       sum(of P0120094-P0120124);
    Hispan_Males_All        sum(of P0130001-P0130031);
    Age1524_HispanM         sum(of P0130010-P0130017);
    Age1524_HispanF         sum(of P0130041-P0130048);
    Hispan_Females_All      sum(of P0130032-P0130062);
    Other_Males_All         sum(of P0120249-P0120279);
    Age1524_OtherM          sum(of P0120258-P0120265);
    Age1524_OtherF          sum(of P0120289- P0120296);
    Other_Females_All       sum(of P0120280-P0120310);
    Pct_WYM                 Age1524_WhiteM/White_Males_All;
    Pct_WYF                 Age1524_WhiteF/White_Females_All;

"""


def create_race_cols(ini_df, new_df):
    new_df['White_count'] = ini_df.loc[:, ['P0100001']]

    new_df['Black_count'] = ini_df.loc[:, ['P0100002']]

    new_df['Hispanic_count'] = ini_df.loc[:, ['P0100006', 'P0100007', 'P0100008', 'P0100009', 'P0100010']].sum(axis=1)

    new_df['Age1524_WhiteM'] = ini_df.loc[:, ['P0120010', 'P0120011', 'P0120012', 'P0120013', 'P0120014', 'P0120015', 'P0120016', 'P0120017']].sum(axis=1)

    new_df['White_Males_All'] = ini_df.loc[:, ['P0120001', 'P0120002', 'P0120003', 'P0120004', 'P0120005', 'P0120006', 'P0120007', 'P0120008', 'P0120009', 'P0120010','P0120011', 'P0120012', 'P0120013', 'P0120014', 'P0120015', 'P0120016', 'P0120017', 'P0120018', 'P0120019', 'P0120020',
                                               'P0120021', 'P0120022', 'P0120023', 'P0120024', 'P0120025', 'P0120026', 'P0120027', 'P0120028', 'P0120029', 'P0120030','P0120031']].sum(axis=1)

    new_df['Age1524_WhiteF'] = ini_df.loc[:, ['P0120041', 'P0120042', 'P0120043', 'P0120044', 'P0120045', 'P0120046', 'P0120047', 'P0120048']].sum(axis=1)

    new_df['White_Females_All'] = ini_df.loc[:, ['P0120032','P0120033', 'P0120034', 'P0120035', 'P0120036', 'P0120037', 'P0120038', 'P0120039', 'P0120040','P0120041', 'P0120042', 'P0120043', 'P0120044', 'P0120045', 'P0120046', 'P0120047', 'P0120048', 'P0120049', 'P0120050','P0120051', 'P0120052',
                                                 'P0120053', 'P0120054', 'P0120055', 'P0120056', 'P0120057', 'P0120058', 'P0120059', 'P0120060','P0120061', 'P0120062']].sum(axis=1)

    new_df['Age1524_BlackM'] = ini_df.loc[:, ['P0120072', 'P0120073', 'P0120074', 'P0120075', 'P0120076', 'P0120077', 'P0120078', 'P0120079']].sum(axis=1)

    new_df['Black_Males_All'] = ini_df.loc[:, ['P0120063', 'P0120064', 'P0120065', 'P0120066', 'P0120067', 'P0120068', 'P0120069', 'P0120070', 'P0120071', 'P0120072','P0120073', 'P0120074', 'P0120075', 'P0120076', 'P0120077', 'P0120078', 'P0120079', 'P0120080', 'P0120081', 'P0120082',
                                               'P0120083', 'P0120084', 'P0120085', 'P0120086', 'P0120087', 'P0120088', 'P0120089', 'P0120090', 'P0120091', 'P0120092','P0120093']].sum(axis=1)

    new_df['Age1524_BlackF'] = ini_df.loc[:, ['P0120103', 'P0120104', 'P0120105', 'P0120106', 'P0120107', 'P0120108', 'P0120109', 'P0120110']].sum(axis=1)

    new_df['Black_Females_All'] = ini_df.loc[:, ['P0120094', 'P0120095', 'P0120096', 'P0120097', 'P0120098', 'P0120099', 'P0120100', 'P0120101', 'P0120102',
                                                 'P0120103', 'P0120104', 'P0120105', 'P0120106', 'P0120107', 'P0120108', 'P0120109', 'P0120110', 'P0120111', 'P0120112','P0120113', 'P0120114', 'P0120115', 'P0120116', 'P0120117', 'P0120118', 'P0120119', 'P0120120', 'P0120121', 'P0120122',
                                                 'P0120123', 'P0120124']].sum(axis=1)

    new_df['Age1524_HispanicM'] = ini_df.loc[:, ['P0130010','P0130011', 'P0130012', 'P0130013', 'P0130014', 'P0130015', 'P0130016', 'P0130017']].sum(axis=1)

    new_df['Hispanic_Males_All'] = ini_df.loc[:, ['P0130001', 'P0130002', 'P0130003', 'P0130004', 'P0130005', 'P0130006', 'P0130007', 'P0130008', 'P0130009', 'P0130010','P0130011', 'P0130012', 'P0130013', 'P0130014', 'P0130015', 'P0130016', 'P0130017', 'P0130018', 'P0130019', 'P0130020',
                                                  'P0130021', 'P0130022', 'P0130023', 'P0130024', 'P0130025', 'P0130026', 'P0130027', 'P0130028', 'P0130029', 'P0130030','P0130031']].sum(axis=1)

    new_df['Age1524_HispanicF'] = ini_df.loc[:, ['P0130041', 'P0130042', 'P0130043', 'P0130044', 'P0130045', 'P0130046', 'P0130047', 'P0130048']].sum(axis=1)

    new_df['Hispanic_Females_All'] = ini_df.loc[:, ['P0130032', 'P0130033', 'P0130034', 'P0130035', 'P0130036', 'P0130037', 'P0130038', 'P0130039', 'P0130040',
                                                    'P0130041', 'P0130042', 'P0130043', 'P0130044', 'P0130045', 'P0130046', 'P0130047', 'P0130048', 'P0130049', 'P0130050','P0130051', 'P0130052', 'P0130053', 'P0130054', 'P0130055', 'P0130056', 'P0130057', 'P0130058', 'P0130059', 'P0130060',
                                                    'P0130061', 'P0130062']].sum(axis=1)

    return new_df


"""
    Pct_WYM	Age1524_WhiteM/White_Males_All
    Pct_WYF	Age1524_WhiteF/White_Females_All
"""


def create_white_perc_cols(new_df):
    new_df['Pct_WYM'] = new_df['Age1524_WhiteM'] / new_df['White_Males_All']
    new_df['Pct_WYF'] = new_df['Age1524_WhiteF'] / new_df['White_Females_All']
    return new_df


def write_final_df_csv(final_df, op_file):
    cols = list(final_df)
    cols.pop(cols.index('place_fips'))
    cols.pop(cols.index('placename'))
    cols.pop(cols.index('CNTY'))
    cols.pop(cols.index('STATEFP'))
    cols.pop(cols.index('POP100'))
    cols.pop(cols.index('Govt_level'))
    cols.pop(cols.index('YEAR'))

    # Arrange the columns in order similar to city and county census files
    final_df_arngd = final_df[['Govt_level', 'place_fips', 'placename', 'CNTY', 'STATEFP', 'YEAR', 'POP100'] + cols]

    # Write the final df with new vars to a csv
    final_df_arngd.to_csv(f'/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/census_cities_1990/{op_file}.csv',index=False)

new_twnshp_df = pd.DataFrame()

"""
Create new vars for 1990 township file
"""
ini_twnshp_df = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/cen_90/census_cities_1990/new_census_townships_90.csv')
new_twnshp_df = create_fixed_columns(ini_twnshp_df, new_twnshp_df, 1990)
new_twnshp_race_df = create_race_cols(ini_twnshp_df, new_twnshp_df)
new_twnshp_race_pct_df = create_white_perc_cols(new_twnshp_race_df)

write_final_df_csv(new_twnshp_race_pct_df, 'new_census_townships_90_new_vars')


def update_90_census_with_new_twnshps():
    # 1st get the correct glevels for townships into the new township census file from the crime file
    crime_major_gov_fips = pd.read_csv(
        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/cleaned_files/crime/Crime_Major_Gov_Fips.csv')
    townships_new_census_vars_90 = pd.read_csv(
        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/census_cities_1990/new_census_townships_90_new_vars.csv')

    townships_new_census_vars_90_glevel = townships_new_census_vars_90.merge(crime_major_gov_fips, on=['STATEFP', 'place_fips'], how='right')

    # Get only glevel 3 entries
    townships_new_census_vars_90_glevel = townships_new_census_vars_90_glevel[(townships_new_census_vars_90_glevel.Govt_level_y == 3)]
    # rename Govt_level_y to Govt_level and CNTY_y to CNTY and then drop CNTY_x, Govt_level_x
    townships_new_census_vars_90_glevel.rename({'Govt_level_y': 'Govt_level', 'CNTY_y': 'CNTY'}, axis=1, inplace=True)
    townships_new_census_vars_90_glevel.drop(['Govt_level_x', 'CNTY_x'], axis=1, inplace=True)

    # Read the initial census file merged with crime for glevels
    nat_cen_90_unique_glevels = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/cen_90/Census_1990_Crime_Merge_Right.csv')

    # Get only the glevel 1 and glevel 2 entries from nat_cen_90_unique
    cen_90_cnty_city = nat_cen_90_unique_glevels[(nat_cen_90_unique_glevels.Govt_level == 1) | (nat_cen_90_unique_glevels.Govt_level == 2)]

    # 9890 cities in 1990 where as 10057(2000), 10091(2010). So trying to get the cities that are new 90 api cen but not in earlier one.
    townships_new_census_vars_90_glevel_2 = townships_new_census_vars_90_glevel[(townships_new_census_vars_90_glevel.Govt_level == 2)]

    """
    find elements in one list that are not present in another list
    import numpy as np
    list_1 = ["a", "b", "c", "d", "e"]
    list_2 = ["a", "f", "c", "m"]
    main_list = np.setdiff1d(list_2,list_1)
    """
    mcng_cities = np.setdiff1d(list(townships_new_census_vars_90_glevel_2['ORI']), list(cen_90_cnty_city['ORI']))
    print('mcng_cities: ', mcng_cities) # 0

   # cities_new_cen_vars_90 = townships_new_census_vars_90_glevel[(townships_new_census_vars_90_glevel.Govt_level == 2)]
    # append the new townships to the bottom of initial counties and cities.
    cen_90_new_twnshps = cen_90_cnty_city.append([townships_new_census_vars_90_glevel], sort=False)

    # there are 3 entries with only POP100, drop them
    cen_90_new_twnshps.drop(cen_90_new_twnshps.loc[cen_90_new_twnshps['place_fips'].isnull()].index, inplace=True)
    cen_90_new_twnshps.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/cen_90/census_cities_1990/new_census_variables/cen_90_ini_cnty_city_new_twnshp_glevels.csv', index=False)


update_90_census_with_new_twnshps()