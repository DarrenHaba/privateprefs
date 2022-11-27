import pytest

import privateprefs

test_key = "test key"
test_value = "test value"
test_dict = {'test key': 'test value'}
test_dict_as_str = "{'test key': 'test value'}"


def clear_text_file():
    path_to_test_file = privateprefs.path_to_test_file
    with open(path_to_test_file, "w") as file:
        file.write("")


@pytest.fixture(autouse = True)
def setup_and_teardown_for_stuff():
    # set up
    clear_text_file()
    yield
    # tear down
    # clear_text_file()


def _load_test_file_str():
    with open(privateprefs.path_to_test_file, "r") as file:
        return file.read()


def _save_dict_str_to_file(dict_str):
    with open(privateprefs.path_to_test_file, "w") as file:
        file.write(dict_str)


def test_save():
    privateprefs.save(test_key, test_value)
    str_form_text_file = _load_test_file_str()
    assert str_form_text_file == test_dict_as_str


def test_save_dict():
    privateprefs.save_dict(test_dict)
    str_form_text_file = _load_test_file_str()
    assert str_form_text_file == test_dict_as_str


def test_load():
    _save_dict_str_to_file(test_dict_as_str)
    assert privateprefs.load(test_key) == test_value


def test_load_default_value():
    _save_dict_str_to_file("")
    assert privateprefs.load(test_key, "default value") == "default value"


def test_load_default_value_null():
    _save_dict_str_to_file("")
    assert privateprefs.load(test_key) is None


def test_load_from_empty_file():
    _save_dict_str_to_file("")
    assert privateprefs.load(test_key) is None


def test_load_dict():
    _save_dict_str_to_file("{'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}")
    ret = privateprefs.load_dict(['key1', 'key3'])
    assert ret['key1'] == 'value1' and ret['key3'] == 'value3'


def test_load_dict_with_only_key_in_dict_text_file():
    _save_dict_str_to_file("{'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}")
    ret = privateprefs.load_dict(['key1', 'key4'])
    assert ret['key1'] == 'value1' and "key4" not in ret.keys()


def test_load_dict_from_empty_file():
    _save_dict_str_to_file("")
    assert privateprefs.load_dict(test_key) == {}
