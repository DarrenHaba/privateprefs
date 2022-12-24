# noinspection PyProtectedMember
import pytest
import privateprefs as prefs
# noinspection PyProtectedMember
from privateprefs.privateprefs import _save, _save_dict

test_key = "test key"
test_value = "test value"
test_dict = {'test key': 'test value'}
test_dict_as_str = "{'test key': 'test value'}"


def clear_text_file():
    path_to_test_file = prefs.path_to_test_file
    with open(path_to_test_file, "w") as file:
        file.write("")


@pytest.fixture(autouse=True)
def setup_and_teardown_for_stuff():
    # set up
    clear_text_file()
    yield
    # tear down
    clear_text_file()


def _load_test_file_str():
    with open(prefs.path_to_test_file, "r") as file:
        return file.read()


def _save_dict_str_to_file(dict_str):
    with open(prefs.path_to_test_file, "w") as file:
        file.write(dict_str)


def test_save():
    _save(test_key, test_value)
    str_form_text_file = _load_test_file_str()
    assert str_form_text_file == test_dict_as_str


def test_save_dict():
    _save_dict(test_dict)
    str_form_text_file = _load_test_file_str()
    assert str_form_text_file == test_dict_as_str


def test_load():
    _save_dict_str_to_file(test_dict_as_str)
    assert prefs.load(test_key) == test_value


def test_load_default_value():
    _save_dict_str_to_file("")
    assert prefs.load(test_key, "default value") == "default value"


def test_load_default_value_null():
    _save_dict_str_to_file("")
    assert prefs.load(test_key) is None


def test_load_from_empty_file():
    _save_dict_str_to_file("")
    assert prefs.load(test_key) is None


def test_load_dict_filtered():
    _save_dict_str_to_file("{'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}")
    ret = prefs.load_dict(['key1', 'key3'])
    assert ret['key1'] == 'value1' and ret['key3'] == 'value3'


def test_load_dict_not_filtered():
    _save_dict_str_to_file("{'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}")
    ret = prefs.load_dict(None)
    assert ret['key1'] == 'value1' and ret['key2'] == 'value2' and ret['key3'] == 'value3'


def test_load_dict_with_only_key_in_dict_text_file():
    _save_dict_str_to_file("{'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}")
    ret = prefs.load_dict(['key1', 'key4'])
    assert ret['key1'] == 'value1' and "key4" not in ret.keys()


def test_load_dict_from_empty_file():
    _save_dict_str_to_file("")
    assert prefs.load_dict(test_key) == {}


def test_clear():
    _save(test_key, test_value)
    prefs.clear()
    assert prefs.load(test_key) is None


def test_delete():
    _save(test_key, test_value)
    _save("other test key", "other test value")
    did_save_value = prefs.load(test_key) == test_value
    prefs.delete(test_key)
    did_delete_value = prefs.load(test_key) is None
    did_not_delete_other_test_value = prefs.load("other test key") == "other test value"
    assert all([did_save_value, did_delete_value, did_not_delete_other_test_value])


def test_delete_empty_dict():
    _save(test_key, test_value)
    print(prefs.load(test_key))
    did_save_value = prefs.load(test_key) == test_value
    prefs.delete(test_key)
    did_delete_value = prefs.load(test_key) is None
    assert all([did_save_value, did_delete_value])
