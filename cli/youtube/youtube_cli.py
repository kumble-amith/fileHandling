import argparse

from cli.youtube.download import download_video

def handle_yt_cli(parser :argparse._SubParsersAction):
    
    yt_parser: argparse.ArgumentParser = parser.add_parser(name='youtube' , help='Handle All youtube related action' )

    yt_subparser = yt_parser.add_subparsers(dest='sub_action')

    download_video(yt_subparser)
