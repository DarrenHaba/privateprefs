import argparse
import privateprefs as prefs
from privateprefs.privateprefs import _save


def save(key, value):
    # noinspection PyProtectedMember
    _save(key, value)
    print(f"saved key='{key}' value='{value}'")


def load(key):
    value = prefs.load(key)
    print(f"loaded key='{key}' value='{value}'")


def delete(key, delete_all):
    if delete_all:
        prefs.clear()
        print(f"all prefs deleted")
    else:
        print(f"deleted key='{key}' value='{prefs.load(key)}'")
        prefs.delete(key)


def list():
    print_list()


def print_list():
    print()
    print("stored (key  :  value)")
    print("-------------------------------------------------------------")
    d = prefs.load_dict()
    if len(d) > 0:
        for key, value in prefs.load_dict().items():
            print(key, '  :  ', value)
    else:
        print("list is empty: (no key-values saved yet)")
    print("-------------------------------------------------------------")


def main(argv=None):
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subparser')

    parser_save = subparsers.add_parser("save")
    parser_save.add_argument("key")
    parser_save.add_argument("value")

    parser_load = subparsers.add_parser("load")
    parser_load.add_argument("key")

    subparsers.add_parser("list")

    parser_delete = subparsers.add_parser("delete")
    parser_delete.add_argument('key', nargs='?')
    parser_delete.add_argument("--all",
                               dest="delete_all",
                               action="store_true")
    args = parser.parse_args(argv)
    no_args_given = args.subparser == "delete" and args.key is None and args.delete_all is False
    if no_args_given:
        raise parser.error("you must enter a key string argument or enter the '--all' flag")

    kwargs = vars(parser.parse_args(argv))
    globals()[kwargs.pop('subparser')](**kwargs)


if __name__ == '__main__':
    main()
