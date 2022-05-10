from __future__ import annotations
import json
import os
from .utilities import get_root_dir


class Config:
    """
    The base config class for a Python script.

    Attributes:

    - file_name: the config file name (default: `"script"`)
    - version: the version of the script (default: `"0.1.0"`)
    - file_path: the config file path
    - data: the data of the config file
    - input_functions: the class methods used to get user inputs

    Methods:

    - read_config(): read the config file and return the config dict
    - initialize_config(): initialize the config file and return the config dict

    Notes:

    - The `data` attribute is only available after invoking `read_config` method.
    - You could override the `input_functions` attribute in subclasses if needed.
    - The functions inside `input_functions` array should return a dict.
    """

    def __init__(self, file_name: str = "script", version: str = "0.1.0") -> None:
        self.file_name = file_name
        self.version = version
        self.file_path = os.path.join(get_root_dir(), self.file_name) + ".json"
        self.input_functions = []
        self.data = {}

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} file_name={self.file_name}>"

    def read_config(self) -> dict[str, str]:
        """ Read the config file and return the data. """
        try:
            print(f"Reading the config file from {self.file_path}.")
            if os.path.isdir(self.file_path):
                raise FileNotFoundError(
                    f"{self.file_path} is a directory, not a file.")
            elif os.path.isfile(self.file_path):
                print(f"{self.file_path} is a file.")
                with open(self.file_path, "r") as f:
                    data = json.loads(f.read())
            else:
                print(f"{self.file_path} does not exist.")
                data = self.initialize_config()
            self.data = data
            return data
        except FileNotFoundError as e:
            print(e)
            exit(1)
        except json.JSONDecodeError:
            print(f"{self.file_path} is not a valid JSON file.")
            exit(1)

    def initialize_config(self) -> dict[str, str]:
        """ Initialize the config file and return the data. """
        print(f"Initializing {self.file_name}.")
        # constants
        data = {
            "app": self.file_name,
            "version": self.version,
        }
        # user inputs
        if self.input_functions:
            for input_fn in self.input_functions:
                data.update(input_fn())
        # write config
        with open(self.file_path, "w") as f:
            f.write(json.dumps(data))
        print(f"{self.file_path} is created.")
        return data


def main(args=None):
    try:
        config = Config("script")
        print("==========================")
        print(config.initialize_config())
        print("==========================\n")

        print("==========================")
        print(config.read_config())
        print("==========================\n")
    except KeyboardInterrupt:
        print("Exiting...")


if __name__ == '__main__':
    main()
