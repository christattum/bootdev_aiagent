import os

MAX_CHARS = 10000

def get_file_content(working_directory, file_path):

    try:
    
        abs_working_dir = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(abs_working_dir, file_path))

        # check target file is a valid file
        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        # Check target file is within working directory
        valid_target_file = os.path.commonpath([abs_working_dir, target_file]) == abs_working_dir
        if not valid_target_file:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        f = open(target_file, "r")
        content = f.read(MAX_CHARS)

        # was the read truncated?
        if f.read(1):
            content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

        return content
    
    except Exception as e:
        return f"Error: {e}"

def main():
    results = get_file_content("calculator", "lorem.txt")
    print(results)

if __name__ == '__main__':
    main()