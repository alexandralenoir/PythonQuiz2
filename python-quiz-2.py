"""python-quiz-2.py
Simplified, easy-to-read example demonstrating:
- variables
- data types
- a function
- a small class

Run this file directly to see the example output.
"""

# Variables
age = 18
name = "Alex"

# Data types
brothers = ["Mason", "Nathan", "Lincoln"]
year = 2025

def introduce(names):
    """Return a single string listing the names."""
    return ", ".join(names)

class Brother:
    """Small class with one method."""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describe(self):
        return f"{self.name} is {self.age} years old"

if __name__ == "__main__":
    print("age value:", age)
    print("name (type):", type(name))
    print("brothers (type):", type(brothers))
    print("year (type):", type(year))

    print("Introduce result:", introduce(brothers))

    s = Brother(name, age)
    print(s.describe())
#Python Quiz 2
#Fork this repository to your own GitHub account and complete the following tasks in the pythonquiz2.py file.

#Submit a URL link to your completed repository ON GITHUB on Moodle. 

#variables: show an example of variable assignment and usage. Be sure to print the variable to demonstrate its value.

#data types: demonstrate at least three different data types (e.g., integer, string, list) and print their types using the type() function.


#functions: define a simple function that takes an argument and returns a value. Call the function and print the result.


#classes: create a simple class with an __init__ method and one other method. Instantiate the class and call the method, printing the result.
class Brothers:
    def __init__(self, names, age):

        self.names = names

        self.__age = age



    def get_age(self):

        return self.__age

    def set_age(self, age):

        self.__age = age
