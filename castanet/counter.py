"""Counting all if statments in a directory"""
import libcst.matchers as match

def match_if_statements(cast_dict):
    """A function for counting the number of if statements in a Python program."""
    if_statements_dictionary = {}
    # Iterate through all of the Python files in a directory
    for file in cast_dict:
        # Find CASTs for each of these files
        cast = cast_dict[file]
        # Determine number of if statements for each file
        ifs = match.findall(cast, match.If())
        if_statements_dictionary[file] = len(ifs)

    return if_statements_dictionary

def total_if_statements(if_statements_dictionary):
    """Find and combine all of the if statements in Python files at a specified directory"""
    total_ifs = 0
    for file in if_statements_dictionary:
        amount_of_ifs = if_statements_dictionary[file]
        total_ifs += amount_of_ifs

    return total_ifs
