from __future__ import annotations

import configparser
import pathlib

PROJECT_NAME = "privateprefs"

PATH_TO_USER_DIR = pathlib.Path.home()
PATH_TO_PROJECT_DATA_DIR = PATH_TO_USER_DIR / f".{PROJECT_NAME}"
PATH_TO_DATA_FILE = PATH_TO_PROJECT_DATA_DIR / "data.ini"
SECTION_NAME = PROJECT_NAME


def write(key, value):
    data_file_config = _get_config_parser_for_data_ini_file()
    data_file_config.set(SECTION_NAME, key, value)

    with PATH_TO_DATA_FILE.open("w") as file:
        data_file_config.write(file)


def read(key):
    data_file_config = _get_config_parser_for_data_ini_file()
    try:
        return data_file_config[SECTION_NAME][key]
    except KeyError:
        return None


def read_all(return_as_list: bool = False):
    data_file_config = _get_config_parser_for_data_ini_file()
    if return_as_list:
        return list(data_file_config.items(SECTION_NAME))
    return dict(data_file_config.items(SECTION_NAME))


def delete(key):
    data_file_config = _get_config_parser_for_data_ini_file()
    data_file_config.remove_option(SECTION_NAME, key)

    with PATH_TO_DATA_FILE.open("w") as file:
        data_file_config.write(file)


def delete_all():
    data_file_config = _get_config_parser_for_data_ini_file()
    data_file_config.remove_section(SECTION_NAME)

    with PATH_TO_DATA_FILE.open("w") as file:
        data_file_config.write(file)


def _get_config_parser_for_data_ini_file():
    _ensure_project_storage_dir_exists()
    _ensure_project_config_file_exists()

    config = configparser.ConfigParser()
    config.read(PATH_TO_DATA_FILE)

    _ensure_section_name_exists(config)
    return config


def _ensure_project_config_file_exists():
    if PATH_TO_DATA_FILE.exists() is False:
        try:
            PATH_TO_DATA_FILE.touch(exist_ok=True)
        except FileNotFoundError as e:
            return e


def _ensure_project_storage_dir_exists():
    if PATH_TO_PROJECT_DATA_DIR.exists() is False:
        try:
            PATH_TO_PROJECT_DATA_DIR.mkdir(exist_ok=True)
        except FileNotFoundError as e:
            return e


def _ensure_section_name_exists(config_parser):
    if not config_parser.sections().__contains__(SECTION_NAME):
        config_parser.add_section(SECTION_NAME)


def _uninstall():
    _delete_data_file()
    _delete_project_data_dir()


def _delete_data_file():
    if PATH_TO_DATA_FILE.exists():
        PATH_TO_DATA_FILE.unlink()


def _delete_project_data_dir():
    if PATH_TO_PROJECT_DATA_DIR.exists():
        PATH_TO_PROJECT_DATA_DIR.rmdir()


# if __name__ == "__main__":
    # write("bar", "gg")
    # write("112", "gg")
    # write("885", "gg")
    # write("524", "gg")
    # print(read("bar"))
    # delete("foo")
    # # delete("bar")
    # delete_all()
    # print(read("bar"))
    # print(read_all())
    # _uninstall()
