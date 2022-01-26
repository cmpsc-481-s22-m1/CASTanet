"""This module tests the castanet.counter module."""

from castanet import counter
from castanet import generate_trees as generator


def test_countloops1():
    """Check that functions and docstrings are counted correctly"""
    directory = "./hello"
    file_list = generator.find_python_files(directory)
    string_file_list = generator.read_files(directory, file_list)
    tree_dict = generator.generate_cast(string_file_list)
    while_dictionary = counter.count_whileloops(tree_dict)
    for_dictionary = counter.count_forloops(tree_dict)
    assert while_dictionary == {'__init__.py': 0, 'say_hello.py': 1}
    #assert for_dictionary == {'__init__.py': 0, 'say_hello.py': 1}
