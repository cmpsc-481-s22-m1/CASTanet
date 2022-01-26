"""This module tests the generate_trees module in castanet."""

import pytest

from castanet import generate_trees as generator

def test_find_python_files():
    """Test the ability of generator to find the python files in a directory."""
    directory = "tests/files_for_tests"
    file_list = generator.find_python_files(directory)
    number_of_files = len(file_list)

    assert number_of_files == 3


def test_read_files():
    """Test generator's reading of files."""
    directory = "tests/files_for_tests"
    file_list = generator.find_python_files(directory)
    string_file_dict = generator.read_files(directory, file_list)

    test_string = string_file_dict["small_test.py"]

    assert test_string == "variable = 42"


def test_generate_cast():
    """Test if CASTs are being made correctly by LibCST."""
    directory = "tests/files_for_tests"
    file_list = generator.find_python_files(directory)
    string_file_dict = generator.read_files(directory, file_list)

    cast_dict = generator.generate_cast(string_file_dict)

    assert len(cast_dict) == 3


