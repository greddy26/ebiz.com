import os

def file_exists(file):
    return os.path.exists(file) and os.path.isfile(file)