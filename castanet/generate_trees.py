"""A Python program to iterate through a directory and create CASTs of each Python file."""

from os import listdir
import libcst as cst

def find_python_files(directory):
    """Find all of the python files in a given directory.

    Args:
        directory: string that contains the path of the directory

    Returns:
        list: every python file in the directory
    """
    file_list = []
    # Use listdir function of os to look through all of the files in a directory
    for file in listdir(directory):
        # Parse out only Python files that have the .py extension
        if file.endswith(".py"):
            file_list.append(file)

    # Return a list of the Python files in a directory
    return file_list


def read_files_in_directory(directory, file_list):
    """Read all of the python files in a directory, and turn them into Strings.

    Args:
        directory: string that contains the path of the directory
        file_list: list that contains python files in the directory

    Returns:
        dict: file name and its content as values
    """
    string_file_dict = {}
    # Iterate through all of the files in the list of Python files
    for file_name in file_list:
        # Create a file path with the directory and file name
        file_path = directory + "/" + file_name
        # Open each file
        with open(file_path, encoding="utf-8") as file:
            # Read each file
            file_string = file.read()
            # Add the name of the file and the string file to a dictionary
            string_file_dict[file_name] = file_string

    # Return a dictionary with the file name as the key, and file contents as value
    return string_file_dict


def read_single_file(file_path):
    """Read a single file as a string.
    Args:
        file_path: path of the file
    Returns:
        dict: file name and its content as values
    """
    string_file_dict = {}
    with open(file_path, encoding="utf-8") as file:
        # Read file
        file_string = file.read()
        # Add the name of the file and the string file to a dictionary
        string_file_dict[file_path] = file_string

    return string_file_dict


def generate_cast(file_strings_dict):
    """Create a CAST of each Python file using LibCST.

    Args:
        file_strings_dict: A dictionary of file names and its content

    Returns:
        dict: file name and the CAST for each file
    """
    tree_dict = {}
    # Iterate through a dictionary of file names and their contents represented as a String
    for file in file_strings_dict:
        file_string = file_strings_dict[file]
        # Generate a CAST using the module parser provided by LibCST
        cast = cst.parse_module(file_string)
        # Create a dictionary with the file name and file CAST
        tree_dict[file] = cast

    # Return a dictionary with the file name as they key and its corresponding CAST as the value
    return tree_dict
