import argparse
import privateprefs as prefs
import privateprefs._cli as cli


def save(key, value):
    # noinspection PyProtectedMember
    cli._save(key, value)
    print(f"saved key='{key}' value='{value}'")


def load(key):
    print(f"loaded key='{key}' value='{prefs.load(key)}'")


# def delete(arguments):
#     if arguments.all:
#         prefs.clear()
#         print(f"all prefs deleted")
#     else:
#         print(f"deleted key='{arguments.key}' value='{prefs.load(arguments.key)}'")
#         prefs.delete(arguments.key)
#
#
# def list(args):
#     print_list()
#
#
#
# def print_list():
#     print()
#     print("prefs saved (key : value)")
#     print("------------------------------")
#     for key, value in prefs.load_dict().items():
#         print(key, ':', value)
#     print("------------------------------")


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subparser')

    parser_a = subparsers.add_parser('save')
    parser_a.add_argument("key")
    parser_a.add_argument("value")

    parser_a = subparsers.add_parser('load')
    parser_a.add_argument("key")

    kwargs = vars(parser.parse_args())
    globals()[kwargs.pop('subparser')](**kwargs)


if __name__ == '__main__':
    main()

