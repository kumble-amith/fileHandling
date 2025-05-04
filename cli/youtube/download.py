"""File for the handling of youtube download action"""

import argparse


def download_video(subparser: argparse._SubParsersAction):
    """Build a parser for the download action of youtube

    Args:
        subparser (argparse._SubParsersAction): Subparser on which download parser has to be built
    """
    downloader: argparse.ArgumentParser = subparser.add_parser(
        "download", help="Download a video from a youtube link"
    )

    downloader.add_argument(
        "-l",
        "--link",
        nargs="+",
        help="List of Youtube Links to download",
        required=True,
    )
    downloader.add_argument(
        "-n",
        "--name",
        help="Name of the Downloaded video : Available only when 1 Link is provided : Default Original Name of the video",
        required=False,
    )
    downloader.add_argument(
        "-f",
        "--format",
        help="Format of the video",
        choices=["mp3", "mp4"],
        default="mp4",
        required=False,
    )
    downloader.add_argument(
        "-p",
        "--path",
        help="Path for the download of the video : Default ./",
        default="./",
        required=False,
    )
    downloader.add_argument(
        "--debug", action="store_true", help="Debug Level Logging information"
    )

    downloader.set_defaults(request_type="post")
