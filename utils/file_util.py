import json
import os

from message_mng.settings import PATH_CONFIG


def load_config(file_config, dir_filename=PATH_CONFIG):
    """
    Load config from file config
    :return: Dictionary contain config value
    """
    # Check file existing
    is_file = check_file_existing(file_config)

    if is_file:
        configurations = dict()
        path_file = os.path.join(dir_filename, file_config)
        try:
            with open(path_file, 'r') as f:
                configurations = json.load(f)
        except Exception as ex:
            print('Cannot load file configuration' + ":" + str(ex))
        return configurations
    print ('File config is not found')


def check_file_existing(file_name):
    if file_name and len(file_name) > 0:
        path_file = os.path.join(PATH_CONFIG, file_name)
        is_file = os.path.isfile(path_file)

        if is_file:
            return True
    return True
