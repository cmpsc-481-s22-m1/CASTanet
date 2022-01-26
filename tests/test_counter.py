"""This module tests the castanet.counter module."""

from castanet import counter
from castanet import generate_trees as generator


def test_match_imports_len():
    """Check that the imports are counted correctly."""
    directory = "./test_files"
    file_list = generator.find_python_files(directory)
    string_file_list = generator.read_files(directory, file_list)
    tree_dict = generator.generate_cast(string_file_list)
    imports_dictionary = counter.match_imports(tree_dict)
    # assert imports_dictionary == {'funcdefs_test_file.py': 0, '__init__.py': 0}
    assert len(imports_dictionary) == 2


def test_funcdef_docstring_count():
    """Check that functions and docstrings are counted correctly."""
    directory = "./test_files"
    file_list = generator.find_python_files(directory)
    string_file_list = generator.read_files(directory, file_list)
    tree_dict = generator.generate_cast(string_file_list)
    funcdefs_dictionary = counter.match_funcdefs(tree_dict)
    # assert funcdefs_dictionary == {'funcdefs_test_file.py': {'function': 3, 'docstring': 3},
    #  '__init__.py': {'function': 0, 'docstring': 0}}
    assert counter.get_missing_docstrings(funcdefs_dictionary) == 0
