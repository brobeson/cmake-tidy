import os.path

def find_cmake_tidy_configuration(cmake_file):
    cmake_file = os.path.abspath(cmake_file)
    directory = os.path.dirname(cmake_file)
    config_file = os.path.join(directory, '.cmake-tidy')
    while directory != '/' and not os.path.isfile(config_file):
        directory = os.path.dirname(directory)
        config_file = os.path.join(directory, '.cmake-tidy')
    if not os.path.isfile(config_file):
        raise ValueError
    return config_file
