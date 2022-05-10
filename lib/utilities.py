import os


def get_root_dir() -> str:
    """ Get the root directory of the project. """
    return os.path.realpath(os.path.join(
        os.getcwd(), os.path.dirname(__file__), ".."))


def safe_makedirs(dir_path: str) -> str:
    """ Safely create a directory and return the path. """
    if os.path.exists(dir_path) and not os.path.isdir(dir_path):
        raise Exception(f"{dir_path} is not a directory.")
    os.makedirs(dir_path, exist_ok=True)
    return os.path.realpath(dir_path)
