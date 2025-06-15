import os

MAX_CHARS = 10000


def get_file_content(working_directory, file_path) -> str:
    abs_file = os.path.abspath(file_path)
    abs_work = os.path.abspath(working_directory)
    if abs_file == abs_work:
        return "Error: The desired file cannot be the working directory, and vice-versa"
    if file_path.startswith("/"):
        return f"Error: File {file_path} should not be specified from the root"
    true_path = os.path.join(abs_work, file_path)
    if not os.path.exists(true_path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(true_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    with open(true_path, "r") as f:
        file_content_str = f.read(MAX_CHARS)
    if len(file_content_str) >= MAX_CHARS:
        file_content_str += f'\n[...File "{file_path}" truncated at 10000 characters]'
    return file_content_str
