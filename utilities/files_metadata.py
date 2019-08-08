import os
import shutil


def find_files_path(data_files_path, ori_files_folder_name, mod_files_folder_name, dir_list=False):
    """
    To get the complete file paths of input files from each subdirectory that need to be worked upon.
    Then create output file destination (complete path) from the input file location to be used in to_csv to write the modified file to.

    :param data_files_path: dir which contains the required subfolders to work with
    :param ori_files_folder_name: dir which contains initial files to be worked upon
    :param mod_files_folder_name: dir to which modified files are written
    :return: list of input and output file path tuples
    """

    # empty list to hold the ip and op file path tuples
    fp_list=[]
    # Switch to the directory which has all the data folders/files
    os.chdir(data_files_path)

    for census_dir in os.listdir():
        # to consider only those dirs that are passed in the dir_list
        if census_dir in dir_list:
            census_folder_path = data_files_path+'/'+census_dir

            # move into the county/city census dir
            os.chdir(census_folder_path)

            # overwrite the mod files folder if it already exists
            out_dir_path = census_folder_path + '/' + mod_files_folder_name
            if os.path.exists(out_dir_path):
                shutil.rmtree(out_dir_path)
            os.mkdir(out_dir_path)
            # os.makedirs(out_dir_path) - if subdirectories. Implement if needed like may be pass a list and mkdirs if list len > 1

            # get a list of input files and capture their paths
            for sub_dir in os.listdir():
                if sub_dir == ori_files_folder_name:
                    sub_dir_path = census_folder_path+'/'+sub_dir
                    os.chdir(sub_dir_path)
                    for f in os.listdir():
                        # create input file path
                        in_file = sub_dir_path + '/' + f
                        # create output file path
                        out_file = out_dir_path + '/' + f
                        fp_list.append((in_file, out_file))
    return fp_list


# pass the indexes of census type and year word locations in the file name if reqd.
# Need to agree upon either having uniform file names or passing on the indexes
def get_census_type_year(file_path):
    cen_type = ''
    # Get a list of all the navigation folders in the file path
    fp_words = file_path.split('/')

    # Get a list of words in the folder name
    fdn_words = fp_words[-3].split('_')

    if 'county' in fdn_words:
        cen_type = 'county'
    elif 'cities' in fdn_words:
        cen_type = 'city'

    # Extract the year from the file name list of words
    cen_year = fp_words[-1].split('_')[-5]  # get year which is in the 5th position from the end

    return cen_type, cen_year
