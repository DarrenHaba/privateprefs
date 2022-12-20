import argparse

# import privateprefs as prefs

if __name__ == "__main__":


    PARSER = argparse.ArgumentParser()
    subparsers = PARSER.add_subparsers(dest="command")


    def argument(*args, **kwargs):
        return list(args), kwargs


    def command(arguments=None, parent=subparsers):
        if arguments is None:
            arguments = []

        def wrapper(func):
            parser = parent.add_parser(func.__name__, description=func.__doc__)
            for arg in arguments:
                parser.add_argument(*arg[0], **arg[1])
            parser.set_defaults(func=func)
        return wrapper


    @command([argument("key", help="Name"), argument("value", help="foo")])
    def save(arguments):
        # noinspection PyProtectedMember
        # prefs._save("foo", "bar")(arguments.key, arguments.value)
        print("save")
        prefs.save(arguments.key, arguments.value)


    @command([argument("key", help="The key to load")])
    def load(arguments):
        load(arguments.key)


    def main():
        args = PARSER.parse_args()
        if args.command is None:
            PARSER.print_help()
        else:
            args.func(args)


# if __name__ == "__main__":
#     save("foo", "bar")

    # prefs._save("foo", "bar")


