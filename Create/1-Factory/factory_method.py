import xml.etree.ElementTree as etree
import json


class JSONConnector():
    def __init__(self, filepath):
        self._data = dict()
        with open(filepath, mode="r", encoding="utf-8") as f:
            self._data = json.load(f)

    @property
    def parsed_data(self):
        return self._data


class XMLConnecter():
    def __init__(self, filepath):
        self._tree = etree.parse(filepath)

    @property
    def parsed_data(self):
        return self._tree


def connection_factory(filepath):
    if filepath.endswith("json"):
        connector = JSONConnector
    elif filepath.endswith("xml"):
        connector = XMLConnecter
    else:
        raise ValueError(f"Cannot connect to {filepath}.")
    return connector(filepath)


def connect_to(filepath):
    factory = None
    try:
        factory = connection_factory(filepath)
    except ValueError as ve:
        print(ve)
    return factory
