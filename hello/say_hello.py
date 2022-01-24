"""This module implements the ability to greet users by name."""
import math

def greet(name):
    """Greet a user by name."""
    greeting = f"Hello, {name}!"
    print(greeting)

def new_function_for_tests(number):
    """A new function to determine the square root of a number."""
    square_root = math.sqrt(number)
    print(square_root)


if __name__ == "__main__":
    greet("World")
