"""A program to test the command line interface of CASTanet."""

from typer.testing import CliRunner

from castanet.main import app

runner = CliRunner()

def test_functions_per_module_cli():
    """Test that cli returns correct number of functions per module."""
    result = runner.invoke(app, ["functions-per-module", "./test_files/funcdefs_test_file.py"])
    assert result.exit_code == 0
    assert "Number of functions: 5" in result.stdout


def test_if_statements_cli():
    """Test that cli returns correct number of if statements."""
    result = runner.invoke(app, ["if-statements", "./test_files/if_statements.py"])
    assert result.exit_code == 0
    assert "Number of if statements: 5" in result.stdout


def test_looping_constructs_cli():
    """Test that cli returns correct number of looping constructs."""
    result = runner.invoke(app, ["looping-constructs", "./test_files/loops.py"])
    assert result.exit_code == 0
    assert "Number for loops: 3" in result.stdout
    assert "Number while loops: 2" in result.stdout
    assert "Number total looping constructs: 5" in result.stdout


def test_assignments_cli():
    """Test that cli returns correct number of assignment statements."""
    result = runner.invoke(app, ["assignments", "./test_files"])
    assert result.exit_code == 0
    assert "Number of assignments: 21" in result.stdout


def test_comments_cli():
    """Test that cli returns the correct number of comments."""
    result = runner.invoke(app, ["comments", "./test_files/comments.py"])
    assert result.exit_code == 0
    assert "Number of comments: 5" in result.stdout


def test_functions_without_docstrings_cli():
    """Test that cli returns correct number of functions w/o docstrings."""
    result = runner.invoke(app, ["functions-without-docstrings", "./test_files"])
    assert result.exit_code == 0
    assert "Number of functions missing docstrings: 2" in result.stdout


def test_imports_cli():
    """Test that cli returns correct number of import statements."""
    result = runner.invoke(app, ["imports", "./test_files"])
    assert result.exit_code == 0
    assert "Number of imports: 1" in result.stdout


def test_total_classes_cli():
    """Test that cli returns correct number of classes."""
    result = runner.invoke(app, ["total-classes", "./test_files"])
    assert result.exit_code == 0
    assert "Number of classes: 6" in result.stdout


def test_classes_without_docstrings_cli():
    """Test that cli returns correct number of classes w/o docstrings."""
    result = runner.invoke(app, ["classes-without-docstrings", "./test_files"])
    assert result.exit_code == 0
    assert "Number of classes missing docstrings: 2" in result.stdout


def test_function_arguments_cli():
    """Test cli returns correct number arguments for given function."""
    result = runner.invoke(app, ["function-arguments", "./test_files", "greet"])
    assert result.exit_code == 0
    assert "Number of arguments for greet function: 1" in result.stdout


def test_function_docstring_exists_cli():
    """Test cli returns if function has docstring."""
    result = runner.invoke(app, ["function-docstring-exists", "./test_files", "greet"])
    second_result = runner.invoke(app, ["function-docstring-exists", "./test_files", "greet3"])
    assert result.exit_code == 0
    assert second_result.exit_code == 0
    assert "Function has a docstring." in result.stdout
    assert "Function does not have a docstring." in second_result.stdout

def test_total_functions_cli():
    """Test cli returns total number of functions."""
    result = runner.invoke(app, ["total-functions", "./test_files"])
    assert result.exit_code == 0
    assert "Number of functions: 7" in result.stdout
