# CASTanet

![logo](castanet.png)

## Table of Contents

* [About CASTanet](#about-castanet)

* [Installing CASTanet](#installing-castanet)

* [Running CASTanet](#running-castanet)

* [CASTanet's Command Line Interface](#castanets-command-line-interface)

* [Testing](#testing)

* [Contributions](#contributions)

* [Contact Us](#contact-us)

## About CASTanet

CASTanet is a tool created by students at
Allegheny College, allowing users to understand
the contents of Python (`.py`) files. CASTanet
has functionality to iterate through a
user-specified directory and generate metrics
associated with the Python files in that given
directory. This tool can be used by educators
interested in evaluating students' code, or
individual developers who would like to better
understand their own implementation strategies
Currently, CASTanet is able to count:

* Number of if statements in a Python file (and
total in directory)
* Number of looping constructs in a Python file
(and total in directory)
* Number of comments in a Python file (and total
in directory)
* Number of arguments for a specified Python function
* Number of functions in a specified Python file (and total
in directory)
* Number of function definitions _without_
docstrings in a Python file (and total in
directory)
* Number of classes in a Python file (and total in directory)
* Number of class definitions _without_ docstrings in a
Python file (and total in directory)
* Number of assignment statements in a Python file (and
total in directory)
* Whether a specified function has a docstring or not
* Number of import statements in a Python file (and total in
directory)

## Installing CASTanet

### Clone the CASTanet repository onto your machine

In the appropriate directory, clone the CASTanet
repository following GitFlow and the GitHub
[documentation](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)

### Install Poetry and dependencies

The documentation and instructions on installing _Poetry_ can be found [here.](https://python-poetry.org/docs/)

_Poetry_ allows dependency installation with
ease. After
cloning the CASTanet
repository, and installing _Poetry_, install all
necessary dependencies for the tool with the
command:

`poetry install`

## Running CASTanet

CASTanet is a fully-functional tool with a dynamic command
line interface, and is built with the user in mind.
To run the CASTanet CLI, in the
home directory of your local, cloned
repository and type the command:

```python
castanet [command-here]
```

Without specifying a command, you will receive this error in
your terminal:

```python
Usage: castanet [OPTIONS] COMMAND [ARGS]...
Try 'castanet --help' for help.

Error: Missing command.
```

Please refer to the next section to see what functionality
CASTanet has, and what commands to run.

### CASTanet's Command Line Interface

CASTanet's command line interface is created with
[Typer](https://typer.tiangolo.com/),
a library for building CLI applications based
on Python 3.6+ type hints.

In order to familiarize yourself with the commands for
CASTanet, run the command: `poetry run castanet --help`

**CASTanet's commands are as follows:**

PLEASE NOTE: Each of the following commands must be run with
the **file path** of the directory of interest given as
input. This directory must be locally installed on your
machine, and CASTanet will provide output pertaining to this
specified directory.

## `CASTanet assignment`

Determine number of assignment statements.

**Usage**:

```console
CASTanet assignment [OPTIONS] DIRECTORY_PATH
```

**Arguments**:

* `DIRECTORY_PATH`: [required]

## `CASTanet classes`

Determine number of classes without docstrings.

**Usage**:

```console
CASTanet classes [OPTIONS] DIRECTORY_PATH
```

**Arguments**:

* `DIRECTORY_PATH`: [required]

## `CASTanet classes-without-docstrings`

Determine number of classes without docstrings.

**Usage**:

```console
CASTanet classes-without-docstrings [OPTIONS] DIRECTORY_PATH
```

**Arguments**:

* `DIRECTORY_PATH`: [required]

## `CASTanet comments`

Determine number of comments.

**Usage**:

```console
CASTanet comments [OPTIONS] DIRECTORY_PATH
```

**Arguments**:

* `DIRECTORY_PATH`: [required]
  
## `CASTanet function-arguments`

Determine the number of parameters for a given function.

**Usage**:

```console
CASTanet function-arguments [OPTIONS] DIRECTORY_PATH FUNCTION_NAME
```

**Arguments**:

* `DIRECTORY_PATH`: [required]
* `FUNCTION_NAME`: [required]
  
## `CASTanet function-with-or-without-docstring`

Determine if a given function has a docstring.

**Usage**:

```console
CASTanet function-with-or-without-docstring [OPTIONS] DIRECTORY_PATH FUNCTION_NAME
```

**Arguments**:

* `DIRECTORY_PATH`: [required]
* `FUNCTION_NAME`: [required]

## `CASTanet functions-without-docstrings`

Determine number of functions without docstrings.

**Usage**:

```console
CASTanet functions-without-docstrings [OPTIONS] DIRECTORY_PATH
```

**Arguments**:

* `DIRECTORY_PATH`: [required]

## `CASTanet if-statements`

Determine number of if statements in a Python directory.

**Usage**:

```console
CASTanet if-statements [OPTIONS] DIRECTORY_PATH
```

**Arguments**:

* `DIRECTORY_PATH`: [required]

## `CASTanet imports`

Determine number of import statements.

**Usage**:

```console
CASTanet imports [OPTIONS] DIRECTORY_PATH
```

**Arguments**:

* `DIRECTORY_PATH`: [required]

## `CASTanet looping-constructs`

Determine number of looping constructs.

**Usage**:

```console
CASTanet looping-constructs [OPTIONS] DIRECTORY_PATH
```

**Arguments**:

* `DIRECTORY_PATH`: [required]

## `CASTanet number-functions-in-module`

Determine number of functions in a Python directory.

**Usage**:

```console
CASTanet number-functions-in-module [OPTIONS] DIRECTORY_PATH DIRECTORY_OR_FILE
```

**Arguments**:

* `DIRECTORY_PATH`: [required]
* `DIRECTORY_OR_FILE`: [required]
  * OPTION: `Directory` if you would like to know
  information for all modules in a directory
  * OPTION: `name_of_file` if you would like to know
  information for only one file in a directory

## `CASTanet total-classes`

Determine total number of classes in a Python directory.

**Usage**:

```console
CASTanet total-classes [OPTIONS] DIRECTORY_PATH
```

**Arguments**:

* `DIRECTORY_PATH`: [required]

## `CASTanet total-functions`

Determine total number of functions in a Python directory.

**Usage**:

```console
CASTanet total-functions [OPTIONS] DIRECTORY_PATH
```

**Arguments**:

* `DIRECTORY_PATH`: [required]

Currently, CASTanet only has functionality
for _one_ metric to be calculated at a time.
As a result, if you are interested in one or
more metric, you must run CASTanet for the first metric
(with the corresponding CLI command),
and then run CASTanet subsequently for
each additional metric (with the corresponding CLI command).

### CASTanet as a Python Library

CASTanet is also available on PyPI to be used as a Python
library. Find it [here](https://pypi.org/project/castanet/).
With the CASTanet library, a user is able to investigate
their Python files with many different function calls.
Specifically, CASTanet is broken down into two parts:

1. `generate_trees`: Traverses a directory and generates
concrete-abstract-syntax trees of Python files using
LibCST
1. `counter`: Uses concrete-abstract-syntax-trees to
calculate metrics associated with the contents of a Python
module

### generate_trees

`from castanet import generate_trees`

#### find_python_files

Find all of the python files in a given directory.

`generate_trees.find_python_files(directory)`

_ARGUMENTS:_
  directory: string that contains the path of a directory

_RETURNS:_
  list: every Python file in specified directory

#### read_files

Read all of the Python files in a directory, and convert
them into Strings.

`generate_trees.read_files(directory, file_list)`

_ARGUMENTS:_
  directory: string that contains the path of a directory
  file_list: list that contains Python files a directory

_RETURNS:_
  dict: file name and its contents (in string format) as values

#### generate_cast

Create a CAST of each Python file using LibCST.

`generate_trees.generate_cast(file_strings_dict)`

_ARGUMENTS:_
  file_strings_dict: A dictionary of file names and its contents as strings

_RETURNS:_
  dict: file name and the CAST for each file

### counter

`from castanet import counter`

#### sum_cast_dict

Calculate the sums of values from dictionaries.
Called to get number values from the result of a function.

`counter.sum_cast_dict(cast_dict)`

_ARGUMENTS:_
  cast_dict: A dictionary of files and corresponding CASTs

_RETURNS:_
  int: total number of items in cast_dict

#### match_imports

Count the number of import statements in a Python file.

`counter.match_imports(cast_dict)`

_ARGUMENTS:_
  cast_dict: A dictionary of files and corresponding CASTs

_RETURNS:_
  dict: files and the corresponding amount of import statements

#### match_function

Count the number of function definitions in a Python file.

`counter.match_function(cast_dict)`

_ARGUMENTS:_
  cast_dict: A dictionary of files and corresponding CASTs

_RETURNS:_
  dict: files and the corresponding amount of function definitions

#### match_comment

Count the number of comments in a Python file.

`counter.match_comment(cast_dict)`

_ARGUMENTS:_
  cast_dict: A dictionary of files and corresponding CASTs

_RETURNS:_
  dict: files and the corresponding amount of comments

#### count_whileloops

Count the number of while loops in a Python file.

`counter.count_whileloops`

_ARGUMENTS:_
  cast_dict: A dictionary of files and corresponding CASTs

_RETURNS:_
  dict: files and the corresponding amount of while loops

#### count_forloops

Count the number of for loops in a Python file.

`counter.count_for_loops`

_ARGUMENTS:_
  cast_dict: A dictionary of files and corresponding CASTs

_RETURNS:_
  dict: files and the corresponding amount of for loops

#### match_if_statements

Count the number of if statements in a Python file.

`counter.match_if_statements(cast_dict)`

_ARGUMENTS:_
  cast_dict: A dictionary of files and corresponding CASTs

_RETURNS:_
  dict: files and the corresponding amount of if statements

#### match_func_defs

Count the number of function definitions in a Python file.

`counter.match_funcdefs(cast_dict)`

_ARGUMENTS:_
  cast_dict: A dictionary of files and corresponding CASTs

_RETURNS:_
  dict: files and the corresponding amount of function_definitions

#### count_function_without_docstrings

Count the number of functions without docstrings.

`counter.count_function_without_docstrings(func_count)`

_ARGUMENTS:_
  func_count (dict): A dictionary of functions and docstring counts per file

_RETURNS:_
  int: total number of functions - total number of docstrings

#### exists_docstring

Determine if a docstring exists for a specified function.

`counter.exists_docstring(cast_dict, function_name)`

_ARGUMENTS:_
  cast_dict: A dictionary of files and corresponding CASTs
  function_name (str): Name of function to check for docstrings

_RETURNS:_
  -1: function does not exist
  0: function exists without docstring
  1: function exists with docstring

#### match_class_def

Count the number of class definitions in a Python file.

`counter.match_class_defs(cast_dict)`

_ARGUMENTS:_
  cast_dict: A dictionary of files and corresponding CASTs

_RETURNS:_
  dict: files and the corresponding amount of class definitions

#### count_class_defs_without_docstrings

Count the number of class definitions without docstrings.

`counter.count_class_defs_without_docstrings(class_count)`

_ARGUMENTS:_
  class_count (dict): A dictionary of classes and docstring counts per file

_RETURNS:_
  int: total number of classes - total number of docstrings

#### count_function_arguments

Count the number of arguments for a specified function.

_ARGUMENTS:_
  cast_dict: A dictionary of files and the corresponding CASTs
  function_name: User-specified file of interest

_RETURNS:_
  -1: Function was not found
  else: The amount of parameters for the given function

#### assignment_count

Count the number of assignment statements in a Python file.

`counter.assignment_count(cast_dict)`

_ARGUMENTS:_
  cast_dict: A dictionary of files and corresponding CASTs

_RETURNS:_
  dict: files and the corresponding amount of assignment statements

#### aug_assignment_count

Count the number of aug assignment statements (x += 5) in a Python file.

`counter.aug_assignment_count(cast_dict)`

_ARGUMENTS:_
  cast_dict: A dictionary of files and corresponding CASTs

_RETURNS:_
  dict: files and the corresponding amount of aug assignment statements

## Testing

### Automated Testing

Developers of this program can run the test
suite with
[Pytest](https://docs.pytest.org/en/stable/)
with the command:

`poetry run task test`

## Contributions

We welcome everyone who is interested in helping to improve
CASTanet!
If you are interested in being a contributor, please review
our
[Code of Conduct](https://github.com/cmpsc-481-s22-m1/CASTanet/blob/documentation/CODE_OF_CONDUCT.md)
and
[Guidelines for Contributors](https://github.com/cmpsc-481-s22-m1/CASTanet/blob/documentation/CONTRIBUTING.md)
before raising an issue, or beginning a contribution.

To raise an issue in
[CASTanet's Issue Tracker](https://github.com/cmpsc-481-s22-m1/CASTanet/issues)
please follow these templates:

* [bug_report.md](https://github.com/cmpsc-481-s22-m1/CASTanet/blob/documentation/.github/ISSUE_TEMPLATE/bug_report.md)

* [feature_request.md](https://github.com/cmpsc-481-s22-m1/CASTanet/blob/documentation/.github/ISSUE_TEMPLATE/feature_request.md)

To create a pull request, please follow this template:

* [pull_request_template.md](https://github.com/cmpsc-481-s22-m1/CASTanet/blob/documentation/.github/pull_request_template.md)

## Contact Us

If you have any questions or concerns about CASTanet, please contact:

* Madelyn Kapfhammer (kapfhammerm@allegheny.edy)
* Thomas Antle (antlet@allegheny.edu)
* Nolan Thompson (thompsonn2@allegheny.edu)
* Caden Hinckley (hinckleyc@allegheny.edu)
* Bailey Matrascia (matrasciab@allegheny.edu)
