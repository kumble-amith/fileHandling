"""Overall Handling function"""

import sys

from cli.parser import handle_parser
from utilities import logger
from utilities.send_cmd import send_cmd


def main() -> None:
    """Main Function"""
    args = handle_parser()

    if args.get("debug", False):
        logger.add(sys.stdout , level="DEBUG")
    else:
        logger.add(sys.stdout, level="INFO")

    logger.info("Received the Arguments from CLI")
    logger.debug(f"Arguments {args} ")

    response = send_cmd(payload=args)
    print(response.json())


if __name__ == "__main__":
    main()
