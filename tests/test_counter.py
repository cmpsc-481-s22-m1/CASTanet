"""This module tests the castanet.counter module."""

import pytest

from castanet import counter
from castanet import generate_trees as generator


def test_funcdef_docstring_count():
    """Check that functions and docstrings are counted correctly"""
    directory = "./test_files"
    file_list = generator.find_python_files(directory)
    string_file_list = generator.read_files(directory, file_list)
    tree_dict = generator.generate_cast(string_file_list)
    funcdefs_dictionary = counter.match_funcdefs(tree_dict)
    assert funcdefs_dictionary == {'funcdefs_test_file.py': {'function': 3, 'docstring': 2}, '__init__.py': {'function': 0, 'docstring': 0}}
    assert counter.get_missing_docstrings(funcdefs_dictionary) == 1
