"""A Python program to iterate through a directory and create CASTs of each Python file."""

from os import listdir
import libcst as cst

def find_python_files(directory):
    """Find all of the python files in a given directory."""
    file_list = []
    # Use listdir function of os to look through all of the files in a directory
    for file in listdir(directory):
        # Parse out only Python files that have the .py extension
        if file.endswith(".py"):
            file_list.append(file)
    
    # Return a list of the Python files in a directory
    return file_list


def read_files(directory, file_list):
    """Read all of the python files in a directory, and turn them into Strings."""
    string_file_dict = {}
    # Iterate through all of the files in the list of Python files
    for file in file_list:
        # Create a file path with the directory and file name
        file_path = directory + "/" + file
        # Open each file
        read_file = open(file_path)
        # Read each file
        file_string = read_file.read()
        # Add the name of the file and the string file to a dictionary
        string_file_dict[file] = file_string

    # Return a dictionary with the file name as the key, and the string of the file contents as the value    
    return string_file_dict


def generate_cast(file_strings_dict):
    """Create a CAST of each Python file using LibCST."""
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


if __name__ == "__main__":
    directory = "/Users/tommyantle/cs481S2022/CASTanet/hello"
    file_list = find_python_files(directory)
    string_file_list = read_files(directory, file_list)
    tree_list = generate_cast(string_file_list)
    print(tree_list)