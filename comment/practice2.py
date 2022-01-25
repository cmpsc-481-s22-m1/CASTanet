"""A program to practice using the LibCST visitor function."""

# Import necessary types for typing
from typing import List, Tuple, Dict, Optional
# Import LibCST
import libcst as cst


class TypingCollector(cst.CSTVisitor):
    """Define the Visitor function for the program."""

    def __init__(self):
        """Define paramaters of the class: self."""
        # Create a stack where nodes will be placed to view them

        # Create a dictionary to store necessary information related to each node
        self.annotations = {}

    def visit_Comment(self, node: cst.Comment) -> Optional[bool]:
        """Visit a node that is typed as a FunctionDef and gather necessary information to add to dataframe."""
        # Temporarily add node to stack
        # Add information related to FunctionDef nodes (names and parameters) to dataframe
        self.annotations["Comment"] = node.value
        # Print the length of the stack to determine if visitor is working properly

        print(self.annotations)
        print(len(self.annotations.keys()))

    #def count_keys(self.annotations):
        #count = 0
        #for i in enumerate(self.annotations):
            #count += 1
            #return count

        #print(count_keys(annotations))

    def leave_Comment(self, node: cst.Comment) -> None:
        """Remove the node from the stack to move on to next node in the CAST."""


# Open the say_hello.py file
file = open(r"C:\Users\Bailey\Desktop\cs481\project-team-1\hello\say_hello.py", "r")
# Read in file as a string
string = file.read()

# Create a CAST of the say_hello.py module
my_tree = cst.parse_module(string)

# Uncomment to print the tree
# print(my_tree)

# Create a visitor instance of the TypingCollector class
visitor = TypingCollector()
# Visit each node in the CAST created from say_hello.py
my_tree.visit(visitor)
