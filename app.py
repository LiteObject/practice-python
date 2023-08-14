"""
This is the module docstring - short description.
"""

from utilities.converters import lb_to_kg
from utilities.dir import get_children
from oop.student import Student

student = Student("John Doe", "johndoe@example.com", 20, "12345")
print(student)

WEIGHT = lb_to_kg(65)
print(f"My weight is {WEIGHT} kg.\n\n")

get_children("C:\\temp")
