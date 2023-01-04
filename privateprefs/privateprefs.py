from __future__ import annotations

import privateprefs.internal.data_serializer as _internal


def load(key: str) -> str | None:
    """
    Loads a value for a given key.
    :param key: A lookup key
    :return: The stored value or None
    """
    return _internal.load(key)


def load_dict(keys: list = None) -> dict:
    """
    Loads multiple values for the given keys.
    :param keys: A list of Keys
    :return: A dict of key-value pairs
    """
    return _internal.load_dict(keys)


def delete_all() -> None:
    """
    Deletes all stored key-value pairs.
    :return: None
    """
    _internal.delete_all()


def delete(key: str) -> None:
    """
    Delete the value for a given key.
    :param key: The key to delete the value of
    :return: None
    """
    _internal.delete(key)
