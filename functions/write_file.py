import os

def write_file(working_directory, file_path, content) -> str:
    abs_working_dir = os.path.abspath(working_directory)
    rel_file_path = os.path.join(working_directory, file_path)
    abs_target_file = os.path.abspath(rel_file_path)
    
    if not abs_target_file.startswith(abs_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(rel_file_path):
        split_dir_path = rel_file_path.split('/')[:-1]
        dir_path = "."

        for d in split_dir_path:
            dir_path = os.path.join(dir_path,d)

        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

    with open(rel_file_path, "w") as f:
        char_written = f.write(content)
        return f'Successfully wrote to "{rel_file_path}" ({char_written} characters written)'


    return ""
