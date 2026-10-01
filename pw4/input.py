import math
from domains import Student, Course

def input_students():
    students = []
    count = int(input("How many students are in the class? "))
    for _ in range(count):
        student_id = input("\nStudent ID: ")
        name = input("Student name: ")
        dob = input("DoB (YYYY-MM-DD): ")
        students.append(Student(student_id, name, dob))
    return students

def input_courses():
    courses = []
    count = int(input("\nHow many courses do you study? "))
    for _ in range(count):
        course_id = input("\nCourse ID: ")
        name = input("Course name: ")
        credits = int(input("Credits: "))
        courses.append(Course(course_id, name, credits))
    return courses

def input_marks(students):
    selected_course_id = input("\nWhich course ID do you want to enter marks for? ")
    for student in students:
        mark = float(input(f"Enter mark for {student.name} (ID: {student.id}): "))
        student.marks[selected_course_id] = math.floor(mark * 10) / 10