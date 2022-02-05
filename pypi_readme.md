# CASTanet

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
the contents of Python (`.py`) files. Through
using concrete abstract syntax trees (CASTs), a
combination of abstract syntax trees (ASTs) and
concrete syntax trees (CSTs), CASTanet uses
`LibCST` to reorganize and name node types and
fields. CASTanet has functionality to iterate
through a user-specified directory and generate
metrics associated with the Python files in that
given directory. This tool can be used by
educators interested in evaluating students'
code, or individual developers who would like to
better understand their own implementation
strategies.

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

## Installing CASTanet - PyPI

Run the command to install: `pip install castanet`

## Installing CASTanet - Repository

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
line interface,
built with the user in mind. To run the CASTanet CLI, in the
base directory of your local, cloned
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
input. This directory must be present on your
machine, and CASTanet will provide output pertaining to this
specified directory.

## `castanet assignments`

Determine number of assignment statements.

**Usage**:

```console
castanet assignment [OPTIONS] PATH
```

**Arguments**:

* `PATH`: [required]

## `castanet total-classes`

Determine number of classes without docstrings.

**Usage**:

```console
castanet total-classes [OPTIONS] PATH
```

**Arguments**:

* `PATH`: [required]

## `castanet classes-without-docstrings`

Determine number of classes without docstrings.

**Usage**:

```console
castanet classes-without-docstrings [OPTIONS] PATH
```

**Arguments**:

* `PATH`: [required]

## `castanet comments`

Determine number of comments.

**Usage**:

```console
castanet comments [OPTIONS] PATH
```

**Arguments**:

* `PATH`: [required]
  
## `castanet function-arguments`

Determine the number of parameters for a given function.

**Usage**:

```console
castanet function-arguments [OPTIONS] PATH FUNCTION_NAME
```

**Arguments**:

* `PATH`: [required]
* `FUNCTION_NAME`: [required]
  
## `castanet function-docstring-exists`

Determine if a given function has a docstring.

**Usage**:

```console
castanet function-docstring-exists [OPTIONS] PATH FUNCTION_NAME
```

**Arguments**:

* `PATH`: [required]
* `FUNCTION_NAME`: [required]

## `castanet functions-without-docstrings`

Determine number of functions without docstrings.

**Usage**:

```console
castanet functions-without-docstrings [OPTIONS] PATH
```

**Arguments**:

* `PATH`: [required]

## `castanet if-statements`

Determine number of if statements in a Python directory.

**Usage**:

```console
castanet if-statements [OPTIONS] PATH
```

**Arguments**:

* `PATH`: [required]

## `castanet imports`

Determine number of import statements.

**Usage**:

```console
castanet imports [OPTIONS] PATH
```

**Arguments**:

* `PATH`: [required]

## `castanet looping-constructs`

Determine number of looping constructs.

**Usage**:

```console
castanet looping-constructs [OPTIONS] PATH
```

**Arguments**:

* `PATH`: [required]

## `castanet functions-per-module`

Determine number of functions in a Python directory.

**Usage**:

```console
castanet functions-per-module [OPTIONS] PATH
```

**Arguments**:

* `PATH`: [required]

## `castanet total-functions`

Determine total number of functions in a Python directory.

**Usage**:

```console
castanet total-functions [OPTIONS] PATH
```

**Arguments**:

* `PATH`: [required]

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

### counter

`from castanet import counter`

#### sum_dict_vals

Calculate the sums of values from dictionaries.
Called to get number values from the result of a
function. Must always be run on the results of
`count` functions to get final numbers.

`counter.sum_dict_vals(values_dict)`

_ARGUMENTS:_

* values_dict: dictionary of total values for metrics

_RETURNS:_

* int: total number of items in dictionary

#### count_imports

Count the number of import statements in a Python file.

`counter.count_imports(path)`

_ARGUMENTS:_
  
* path: A string path corresponding to a Python file or a directory

_RETURNS:_

* dict: files and the corresponding amount of import statements

#### count_functions

Count the number of function definitions in a Python file.

`counter.count_functions(path)`

_ARGUMENTS:_

* path: A string path corresponding to a Python file or a directory

_RETURNS:_

*dict: files and the corresponding amount of function definitions

#### count_comments

Count the number of comments in a Python file.

`counter.count_comments(path)`

_ARGUMENTS:_

* path: A string path corresponding to a Python file or a directory

_RETURNS:_

* dict: files and the corresponding amount of comments

#### count_while_loops

Count the number of while loops in a Python file.

`counter.count_while_loops(path)`

_ARGUMENTS:_

* path: A string path corresponding to a Python file or a directory

_RETURNS:_
  
* dict: files and the corresponding amount of while loops

#### count_for_loops

Count the number of for loops in a Python file.

`counter.count_for_loops(path)`

_ARGUMENTS:_

* path: A string path corresponding to a Python file or a directory

_RETURNS:_

* dict: files and the corresponding amount of for loops

#### count_if_statements

Count the number of if statements in a Python file.

`counter.count_if_statements(path)`

_ARGUMENTS:_

* path: A string path corresponding to a Python file or a directory

_RETURNS:_

* dict: files and the corresponding amount of if statements

#### count_func_defs

Count the number of function definitions in a Python file.

`counter.count_func_defs(path)`

_ARGUMENTS:_

* path: A string path corresponding to a Python file or a directory

_RETURNS:_

* dict: files and the corresponding amount of function_definitions

#### count_function_without_docstrings

Count the number of functions without docstrings.

`counter.count_function_without_docstrings(func_count)`

_ARGUMENTS:_

* dict: A dictionary of functions and docstring counts per file

_RETURNS:_

* int: total number of functions - total number of docstrings

*Note:* It is required to first call `count_func_defs` in
order for this function call to work correctly.

#### docstring_exists

Determine if a docstring exists for a specified function.

`counter.docstring_exists(path, function_name)`

_ARGUMENTS:_

* path: A string path corresponding to a Python file or a directory
* function_name (str): Name of function to check for docstrings

_RETURNS:_

* -1: function does not exist
* 0: function exists without docstring
* 1: function exists with docstring

#### match_class_defs

Count the number of class definitions in a Python file.

`counter.count_class_defs(cast_dict)`

_ARGUMENTS:_

* path: A string path corresponding to a Python file or a directory

_RETURNS:_

* dict: files and the corresponding amount of class definitions

#### count_class_defs_without_docstrings

Count the number of class definitions without docstrings.

`counter.count_class_defs_without_docstrings(class_count)`

_ARGUMENTS:_

* dict: A dictionary of classes and docstring counts per file

_RETURNS:_

* int: total number of classes - total number of docstrings

*Note:* It is required to first call `count_class_defs` in
order for this function call to work correctly.

#### count_function_arguments

Count the number of arguments for a specified function.

`counter.count_function_arguments(path, function_name)`

_ARGUMENTS:_

* path: A string path corresponding to a Python file or a directory
* function_name: User-specified file of interest

_RETURNS:_

* -1: Function was not found
* else: The amount of parameters for the given function

#### count_assignments

Count the number of assignment statements in a Python file.

(does not include augmented assignment)

`counter.count_assignments(path)`

_ARGUMENTS:_

* path: A string path corresponding to a Python file or a directory

_RETURNS:_

* dict: files and the corresponding amount of assignment statements

#### count_aug_assignment

Count the number of aug assignment statements (x += 5) in a Python file.

`counter.count_aug_assignment(path)`

_ARGUMENTS:_

* path: A string path corresponding to a Python file or a directory

_RETURNS:_

* dict: files and the corresponding amount of aug assignment statements

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
