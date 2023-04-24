import os
import json

class Config:
    def __init__(self, config_file=None):
        if config_file is None:
            config_file = "config.json"
        self.config_file = config_file
        self.config = {}
        self.load_config()

    def load_config(self):
        with open(self.config_file, "r") as f:
            self.config = json.load(f)
        if "OPENAI_API_KEY" in os.environ:
            self.config["openai_api_key"] = os.environ["OPENAI_API_KEY"]

    def save_config(self):
        with open(self.config_file, "w") as f:
            json.dump(self.config, f, indent=4)

    def get(self, key):
        return self.config.get(key)

    def set(self, key, value):
        self.config[key] = value
        return self

    def update(self, key, value):
        self.config[key] = value
        return self

    def __getitem__(self, key):
        return self.config[key]

    def __setitem__(self, key, value):
        self.config[key] = value
        return self

    def __delitem__(self, key):
        del self.config[key]
        return self

    def __iter__(self):
        return iter(self.config)
