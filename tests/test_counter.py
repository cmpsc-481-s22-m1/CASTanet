"""This module tests the castanet.counter module."""

import pytest

from castanet import counter
from castanet import generate_trees as generator




def create_casts():
    """Create a dictionary of files and their corresponding CASTs."""
    directory = "./test_files"
    file_list = generator.find_python_files(directory)
    string_file_list = generator.read_files(directory, file_list)
    tree_dict = generator.generate_cast(string_file_list)
    return tree_dict


def test_for_loops_dict():
    """Check that for loops are counted correctly."""
    tree_dict = create_casts()

    for_dictionary = counter.count_forloops(tree_dict)
    amount_for_loops =  counter.sum_cast_dict(for_dictionary)

    assert len(for_dictionary) == 5
    assert amount_for_loops == 3


def test_count_while_loops():
    """Check that while loops are counted correctly."""
    tree_dict = create_casts()
    while_dictionary = counter.count_whileloops(tree_dict)
    amount_while_loops = counter.sum_cast_dict(while_dictionary)

    assert len(while_dictionary) == 5
    assert amount_while_loops == 2



def test_import_dictionary():
    """Test that the dictionary for imports is being generated correctly."""
    tree_dict = create_casts()
    if_dictionary = counter.match_if_statements(tree_dict)
    assert len(if_dictionary) == 5


def test_match_if_statements_2():
    """Uses match_if_statements to identify all the if-statements in the test_files directory."""
    tree_dict = create_casts()
    if_dictionary = counter.match_if_statements(tree_dict)
    assert len(if_dictionary) == 5


def test_calculate_total_imports():
    """Test that imports are totalled for each file in a directory."""
    tree_dict = create_casts()

    imports_dictionary = counter.match_imports(tree_dict)

    total_number_imports = counter.sum_cast_dict(imports_dictionary)

    assert total_number_imports == 0


def test_match_imports_len():
    """Check that the imports are counted correctly."""
    tree_dict = create_casts()
    imports_dictionary = counter.match_imports(tree_dict)
    # assert imports_dictionary == {'funcdefs_test_file.py': 0, '__init__.py': 0}
    assert len(imports_dictionary) == 5


def test_funcdef_docstring_count():
    """Check that functions and docstrings are counted correctly."""
    tree_dict = create_casts()
    funcdefs_dictionary = counter.match_funcdefs(tree_dict)
    # assert funcdefs_dictionary == {'funcdefs_test_file.py': {'function': 3, 'docstring': 3},
    #  '__init__.py': {'function': 0, 'docstring': 0}}
    assert counter.count_function_without_docstrings(funcdefs_dictionary) == 1


def test_match_comment_returns_correct_number_comments():
    """Check that match_Comment identifies all of the comments in a directory."""
    tree_dict = create_casts()
    comment_dictionary = counter.match_comment(tree_dict)
    assert len(comment_dictionary) == 5


def test_total_comment_returns_correct_number_comments():
    """Checks that total_comment adds all identified comments."""
    comment_dictionaries = {'say_hello.py': 1, '__init__.py': 3}
    number_comments = counter.sum_cast_dict(comment_dictionaries)
    assert number_comments == 4


def test_count_function_arguments():
    """Check that CASTanet returns the correct number of arguments for a given function."""
    tree_dict = create_casts()

    function_arguments = counter.count_function_arguments(tree_dict, "greet")

    assert function_arguments == 1


def test_non_existing_function():
    """Check that CASTanet returns an error when a function is not found."""
    tree_dict = create_casts()

    function_arguments = counter.count_function_arguments(tree_dict, "unknown")

    assert function_arguments == -1


@pytest.mark.parametrize(
    "function_name,expected",
    [("greet", 1), ("greet1", 1), ("greet3", 0), ("greet99", -1)],
)
def test_exists_docstring(function_name, expected):
    """Check that functions and docstrings are counted correctly."""
    tree_dict = create_casts()
    class_defs_dictionary = counter.match_class_defs(tree_dict)
    assert counter.count_class_defs_without_docstrings(class_defs_dictionary) == 2

    actual = counter.exists_docstring(tree_dict, function_name)
    assert actual == expected


def test_assignment_count():
    """Check that assignment statements are counted correctly."""
    tree_dict = create_casts()
    assignment_dictionary = counter.assignment_count(tree_dict)
    amount_assignment_dictionary = counter.sum_cast_dict(assignment_dictionary)

    assert len(assignment_dictionary) == 5
    assert amount_assignment_dictionary == 18


def test_aug_assignment_count():
    """Check that aug assignment statements are counted correctly."""
    tree_dict = create_casts()
    aug_assignment_dictionary = counter.aug_assignment_count(tree_dict)
    amount_aug_assignment_count = counter.sum_cast_dict(aug_assignment_dictionary)

    assert len(aug_assignment_dictionary) == 5
    assert amount_aug_assignment_count == 3
