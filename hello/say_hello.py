"""This module implements the ability to greet users by name."""
# comment
def greet(name):
    """Greet a user by name."""
    greeting = f"Hello, {name}!"
    print(greeting)


if __name__ == "__main__":
    greet("World")
