import argparse
import privateprefs as prefs

from privateprefs.privateprefs import _save


def _save_cli(key: str, value: str) -> None:
    """
    Saves a value for a given key.
    :param key: The key used to save the value to
    :param value: The value to save/write to persistent storage
    :return: None
    """
    # noinspection PyProtectedMember
    _save(key, value)
    print(f"saved key='{key}' value='{value}'")


def _load_cli(key: str) -> None:
    """
    Loads a value from a given key.
    :param key: The key to load a value from
    :return: None
    """
    value = prefs.load(key)
    print(f"loaded key='{key}' value='{value}'")


def _delete_cli(key: str, delete_all: bool = False) -> None:
    """
    Deletes a key-value pair, or deletes all stored key-value pairs.
    :param key: The key to be deleted
    :param delete_all: Flag is set to true will delete all key-value pairs
    :return: None
    """
    if delete_all:
        prefs.delete_all()
        print(f"all prefs deleted")
    else:
        print(f"deleted key='{key}' value='{prefs.load(key)}'")
        prefs.delete(key)


def _list_cli() -> None:
    """
    Displays a list of all saved key-value pairs.
    :return: None
    """
    print_list()


def print_list() -> None:
    """
    Prints out a list of all saved key-value pairs.
    :return: None
    """
    print()
    print("stored (key  :  value)")
    print("-------------------------------------------------------------")
    d = prefs.load_dict()
    if len(d) > 0:
        for key, value in prefs.load_dict().items():
            print(key, '  :  ', value)
    else:
        print("list is empty: (no key-value pairs saved yet)")
    print("-------------------------------------------------------------")
    print()


def main(argv=None) -> None:
    """
    This main function is the entry point for our CLI in our package.

    In the project.toml file under [project.scripts] is a line code that invokes
    this method. This method instantiate argparse and instantiates sub-commands
    then injects the sub-commands into the global namespace cache
    :param argv: Injected arguments when running unit tests, and None when called
    from the command line
    :return: None
    """

    # Instantiate argparse and a sub-parsers
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subparser')

    # To make argparse sub-parsers easier to deal with, we set up one function per subparsers.

    # The Save sub-parsers.
    # A function called 'save_' will be dynamically called when the 'save' command is invoked
    parser_save = subparsers.add_parser("save")
    parser_save.add_argument("key")
    parser_save.add_argument("value")

    # The Load sub-parsers.
    # A function called 'load_' will be dynamically called when the 'load' command is invoked
    parser_load = subparsers.add_parser("load")
    parser_load.add_argument("key")

    # The List sub-parsers.
    # A function called 'list_' will be dynamically called when the 'list' command is invoked
    subparsers.add_parser("list")

    # The Delete sub-parsers.
    # A function called 'delete_' will be dynamically called when the 'delete' command is invoked
    # Note that only the 'key' or '--all' argument is required, depending on if we want to delete
    # single key-value pair or all key-value pairs.
    parser_delete = subparsers.add_parser("delete")
    parser_delete.add_argument('key', nargs='?')
    parser_delete.add_argument("--all",
                               dest="delete_all",
                               action="store_true")
    args = parser.parse_args(argv)
    no_args_given = args.subparser == "delete" and args.key is None and args.delete_all is False
    if no_args_given:
        raise parser.error("you must enter a key string argument or enter the '--all' flag")

    # Extract a dict containing the name of the sub processor invoked and its arguments
    kwargs = vars(parser.parse_args(argv))

    # Extract the name of the subcommand being invoked, note we pop/remove the subcommand name,
    # so now kwargs will be just the given arguments without the subcommand in the dict.
    func_name_to_call = kwargs.pop('subparser')  # will be: save, load, delete, etc.

    # The private functions end with an underscore and in with _cli, so we add it here.
    func_name_to_call = f"_{func_name_to_call}_cli"

    # We need to dynamically call one of the save(), load(), delete(), etc functions,
    # We dynamically call the function from the globals namespace dictionary, passing in the arguments.
    globals()[func_name_to_call](**kwargs)


if __name__ == '__main__':
    main()
