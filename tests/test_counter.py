"""This module tests the castanet.counter module."""

from castanet import counter
from castanet import generate_trees as generator


def test_countloops1():
    """Check that if and while loops are counted correctly"""
    directory = "./hello"
    file_list = generator.find_python_files(directory)
    string_file_list = generator.read_files(directory, file_list)
    tree_dict = generator.generate_cast(string_file_list)
    while_dictionary = counter.count_whileloops(tree_dict)
    for_dictionary = counter.count_forloops(tree_dict)
    assert len(while_dictionary) == 2
    assert len(for_dictionary) == 2
