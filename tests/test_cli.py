import os
import platform

import pytest

import privateprefs.core.cli as cli
from privateprefs.core.cli import main
import privateprefs.core.database as _db

test_key = "test key"
test_key2 = "test key2"

test_value = "test value"
test_value2 = "test value2"

test_group = "test group"


@pytest.fixture(autouse=True)
def setup_and_teardown():
    # -- set up --

    # create a new data file used for testing
    _db.PATH_TO_DATA_FILE = _db.PATH_TO_USER_DATA_PROJECT_DIR / "data_unit_test.ini"

    yield
    # -- tear down --

    # delete the data file used for testing
    _db.PATH_TO_DATA_FILE.unlink()


def test__command__save__no_group(capsys):
    main(["save", test_key, test_value])
    cli_output = capsys.readouterr().out

    data_file = _db._get_config_parser_for_data_ini_file()
    loaded_value = data_file[_db.DEFAULT_GROUP_NAME][test_key]

    assert cli_output.__contains__(test_value)
    assert loaded_value == test_value


def test__command__save__with_group_shorthand(capsys):
    main(["save", test_key, test_value, "-g", test_group])
    cli_output = capsys.readouterr().out

    data_file = _db._get_config_parser_for_data_ini_file(test_group)
    loaded_value = data_file[test_group][test_key]

    assert cli_output.__contains__(test_value)
    assert cli_output.__contains__(test_group)
    assert loaded_value == test_value


def test__command__save__with_group_full_group_name(capsys):
    main(["save", test_key, test_value, "--group", test_group])
    cli_output = capsys.readouterr().out

    data_file = _db._get_config_parser_for_data_ini_file(test_group)
    loaded_value = data_file[test_group][test_key]

    assert cli_output.__contains__(test_value)
    assert cli_output.__contains__(test_group)
    assert loaded_value == test_value


def test__command__load__no_group(capsys):
    data_file = _db._get_config_parser_for_data_ini_file()
    data_file.set(_db.DEFAULT_GROUP_NAME, test_key, test_value)
    with _db.PATH_TO_DATA_FILE.open("w") as file:
        data_file.write(file)

    main(["load", test_key])
    cli_output = capsys.readouterr().out

    loaded_value = _db.read(test_key)

    assert cli_output.__contains__(test_value)
    assert loaded_value == test_value


def test__command__load__with_group_shorthand(capsys):
    data_file = _db._get_config_parser_for_data_ini_file(test_group)
    data_file.set(test_group, test_key, test_value)
    with _db.PATH_TO_DATA_FILE.open("w") as file:
        data_file.write(file)

    main(["load", test_key, "-g", test_group])
    cli_output = capsys.readouterr().out

    loaded_value = _db.read(test_key, test_group)

    assert cli_output.__contains__(test_value)
    assert loaded_value == test_value


def test__command__load__with_group_full_group_name(capsys):
    data_file = _db._get_config_parser_for_data_ini_file(test_group)
    data_file.set(test_group, test_key, test_value)
    with _db.PATH_TO_DATA_FILE.open("w") as file:
        data_file.write(file)

    main(["load", test_key, "--group", test_group])
    cli_output = capsys.readouterr().out

    loaded_value = _db.read(test_key, test_group)

    assert cli_output.__contains__(test_value)
    assert loaded_value == test_value


def test__command__data(capsys):
    with capsys.disabled():
        main(["save", test_key, test_value])
    main(["data"])
    capture = capsys.readouterr()
    contains_test_key = capture.out.__contains__(test_key)
    contains_test_value = capture.out.__contains__(test_value)
    assert all([contains_test_key, contains_test_value])


def test__command__data__show_path(capsys):
    main(["data"])
    capture = capsys.readouterr().out
    assert capture.__contains__("privateprefs") and capture.__contains__("data.ini")


def test__command__data__empty(capsys):
    main(["data"])
    capture = capsys.readouterr()
    displays_empty_list = capture.out.__contains__("no key-value pairs saved")
    assert displays_empty_list


def test__command__delete_all(capsys):
    with capsys.disabled():
        main(["save", test_key, test_value])
        main(["save", test_key2, test_value2])
    main(["delete_all"])
    capture = capsys.readouterr()
    all_key_value_deleted = capture.out.__contains__("all key-value pairs deleted")
    assert all_key_value_deleted


def test__command__delete(capsys):
    with capsys.disabled():
        main(["save", test_key, test_value])
    main(["delete", test_key])
    capture = capsys.readouterr()
    test_value_deleted = capture.out.__contains__(test_value)
    assert test_value_deleted


def test__command__pre_uninstall(capsys):
    main(["pre_uninstall"])
    capture = capsys.readouterr().out
    assert capture.__contains__("removed all persistent files and")


def test__command__open__did_open_file__true(mocker, capsys):
    mocker.patch(
        'privateprefs.core.cli._open_file_with_application',
        return_value=True
    )
    main(["open"])
    capture = capsys.readouterr().out
    print(capture)
    assert capture.__contains__("opened data.ini file in default application")


def test__command__open__did_open_file__false(mocker, capsys):
    mocker.patch(
        'privateprefs.core.cli._open_file_with_application',
        return_value=False
    )
    main(["open"])
    capture = capsys.readouterr().out
    assert capture.__contains__("sorry, could not open the file on you operating system")


def test__open_file_with_application__mac(mocker):
    mocker.patch(
        'privateprefs.core.cli.subprocess.call',
    )
    mocker.patch(
        'privateprefs.core.cli.platform.system',
        return_value="Darwin"
    )
    result = cli._open_file_with_application("fake/path")
    assert result is True


def test__open_file_with_application__windows(mocker):
    # monkey patch for linux ci
    if platform.system() != 'Windows':
        def startfile():
            return True
        os.startfile = startfile

    mocker.patch(
        'privateprefs.core.cli.os.startfile',
        return_value=True
    )
    mocker.patch(
        'privateprefs.core.cli.platform.system',
        return_value="Windows"
    )

    result = cli._open_file_with_application("fake/path")
    assert result is True


def test__open_file_with_application__linux(mocker):
    mocker.patch(
        'privateprefs.core.cli.subprocess.call',
    )
    mocker.patch(
        'privateprefs.core.cli.platform.system',
        return_value="Linux"
    )
    result = cli._open_file_with_application("fake/path")
    assert result is True


def test__open_file_with_application__unsupported_operating_system(mocker):
    mocker.patch(
        'privateprefs.core.cli.subprocess.call',
    )
    mocker.patch(
        'privateprefs.core.cli.platform.system',
        return_value="not Darwin Windows or Linux"
    )
    result = cli._open_file_with_application("fake/path")
    assert result is False


def test__privateprefs_cli(capsys):
    main("")
    capture = capsys.readouterr().out
    assert capture.__contains__("Thanks for using Private Prefs!")
