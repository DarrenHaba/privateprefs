from pathlib import Path

import pytest
import privateprefs.core.database as _db

test_key = "test key"
test_group = "test group"
test_value = "test value"

test_key2 = "test key2"
test_value2 = "test value2"
test_group2 = "test group2"


@pytest.fixture(autouse=True)
def setup_and_teardown():
    # -- set up --

    # create a new data file used for testing
    _db.PATH_TO_DATA_FILE = _db.PATH_TO_USER_DATA_PROJECT_DIR / "data_unit_test.ini"

    yield
    # -- tear down --

    # delete the data file used for testing
    _db.PATH_TO_DATA_FILE.unlink()


def test__write__no_group():
    _db.write(test_key, test_value)
    data_file = _db._get_config_parser_for_data_ini_file(_db.DEFAULT_GROUP_NAME)
    loaded_value = data_file[_db.DEFAULT_GROUP_NAME][test_key]
    assert loaded_value == test_value


def test__write__with_group():
    _db.write(test_key, test_value, test_group)
    data_file = _db._get_config_parser_for_data_ini_file(test_group)
    loaded_value = data_file[test_group][test_key]
    assert loaded_value == test_value


def test__read__no_group():
    _add_group_key_value_to_data_file(test_key, test_value, None)
    assert _db.read(test_key) == test_value


def test__read__with_group():
    _add_group_key_value_to_data_file(test_key, test_value, test_group)
    assert _db.read(test_key, test_group) == test_value


def test__read__group_does_not_exist():
    assert _db.read(test_key, "this group does not exist") is None


def test__read_keys():
    _add_group_key_value_to_data_file(test_key, test_value, test_group)
    _add_group_key_value_to_data_file(test_key2, test_value2, test_group)
    group = _db.read_keys(test_group)
    assert group[test_key] == test_value
    assert group[test_key2] == test_value2


def test__read_keys__get_only_from_group():
    _add_group_key_value_to_data_file(test_key, test_value, test_group)
    _add_group_key_value_to_data_file(test_key2, test_value2, test_group2)
    group = _db.read_keys(test_group)
    assert group[test_key] == test_value
    assert len(group) == 1


def test__read_keys__group_does_not_exist():
    _add_group_key_value_to_data_file(test_key, test_value, test_group)
    _add_group_key_value_to_data_file(test_key2, test_value2, test_group2)
    group = _db.read_keys("key dose not exist")
    assert group == {}


def test__delete__no_group():
    group = _db.DEFAULT_GROUP_NAME
    _add_group_key_value_to_data_file(test_key, test_value, None)
    dose_data_file_contain_test_key = _get_data_file_values(group)[group].__contains__(test_key)
    assert dose_data_file_contain_test_key is True
    _db.delete(test_key)
    dose_data_file_contain_test_key = _get_data_file_values(group)[group].__contains__(test_key)
    assert dose_data_file_contain_test_key is False


def test__delete__with_group():
    group = test_group
    _add_group_key_value_to_data_file(test_key, test_value, group)
    dose_data_file_contain_test_key = _get_data_file_values(group)[group].__contains__(test_key)
    assert dose_data_file_contain_test_key is True
    _db.delete(test_key, group)
    dose_data_file_contain_test_key = _get_data_file_values(group)[group].__contains__(test_key)
    assert dose_data_file_contain_test_key is False


def test__delete_all():
    _db.write(test_key, test_value)
    _db.write(test_key2, test_value2)
    _db.delete_all()
    assert _db.read(test_key) is None


def test__delete_data_file():
    _db.write(test_key, test_value)
    dose_file_exists_before_delete = _db.PATH_TO_DATA_FILE.exists()
    _db._delete_data_file()
    dose_file_exists_after_delete = _db.PATH_TO_DATA_FILE.exists()
    assert dose_file_exists_before_delete is True
    assert dose_file_exists_after_delete is False


def test___delete_project_data_dir():
    _db.write(test_key, test_value)
    dose_dir_exists_before_delete = _db.PATH_TO_USER_DATA_PROJECT_DIR.exists()
    _db._delete_data_file()
    _db._delete_project_data_dir()
    dose_dir_exists_after_delete = _db.PATH_TO_USER_DATA_PROJECT_DIR.exists()
    assert dose_dir_exists_before_delete is True
    assert dose_dir_exists_after_delete is False


def test___delete_project_data_dir__mock_exists__true(mocker):
    mocker.patch(
        'privateprefs.core.database.pathlib.Path.exists',
        return_value=True
    )
    _db.write(test_key, test_value)
    _db._delete_data_file()
    _db._delete_project_data_dir()
    dose_dir_exists_after_delete = _db.PATH_TO_USER_DATA_PROJECT_DIR.exists()
    print(dose_dir_exists_after_delete)
    assert dose_dir_exists_after_delete is True


def test___delete_project_data_dir__mock_exists__false(mocker):
    mocker.patch(
        'privateprefs.core.database.pathlib.Path.exists',
        return_value=False
    )
    _db.write(test_key, test_value)
    _db._delete_data_file()
    _db._delete_project_data_dir()
    dose_dir_exists_after_delete = _db.PATH_TO_USER_DATA_PROJECT_DIR.exists()
    print(dose_dir_exists_after_delete)
    assert dose_dir_exists_after_delete is False


def _add_group_key_value_to_data_file(key, value, group):
    if group is None:
        group = _db.DEFAULT_GROUP_NAME
    data_file = _db._get_config_parser_for_data_ini_file(group)
    data_file.set(group, key, value)
    with _db.PATH_TO_DATA_FILE.open("w") as file:
        data_file.write(file)


def _get_data_file_values(group):
    return _db._get_config_parser_for_data_ini_file(group)
