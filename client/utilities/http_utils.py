"""Overall HTTP Utils File"""

import sys
import typing

from utilities import logger
from utilities.utils import get_configurator


def get_base_url() -> str:
    """ Reads the configuration file (configs.ini) and then returns the base url for the request 

    Returns:
        str: Base URL for the request
    """
    configs = get_configurator()
    base_url = configs["URLS"]["BASE_URL"]
    logger.debug(f"Base Url from configs in {base_url} ")
    return base_url


def prepare_url(payload: dict[str, typing.Any]):
    """Prepares the base URL for any kind of request That needs to be sent

    Args:
        payload (dict[str ,  typing.Any]): The data that needs to be sent to the server

    Returns:
        str: The Url on which the request has to be sent
    """

    endpoint = ""
    logger.debug("Preparing the url for get request")

    if payload.get("action"):
        endpoint += payload.get("action") + "/"

    if payload.get("sub_action"):
        endpoint += payload.get("sub_action") + "/"

    if not endpoint:
        logger.error("Unable to create a end point with the details provided")
        sys.exit(1)

    
    base_url = get_base_url()
    
    url = base_url + endpoint

    logger.debug(f"The Request URL is {url} ")
    return url
