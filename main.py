from cli.parser import handle_parser
from utilities.send_cmd import send_cmd


def main():
    args = handle_parser()
    response = send_cmd(payload=args)

    print(response.json())

if __name__ == "__main__":
    main()
