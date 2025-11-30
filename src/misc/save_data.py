import flet as ft
import json

from misc.singleton import singleton

@singleton
class SaveData:
    def __init__(self):
        self.file_data = ""

    def is_json(self, myjson):
        try:
            json.loads(myjson)
        except ValueError as e:
            return False
        return True

    def load_json(self, path):
        file_content = ""
        with open(path) as f:
            file_content = f.read()

        if self.is_json(file_content):
            self.file_data = json.loads(file_content)

    def set_element(self, element, data):
        self.file_data[element] = data

    def get_element(self, element):
        if element in self.file_data:
            return self.file_data[element]
        else:
            return ""