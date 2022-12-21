import argparse
import privateprefs as prefs

from privateprefs.privateprefs import _save

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command")


def argument(*args, **kwargs):
    return list(args), kwargs


def command(arguments=None, parent=subparsers):
    if arguments is None:
        arguments = []

    def wrapper(func):
        parent_parser = parent.add_parser(func.__name__, description=func.__doc__)
        for arg in arguments:
            parent_parser.add_argument(*arg[0], **arg[1])
        parent_parser.set_defaults(func=func)
    return wrapper


@command([argument("key", help="Name"), argument("value", help="foo")])
def save(arguments):
    _save(arguments.key, arguments.value)
    print(f"saved key='{arguments.key}' value='{arguments.value}'")


@command([argument("key", help="The key to load")])
def load(arguments):
    print(f"loaded key='{arguments.key}' value='{prefs.load(arguments.key)}'")


@command([argument("key", help="The key to delete the value of", nargs='?'),
          argument("--all", action=argparse.BooleanOptionalAction, help="delete all")])
def delete(arguments):
    if arguments.all:
        prefs.clear()
        print(f"all prefs deleted")
    else:
        print(f"deleted key='{arguments.key}' value='{prefs.load(arguments.key)}'")
        prefs.delete(arguments.key)


@command()
def list(args):
    print_list()


def print_list():
    print()
    print("prefs saved (key : value)")
    print("------------------------------")
    for key, value in prefs.load_dict().items():
        print(key, ':', value)
    print("------------------------------")


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

