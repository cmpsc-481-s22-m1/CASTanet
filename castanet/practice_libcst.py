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
        self.stack: List[Tuple[str, ...]]= []
        # Create a dictionary to store necessary information related to each node
<<<<<<< HEAD
        self.annotations: Dict[Tuple[str, ...], Tuple[cst.Parameters, Optional[cst.Annotation]],] = {}
=======
        self.annotations = {}
>>>>>>> develop

    def visit_FunctionDef(self, node: cst.FunctionDef) -> Optional[bool]:
        """Visit a node that is typed as a FunctionDef and gather necessary information to add to dataframe."""
        # Temporarily add node to stack
        self.stack.append(node.name.value)
        # Add information related to FunctionDef nodes (names and parameters) to dataframe
<<<<<<< HEAD
        self.annotations[tuple(self.stack)] = (node.name.value, node.params)
        # Print the length of the stack to determine if visitor is working properly
        print(len(self.stack))
    
=======
        self.annotations["FunctionDef"] = node.get_docstring()
        # Print the length of the stack to determine if visitor is working properly
        # print(len(self.stack))

        print(self.annotations)
    

>>>>>>> develop
    def leave_function_def(self, node: cst.FunctionDef) -> None:
        """Remove the node from the stack to move on to next node in the CAST."""
        self.stack.pop()

<<<<<<< HEAD
=======

>>>>>>> develop
# Open the say_hello.py file
file = open("/home/mkapfhammer/Documents/Allegheny/2022/Spring/CMPSC481/project-team-1/hello/say_hello.py", "r")
# Read in file as a string
string = file.read()

# Create a CAST of the say_hello.py module
my_tree = cst.parse_module(string)

# Uncomment to print the tree
# print(my_tree)

# Create a visitor instance of the TypingCollector class
visitor = TypingCollector()
# Visit each node in the CAST created from say_hello.py
<<<<<<< HEAD
my_tree.visit(visitor)
=======

my_tree.visit(visitor)

print(visitor.annotations)
>>>>>>> develop
