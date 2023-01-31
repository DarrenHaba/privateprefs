import pathlib
from platformdirs import user_data_dir
import pytest

import privateprefs.core.database as _db
import privateprefs as prefs

test_key = "test key"
test_value = "test value"
test_group = "test group"

test_key2 = "test key2"
test_value2 = "test value2"
test_group2 = "test group2"


@pytest.fixture(autouse=True)
def setup_and_teardown():
    # -- set up --

    # create a new path for testing
    _db.PATH_TO_USER_DATA_PROJECT_DIR = pathlib.Path(user_data_dir(_db.PROJECT_NAME + "_unit_test", appauthor=False))
    # create a new data file used for testing
    _db.PATH_TO_DATA_FILE = _db.PATH_TO_USER_DATA_PROJECT_DIR / "data_unit_test.ini"

    # delete last data file used for testing (if left over for some reason)
    if _db.PATH_TO_DATA_FILE.exists():
        _db.PATH_TO_DATA_FILE.unlink()

    yield
    # -- tear down --

    # delete the data file used for testing
    if _db.PATH_TO_DATA_FILE.exists():
        _db.PATH_TO_DATA_FILE.unlink()


def test__load():
    _db.write(test_key, test_value)
    assert prefs.load(test_key) == test_value


def test__load__return_null_if_key_does_not_exist():
    assert prefs.load(test_key) is None


def test__load_keys__as_dict():
    _db.write(test_key, test_value, test_group)
    _db.write(test_key2, test_value2, test_group)
    key_values = prefs.load_keys(test_group)
    assert key_values[test_key] == test_value and key_values[test_key2] == test_value2


def test__delete__no_group():
    _db.write(test_key, test_value, None)
    dose_data_file_contain_test_key = _db.read(test_key) == test_value
    assert dose_data_file_contain_test_key is True
    prefs.delete(test_key)
    dose_data_file_contain_test_key = _db.read(test_key) == test_value
    assert dose_data_file_contain_test_key is False


def test__delete__with_group():
    _db.write(test_key, test_value, test_group)
    dose_data_file_contain_test_key = _db.read(test_key, test_group) == test_value
    assert dose_data_file_contain_test_key is True
    prefs.delete(test_key, test_group)
    dose_data_file_contain_test_key = _db.read(test_key, test_group) == test_value
    assert dose_data_file_contain_test_key is False


def test__delete_all():
    _db.write(test_key, test_value)
    _db.write(test_key2, test_value2)
    prefs.delete_all("NO_GROUP")
    assert _db.read(test_key) is None


def test__delete_all__no_group():
    _db.write(test_key, test_value)
    dose_data_file_contain_test_key = _db.read(test_key) == test_value
    assert dose_data_file_contain_test_key is True

    _db.write(test_key2, test_value2, test_group2)
    dose_data_file_contain_test_key = _db.read(test_key2, test_group2) == test_value2
    assert dose_data_file_contain_test_key is True

    prefs.delete_all("NO_GROUP")

    dose_data_file_contain_test_key = _db.read(test_key) == test_value
    assert dose_data_file_contain_test_key is False

    dose_data_file_contain_test_key = _db.read(test_key2, test_group2) == test_value2
    assert dose_data_file_contain_test_key is True


def test__delete_all__with_group():
    _db.write(test_key, test_value, test_group)
    dose_data_file_contain_test_key = _db.read(test_key, test_group) == test_value
    assert dose_data_file_contain_test_key is True

    _db.write(test_key2, test_value2, test_group2)
    dose_data_file_contain_test_key = _db.read(test_key2, test_group2) == test_value2
    assert dose_data_file_contain_test_key is True

    prefs.delete_all(test_group)

    dose_data_file_contain_test_key = _db.read(test_key, test_group) == test_value
    assert dose_data_file_contain_test_key is False

    dose_data_file_contain_test_key = _db.read(test_key2, test_group2) == test_value2
    assert dose_data_file_contain_test_key is True
