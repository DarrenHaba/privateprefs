import pkg_resources
import ast

path_to_test_file = pkg_resources.resource_filename(__name__, 'data/prefs.txt')

def _save_dict_to_file(dict_form_text_file: dict):
    str_form_text_file = str(dict_form_text_file)
    with open(path_to_test_file, "w") as file:
        file.write(str_form_text_file)


def _save_empty_file():
    with open(path_to_test_file, "w") as file:
        file.write("")


def _load_dict_from_file():
    with open(path_to_test_file, "r") as file:
        str_form_text_file = file.read()
        if str_form_text_file == "":
            dict_form_text_file = {}
        else:
            dict_form_text_file = ast.literal_eval(str_form_text_file)
        return dict_form_text_file


def _save(key, value):
    _save_dict({key: value})


def _save_dict(data: dict):
    dict_form_text_file = _load_dict_from_file()
    dict_form_text_file.update(data)
    _save_dict_to_file(dict_form_text_file)


def load(key, default_value = None):
    dict_form_text_file = _load_dict_from_file()
    if key in dict_form_text_file.keys():
        return dict_form_text_file[key]
    if default_value is not None:
        _save(key, default_value)
    return default_value


def load_dict(keys=None):
    dict_form_text_file = _load_dict_from_file()
    if keys is None:
        return dict_form_text_file
    filtered_dict = {}
    for key in keys:
        if key in dict_form_text_file.keys():
            filtered_dict[key] = dict_form_text_file[key]
    return filtered_dict


def clear():
    _save_empty_file()


def delete(key: str):
    loaded_dict = _load_dict_from_file()
    loaded_dict.pop(key)
    is_dict_empty = (loaded_dict == {})
    if is_dict_empty:
        _save_empty_file()
    else:
        _save_dict_to_file(loaded_dict)
