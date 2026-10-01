import math
from domains import Student, Course

def input_students():
    students = []
    count = int(input("How many students are in the class? "))

    with open("students.txt", "w") as f:
        for _ in range(count):
            student_id = input("\nStudent ID: ")
            name = input("Student name: ")
            dob = input("DoB (YYYY-MM-DD): ")
            students.append(Student(student_id, name, dob))
            f.write(f"{student_id}, {name}, {dob}\n")
    return students

def input_courses():
    courses = []
    count = int(input("\nHow many courses do you study? "))

    with open("courses.txt", "w") as f:
        for _ in range(count):
            course_id = input("\nCourse ID: ")
            name = input("Course name: ")
            credits = int(input("Credits: "))
            courses.append(Course(course_id, name, credits))
            f.write(f"{course_id}, {name}, {credits}\n")
    return courses

def input_marks(students, courses):
    with open("marks.txt", "a") as f:
        for course in courses:
            print(f"\nEntering marks for course: {course.name} (ID: {course.id}) ")
            for student in students:
                mark = float(input(f"Enter mark for {student.name} (ID: {student.id}): "))
                rounded_mark = math.floor(mark * 10) / 10
                student.marks[course.id] = rounded_mark
                f.write(f"{course.id},{student.id},{rounded_mark}\n")