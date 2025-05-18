"""Generally used function for the api"""

import os


def is_file_exists(file_path: str):
    """Checks if there is a file in the given path or no"""
    return "." in file_path and os.path.exists(file_path)


def get_file_type(file_path: str):
    """Gets The file type of the given file"""

    folder_structure = file_path.split("/")

    file_name_type = folder_structure[-1].split(".")

    return file_name_type[-1]


def get_ms_time(timestamp: str):
    """Gets the time in ms for the given time stamp"""
    timestamps = timestamp.split(':')
    timestamps = timestamps[::-1]
    value = 0

    for i in range(len(timestamps)):
        
        value += (int(timestamps[i])) * (60 ** i)

    return value * 1000

def get_base_file_name(file_path : str):
    if is_file_exists(file_path=file_path):
        if get_file_type(file_path=file_path):
            structure = file_path.split("/")
            return structure[-1].split(".")[0]
    
    return "temp"