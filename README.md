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
* Number of function definitions _without_
docstrings in a Python file (and total in
directory)

### Coming Soon

Soon CASTanet will have functionality for
determining:

* Number of class definitions _without_
docstrings in a Python file (and total in
directory)
* Number of parameters for a given function in a
Python file (and total in directory)
* If a function has a docstring
* Number of import statements in a Python file
(and total in directory)
* Number of assignment statements in a Python
file (and total in directory)

Stay tuned for more features and details!

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
line interface,
built with the user in mind. To run the CASTanet CLI, in the home
directory of your local, cloned
repository and type the command:

```python
poetry run castanet [command-here]
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

### CASTanet's Command Line Interface - Commands

CASTanet's command line interface is created with
[Typer](https://typer.tiangolo.com/),
a library for building CLI applications based
on Python 3.6+ type hints.

In order to familiarize yourself with the commands for CASTanet, run the command: `poetry run castanet --help`

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
$ CASTanet assignment [OPTIONS] DIRECTORY_PATH
```

**Arguments**:

* `DIRECTORY_PATH`: [required]


## `CASTanet classes`

Determine number of classes without docstrings.

**Usage**:

```console
$ CASTanet classes [OPTIONS] DIRECTORY_PATH
```

**Arguments**:

* `DIRECTORY_PATH`: [required]

## `CASTanet classes-without-docstrings`

Determine number of classes without docstrings.

**Usage**:

```console
$ CASTanet classes-without-docstrings [OPTIONS] DIRECTORY_PATH
```

**Arguments**:

* `DIRECTORY_PATH`: [required]

## `CASTanet comments`

Determine number of comments.

**Usage**:

```console
$ CASTanet comments [OPTIONS] DIRECTORY_PATH
```

**Arguments**:

* `DIRECTORY_PATH`: [required]
  
## `CASTanet function-arguments`

Determine the number of parameters for a given function.

**Usage**:

```console
$ CASTanet function-arguments [OPTIONS] DIRECTORY_PATH FUNCTION_NAME
```

**Arguments**:

* `DIRECTORY_PATH`: [required]
* `FUNCTION_NAME`: [required]
  
## `CASTanet function-with-or-without-docstring`

Determine if a given function has a docstring.

**Usage**:

```console
$ CASTanet function-with-or-without-docstring [OPTIONS] DIRECTORY_PATH FUNCTION_NAME
```

**Arguments**:

* `DIRECTORY_PATH`: [required]
* `FUNCTION_NAME`: [required]

## `CASTanet total-functions`

Determine number of functions.

**Usage**:

```console
$ CASTanet total-functions [OPTIONS] DIRECTORY_PATH
```

**Arguments**:

* `DIRECTORY_PATH`: [required]

## `CASTanet functions-without-docstrings`

Determine number of functions without docstrings.

**Usage**:

```console
$ CASTanet functions-without-docstrings [OPTIONS] DIRECTORY_PATH
```

**Arguments**:

* `DIRECTORY_PATH`: [required]

## `CASTanet if-statements`

Determine number of if statements in a Python directory.

**Usage**:

```console
$ CASTanet if-statements [OPTIONS] DIRECTORY_PATH
```

**Arguments**:

* `DIRECTORY_PATH`: [required]

## `CASTanet imports`

Determine number of import statements.

**Usage**:

```console
$ CASTanet imports [OPTIONS] DIRECTORY_PATH
```

**Arguments**:

* `DIRECTORY_PATH`: [required]

## `CASTanet looping-constructs`

Determine number of looping constructs.

**Usage**:

```console
$ CASTanet looping-constructs [OPTIONS] DIRECTORY_PATH
```

**Arguments**:

* `DIRECTORY_PATH`: [required]

## `CASTanet number-functions-in-module`

Determine number of functions in a Python directory.

**Usage**:

```console
$ CASTanet number-functions-in-module [OPTIONS] DIRECTORY_PATH DIRECTORY_OR_FILE
```

**Arguments**:

* `DIRECTORY_PATH`: [required]
* `DIRECTORY_OR_FILE`: [required]
  * OPTION: `Directory` if you would like to know information for all modules in a directory
  * OPTION: `name_of_file` if you would like to know information for only one file in a directory

## `CASTanet total-classes`

Determine total number of classes in a Python directory.

**Usage**:

```console
$ CASTanet total-classes [OPTIONS] DIRECTORY_PATH
```

**Arguments**:

* `DIRECTORY_PATH`: [required]

## `CASTanet total-functions`

Determine total number of functions in a Python directory.

**Usage**:

```console
$ CASTanet total-functions [OPTIONS] DIRECTORY_PATH
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
