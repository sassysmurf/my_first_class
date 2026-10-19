from creating_class import Student

# create an empty list to store student objects
students = []

# ask how many students to create
n = int(input("How many students do you want to create? "))

# create students
for i in range(n):
    print(f"\nCreating student {i + 1}")
    choice = input("Choose constructor (1 = Default, 2 = Parameterized): ")

    if choice == "1":
        #create with default values
        student = Student()

    elif choice == "2":
        #ask student info
        name = input("Enter student name: ")
        studentid = input("Enter student ID: ")
        major = input("Enter student major: ")
        gpa = float(input("Enter GPA: "))
        email = input("Enter email: ")
        yearofstudy = int(input("Enter year of study: "))

        student = Student(name, studentid, major, gpa, email, yearofstudy)

    else:
        print("Invalid choice")
        student = Student()
    #add student to the list
    students.append(student)

print("\n All Students ")
for student in students:
    student.display_info()