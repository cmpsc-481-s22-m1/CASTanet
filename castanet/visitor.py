# Import necessary types for typing
from typing import List, Tuple, Dict, Optional
# Import LibCST
import libcst as cst
import generate_trees as generator

class TypingCollector(cst.CSTVisitor):
    """Define the Visitor function for the program."""

    def __init__(self):
        """Define paramaters of the class: self."""
        # Create a stack where nodes will be placed to view them
        self.stack: List[Tuple[str, ...]]= []
        # Create a dictionary to store necessary information related to each node
        self.annotations = {}

    # TODO: Fill in function definitions related to all necessary user stories
    # TODO: Modify annotations to have node key as type and key as necessary information
    # Should look like:
    # self.annotations["TypeHere"] = necessary_information_here


def visit_trees(cast_dict):
    """Use a visitor function to check types of all nodes in a CAST."""
    # Create an instance of the visitor class
    visitor = TypingCollector()
    file_type_match = {}
    # Iterate through files in dictionary
    for file in cast_dict:
        # Find CAST for each file
        cast = cast_dict[file]
        # Visit each node in each CAST corresponding to a Python file
        cast.visit(visitor)
        # Create a dictionary with the file as the key and the annotations dictionary as the value
        file_type_match[file] = visitor.annotations

    return file_type_match


if __name__ == "__main__":
    directory = "/Users/tommyantle/cs481S2022/CASTanet/hello"
    file_list = generator.find_python_files(directory)
    string_file_list = generator.read_files(directory, file_list)
    tree_dict = generator.generate_cast(string_file_list)
    final_dictionary = visit_trees(tree_dict)

    print(final_dictionary)