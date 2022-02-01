"""This module tests the castanet.counter module."""

from castanet import counter
from castanet import generate_trees as generator


def test_for_loops_dict():
    """Check that for loops are counted correctly."""
    directory = "./test_files"
    file_list = generator.find_python_files(directory)
    string_file_list = generator.read_files(directory, file_list)
    tree_dict = generator.generate_cast(string_file_list)
    for_dictionary = counter.count_forloops(tree_dict)
    amount_for_loops =  counter.sum_cast_dict(for_dictionary)

    assert len(for_dictionary) == 5
    assert amount_for_loops == 3


def test_count_while_loops():
    """Check that while loops are counted correctly."""
    directory = "./test_files"
    file_list = generator.find_python_files(directory)
    string_file_list = generator.read_files(directory, file_list)
    tree_dict = generator.generate_cast(string_file_list)
    while_dictionary = counter.count_whileloops(tree_dict)
    amount_while_loops = counter.sum_cast_dict(while_dictionary)

    assert len(while_dictionary) == 5
    assert amount_while_loops == 2



def test_import_dictionary():
    """Test that the dictionary for imports is being generated correctly."""
    directory_path = "./test_files"
    file_list = generator.find_python_files(directory_path)
    string_file_list = generator.read_files(directory_path, file_list)
    tree_dict = generator.generate_cast(string_file_list)
    if_dictionary = counter.match_if_statements(tree_dict)
    assert len(if_dictionary) == 5


def test_match_if_statements_2():
    """Uses match_if_statements to identify all the if-statements in the test_files directory."""
    directory_path = "./test_files"
    file_list = generator.find_python_files(directory_path)
    string_file_list = generator.read_files(directory_path, file_list)
    tree_dict = generator.generate_cast(string_file_list)
    if_dictionary = counter.match_if_statements(tree_dict)
    assert len(if_dictionary) == 5


def test_calculate_total_imports():
    """Test that imports are totalled for each file in a directory."""
    directory_path = "./test_files"
    file_list = generator.find_python_files(directory_path)
    string_file_list = generator.read_files(directory_path, file_list)
    tree_dict = generator.generate_cast(string_file_list)

    imports_dictionary = counter.match_imports(tree_dict)

    total_number_imports = counter.sum_cast_dict(imports_dictionary)

    assert total_number_imports == 2


def test_match_imports_len():
    """Check that the imports are counted correctly."""
    directory = "./test_files"
    file_list = generator.find_python_files(directory)
    string_file_list = generator.read_files(directory, file_list)
    tree_dict = generator.generate_cast(string_file_list)
    imports_dictionary = counter.match_imports(tree_dict)
    # assert imports_dictionary == {'funcdefs_test_file.py': 0, '__init__.py': 0}
    assert len(imports_dictionary) == 5


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
    """Check that comments are counted correctly."""
    directory = "./test_files"
    file_list = generator.find_python_files(directory)
    string_file_list = generator.read_files(directory, file_list)
    tree_dict = generator.generate_cast(string_file_list)
    comment_dictionary = counter.match_comment(tree_dict)
    assert len(comment_dictionary) == 5


def test_match_function():
    """Check that functions are counted correctly."""
    directory = "./test_files"
    file_list = generator.find_python_files(directory)
    string_file_list = generator.read_files(directory, file_list)
    tree_dict = generator.generate_cast(string_file_list)
    function_dictionary = counter.match_function(tree_dict)
    assert len(function_dictionary) == 5
