import argparse


def build_split_parser(subparser: argparse._SubParsersAction):
    split_parser: argparse.ArgumentParser = subparser.add_parser(
        name="split_file", help="Split any file"
    )
    split_parser.add_argument(
        "-s", "--source", required=True, help="The Source path for the file to split"
    )
    split_parser.add_argument(
        "-t",
        "--target",
        default="./",
        required=False,
        help="The destination folder for the file after splitting",
    )
    split_parser.add_argument(
        "--parts",
        required=True,
        help="The parts of the file required in the form of `from.to` ",
        nargs="+",
    )
    split_parser.set_defaults(request_type="post")
