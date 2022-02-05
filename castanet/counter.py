"""This module counts instances of statements in Python files."""
from typing import Dict
import libcst.matchers as match
from castanet import generate_trees as generator

def generate_cast_single_file(path):
    """Generate a dictionary of a single file and its CAST.
    Args:
        path: The path of a file

    Returns:
        dict: Dictionary of file and corresponding CAST as value
    """
    string_file_dict = generator.read_single_file(path)
    cast_dict = generator.generate_cast(string_file_dict)

    return cast_dict


def generate_cast_directory(path):
    """Generate a dictionary of all of multiple files and CASTs.
    Args:
        path: The path of a directory

    Returns:
        dict: Dictionary of files in a directory and corresponding CASTs
    """
    file_list = generator.find_python_files(path)
    string_file_list = generator.read_files_in_directory(path, file_list)
    cast_dict = generator.generate_cast(string_file_list)

    return cast_dict


def file_or_directory(path):
    """Determine if path is for file or directory."""
    if path.endswith(".py"):
        cast_dict = generate_cast_single_file(path)
    else:
        cast_dict = generate_cast_directory(path)
    return cast_dict


def sum_dict_vals(values_dict):
    """Calculate the sums of values from dictionaries in following functions.

    Args:
        values_dict: dictionary of total values for metrics

    Returns:
        int: total number of items in dictionary
    """
    total = 0
    # Total imports
    for file in values_dict:
        amount = values_dict[file]
        total += amount

    return total


def count_imports(path:str):
    """Count the number of import statements.

    Args:
        cast_dict: A dictionary of files and the corresponding CAST's

    Returns:
        dict: files and the corresponding amount of imports
    """
    imports_dict = {}

    cast_dict = file_or_directory(path)
    # Iterate through all of the Python files in a directory
    for file, cast in cast_dict.items():
        # Find CASTs for each of these files
        # Determine number of import statements for each file
        imports_list = match.findall(cast, match.Import())
        imports_dict[file] = len(imports_list)

    return imports_dict


def count_functions(path:str):
    """Count the number of functions.

    Args:
        cast_dict: A dictionary of files and the corresponding CAST's

    Returns:
        dict: files and the corresponding amount of functions
    """
    function_dictionary = {}

    cast_dict = file_or_directory(path)
    #Iterate through all python files in a dictionary
    for file, cast in cast_dict.items():
        # Determine number of functions for each file
        function = match.findall(cast, match.FunctionDef())
        function_dictionary[file] = len(function)

    return function_dictionary


def count_comments(path: str):
    """Count the number of comments.

    Args:
        cast_dict: A dictionary of files and the corresponding CAST's

    Returns:
        dict: files and the corresponding amount of comments
    """
    comments_dict = {}

    cast_dict = file_or_directory(path)
    for file, cast in cast_dict.items():
        # Determine number of comments for each file
        comments_list = match.findall(cast, match.Comment())
        comments_dict[file] = len(comments_list)

    return comments_dict


def count_while_loops(path: str):
    """Count the number of while loops.

    Args:
        cast_dict: A dictionary of files and the corresponding CAST's

    Returns:
        dict: files and the corresponding amount of while loops
    """
    while_loops_dict = {}

    cast_dict = file_or_directory(path)

    # Iterate through all of the Python files in a directory
    for file, cast in cast_dict.items():
        while_loops_list = match.findall(cast, match.While())
        while_loops_dict[file] = len(while_loops_list)

    return while_loops_dict


def count_for_loops(path: str):
    """Count the number of for loops.

    Args:
        cast_dict: A dictionary of files and the corresponding CAST's

    Returns:
        dict: files and the corresponding amounts of for loops
    """
    for_loops_dict = {}

    cast_dict = file_or_directory(path)

    # Iterate through all of the Python files in a directory
    for file, cast in cast_dict.items():
        # Determine number of for statements for each file
        for_loops_list = match.findall(cast, match.For())
        for_loops_dict[file] = len(for_loops_list)

    return for_loops_dict


def count_if_statements(path: str):
    """Count the number of if statements.

    Args:
        cast_dict: A dictionary of files and the corresponding CAST's

    Returns:
        dict: files and the corresponding amounts of if statements
    """
    if_statements_dict = {}
    cast_dict = file_or_directory(path)

    # Iterate through all of the Python files in a directory
    for file, cast in cast_dict.items():
        # Determine number of if statements for each file
        if_statements_list = match.findall(cast, match.If())
        if_statements_dict[file] = len(if_statements_list)

    return if_statements_dict


