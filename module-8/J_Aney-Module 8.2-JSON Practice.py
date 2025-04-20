# Jonah Aney CSD325 Module 8.2 Assignment: JSON Practice

# Import .json module - JHA
import json

# Create a function using for loop to grab all the data from the .json file - JHA
def print_student(student):
    for student in students:
        first_name = student.get('F_Name')
        last_name = student.get('L_Name')
        student_id = student.get('Student_ID')
        email = student.get('Email')

        print(f'{last_name}, {first_name}: ID = {student_id}, Email = {email}')

# Open and load the json file into a python list - JHA
with open('student.json', 'r') as file:
    students = json.load(file)

# Display original student list to user. - JHA
print("Original Student List")
print_student(students)

# New student information to be added. - JHA
new_student = {"F_Name": "Jonah",
               "L_Name": "Aney",
               "Student_ID": 123456,
               "Email": "janey@fictemail.com"
}
# Adding new student information to student list. - JHA
students.append(new_student)

# Display the updated list to the user. - JHA
print("\nUpdated Student List")
print_student(students)

# Save updated list to student.json file - JHA
with open('student.json', 'w') as file:
    json.dump(students, file, indent=4)

# Display output to let user know of the .json file update - JHA
print("\n student.json file has been updated")