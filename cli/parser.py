"""File to build the entire cli for the architecture"""

import argparse
import sys
import typing

from cli.ping.ping_server import build_ping_parser
from cli.youtube.youtube_cli import handle_yt_cli
from utilities.constants import PARSERS_WITHOUT_ARGS


def create_parser() -> argparse.ArgumentParser:
    """Creates the cli for the project: fileHandling

    Returns:
        argparse.ArgumentParser: Parser built
    """
    parser = argparse.ArgumentParser()

    if sys.argv[-1] not in PARSERS_WITHOUT_ARGS and "-" not in " ".join(sys.argv):
        sys.argv.append("-h")

    subparser = parser.add_subparsers(dest="action")
    handle_yt_cli(subparser=subparser)
    build_ping_parser(subparser=subparser)
    return parser


def handle_parser() -> dict[str, typing.Any]:
    """Overall function to handle cli activities 

    Returns:
        dict[str, typing.Any]: Data passed by the user 
    """
    parser = create_parser()

    args = parser.parse_args()

    return vars(args)
