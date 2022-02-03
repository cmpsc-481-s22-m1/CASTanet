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


def test_count_for_loops():
    """Test that for loops are counted correctly."""
    tree_dict = create_casts()

    for_dictionary = counter.count_forloops(tree_dict)
    amount_for_loops =  counter.sum_cast_dict(for_dictionary)

    correct_dictionary = {'__init__.py': 0, 'classdefs.py': 0, 'comments.py': 0,
        'funcdefs_test_file.py': 0, 'if_statements.py': 0, 'loops.py': 3}

    assert amount_for_loops == 3
    assert for_dictionary == correct_dictionary


def test_count_while_loops():
    """Test that while loops are counted correctly."""
    tree_dict = create_casts()
    while_dictionary = counter.count_whileloops(tree_dict)
    amount_while_loops = counter.sum_cast_dict(while_dictionary)

    correct_dictionary = {'__init__.py': 0, 'classdefs.py': 0, 'comments.py': 0,
        'funcdefs_test_file.py': 0, 'if_statements.py': 0, 'loops.py': 2}

    assert amount_while_loops == 2
    assert while_dictionary == correct_dictionary


def test_count_imports():
    """Test that import statements are counted correctly."""
    tree_dict = create_casts()
    import_dictionary = counter.match_imports(tree_dict)
    amount_imports = counter.sum_cast_dict(import_dictionary)

    correct_dictionary = {'__init__.py': 0, 'classdefs.py': 0, 'comments.py': 0,
        'funcdefs_test_file.py': 1, 'if_statements.py': 0, 'loops.py': 0}

    assert amount_imports == 1
    assert import_dictionary == correct_dictionary


def test_count_if_statements():
    """Test that if statements are counted correctly."""
    tree_dict = create_casts()
    if_dictionary = counter.match_if_statements(tree_dict)
    amount_ifs = counter.sum_cast_dict(if_dictionary)

    correct_dictionary = {'__init__.py': 0, 'classdefs.py': 0, 'comments.py': 0,
        'funcdefs_test_file.py': 1, 'if_statements.py': 5, 'loops.py': 0}

    assert amount_ifs == 6
    assert if_dictionary == correct_dictionary


def test_count_funcdef_without_docstring():
    """Check that functions and docstrings are counted correctly."""
    tree_dict = create_casts()
    funcdefs_dictionary = counter.match_funcdefs(tree_dict)

    assert counter.count_function_without_docstrings(funcdefs_dictionary) == 2


def test_count_comments():
    """Check that match_Comment identifies all of the comments in a directory."""
    tree_dict = create_casts()
    comment_dictionary = counter.match_comment(tree_dict)
    amount_comments = counter.sum_cast_dict(comment_dictionary)

    correct_dictionary = {'__init__.py': 0, 'classdefs.py': 0,'comments.py': 5,
        'funcdefs_test_file.py': 0, 'if_statements.py': 3, 'loops.py': 0}

    assert amount_comments == 8
    assert comment_dictionary == correct_dictionary


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


def test_count_assignments():
    """Check that assignment statements are counted correctly."""
    tree_dict = create_casts()
    assignment_dictionary = counter.assignment_count(tree_dict)
    amount_assignment_dictionary = counter.sum_cast_dict(assignment_dictionary)

    correct_dictionary = {'__init__.py': 0, 'classdefs.py': 2, 'comments.py': 6,
        'funcdefs_test_file.py': 5, 'if_statements.py': 4, 'loops.py': 4}

    assert amount_assignment_dictionary == 21
    assert assignment_dictionary == correct_dictionary


def test_count_aug_assignment():
    """Check that aug assignment statements are counted correctly."""
    tree_dict = create_casts()
    aug_assignment_dictionary = counter.aug_assignment_count(tree_dict)
    amount_aug_assignment_count = counter.sum_cast_dict(aug_assignment_dictionary)

    correct_dictionary = {'__init__.py': 0, 'classdefs.py': 0, 'comments.py': 0,
        'funcdefs_test_file.py': 0, 'if_statements.py': 3, 'loops.py': 0}

    assert amount_aug_assignment_count == 3
    assert aug_assignment_dictionary == correct_dictionary

def test_count_functions_per_module():
    """Check that functions are correctly tested per module."""
    tree_dict = create_casts()
    functions_dict = counter.match_function(tree_dict)

    correct_dictionary = {'__init__.py': 0, 'classdefs.py': 0, 'comments.py': 0,
        'funcdefs_test_file.py': 5, 'if_statements.py': 1, 'loops.py': 1}

    assert functions_dict == correct_dictionary
