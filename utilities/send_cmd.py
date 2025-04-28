import sys
import typing
from utilities.http_utils import prepare_url
from http_requests.request import get_request, post_request


def send_cmd(payload: dict[str, typing.Any]):
    
    url = prepare_url(payload=payload)
    match (payload["request_type"]):

        case "post":
            return post_request(payload=payload, url=url)
        case "get":
            return get_request(payload=payload, url=url)

        case _:
            print("Invalid Request povided ")
            sys.exit(1)
