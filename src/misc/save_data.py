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
            print("Error! This file is not structured like a JSON!")
            return False
        return True

    def load_json(self, path):
        if path:
            try:
                with open(path) as f:
                    file_content = f.read()

                    if self.is_json(file_content):
                        self.file_data = json.loads(file_content)                   
            except Exception as e:
                print("An Error occured while trying to read the JSON!",e)

    def save_json(self, path):
        if path:
            try:
                with open(path + ".json","w",encoding="utf-8") as f:
                    save_data = json.dumps(self.file_data)
                    f.write(save_data)
            except Exception as e:
                print("An Error occured while trying to save the JSON!",e)

    def set_element(self, element, data):
        self.file_data[element] = data

    def get_element(self, element):
        if element in self.file_data:
            return self.file_data[element]
        else:
            print("Error! This JSON element doesn't exist!")
            return ""