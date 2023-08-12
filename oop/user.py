"""
This is the module docstring - short description.
"""

class User:

    """
    In this example, the User class has an initializer method __init__ 
    that takes in the name, email, and age as arguments and assigns them 
    to corresponding instance variables (self.name, self.email, and self.age).
    """
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    # The __str__ method is overridden to provide a custom string representation 
    # of the User object. It returns a formatted string that includes the user's 
    # name, email, and age.

    def __str__(self):
        """This method does something."""
        return f"Name: {self.name}\nEmail: {self.email}\nAge: {self.age}"


