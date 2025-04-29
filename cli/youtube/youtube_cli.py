"""File to handle cli for youtube related actions"""

import argparse

from cli.youtube.download import download_video


def handle_yt_cli(subparser: argparse._SubParsersAction):
    """Builds a separate subparser for each of the youtube actions.
        Creates the parser for
            1 download

    Args:
        subparser (argparse._SubParsersAction): The Subparser on which the youtube parser has to be built
    """
    yt_parser: argparse.ArgumentParser = subparser.add_parser(
        name="youtube", help="Handle All youtube related action"
    )

    yt_subparser = yt_parser.add_subparsers(dest="sub_action")

    download_video(yt_subparser)
