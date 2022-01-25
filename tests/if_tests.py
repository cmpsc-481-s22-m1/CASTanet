"""This module test the counter.py module regarding if statements"""
from castanet import counter
from castanet import generate_trees as generator
import libcst.matchers as match

def test_identifing_ifs():
    """Check that match_ifstatements identifies all of the if-statements in a directory"""
    directory = "./hello"
    file_list = generator.find_python_files(directory)
    string_file_list = generator.read_files(directory, file_list)
    tree_dict = generator.generate_cast(string_file_list)
    if_dictionary = counter.match_imports(tree_dict)
    assert if_dictionary == {'say_hello.py': 1, '__init__.py': 0}