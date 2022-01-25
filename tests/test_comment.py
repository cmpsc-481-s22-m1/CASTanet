"""This module test the counter.py module regarding comments"""
from castanet import counter
from castanet import generate_trees as generator

def test_comment():
    """Check that match_Comment identifies all of the comments in a directory"""
    directory = "./hello"
    file_list = generator.find_python_files(directory)
    string_file_list = generator.read_files(directory, file_list)
    tree_dict = generator.generate_cast(string_file_list)
    comment_dictionary = counter.match_Comment(tree_dict)
    assert comment_dictionary == {'say_hello.py': 1, 'init.py': 0}
