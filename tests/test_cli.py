import pytest

import privateprefs.cli as cli


# def test_argument():
#     foo = [cli.argument("key", help="Name"), cli.argument("value", help="foo")]
#     print(type(foo))
#     assert True



# def test_command():
#     assert False


# def myFun(*args, **kwargs):
#     print("args: ", args)
#     print("kwargs: ", kwargs)


def my_argument(*args, **kwargs):
    return list(args), kwargs


# @command([argument("key", help="Name"), argument("value", help="foo")])
# def save(arguments):
#     _save(arguments.key, arguments.value)
#     print(f"saved key='{arguments.key}' value='{arguments.value}'")


# @pytest.mark.parametrize("save")
# def test_save():
#     c = cli.cli_entry_point()
#     print(c)
#     print(55555555555555555555555555555555555555555555555555555555555555555555555555)
#     # c = cli.cli_entry_point()
#     # print(c)
#     # cli.save([cli.argument("key", help="Name"), cli.argument("value", help="foo")])
#     # f = myFun('geeks', 'for', 'geeks', first="Geeks", mid="for", last="Geeks")
#     # cli.cli_entry_point()
#     # f = my_argument('key', help="key help info")
#     # f = cli.argument('key', help="key help info")
#     # f = cli.argument("key", help="Name")
#     # print(f)
#     assert True

#
# def test_load():
#     assert False
#
#
# def test_delete():
#     assert False
#
#
# def test_list():
#     assert False
#
#
# def test_print_list():
#     assert False
#
#
# def test_cli_entry_point():
#     assert False
