import pandas as pd


def create_fips_cols(incarc_df):
    """
    Get the below required vars
        year
        fips
        state
        county_name
        urbanicity
        metro_area
        land_area
        total_jail_pop
        black_jail_pop
        latino_jail_pop
        white_jail_pop
        total_prison_pop
        black_prison_pop
        latino_prison_pop
        white_prison_pop
        total_prison_adm
        black_prison_adm
        latino_prison_adm
        white_prison_adm
        capacity
    """

    incarc_req = incarc_df[['year','fips','state','county_name','urbanicity','metro_area','land_area','total_jail_pop','black_jail_pop','latino_jail_pop',
                            'white_jail_pop','total_prison_pop','black_prison_pop','latino_prison_pop','white_prison_pop','total_prison_adm','black_prison_adm',
                            'latino_prison_adm','white_prison_adm','capacity']]


    """
        Create fips state and fips county codes from fips column
        split fips at 3rd index from right
    """

    # split state and county code from fips:  STATEFP	CNTY
    incarc_req['STATEFP'] = [str(x)[:-3] for x in incarc_req['fips']]
    incarc_req['CNTY'] = [str(x)[-3:] for x in incarc_req['fips']]


    # Get only fips, year and jail_interp vars from David's jail pop interpolated file
    intpltd_incarc = pd.read_excel('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/incarceration/incarc_interpol_final_salma.xlsx')
    intpltd_incarc = intpltd_incarc[['fips', 'year', 'jail_interp']]

    #  merge david's jail pop interpolated file on fips to get the
    incarc_req = incarc_req.merge(intpltd_incarc, on=['fips', 'year'])
    #incarc_req.drop(['fips'], axis=1, inplace=True)
    incarc_req.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/incarceration/incarc_req_vars_updated_fips.csv', index=False)


incarc_df = pd.read_excel('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/incarceration/incarc_all_1990_2015.xlsx')

create_fips_cols(incarc_df)
