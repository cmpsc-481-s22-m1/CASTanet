"""This module uses commands to call functions from counter.py."""
import pprint
import typer
from castanet import counter

app = typer.Typer(
    help=("CASTAnet: A tool that helps you count the contents of your Python files!")
)


@app.command()
def functions_per_module(directory_path:str):
    """Determine number of functions in a Python directory."""
    function_dictionary = counter.count_functions(directory_path)

    if directory_path.endswith(".py"):
        functions = counter.sum_dict_vals(function_dictionary)
        print("Number of functions: " + str(functions))
    else:
        pretty_print = pprint.PrettyPrinter(indent=4)
        pretty_print.pprint(function_dictionary)


@app.command()
def if_statements(directory_path: str):
    """Determine number of if statements in a Python directory."""
    if_dictionary = counter.count_if_statements(directory_path)
    total_if_statements = counter.sum_dict_vals(if_dictionary)
    print("Number of if statements: " + str(total_if_statements))


@app.command()
def looping_constructs(directory_path: str):
    """Determine number of looping constructs."""
    while_loops_dict = counter.count_while_loops(directory_path)
    for_loops_dict = counter.count_for_loops(directory_path)
    total_for_loops = counter.sum_dict_vals(for_loops_dict)
    total_while_loops = counter.sum_dict_vals(while_loops_dict)
    total_loops = total_for_loops + total_while_loops
    print("Number for loops: " + str(total_for_loops))
    print("Number while loops: " + str(total_while_loops))
    print("Number total looping constructs: " + str(total_loops))


@app.command()
def assignments(directory_path: str):
    """Determine number of assignment statements."""
    assignment_count_dict = counter.count_assignments(directory_path)
    aug_assignment_count_dict = counter.count_aug_assignment(directory_path)
    total_assignment_count = counter.sum_dict_vals(assignment_count_dict)
    total_aug_assign_count = counter.sum_dict_vals(aug_assignment_count_dict)
    total_assignments = total_assignment_count + total_aug_assign_count
    print("Number of assignments: " + str(total_assignment_count))
    print("Number of aug assignments: " + str(total_aug_assign_count))
    print("Number total assignments: " + str(total_assignments))


@app.command()
def comments(directory_path: str):
    """Determine number of comments."""
    comment_dictionary = counter.count_comments(directory_path)
    total_comments = counter.sum_dict_vals(comment_dictionary)
    print("Number of comments: " + str(total_comments))


@app.command()
def total_functions(directory_path: str):
    """Determine number of functions in a directory."""
    functions_dictionary = counter.count_functions(directory_path)
    number_of_functions = counter.sum_dict_vals(functions_dictionary)

    print("Number of functions: " + str(number_of_functions))


@app.command()
def functions_without_docstrings(directory_path: str):
    """Determine number of functions without docstrings."""
    functions_dictionary = counter.count_func_defs(directory_path)
    number_missing_docstrings = counter.count_function_without_docstrings(
        functions_dictionary
    )
    print("Number of functions missing docstrings: " + str(number_missing_docstrings))


@app.command()
def imports(directory_path: str):
    """Determine number of import statements."""
    import_dictionary = counter.count_imports(directory_path)
    total_imports = counter.sum_dict_vals(import_dictionary)
    print("Number of imports: " + str(total_imports))


@app.command()
def total_classes(directory_path: str):
    """Determine number of classes in a directory."""
    classes_dictionary = counter.count_classes(directory_path)
    number_of_classes = counter.sum_dict_vals(classes_dictionary)
    print("Number of classes: " + str(number_of_classes))


@app.command()
def classes_without_docstrings(directory_path: str):
    """Determine number of classes without docstrings."""
    classes_dictionary = counter.count_class_defs(directory_path)
    number_missing_docstrings = counter.count_class_defs_without_docstrings(
        classes_dictionary
    )
    print("Number of classes missing docstrings: " + str(number_missing_docstrings))


@app.command()
def function_arguments(directory_path:str, function_name:str):
    """Determine the number of parameters for a given function."""
    arguments = counter.count_function_arguments(directory_path, function_name)

    if arguments == -1:
        print("Function does not exist.")
    else:
        print(
            "Number of arguments for " + function_name + " function: " + str(arguments)
        )


@app.command()
def function_docstring_exists(directory_path: str, function_name: str):
    """Determine if a given function has a docstring."""
    docstring_status = counter.docstring_exists(directory_path, function_name)
    if docstring_status == -1:
        print("Function does not exist.")
    if docstring_status == 0:
        print("Function does not have a docstring.")
    if docstring_status == 1:
        print("Function has a docstring.")


if __name__ == "__main__":
    app()
