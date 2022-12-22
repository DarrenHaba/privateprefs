import argparse
import sys

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command")


def command(arguments=None, parent=subparsers):
    if arguments is None:
        arguments = []

    def wrapper(func):
        parent_parser = parent.add_parser(func.__name__, description=func.__doc__)
        for arg in arguments:
            parent_parser.add_argument(*arg[0], **arg[1])
        parent_parser.set_defaults(func=func)
    return wrapper


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', required=True)
    args = parser.parse_args(argv)
    print(f'Hello {args.name}')


def cli_entry_point(args=None):
    if args is None:
        args = parser.parse_args()
    print("cli_entry_point()")
    print(f"args {args}")

    if args.command is None:
        parser.print_help()
        print_list()
    else:
        args.func(args)





if __name__ == '__main__':
    main()
