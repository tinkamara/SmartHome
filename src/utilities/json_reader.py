import json

class JsonReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_json(self):
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            print("Die angegebene Datei wurde nicht gefunden.")
        except json.JSONDecodeError:
            print("Die Datei enthält ungültiges JSON.")