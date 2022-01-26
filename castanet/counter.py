"""This module counts instances in Python files."""

import libcst.matchers as match

def match_imports(cast_dict):
    """A function for counting the number of if statements in a Python program."""
    imports_dictionary = {}
    # Iterate through all of the Python files in a directory
    for file in cast_dict:
        # Find CASTs for each of these files
        cast = cast_dict[file]
        # Determine number of import statements for each file
        imports_list = match.findall(cast, match.Import())
        imports_dictionary[file] = len(imports_list)

    return imports_dictionary


def total_imports(imports_dict):
    """Find and combine the number of import statements in Python files in a specific directory."""
    total = 0
    for file in imports_dict:
        amount_of_imports = imports_dict[file]
        total += amount_of_imports

    return total

#matcher function to iterate through a file to get the total number of comments in a file
def match_comment(cast_dict):
    """A function for counting the number of comments statements in a Python program."""
    comment_dictionary = {}
    # Iterate through all of the Python files in a directory
    for file in cast_dict:
        # Find CASTs for each of these files
        cast = cast_dict[file]
        # Determine number of comments for each file
        comment = match.findall(cast, match.Comment())
        comment_dictionary[file] = len(comment)

    return comment_dictionary

#iterates through the number of comments found in each file
#and adds them up to get the total number of comments
def total_comment(cast_dict):
    """ function to add the total number of comments in dir """
    count = 0
    for file in cast_dict:
        comments = cast_dict[file]
        count += comments
    return count
