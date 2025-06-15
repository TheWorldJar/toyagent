import os


def get_files_info(working_directory, directory=None) -> str:
    if directory is None:
        directory = working_directory
    if directory.startswith("/"):
        return f"Error: Directory {directory} should not be specified from the root"
    abs_dir = os.path.abspath(directory)
    abs_work = os.path.abspath(working_directory)
    if abs_dir == abs_work:
        true_dir = abs_work
    else:
        true_dir = os.path.join(abs_work, directory)
    if not os.path.exists(true_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(true_dir):
        return f'Error: "{directory}" is not a directory'
    contents = os.listdir(true_dir)
    files_info = ""
    for file in contents:
        files_info += f"{file}: file_size={os.path.getsize(os.path.join(true_dir, file))} bytes, is_dir={os.path.isdir(os.path.join(true_dir, file))}\n"
    return files_info[:-1]
