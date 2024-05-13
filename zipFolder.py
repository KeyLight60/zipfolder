#!python3
# coding: utf-8

import sys
import os
import shutil
import datetime as dt
import configparser as config


# function
# ini information acquisition
def getInfo(section, value):
    config_ini = config.ConfigParser()
    config_ini.read('setting.ini', encoding='utf-8')
    data = config_ini[section][value]
    return data

# Get date and time
def getDateTime():
    dt_now = dt.datetime.now()
    get_dt = dt_now.strftime('%Y_%m_%d_%H_%M_%S')
    return get_dt

def main():
    arg1 = 'config'
    arg2_1 = 'FOLDER_PATH'
    arg2_2 = 'DESTINATION_PATH'

    # Information acquisition
    f_path = getInfo(arg1, arg2_1)
    destination_path = getInfo(arg1, arg2_2)
    date = getDateTime()

    # Zip specified folder
    shutil.make_archive(date, 'zip', root_dir = f_path)
    print('zipped path :' + f_path)

    # Move zip file
    source_path = (os.getcwd() + '\\' + date + '.zip')
    shutil.move(source_path, destination_path)
    print('Moved the file to ' + destination_path)


# main process
try:
    main()
except Exception as e:
    print(e, file=sys.stderr)
