# from argparse import ArgumentParser
#
# cli = ArgumentParser()
# subparsers = cli.add_subparsers(dest="subcommand")
#
#
# def argument(*name_or_flags, **kwargs):
#     return list(name_or_flags), kwargs
#
#
# def subcommand(arg_list=None, parent=subparsers):
#     if arg_list is None:
#         arg_list = []
#
#     def decorator(func):
#         parser = parent.add_parser(func.__name__, description=func.__doc__)
#         for arg in arg_list:
#             parser.add_argument(*arg[0], **arg[1])
#         parser.set_defaults(func=func)
#     return decorator
#
#
# @subcommand([argument("key", help="Name"), argument("value", help="foo")])
# def save(arg_list):
#     print(arg_list.key)
#     print(arg_list.value)
#
#
# if __name__ == "__main__":
#     args = cli.parse_args()
#     if args.subcommand is None:
#         cli.print_help()
#     else:
#         args.func(args)
