from pathlib import Path


def get_file_path_stem(file_path):
    return Path(file_path).stem
