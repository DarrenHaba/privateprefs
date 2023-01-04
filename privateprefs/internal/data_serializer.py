from __future__ import annotations

import ast
import pkg_resources

path_to_test_file = pkg_resources.resource_filename(__name__, 'data/prefs.txt')


def load(key: str) -> str | None:
    """
    Loads a value for a given key.
    :param key: A lookup key
    :return: The stored value or None
    """
    dict_form_text_file = load_dict_from_file()
    if key in dict_form_text_file.keys():
        return dict_form_text_file[key]
    else:
        return None


def load_dict(keys: list = None) -> dict:
    """
    Loads multiple values for the given keys.
    :param keys: A list of Keys
    :return: A dict of key-value pairs
    """
    dict_form_text_file = load_dict_from_file()
    if keys is None:
        return dict_form_text_file
    filtered_dict = {}
    for key in keys:
        if key in dict_form_text_file.keys():
            filtered_dict[key] = dict_form_text_file[key]
    return filtered_dict


def delete_all() -> None:
    """
    Deletes all stored key-value pairs.
    :return: None
    """
    save_empty_file()


def delete(key: str) -> None:
    """
    Delete the value for a given key.
    :param key: The key to delete the value of
    :return: None
    """
    loaded_dict = load_dict_from_file()
    loaded_dict.pop(key)
    is_dict_empty = (loaded_dict == {})
    if is_dict_empty:
        save_empty_file()
    else:
        save_dict_to_file(loaded_dict)


def save_dict_to_file(date: dict) -> None:
    """
    Converts a dict into a string and saves it to a .txt file
    :param date: A dict containing key-value pairs
    :return: None
    """
    str_form_text_file = str(date)
    with open(path_to_test_file, "w") as file:
        file.write(str_form_text_file)


def load_dict_from_file() -> dict:
    """
    Loads a string from a .txt file and converts it to the returned dict
    :return: A dict containing key-value pairs
    """
    with open(path_to_test_file, "r") as file:
        str_form_text_file = file.read()
        if str_form_text_file == "":
            dict_form_text_file = {}
        else:
            dict_form_text_file = ast.literal_eval(str_form_text_file)
        return dict_form_text_file


def save_empty_file() -> None:
    """
    Deletes all stored key-value pairs by writing a blank string to stored .txt file
    :return: None
    """
    with open(path_to_test_file, "w") as file:
        file.write("")


def save(key, value) -> None:
    """
    Saves a value inside the given key.
    :param key: The key used to save the value to
    :param value: The value to save
    :return: None
    """
    save_dict({key: value})


def save_dict(data: dict) -> None:
    """
    Saves a dict of key-value pairs.
    :param data: A dict containing key-value pairs
    :return: None
    """
    dict_form_text_file = load_dict_from_file()
    dict_form_text_file.update(data)
    save_dict_to_file(dict_form_text_file)
