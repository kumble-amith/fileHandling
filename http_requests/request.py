import typing
import sys

import requests


def get_request(payload: dict[str, typing.Any], url: str):

    try:
        response = requests.get(url=url, params=payload, timeout=60)
        response.raise_for_status()

    except Exception as e:

        print(f"Unexpected resonse recieved {e}")
        print(response.status_code)
        print(response.text)
        sys.exit()

    return response


def post_request(payload: dict[str, typing.Any], url: str):

    print("Sending Post Request ")
    print(f"URL : {url}")
    print(f"Payload : {payload}" )
    try:
        response = requests.post(url=url, json=payload, timeout=60)

        response.raise_for_status()

    except Exception as e:

        # print(f"Unexpected resonse recieved {e}")
        # print(response.status_code)
        # print(response.text)
        print("Hello world ")
        sys.exit()

    return response
