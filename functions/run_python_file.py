import os
import subprocess

def run_python_file(working_directory, file_path, args=[]) -> str:
    abs_working_dir = os.path.abspath(working_directory)
    rel_file_path = os.path.join(working_directory,file_path)
    abs_file_path = os.path.abspath(rel_file_path)

    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(rel_file_path):
        return f'Error: File "{file_path}" not found.'

    if not rel_file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        process_args = ["python3", rel_file_path] + args
        process = subprocess.run(process_args, capture_output=True, timeout=30)
        if process.returncode != 0:
            return f"Process exited with code {process.returncode}"
        if len(process.stdout) > 0:
            return f"STDOUT: {process.stdout}"
        if len(process.stderr) > 0:
            return f"STDERR: {process.stderr}"
        return "No output produced"

    except Exception as e:
        return f"Error: executing Python file: {e}"

    return ""