def count_func_defs(path):
    """Count the number of function definitions.

    Args:
        cast_dict: A dictionary of files and corresponding CAST's

    Returns:
        dict: files and the corresponding amounts of function definitions
    """
    func_defs_dict = {}
    cast_dict = file_or_directory(path)

    # Iterate through all of the Python files in a directory
    for file, cast in cast_dict.items():
        # Track the number of docstrings
        docstring_num = 0
        # Determine number of function definitions for each file
        func_defs_list = match.findall(cast, match.FunctionDef())
        # Store the number of functions
        func_defs_dict[file] = {"function": 0, "docstring": 0}
        func_defs_dict[file]["function"] = len(func_defs_list)
        # Iterate and count the number of docstrings
        for node in func_defs_list:
            if node.get_docstring():
                docstring_num += 1
        func_defs_dict[file]["docstring"] = docstring_num

    return func_defs_dict


def count_function_without_docstrings(func_count: Dict) -> int:
    """Count the number of functions without docstrings.

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


def docstring_exists(path: str, function_name: str) -> int:
    """Count the number of function definitions.
    returns:
        -1: function does not exist
        0: function exists without docstring
        1: function exists with docstring
    """
    cast_dict = file_or_directory(path)

    # Iterate through all of the Python files in a directory
    for cast in cast_dict.values():
        # Determine number of function definitions for each file
        func_defs_list = match.findall(cast, match.FunctionDef())
        for func in func_defs_list:
            if func.name.value == function_name:
                if func.get_docstring():
                    return 1
                return 0
    return -1


def count_class_defs(path: str):
    """Count the number of class definitions.

    Args:
        cast_dict: A dictionary of files and the corresponding CAST's

    Return:
        dict: files and the corresponding amounts of class definitions

    """
    class_defs_dict = {}
    cast_dict = file_or_directory(path)

    # Iterate through all of the Python files in a directory
    for file, cast in cast_dict.items():
        # Track the number of docstrings
        docstring_num = 0
        # Determine number of class definitions for each file
        class_defs_list = match.findall(cast, match.ClassDef())
        # Store the number of functions
        class_defs_dict[file] = {"class": 0, "docstring": 0}
        class_defs_dict[file]["class"] = len(class_defs_list)
        # Iterate and count the number of docstrings
        for node in class_defs_list:
            if node.get_docstring():
                docstring_num += 1
        class_defs_dict[file]["docstring"] = docstring_num

    return class_defs_dict


def count_classes(path:str):
    """Count the number of classes.

    Args:
        cast_dict: A dictionary of files and the corresponding CAST's

    Returns:
        dict: files and the corresponding amount of classes
    """
    class_dictionary = {}

    cast_dict = file_or_directory(path)

    #Iterate through all python files in a dictionary
    for file, cast in cast_dict.items():
        # Determine number of functions for each file
        class_def = match.findall(cast, match.ClassDef())
        class_dictionary[file] = len(class_def)

    return class_dictionary


def count_class_defs_without_docstrings(class_count: Dict) -> int:
    """Count the number of class definitions without docstrings.

    Args:
        class_count (Dict): class and docstring counts per file

    Returns:
        int: total number of classes - total number of classes with docstrings

    """
    class_total = 0
    docstring_total = 0
    for file_count in class_count.values():
        class_total += file_count["class"]

        docstring_total += file_count["docstring"]
    return class_total - docstring_total


def count_function_arguments(path: str, function_name):
    """Count the number of arguments for a given function.

    Args:
        cast_dict:A dictionary of files and the corresponding CAST's
        function_name: User picks a function to look into

    Returns:
        -1: Function wasn't found:
        else: it returns the length of the parameters that was given
    """
    final_list = []
    necessary_nodes = []

    cast_dict = file_or_directory(path)

    # Iterate through every file and find its CAST
    for cast in cast_dict.values():
        # Create a list of each of the function nodes for a given file
        function_list = match.findall(cast, match.FunctionDef())
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
        # If the function was found, count number of parameters and return
        for node in necessary_nodes:
            parameters = node.params.params
            return_statement = len(parameters)

    return return_statement


def count_assignments(path: str):
    """Count the number of assignment statements.

    Args:
        cast_dict: A dictionary of files and the corresponding CAST's

    Returns:
        dict: files and the corresponding amounts of assignment statements

    Example of assignments: x = y
    """
    assignment_dict = {}
    cast_dict = file_or_directory(path)

    # Iterate through all of the Python files in a directory
    for file, cast in cast_dict.items():
        # Determine number of assignment statements for each file
        assignment_list = match.findall(cast, match.Assign())
        assignment_dict[file] = len(assignment_list)

    return assignment_dict

def count_aug_assignment(path: str):
    """Count the number of aug assignment statements.

    Args:
        cast_dict: A dictionary of files and the corresponding CAST's

    Returns:
        dict: files and the corresponding amounts of aug assignment statements

    An example of an aug assignment is x +=5
    """
    aug_assignment_dict = {}

    cast_dict = file_or_directory(path)

    # Iterate through all of the Python files in a directory
    for file, cast in cast_dict.items():
        # Determine number of aug assignment statements for each file
        aug_assignment_list = match.findall(cast, match.AugAssign())
        aug_assignment_dict[file] = len(aug_assignment_list)

    return aug_assignment_dict
