"""
This is the module docstring - short description.
"""

from utilities.converters import lb_to_kg
from oop.student import Student

student = Student("John Doe", "johndoe@example.com", 20, "12345")
print(student)

WEIGHT = lb_to_kg(65)
print(f"My weight is {WEIGHT} kg.")
