import os

def get_files_info(working_directory, directory=".") -> str:
    abs_working_dir = os.path.abspath(working_directory)
    path = os.path.abspath(os.path.join(working_directory, directory))

    if not os.path.exists(path):
        return f"Error: {path} does not exist"

    if not path.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(path):
        return f'Error: "{directory}" is not a directory'

    try:
        #files = os.listdir(path)
        file_details = []

        with os.scandir(path) as dir:
            for entry in dir:
                file_details.append(f"{entry.name}: file_size= {entry.stat().st_size} byte, is_dir={entry.is_dir()}")
        
        
        #for file in files:
        #    filepath = os.path.join(path,file)
        #    filesize = os.stat(filepath).st_size
        #    file_details.append(f"- {file}: file_size={filesize} bytes, is_dir={os.path.isdir(filepath)}")

        return "\n".join(file_details)

    except FileNotFoundError:
        return f"Error: {path} does not exist"

