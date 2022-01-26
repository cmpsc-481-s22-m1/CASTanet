"""A Python module to count the number of statements in a program."""
from libcst import matchers as match


def match_imports(cast_dict):
    """A function for counting the number of if statements in a Python program."""
    imports_dictionary = {}
    # Iterate through all of the Python files in a directory
    for file in cast_dict:
        # Find CASTs for each of these files
        cast = cast_dict[file]
        # Determine number of import statements for each file
        imports = match.findall(cast, match.Imports())
        imports_dictionary[file] = len(imports)

    return imports_dictionary


def total_imports(imports_dict):
    """Find and combine the number of import statements in Python files in a specific directory."""
    total_imports = 0
    for file in imports_dict:
        amount_of_imports = imports_dict[file]
        total_imports += amount_of_imports

    return total_imports
