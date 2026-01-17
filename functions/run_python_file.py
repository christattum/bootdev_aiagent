import os

def run_python_file(working_directory, file_path, args=None):
    
    abs_working_dir = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(abs_working_dir, file_path))

    # Check file_path ends in .py
    if len(target_file) < 3 or target_file[-3:] != ".py":
        return f'Error: "{file_path}" is not a Python file'

    # Check file_path is a file
    if not os.path.isfile(target_file):
        return f'Error: "{file_path}" does not exist or is not a regular file'

    # Check target file is within working directory
    if not os.path.commonpath([abs_working_dir, target_file]) == abs_working_dir:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        