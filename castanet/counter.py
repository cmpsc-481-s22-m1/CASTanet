# Import necessary types for typing
from typing import List, Tuple, Dict, Optional
# Import LibCST
import libcst as cst
import generate_trees as generator

import libcst.matchers as match
    
# TODO: Create function definitions related to all necessary user stories (should look somewhat like match_imports)
# TODO: Modify annotations to have node key as type and key as necessary information


def match_class_defs(cast_dict):
    """A function for counting the number of class definitions in a Python program."""
    class_defs_dictionary = {}
    # Iterate through all of the Python files in a directory
    for file in cast_dict:
        docstring_num = 0
        # Find CASTs for each of these files
        cast = cast_dict[file]
        # Determine number of class definitions for each file
        class_defs = match.findall(cast, match.ClassDef())
        class_defs_dictionary[file] = {"class" : 0, "docstring" : 0}
        class_defs_dictionary[file]["class"] = len(class_defs)

        for node in class_defs:
            if node.get_docstring():
                docstring_num += 1
        class_defs_dictionary[file]["docstring"] = docstring_num

    return class_defs_dictionary

def count_class_defs_without_docstrings(class_defs_dictionary: Dict) -> int:
    """Find the number of class definitions missing a docstring"""
    class_total = 0
    docstring_total = 0
    for file_count in class_defs_dictionary.values():
        class_total += file_count["class"]
        docstring_total += file_count["docstring"]
    return class_total - docstring_total

if __name__ == "__main__":
    directory = "/Users/nolanthompson/Desktop/College/CS481/CASTanet/hello"
    file_list = generator.find_python_files(directory)
    string_file_list = generator.read_files(directory, file_list)
    tree_dict = generator.generate_cast(string_file_list)

    class_def_dictionary = match_class_defs(tree_dict)
    class_def_without_docstring = count_class_defs_without_docstrings(class_def_dictionary)
    print(class_def_dictionary)
    print(class_def_without_docstring)

