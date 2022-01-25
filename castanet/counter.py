# Import necessary types for typing
from typing import List, Tuple, Dict, Optional
# Import LibCST
import libcst as cst
from castanet import generate_trees as generator

import libcst.matchers as match

def match_imports(cast_dict):
    """A function for counting the number of if statements in a Python program."""
    imports_dictionary = {}
    # Iterate through all of the Python files in a directory
    for file in cast_dict:
        # Find CASTs for each of these files
        cast = cast_dict[file]
        # Determine number of import statements for each file
        imports = match.findall(cast, match.Import())
        imports_dictionary[file] = len(imports)

    return imports_dictionary


def match_funcdefs(cast_dict):
    """A function for counting the number of function definitions in a Python program."""
    func_count = {}
    # Iterate through all of the Python files in a directory
    for file in cast_dict:
        # track the number of docstrings
        docstring_num = 0
        # Find CASTs for each of these files
        cast = cast_dict[file]
        # Determine number of import statements for each file
        funcdefs = match.findall(cast, match.FunctionDef())
        # store the number of functions
        func_count[file] = {"function" : 0, "docstring": 0}
        func_count[file]["function"] = len(funcdefs)
        # iterate and count the number of docstrings
        for node in funcdefs:
            if node.get_docstring():
                docstring_num += 1
        func_count[file]["docstring"] = docstring_num

    return func_count


def get_missing_docstrings(func_count: Dict) -> int:
    """Find the number of functions missing a docstring.

    Args:
        func_count (Dict): function and docstring counts per file

    Returns:
        int: total number of functions - total number of docstrings
    """
    func_total = 0
    docstring_total = 0
    for file_count in func_count.values():
        func_total += file_count["function"]
        docstring_total += file_count["docstring"]
    return func_total - docstring_total


if __name__ == "__main__":
    directory = "/Users/tommyantle/cs481S2022/CASTanet/test_files"
    file_list = generator.find_python_files(directory)
    string_file_list = generator.read_files(directory, file_list)
    tree_dict = generator.generate_cast(string_file_list)

    imports_dictionary = match_imports(tree_dict)
    funcdefs_dictionary = match_funcdefs(tree_dict)

    print("\t")
    print("-------------------------------------------")
    print("Dictionary of imports: ", imports_dictionary)
    print("-------------------------------------------")
    print("Functions without docstrings: ", get_missing_docstrings(funcdefs_dictionary))
    print("-------------------------------------------")
    print("\t")
