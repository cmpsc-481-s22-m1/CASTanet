import typer
import generate_trees as generator

app = typer.Typer(help="Awesome CLI user manager.")

@app.command()
def generate_trees(directory_path:str):
    """Generate CASTs for each Python file in a directory."""
    file_list = generator.find_python_files(directory_path)
    string_file_list = generator.read_files(directory_path, file_list)
    tree_list = generator.generate_cast(string_file_list)
    print(tree_list)

@app.command()
def new_command():
    """Test command to make sure the CLI is working properly."""
    print("Hello!")

if __name__ == "__main__":
    app()
