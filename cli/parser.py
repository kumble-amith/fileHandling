import argparse
import sys
import typing

from cli.youtube.youtube_cli import handle_yt_cli


import certifi
# certifi.contents()
def create_parser() -> argparse.ArgumentParser:

    parser = argparse.ArgumentParser()
    if '-' not in ' '.join(sys.argv):
        sys.argv.append('-h')

    subparser = parser.add_subparsers(dest="action")

    handle_yt_cli(subparser)
    return parser


def handle_parser() -> dict[str, typing.Any]:

    parser = create_parser()

    args = parser.parse_args()

    return vars(args)
