"""File to handle the cli for ping parser"""

import argparse


def build_ping_parser(subparser: argparse._SubParsersAction) -> None:
    """Cli handling for the ping action 

    Args:
        subparser (argparse._SubParsersAction): Subparser on which ping parser has to be built
    """
    ping_parser : argparse.ArgumentParser = subparser.add_parser(name="ping", help="Ping the server to check the status")

    ping_parser.set_defaults(request_type = "get")
