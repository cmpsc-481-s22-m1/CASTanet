# Import necessary types for typing
from typing import List, Tuple, Dict, Optional
# Import LibCST
import libcst as cst
import generate_trees as generator

import libcst.matchers as match
    
# TODO: Create function definitions related to all necessary user stories (should look somewhat like match_imports)
# TODO: Modify annotations to have node key as type and key as necessary information


def match_imports(cast_dict):
    """A function for counting the number of if statements in a Python program."""
    imports_dictionary = {}
    # Iterate through all of the Python files in a directory
    for file in cast_dict:
        # Find CASTs for each of these files
        cast = cast_dict[file]
        # Determine number of import statements for each file
        imports = match.findall(cast, match.For.Iter())
        imports_dictionary[file] = len(imports)

    return imports_dictionary


def match_import(cast_dict):
    """A function for counting the number of if statements in a Python program."""
    imports_dictionary = {}
    # Iterate through all of the Python files in a directory
    for file in cast_dict:
        # Find CASTs for each of these files
        cast = cast_dict[file]
        # Determine number of import statements for each file
        imports = match.findall(cast, match.While.body())
        imports_dictionary[file] = len(imports)

    return imports_dictionary

if __name__ == "__main__":
    directory = "say_hello.py"
    file_list = generator.find_python_files(directory)
    string_file_list = generator.read_files(directory, file_list)
    tree_dict = generator.generate_cast(string_file_list)

    imports_dictionary = match_imports(tree_dict), match_import(tree_dict)
    print(imports_dictionary)

