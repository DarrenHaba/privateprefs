# noinspection PyProtectedMember

import privateprefs._cli as cli

def test_save():
    cli._save("Fee", "fi")


def test_load():
    assert False
