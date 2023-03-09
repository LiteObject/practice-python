"""
Exploring list, tuple, and sets

List:
Python’s lists are the most flexible data type. It can be created by writing a list 
of comma-separated values between square brackets. Note that that the items in the list need not be 
of the same data type.

Tuple:
A Python tuple is a sequences or series of "immutable" objects very much similar to 
the lists.

Sets:
As the name implies, sets are the implementations of mathematical sets. Three key 
characteristic of set are the following:
    1. The collection of items is unordered.
    2. No duplicate items will be stored, which means that each item is unique.
    3. Sets are mutable, which means the items of it can be changed.

"""

# Create a list
my_list = ["Computer", "laptop", 1, 2]

# Update list item
my_list[3] = 3

for item in my_list:
    print(item)

# Create a tuple
my_tuple = ('a','b','c','d',1,2,3)

for item in my_tuple:
    print(item)

# Initialize a set
languages = {'Python', 'Java'}

# Add an element
languages.add("C#")

for l in languages:
    print(l)
