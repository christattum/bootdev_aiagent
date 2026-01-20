import os
import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)

def get_files_info(working_directory, directory="."):

    try:
        abs_working_dir = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_working_dir, directory))

        # check target directory is a valid directory
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'

        # Check target dir is within working directory
        valid_target_dir = os.path.commonpath([abs_working_dir, target_dir]) == abs_working_dir
        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        # now return the info
        lines = []
        names = os.listdir(target_dir)
        for name in names:
            abs_name = os.path.join(target_dir, name)
            is_dir = os.path.isdir(abs_name)
            file_size = os.path.getsize(abs_name)
            text = f"- {name}: file_size={file_size} bytes, is_dir={is_dir}"
            lines.append(text)

        results = "\n".join(lines)

        return results
    
    except Exception as e:
        return f"Error: {e}"


def main():
    results = get_files_info(".", "calculator")
    print(results)

if __name__ == '__main__':
    main()