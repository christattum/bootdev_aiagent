import os
from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write to python file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Python file to update",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to write",
            ),
        },
    ),
)

def write_file(working_directory, file_path, content):

    try:
        abs_working_dir = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(abs_working_dir, file_path))

        # Check file_path is not a directory
        if os.path.isdir(target_file):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        # Check target file is within working directory
        valid_target_file = os.path.commonpath([abs_working_dir, target_file]) == abs_working_dir
        if not valid_target_file:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        # Create any required parent directories
        dir_path = os.path.dirname(target_file)
        os.makedirs(dir_path, exist_ok = True)

        # update file contents
        f = open(target_file, "w")
        chars = f.write(content)
        if chars != len(content):
            return f"Error: Wrote {chars} to {file_path} but content was {len(content)} bytes"        
            
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
    except Exception as e:
        return f'Error: {e}'



