import typer
import generate_trees as generator
import castanet.counter as counter

app = typer.Typer(help="Awesome CLI user manager.")

@app.command()
def generate_trees(directory_path:str):
    """Generate CASTs for each Python file in a directory."""
    file_list = generator.find_python_files(directory_path)
    string_file_list = generator.read_files(directory_path, file_list)
    tree_dict = generator.generate_cast(string_file_list)
    final_dictionaries = counter.visit_trees(tree_dict)

    print(final_dictionaries)


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
def comments():
    """Determine number of comments in a Python directory."""
    print("In progress")


@app.command()
def functions_without_docstrings():
    """Determine number of functions without docstrings in a Python directory."""
    print("In progress")

if __name__ == "__main__":
    app()
