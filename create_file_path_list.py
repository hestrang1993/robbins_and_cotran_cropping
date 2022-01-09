# -*- coding: utf-8 -*-

import os


def create_file_path_list(root_dir):
    """
    Parse through a specific directory.
    Then, create an absolute path string for every file in a directory (exclude subdirectories).
    Finally, return all these paths as a list.

    Parameters
    ----------
    root_dir : str
        The absolute path to the directory.

    Returns
    -------
    list:
        A list of all absolute filepaths for all files in a specific directory.
    """
    files = [f for f in os.listdir(root_dir) if os.path.isfile(os.path.join(root_dir, f))]
    files_list = []
    root = os.path.dirname(os.path.abspath(__file__))
    for file in files:
        file_path = os.path.join(root, root_dir, file)
        files_list.append(file_path)
    return files_list
