"""
This is the module docstring - short description.
"""

from oop.user import User

class Student(User):
    """ 
    In this example, the Student class is defined as a subclass of the User class. 
    It inherits all the properties and methods from the User class and adds a student_id 
    property specific to students.
    """

    def __init__(self, name, email, age, student_id):
        super().__init__(name, email, age)
        self.student_id = student_id

    # The __str__ method in the Student class overrides the __str__ method in the User class.
    # It first calls the __str__ method of the User class using super() to retrieve the user's
    # information. Then it appends the student's ID to the string representation.

    def __str__(self):
        user_info = super().__str__()
        return f"{user_info}\nStudent Id: {self.student_id}"

