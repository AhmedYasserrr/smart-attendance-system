import json


class Configuration:
    path = None
    data = None

    def __init__(self, path: str = "config.json"):
        self.path = path
        self.data = self.load_config()

    def load_config(self):
        with open(self.path, "r") as file:
            data = json.load(file)
        return data
