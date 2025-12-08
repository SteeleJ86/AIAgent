import os

def get_file_content(working_directory, file_path) -> str:
    MAX_CHARS = 10000

    abs_working_dir = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))

    if not os.path.isfile(target_file):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    if not target_file.startswith(abs_working_dir):
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'

    try:
        with open(target_file, "r") as f:
            file_content_string = f.read(MAX_CHARS)

            return file_content_string if len(file_content_string) < MAX_CHARS else file_content_string + f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

    except Exception as e:
        return f'Error: failed to read "{file_path}": {e}'
