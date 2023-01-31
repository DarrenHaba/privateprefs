from __future__ import annotations

import privateprefs.core.database as _db


def load(key: str, group: None | str = None) -> str | None:
    """
    Loads the value for a given key.
    :param key: A key return the value for
    :type group: The group name to load the key-value pairs from
    :return: The stored value or None if key does not exist.
    """
    return _db.read(key, group)


def load_keys(group: str) -> dict | list:
    """
    Loads and returns key-value pairs for the given keys.
    :param group: The group name to load all key-value pairs from
    :return: A dict of key-value pairs by default, or a list of tuples.
    """
    return _db.read_keys(group)


def delete_all(group: str) -> None:
    """
    Deletes all stored key-value pairs.
    :param group: The group name to delete all the key-values from. To delete the default
    :return: None
    """
    _db.delete_all(group)


def delete(key: str, group: str | None = None) -> None:
    """
    Delete the value for the given key.
    :param key: The key to delete the value of
    :param group: The group name to delete the value from, is None key will be deleted
    :return: None
    """
    _db.delete(key, group)
