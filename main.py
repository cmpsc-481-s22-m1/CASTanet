"""This module uses commands to call functions from counter.py."""
import typer
from castanet import generate_trees as generator
from castanet import counter

app = typer.Typer(help="Awesome CLI user manager.")

def generate_trees(directory_path:str):
    """Generate CASTs for each Python file in a directory with LibCST."""
    file_list = generator.find_python_files(directory_path)
    string_file_list = generator.read_files(directory_path, file_list)
    tree_dict = generator.generate_cast(string_file_list)

    return tree_dict


@app.command()
def if_statements(directory_path):
    """Determine number of if statements in a Python directory."""
    cast_dict = generate_trees(directory_path)
    if_statements_directory = counter.total_if_statements(cast_dict)
    print("Number of if statements: ", if_statements_directory)


@app.command()
def looping_constructs(directory_path):
    """Determine number of looping constructs in a Python directory."""
    cast_dict = generate_trees(directory_path)
    while_loops_dict = counter.count_whileloops(cast_dict)
    for_loops_dict = counter.count_forloops(cast_dict)
    number_for_loops = counter.amount_loops(for_loops_dict)
    number_while_loops = counter.amount_loops(while_loops_dict)
    total_loops = number_for_loops + number_while_loops
    print("Number for loops: " + number_for_loops)
    print("Number while loops: " + number_while_loops)
    print("Number total looping constructs: " + total_loops)


@app.command()
def comments(directory_path:str):
    """Determine number of comments in a Python directory."""
    cast_dict = generate_trees(directory_path)
    comment_dictionary = counter.match_comment(cast_dict)
    total_comments = counter.total_comment(comment_dictionary)
    print("Number of comments: " + total_comments)


@app.command()
def functions_without_docstrings(directory_path):
    """Determine number of functions without docstrings in a Python directory."""
    cast_dict = generate_trees(directory_path)
    functions_dictionary = counter.match_funcdefs(cast_dict)
    number_missing_docstrings = counter.get_missing_docstrings(functions_dictionary)
    print("Number of functions without docstrings: ", number_missing_docstrings)


if __name__ == "__main__":
    app()
