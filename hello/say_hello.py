"""This module implements the ability to greet users by name."""
import os

def greet(name):
    """Greet a user by name."""
    greeting = f"Hello, {name}!"
    print(greeting)

def new_function_for_tests(nothing):
    print(nothing)

if __name__ == "__main__":
    greet("World")
