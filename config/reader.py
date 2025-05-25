from pydantic_core import from_json

from config.config import Config


class ConfigReader:
    def __init__(self, path_to_file: str = "config/config.json"):
        self.__path_to_file = path_to_file

    def read(self) -> Config:
        with open(self.__path_to_file, "r") as f:
            return Config.model_validate(from_json(f.read()))
