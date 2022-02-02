"""This module counts instances of statements in Python files."""
from typing import Dict
import libcst.matchers as match

def sum_cast_dict(cast_dict):
    """A function for calculating the sums of values from dictionaries in previous functions."""
    total = 0
    # Total imports
    for file in cast_dict:
        amount = cast_dict[file]
        total += amount

    return total

def match_imports(cast_dict):
    """A function for counting the number of import statements in a Python program."""
    imports_dictionary = {}
    # Iterate through all of the Python files in a directory
    for file in cast_dict:
        # Find CASTs for each of these files
        cast = cast_dict[file]
        # Determine number of import statements for each file
        imports_list = match.findall(cast, match.Import())
        imports_dictionary[file] = len(imports_list)

    return imports_dictionary


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


def count_function_without_docstrings(func_count: Dict) -> int:
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


def exists_docstring(cast_dict: dict, function_name: str) -> int:
    """A function for counting the number of function definitions in a Python program.
    returns:
        -1: function does not exist
        0: function exists without docstring
        1: function exists with docstring
    """
    # Iterate through all of the Python files in a directory
    for cast in cast_dict.values():
        # Determine number of function definitions for each file
        funcdefs = match.findall(cast, match.FunctionDef())
        for func in funcdefs:
            if func.name.value == function_name:
                if func.get_docstring():
                    return 1
                return 0
    return -1

    return total


def count_function_arguments(cast_dict, function_name):
    """A function to count the number of arguments for a given function."""
    function_dict = {}
    final_list = []
    necessary_nodes = []

    # Iterate through every file and find its CAST
    for file in cast_dict:
        cast = cast_dict[file]
        # Create a list of each of the function nodes for a given file
        function_list = match.findall(cast, match.FunctionDef())
        # Add function list to a dictionary
        function_dict[file] = function_list

    # Iterate through dictionary of function nodes per file
    for function_list in function_dict.values():
        # Create a list of all of the function nodes in a given directory
        final_list = final_list + function_list

    # Iterate through all function nodes in a directory
    for node in final_list:
        # Check to see if the provided function name is in the list
        if node.name.value == function_name:
            necessary_nodes.append(node)

    # If the function was not found, return function not found
    if len(necessary_nodes) == 0:
        return_statement = -1
    else:
        # If the function was found, count number of parameters for the function and return
        for node in necessary_nodes:
            parameters = node.params.params
            return_statement = len(parameters)

    return return_statement


def assignment_count(cast_dict):
    """A function for counting the number of assignment."""
    # An example of an assignment is x = y
    assignment_dictionary = {}

    for file in cast_dict:
        cast = cast_dict[file]
        # Determine number of assignment statements for each file
        imports = match.findall(cast, match.Assign())
        assignment_dictionary[file] = len(imports)

    return assignment_dictionary


def aug_assignment_count(cast_dict):
    """A function for counting the number of aug assignment."""
    # An example of an aug assignment is x += 5
    aug_assignment_dictionary = {}

    for file in cast_dict:
        cast = cast_dict[file]
        # Determine number of aug assignment statements for each file
        imports = match.findall(cast, match.AugAssign())
        aug_assignment_dictionary[file] = len(imports)

    return aug_assignment_dictionary
