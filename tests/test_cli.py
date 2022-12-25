import pytest

import privateprefs.cli as cli

test_key = "test key"
test_value = "test value"


@pytest.fixture(autouse=True)
def setup_and_teardown():
    # set up
    cli.main(["delete", "--all"])
    yield
    # tear down
    cli.main(["delete", "--all"])


def test_save(capsys):
    with capsys.disabled():
        cli.main(["save", test_key, test_value])
    cli.main(["load", test_key])
    capture = capsys.readouterr()
    assert capture.out.__contains__(test_value)


def test_load(capsys):
    with capsys.disabled():
        cli.main(["save", test_key, test_value])
    cli.main(["load", test_key])
    capture = capsys.readouterr()
    assert capture.out.__contains__(test_value)


def test_list(capsys):
    with capsys.disabled():
        cli.main(["save", test_key, test_value])
    cli.main(["list"])
    capture = capsys.readouterr()
    contains_test_key = capture.out.__contains__(test_key)
    contains_test_value = capture.out.__contains__(test_value)
    assert all([contains_test_key, contains_test_value])


def test_list_empty(capsys):
    cli.main(["list"])
    capture = capsys.readouterr()
    displays_empty_list = capture.out.__contains__("list is empty: (no key-values saved yet)")
    assert displays_empty_list


def test_delete_all(capsys):
    with capsys.disabled():
        cli.main(["save", test_key, test_value])
        cli.main(["save", "other key", "other value"])
    cli.main(["delete", "--all"])
    capture = capsys.readouterr()
    all_key_value_deleted = capture.out.__contains__("all prefs deleted")
    assert all_key_value_deleted


def test_delete_key(capsys):
    with capsys.disabled():
        cli.main(["save", test_key, test_value])
    cli.main(["delete", test_key])
    capture = capsys.readouterr()
    test_value_deleted = capture.out.__contains__(test_value)
    assert test_value_deleted


def test_delete__no_args_given_error(capsys):
    try:
        cli.main(["delete"])
    except SystemExit:
        assert True
    else:
        assert False
