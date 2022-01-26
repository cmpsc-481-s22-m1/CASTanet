"""This module test the counter.py module regarding if statements"""
from castanet import counter
from castanet import generate_trees as generator

directory = "./test_files"
if_list = []
file_list = generator.find_python_files(directory)
string_file_list = generator.read_files(directory, file_list)
tree_dict = generator.generate_cast(string_file_list)
ifs = counter.match_if_statements(tree_dict)
if_list += ifs
print(if_list, len(if_list))


