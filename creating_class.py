# This file shows the structure of a class Computer

# Requirements:

# Class Definition: Define a class with the chosen name (e.g.,  Car, Book etc.).
# UML Class Diagram: Draw a UML Class Diagram that represents the structure of your class.

# Attributes (Fields):
# Choose at least 4 attributes that represent the key characteristics of the chosen entity. For example:
# Computer: brand, model, processor, RAM

# Constructors:
# Create a parameterized constructor to initialize all the attributes.
# Create a default constructor that initializes attributes with default None values.

# Methods:
# display_info Method: Create a method named display_info that prints out the entity’s details in a formatted manner.
# Additional Method: Create an additional method that performs a meaningful action related to the entity.

# Testing the Class:
# In the main file, prompt the user to create N objects of your chosen class using both the default and parameterized constructors.
# Input the attributes of N objects from user input.
# Create N objects and save them to a list.
# Call the display_info method to display each entity’

class Student:
    def __init__(self, name="Jane Doe", studentid="studentid1", major="Software engineering",
                 gpa=3.5, email="janedoe@student.com", yearofstudy=1):
        self.name = name
        self.studentid = studentid
        self.major = major
        self.gpa = gpa
        self.email = email
        self.yearofstudy = yearofstudy

    def display_info(self):
        print(f'''Student name: {self.name} \nStudent ID: {self.studentid}\nMajor: {self.major}
GPA: {self.gpa}\nEmail: {self.email}\nYear of study: {self.yearofstudy}\n''')

    def update_gpa(self, new_gpa):
        self.gpa = new_gpa

