"""A file for testing the functionality of counter.py."""

from castanet import generate_trees as generator
from castanet import counter

def test_import_dictionary():
    """Test that the dictionary for imports is being generated correctly."""
    directory_path = "tests/files_for_tests"
    file_list = generator.find_python_files(directory_path)
    string_file_list = generator.read_files(directory_path, file_list)
    tree_dict = generator.generate_cast(string_file_list)

    imports_dictionary = counter.match_imports(tree_dict)

    assert len(imports_dictionary) == 5


def test_calculate_total_imports():
    """Test that imports are totalled for each file in a directory."""
    directory_path = "tests/files_for_tests"
    file_list = generator.find_python_files(directory_path)
    string_file_list = generator.read_files(directory_path, file_list)
    tree_dict = generator.generate_cast(string_file_list)

    imports_dictionary = counter.match_imports(tree_dict)

    total_number_imports = counter.total_imports(imports_dictionary)

    assert total_number_imports == 0


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
