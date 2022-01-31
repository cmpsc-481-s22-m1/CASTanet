"""This module tests the castanet.counter module."""

from castanet import counter
from castanet import generate_trees as generator


def test_funcdef_docstring_count():
    """Check that functions and docstrings are counted correctly."""
    directory = "./test_files"
    file_list = generator.find_python_files(directory)
    string_file_list = generator.read_files(directory, file_list)
    tree_dict = generator.generate_cast(string_file_list)
    funcdefs_dictionary = counter.match_funcdefs(tree_dict)
    # assert funcdefs_dictionary == {'funcdefs_test_file.py': {'function': 3, 'docstring': 3},
    #  '__init__.py': {'function': 0, 'docstring': 0}}
    assert counter.count_function_without_docstrings(funcdefs_dictionary) == 0


def test_match_comment_returns_correct_number_comments():
    """Check that match_Comment identifies all of the comments in a directory."""
    directory = "./test_files"
    file_list = generator.find_python_files(directory)
    string_file_list = generator.read_files(directory, file_list)
    tree_dict = generator.generate_cast(string_file_list)
    comment_dictionary = counter.match_comment(tree_dict)
    assert len(comment_dictionary) == 5

