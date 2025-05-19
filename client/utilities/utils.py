"""Overall Common utils file"""

import configparser
import os

from utilities import logger


def get_configurator() -> configparser.ConfigParser:
    """Reads the configs.ini file from configurations/configs.ini file

    Returns:
        configparser.ConfigParser: Returns the object of the configs file
    """
    config = configparser.ConfigParser()
    config.optionxform = str

    current_dir = os.path.dirname(os.path.abspath(__file__))

    configs_path = f"{current_dir}/../configurations/configs.ini"

    logger.debug("Reading the configs from the path %s ", configs_path)

    config.read(configs_path)

    return config
