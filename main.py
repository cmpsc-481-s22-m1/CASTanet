import typer
from castanet import generate_trees as generator
from castanet import counter

app = typer.Typer(help="Awesome CLI user manager.")

def generate_trees(directory_path:str):
    """Generate CASTs for each Python file in a directory."""
    file_list = generator.find_python_files(directory_path)
    string_file_list = generator.read_files(directory_path, file_list)
    tree_dict = generator.generate_cast(string_file_list)

    return tree_dict


@app.command()
def new_command():
    """Test command to make sure the CLI is working properly."""
    print("Hello!")


@app.command()
def if_statements():
    """Determine number of if statements in a Python directory."""
    print("In progress")


@app.command()
def looping_constructs():
    """Determine number of looping constructs in a Python directory."""
    print("In progress")


@app.command()
def comments(directory_path:str):
    """Determine number of comments in a Python directory."""
    cast_dict = generate_trees(directory_path)
    comment_dictionary = counter.match_Comment(cast_dict)
    total_comments = counter.total_comment(comment_dictionary)
    print(total_comments)


@app.command()
def functions_without_docstrings():
    """Determine number of functions without docstrings in a Python directory."""
    print("In progress")

if __name__ == "__main__":
    app()
