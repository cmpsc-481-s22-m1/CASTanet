"""This module test the counter.py module regarding comments"""
from castanet import counter
from castanet import generate_trees as generator

def test_match_comment_returns_correct_number_comments():
    """Check that match_Comment identifies all of the comments in a directory"""
    directory = "./hello"
    file_list = generator.find_python_files(directory)
    string_file_list = generator.read_files(directory, file_list)
    tree_dict = generator.generate_cast(string_file_list)
    comment_dictionary = counter.match_comment(tree_dict)
    assert comment_dictionary == {'say_hello.py': 1, '__init__.py': 0}

def test_total_comment_returns_correct_number_comments():
    """Checks that total_comment adds all identified comments"""
    comment_dictionaries = {'say_hello.py': 1, '__init__.py': 3}
    number_comments = counter.total_comment(comment_dictionaries)
    assert number_comments == 4
