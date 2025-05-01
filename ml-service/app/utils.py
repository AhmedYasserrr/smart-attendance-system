import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


class Configuration:
    path = None
    data = None

    def __init__(self, path: str = "config.json"):
        self.path = BASE_DIR / path
        self.data = self.load_config()

    def load_config(self):
        with open(self.path, "r") as file:
            data = json.load(file)
        return data
