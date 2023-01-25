from __future__ import annotations

import configparser
import pathlib

from platformdirs import user_data_dir

PROJECT_NAME = "privateprefs"

PATH_TO_USER_DATA_PROJECT_DIR = pathlib.Path(user_data_dir(PROJECT_NAME, appauthor=False))
PATH_TO_DATA_FILE = PATH_TO_USER_DATA_PROJECT_DIR / "data.ini"
PATH_TO_CONFIG_FILE = pathlib.Path(PATH_TO_USER_DATA_PROJECT_DIR) / "config.ini"
DEFAULT_GROUP_NAME = "default"


def write(key: str, value: str, group: None | str = None) -> None:
    """
    Write a key-value pair to the data.ini file.
    :type group: The group name to store the key-value pairs under
    :param key: A unique key to write the value under
    :param value: The value to be stored
    :return: None
    """
    if group is None:
        group = DEFAULT_GROUP_NAME

    data_file_config = _get_config_parser_for_data_ini_file(group)
    data_file_config.set(group, key, value)

    with PATH_TO_DATA_FILE.open("w") as file:
        data_file_config.write(file)


def read(key: str) -> str | None:
    """
    Reads and returns the value for a given key from the data.ini file.
    :param key: A key to read the value of
    :return: The value stored under the given key, or None if the key does not exist
    """
    data_file_config = _get_config_parser_for_data_ini_file()
    try:
        return data_file_config[DEFAULT_GROUP_NAME][key]
    except KeyError:
        return None


def read_keys(keys: list = None, return_as_list: bool = False) -> dict | list:
    """
    Reads and returns key-value pairs for the given keys.
    :param keys: List of keys to return, by default all key-value pairs will be returned.
    :param return_as_list: If true a list of tuples will be returned, If false the default dict will be returned
    :return: A dict of key-value pairs by default, or a list of tuples.
    """
    data_file_config = _get_config_parser_for_data_ini_file()
    tuple_key_values = data_file_config.items(DEFAULT_GROUP_NAME)

    filtered_list = []
    if keys is None:
        filtered_list = tuple_key_values
    else:
        for tuple_key_value in tuple_key_values:
            key = tuple_key_value[0]
            if keys.__contains__(key):
                filtered_list.append(tuple_key_value)

    if return_as_list:
        return filtered_list
    return dict(filtered_list)


def delete(key: str) -> None:
    """
    Deletes a key-value pair from the data.ini file for the given key.
    :param key: A key that will be used to delete the corresponding key-value pair
    :return: None
    """
    data_file_config = _get_config_parser_for_data_ini_file()
    data_file_config.remove_option(DEFAULT_GROUP_NAME, key)

    with PATH_TO_DATA_FILE.open("w") as file:
        data_file_config.write(file)


def delete_all() -> None:
    """
    Deletes all key-value pair from the data.ini file.
    :return: None
    """
    data_file_config = _get_config_parser_for_data_ini_file()
    data_file_config.remove_section(DEFAULT_GROUP_NAME)
    _ensure_section_name_exists(data_file_config)

    with PATH_TO_DATA_FILE.open("w") as file:
        data_file_config.write(file)


def pre_uninstall() -> None:
    """
    Removes all dictionaries and files created by this package.
    :return: None
    """
    _delete_data_file()
    _delete_project_data_dir()


def _get_config_parser_for_data_ini_file(group_name: str | None = None) -> configparser:
    """
    Creates an instance of a ConfigParser and reads in the persistent data.ini file.
    :type group_name: The group name to store the key-value pairs under
    :return: An instance of ConfigParser
    """
    if group_name is None:
        group_name = DEFAULT_GROUP_NAME

    _ensure_project_data_dir_exists()
    _ensure_project_config_file_exists()

    config = configparser.ConfigParser()
    config.read(PATH_TO_DATA_FILE)

    _ensure_section_name_exists(config, group_name)
    return config


def _ensure_project_config_file_exists() -> None:
    """
    Make sure a data.ini file exists in the projects persistent storage directory.
    :return: None or the IO Error given.
    """
    if PATH_TO_DATA_FILE.exists() is False:
        PATH_TO_DATA_FILE.touch(exist_ok=True)


def _ensure_project_data_dir_exists() -> None:
    """
    Make sure the project dictionary exist to store persistent data.
    """
    if PATH_TO_USER_DATA_PROJECT_DIR.exists() is False:
        PATH_TO_USER_DATA_PROJECT_DIR.mkdir(exist_ok=True)


def _ensure_section_name_exists(config_parser: configparser, group_name: str | None = None) -> None:
    """
    We store all data under a section named the same as the project name e.g. [privateprefs].
    This name doesn't exist for new ini files, so we make sure it is added here.
    :type group_name: The group name to store the key-value pairs under
    :param config_parser: An instance of ConfigParser()
    :return: None
    """
    if group_name is None:
        group_name = DEFAULT_GROUP_NAME
    if not config_parser.sections().__contains__(group_name):
        config_parser.add_section(group_name)


def _delete_data_file() -> None:
    """
    Deletes the data.ini file created to store persistent data
    :return: None
    """
    if PATH_TO_DATA_FILE.exists():
        PATH_TO_DATA_FILE.unlink()


def _delete_project_data_dir() -> None:
    """
    Deletes the privateprefs dictionary created to store persistent data
    :return: None
    """
    if PATH_TO_USER_DATA_PROJECT_DIR.exists():
        PATH_TO_USER_DATA_PROJECT_DIR.rmdir()

