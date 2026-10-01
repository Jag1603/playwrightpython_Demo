import os
import yaml


class ConfigReader:

    @staticmethod
    def load():

        environment = os.getenv("ENV", "qa")

        file_path = f"config/{environment}.yaml"

        with open(file_path, "r") as file:
            return yaml.safe_load(file)