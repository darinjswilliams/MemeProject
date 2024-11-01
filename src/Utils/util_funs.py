import os


def create_tmp_dirs():
    path = ['./tmp', './static']
    [os.makedirs(name, exist_ok=True) for name in path]
