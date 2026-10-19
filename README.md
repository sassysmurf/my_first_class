This project implements a simple Student class in Python to represent a student and store their information.

Attributes

The class contains six attributes:

name: Student's name
studentid: Student's ID
major: Student's field of study
gpa: Student's grade point average
email: Student's email address
yearofstudy: Student's current year of study

Constructors

The class uses one __init__() method with default parameter values. It supports both:

Default constructor: Creates a student using predefined default values.
Parameterized constructor: Creates a student using information provided by the user.

Methods

display_info(): Displays the student's information in a formatted manner.
update_gpa(new_gpa): Updates the student's GPA.

Testing

The main program asks the user how many students to create. For each student, the user can choose between the default and parameterized constructors. The created student objects are stored in a list, and the program displays the information of every student.

Requirements

The project meets the assignment requirements by defining a class, including at least four attributes, supporting both default and parameterized object creation, implementing the required display method and an additional method, and testing multiple student objects through user input.

How to Run

Save the Python code in a file named main.py.
Run the program using Python:
python main.py
Follow the prompts to create and display student objects.
