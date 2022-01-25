# Import necessary types for typing
from typing import List, Tuple, Dict, Optional
# Import LibCST
import libcst as cst
from castanet import generate_trees as generator
import libcst.matchers as match

def match_ifstatements(cast_dict):
    """A function for counting the number of if statements in a Python program."""
    ifstatements_dictionary = {}
    # Iterate through all of the Python files in a directory
    for file in cast_dict:
        # Find CASTs for each of these files
        cast = cast_dict[file]
        # Determine number of if statements for each file
        ifs = match.findall(cast, match.If())
        ifstatements_dictionary[file] = len(ifs)

    return ifstatements_dictionary

if __name__ == "__main__":
    directory = "/Users/nolanthompson/Desktop/College/CS481/CASTanet/hello"
    file_list = generator.find_python_files(directory)
    string_file_list = generator.read_files(directory, file_list)
    tree_dict = generator.generate_cast(string_file_list)

    ifstatements_dictionary = match_ifstatements(tree_dict)
    print(ifstatements_dictionary)

