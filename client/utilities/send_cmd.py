"""File responsible for the sending and receiving of the http requests"""

import sys
import typing

import requests

from http_requests.request import get_request, post_request
from utilities import logger
from utilities.http_utils import prepare_url


def send_cmd(payload: dict[str, typing.Any]) -> requests.Response:
    """Overall Handler function for the http actions
        1 prepares the url for the http_request
        2 triggers the http request based on the request type parameter set from the cli
        3 returns any kind of response received from the cli

    Args:
        payload (dict[str, typing.Any]): The data expected from the endpoint

    Returns:
        requests.Response: The response from the http server
    """

    url = prepare_url(payload=payload)
    logger.debug("Preparing to send a request")
    match (payload["request_type"]):

        case "post":
            logger.debug("Triggering Post request")
            return post_request(payload=payload, url=url)
        case "get":
            logger.debug("Triggering Post request")
            return get_request(payload=payload, url=url)

        case _:
            logger.error(
                "Getting a invalid request type %s. Exiting !!!",
                payload["request_type"],
            )
            sys.exit(1)
