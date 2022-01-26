"""This module counts instances in Python files."""
from typing import Dict
import libcst.matchers as match

def match_imports(cast_dict):
    """A function for counting the number of if statements in a Python program."""
    imports_dictionary = {}
    # Iterate through all of the Python files in a directory
    for file in cast_dict:
        # Find CASTs for each of these files
        cast = cast_dict[file]
        # Determine number of import statements for each file
        imports_list = match.findall(cast, match.While())
        imports_dictionary[file] = len(imports_list)

    return imports_dictionary


def total_imports(imports_dict):
    """Find and combine the number of import statements in Python files in a specific directory."""
    total = 0
    for file in imports_dict:
        amount_of_imports = imports_dict[file]
        total += amount_of_imports

    return total


def match_comment(cast_dict):
    """A function for counting the number of comments statements in a Python program."""
    comment_dictionary = {}
    for file in cast_dict:
        # Find CASTs for each of these files
        cast = cast_dict[file]
        # Determine number of comments for each file
        comment = match.findall(cast, match.Comment())
        comment_dictionary[file] = len(comment)

    return comment_dictionary


def total_comment(cast_dict):
    """Add the total number of comments in directory."""
    count = 0
    for file in cast_dict:
        comments = cast_dict[file]
        count += comments
    return count


def count_whileloops(cast_dict):
    """A function for counting the number of while loops in a Python program."""
    while_dictionary = {}
    # Iterate through all of the Python files in a directory
    for file in cast_dict:
        # Find CASTs for each of these files
        cast = cast_dict[file]
        while_loops = match.findall(cast, match.While())
        while_dictionary[file] = len(while_loops)

    return while_dictionary


def count_forloops(cast_dict):
    """A function for counting the number of while loops in a Python program."""
    for_dictionary = {}
    # Iterate through all of the Python files in a directory
    for file in cast_dict:
        # Find CASTs for each of these files
        cast = cast_dict[file]
        # Determine number of for statements for each file
        imports = match.findall(cast, match.For())
        for_dictionary[file] = len(imports)

    return for_dictionary


def amount_loops(loops_dict):
    """Find and combine the number of for and while loops in a Python file."""
    total_loops = 0
    for file in loops_dict:
        amount_of_loops = loops_dict[file]
        total_loops += amount_of_loops

    return total_loops


def match_if_statements(cast_dict):
    """A function for counting the number of if statements in a Python program."""
    if_statements_dictionary = {}
    # Iterate through all of the Python files in a directory
    for file in cast_dict:
        # Find CASTs for each of these files
        cast = cast_dict[file]
        # Determine number of comments for each file
        ifs = match.findall(cast, match.If())
        if_statements_dictionary[file] = len(ifs)

    return if_statements_dictionary


def total_if_statements(if_statements_dictionary):
    """Find and combine all of the if statements in Python files at a specified directory"""
    total_ifs = 0
    for file in if_statements_dictionary:
        amount_of_ifs = if_statements_dictionary[file]
        total_ifs += amount_of_ifs

    return total_ifs


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
