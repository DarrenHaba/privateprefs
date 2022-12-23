import argparse
import privateprefs as prefs
# noinspection PyProtectedMember
import privateprefs.internal as internal


def save(key, value):
    # noinspection PyProtectedMember
    internal._save(key, value)
    print(f"saved key='{key}' value='{value}'")


def load(key):
    print(f"loaded key='{key}' value='{prefs.load(key)}'")
    return key


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


# def main(argv=None):
#     parser = argparse.ArgumentParser()
#     parser.add_argument('--name', required=True)
#     args = parser.parse_args(argv)
#     print(f'Hello {args.name}')
#
# def test_main_even_simpler(capsys):
#     main(["--name", "Jürgen"])
#     captured = capsys.readouterr()
#     print(5555555)
#     print(captured)
#     assert captured.out == "Hello Jürgen\n"


def main(argv=None):
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subparser')

    parser_a = subparsers.add_parser('save')
    parser_a.add_argument("key")
    parser_a.add_argument("value")

    parser_a = subparsers.add_parser('load')
    parser_a.add_argument("key")

    kwargs = vars(parser.parse_args(argv))
    globals()[kwargs.pop('subparser')](**kwargs)


if __name__ == '__main__':
    main()

