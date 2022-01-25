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
        imports = match.findall(cast, match.Import())
        imports_dictionary[file] = len(imports)

    return imports_dictionary

    #matcher function to iterate through a file to get the total number of comments in a file
def match_Comment(cast_dict):
    """A function for counting the number of comments statements in a Python program."""
    Comment_dictionary = {}
    # Iterate through all of the Python files in a directory
    for file in cast_dict:
        # Find CASTs for each of these files
        cast = cast_dict[file]
        # Determine number of comments for each file
        Comment = match.findall(cast, match.Comment())
        Comment_dictionary[file] = len(Comment)

    return Comment_dictionary

#iterates through the number of comments found in each file and adds them up to get the total number of comments
def total_Comment(cast_dict):
    count = 0
    for file in cast_dict:
        comments = cast_dict[file]
        count += comments
    return count


if __name__ == "__main__":
    directory = "/home/mkapfhammer/Documents/Allegheny/2022/Spring/CMPSC481/project-team-1/hello"
    file_list = generator.find_python_files(directory)
    string_file_list = generator.read_files(directory, file_list)
    tree_dict = generator.generate_cast(string_file_list)

    imports_dictionary = match_imports(tree_dict)
    print(imports_dictionary)

    Comment_dictionary = match_Comment(tree_dict)
    number_of_comments = total_comment(Comment_dictionary)
    print(Comment_dictionary)
