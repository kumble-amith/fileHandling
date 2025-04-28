import sys

import typing

BASE_URL = "http://127.0.0.1:8000/"


def prepare_url(payload: dict[str, typing.Any]):

    base_url = ""
    if payload["action"]:
        base_url += payload["action"] + "/"

    if payload["sub_action"]:
        base_url += payload["sub_action"] + "/"

    if not base_url:
        print("Unable to create a end point")
        sys.exit(1)

    return BASE_URL + base_url
