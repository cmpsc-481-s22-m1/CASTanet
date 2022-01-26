"""This module tests the castanet.counter module."""

from castanet import counter
from castanet import generate_trees as generator


def test_countloops1():
    """Check that functions and docstrings are counted correctly"""
    directory = "./hello"
    file_list = generator.find_python_files(directory)
    string_file_list = generator.read_files(directory, file_list)
    tree_dict = generator.generate_cast(string_file_list)
    imports_dictionary1 = counter.count_whileloops(tree_dict)
    imports_dictionary = counter.count_forloops(tree_dict)
    assert imports_dictionary1 == {'__init__.py': 0, 'test.py': 0, 'say_hello.py': 1,
                                   'test-while.py': 0}
    assert imports_dictionary == ({'__init__.py': 0, 'test.py': 0, 'say_hello.py': 1,
                                  'test-while.py': 0})

def test_countloops2():
    """Uses count_forloops to identify all the if statements in the test_files directory"""
    directory = "./test_files"
    file_list = generator.find_python_files(directory)
    string_file_list = generator.read_files(directory, file_list)
    tree_dict = generator.generate_cast(string_file_list)
    if_dictionary = counter.count_forloops(tree_dict)
    assert if_dictionary == {'loops.py': 3}

def test_countloops3():
    """Uses count_whileloops to identify all the if statements in the test_files directory"""
    directory = "./test_files"
    file_list = generator.find_python_files(directory)
    string_file_list = generator.read_files(directory, file_list)
    tree_dict = generator.generate_cast(string_file_list)
    if_dictionary = counter.count_whileloops(tree_dict)
    assert if_dictionary == {'loops.py': 2}
