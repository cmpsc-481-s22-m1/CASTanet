"""This module counts instances in Python files."""
# Import LibCST
import libcst.matchers as match

def count_whileloops(cast_dict):
    """A function for counting the number of while loops in a Python program."""
    while_dictionary = {}
    # Iterate through all of the Python files in a directory
    for file in cast_dict:
        # Find CASTs for each of these files
        cast = cast_dict[file]
        # Determine number of import statements for each file
        imports = match.findall(cast, match.While())
        while_dictionary[file] = len(imports)

    return while_dictionary


def count_forloops(cast_dict):
    """A function for coutning the number of while loops in a Python program."""
    for_dictionary = {}
    # Iterate through all of the Python files in a directory
    for file in cast_dict:
        # Find CASTs for each of these files
        cast = cast_dict[file]
        # Determine number of import statements for each file
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


# if __name__ == "__main__":
#     DIRECTORY_PATH = "/Users/chinckley/Desktop/Comp Sci/cs481/project-team-1/hello"
#     file_list = generator.find_python_files(DIRECTORY_PATH)
#     string_file_list = generator.read_files(DIRECTORY_PATH, file_list)
#     tree_dict = generator.generate_cast(string_file_list)

#     for_dictionary = count_forloops(tree_dict)
#     while_dictionary1 = count_whileloops(tree_dict)
#     print(for_dictionary)
#     print(while_dictionary)
