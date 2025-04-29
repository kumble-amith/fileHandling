"""File responsible for the actual trigger of the request and related error handling"""

import sys
import typing

import requests

from utilities import logger


def get_request(payload: dict[str, typing.Any], url: str) -> requests.Response:
    """Sends a Get request based on the provided url and payload
        Checks for the following error
            1 requests.exceptions.ConnectionError , requests.exceptions.MissingSchema
                This indicates that the url provided is wrong and hence exiting form the cli page
            2 requests.exceptions.HTTPError
                This indicates that a successful http request was fired but getting a invalid response status code
                Hence reporting all the error to the user as the error is in the payload

    Args:
        payload (dict[str, typing.Any]): Data to be sent
        url (str): Destination url

    Returns:
        requests.Response: Response from the server
    """
    try:
        response = requests.get(url=url, params=payload, timeout=120)
        response.raise_for_status()

    except (
        requests.exceptions.ConnectionError,
        requests.exceptions.MissingSchema,
    ) as e:
        logger("Error received: %s ", e)
        logger.error(
            "Invalid URL %s. Exiting !! \nPlease contact the administrator", url
        )
        sys.exit()

    except requests.exceptions.ReadTimeout:
        logger.info(
            "Request Taking longer to execute than expected. Please contact the administrator"
        )
        
    except requests.exceptions.HTTPError as e:
        logger("Error received: %s ", e)
        logger.error("Invalid response status code received %s ", response.status_code)
    return response


def post_request(payload: dict[str, typing.Any], url: str) -> requests.Response:
    """Sends a Post request based on the provided url and payload
        Checks for the following error
            1 requests.exceptions.ConnectionError , requests.exceptions.MissingSchema
                This indicates that the url provided is wrong and hence exiting form the cli page
            2 requests.exceptions.HTTPError
                This indicates that a successful http request was fired but getting a invalid response status code
                Hence reporting all the error to the user as the error is in the payload

    Args:
        payload (dict[str, typing.Any]): Data to be sent
        url (str): Destination url

    Returns:
        requests.Response: Response from the server
    """
    try:
        response = requests.post(url=url, json=payload, timeout=120)
        response.raise_for_status()

    except (
        requests.exceptions.ConnectionError,
        requests.exceptions.MissingSchema,
    ) as e:
        logger("Error received: %s ", e)
        logger.error(
            "Invalid URL %s. Exiting !! \nPlease contact the administrator", url
        )
        sys.exit()

    except requests.exceptions.ReadTimeout:
        logger.info(
            "Request Taking longer to execute than expected. Please contact the administrator"
        )
    except requests.exceptions.HTTPError as e:
        logger("Error received: %s ", e)
        logger.error("Invalid response status code received %s ", response.status_code)

    return response
