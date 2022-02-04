"""This module uses commands to call functions from counter.py."""
import pprint
import typer
from castanet import generate_trees as generator
from castanet import counter

app = typer.Typer(
    help=("CASTAnet: A tool that helps you count the contents of your Python files!")
)


def generate_trees(directory_path: str):
    """Generate CASTs for each Python file in a directory with LibCST."""
    file_list = generator.find_python_files(directory_path)
    string_file_list = generator.read_files(directory_path, file_list)
    tree_dict = generator.generate_cast(string_file_list)

    return tree_dict


@app.command()
def number_functions_in_module(directory_path:str, directory_or_file: str):
    """Determine number of functions in a Python directory."""
    cast_dict = generate_trees(directory_path)
    function_dictionary = counter.count_function(cast_dict)

    if directory_or_file == "Directory":
        pretty_print = pprint.PrettyPrinter(indent=4)
        pretty_print.pprint(function_dictionary)
    else:
        for file_name, total in function_dictionary.items():
            if file_name == directory_or_file:
                print("Number of functions: " + str(total))


@app.command()
def if_statements(directory_path):
    """Determine number of if statements in a Python directory."""
    cast_dict = generate_trees(directory_path)
    if_dictionary = counter.count_if_statements(cast_dict)
    total_if_statements = counter.sum_dict_vals(if_dictionary)
    print("Number of if statements: ", str(total_if_statements))


@app.command()
def looping_constructs(directory_path: str):
    """Determine number of looping constructs."""
    cast_dict = generate_trees(directory_path)
    while_loops_dict = counter.count_while_loops(cast_dict)
    for_loops_dict = counter.count_for_loops(cast_dict)
    total_for_loops = counter.sum_dict_vals(for_loops_dict)
    total_while_loops = counter.sum_dict_vals(while_loops_dict)
    total_loops = total_for_loops + total_while_loops
    print("Number for loops: " + str(total_for_loops))
    print("Number while loops: " + str(total_while_loops))
    print("Number total looping constructs: " + str(total_loops))


@app.command()
def assignment(directory_path: str):
    """Determine number of assignment statements."""
    cast_dict = generate_trees(directory_path)
    assignment_count_dict = counter.assignment_count(cast_dict)
    aug_assignment_count_dict = counter.aug_assignment_count(cast_dict)
    total_assignment_count = counter.sum_dict_vals(assignment_count_dict)
    total_aug_assign_count = counter.sum_dict_vals(aug_assignment_count_dict)
    total_assignments = total_assignment_count + total_aug_assign_count
    print("Number of assignments: " + str(total_assignment_count))
    print("Number of aug assignments: " + str(total_aug_assign_count))
    print("Number total assignments in program: " + str(total_assignments))


@app.command()
def comments(directory_path: str):
    """Determine number of comments."""
    cast_dict = generate_trees(directory_path)
    comment_dictionary = counter.count_comment(cast_dict)
    total_comments = counter.sum_dict_vals(comment_dictionary)
    print("Number of comments: " + str(total_comments))


@app.command()
def total_functions(directory_path: str):
    """Determine number of functions in a directory."""
    cast_dict = generate_trees(directory_path)
    functions_dictionary = counter.count_class_defs(cast_dict)
    number_of_functions = counter.sum_dict_vals(functions_dictionary)

    print("Number of functions: " + str(number_of_functions))


@app.command()
def functions_without_docstrings(directory_path: str):
    """Determine number of functions without docstrings."""
    cast_dict = generate_trees(directory_path)
    functions_dictionary = counter.count_func_defs(cast_dict)
    number_missing_docstrings = counter.count_function_without_docstrings(
        functions_dictionary
    )
    print("Number of functions missing docstrings: " + str(number_missing_docstrings))


@app.command()
def imports(directory_path: str):
    """Determine number of import statements."""
    cast_dict = generate_trees(directory_path)
    import_dictionary = counter.count_imports(cast_dict)
    total_imports = counter.sum_dict_vals(import_dictionary)
    print("Number of imports: " + str(total_imports))


@app.command()
def total_classes(directory_path: str):
    """Determine number of classes in a directory."""
    cast_dict = generate_trees(directory_path)
    classes_dictionary = counter.count_class_defs(cast_dict)
    number_of_classes = counter.sum_dict_vals(classes_dictionary)
    print("Number of classes: " + str(number_of_classes))


@app.command()
def classes_without_docstrings(directory_path: str):
    """Determine number of classes without docstrings."""
    cast_dict = generate_trees(directory_path)
    classes_dictionary = counter.count_class_defs(cast_dict)
    number_missing_docstrings = counter.count_class_defs_without_docstrings(
        classes_dictionary
    )
    print("Number of classes missing docstrings: " + str(number_missing_docstrings))


@app.command()
def function_arguments(directory_path:str, function_name:str):
    """Determine the number of parameters for a given function."""
    cast_dict = generate_trees(directory_path)
    arguments = counter.count_function_arguments(cast_dict, function_name)

    if arguments == -1:
        print("Function does not exist.")
    else:
        print(
            "Number of arguments for " + function_name + " function: " + str(arguments)
        )


@app.command()
def function_with_or_without_docstring(directory_path: str, function_name: str):
    """Determine if a given function has a docstring."""
    cast_dict = generate_trees(directory_path)
    docstring_status = counter.exists_docstring(cast_dict, function_name)
    if docstring_status == -1:
        print("Function does not exist.")
    if docstring_status == 0:
        print("Function does not have a docstring.")
    if docstring_status == 1:
        print("Function has a docstring.")


if __name__ == "__main__":
    app()
