import math
import numpy as np

class Student:
    def __init__(self, student_id, name, dob):
        self.id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}
        self.gpa = 0.0

    def calculate_gpa(self, courses_list):
        marks = []
        credits = []

        for course in courses_list:
            if course.id in self.marks:
                marks.append(self.marks[course.id])
                credits.append(course.credits)

        if not credits:
            self.gpa = 0.0
            return self.gpa

        marks_array = np.array(marks)
        credits_array = np.array(credits)

        self.gpa = np.sum(marks_array * credits_array) / np.sum(credits_array)
        return self.gpa

class Course:
    def __init__(self, course_id, name, credits):
        self.id = course_id
        self.name = name
        self.credits = credits

class SchoolManagement:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_students(self):
        count = int(input("How many students are in the class? "))
        for _ in range(count):
            student_id = input("\nStudent ID: ")
            name = input("Student name: ")
            dob = input("DoB (YYYY-MM-DD): ")
            self.students.append(Student(student_id, name, dob))

    def input_courses(self):
        count = int(input("\nHow many courses do you study? "))
        for _ in range(count):
            course_id = input("\nCourse ID: ")
            name = input("Course name: ")
            credits = int(input("Credits: "))
            self.courses.append(Course(course_id, name, credits))

    def input_marks(self):
        selected_course_id = input("\nWhich course ID do you want to enter marks for? ")
        for student in self.students:
            mark = float(input(f"Enter mark for {student.name} (ID: {student.id}): "))
            student.marks[selected_course_id] = math.floor(mark * 10) / 10

    def list_courses(self):
        print("\n Course List ")
        for course in self.courses:
            print(f"ID: {course.id} | Name: {course.name} | Credits: {course.credits}")

    def list_students(self):
        print("\n Student List ")
        for student in self.students:
            print(f"ID: {student.id} | Name: {student.name} | DoB: {student.dob}")

    def show_marks(self):
        selected_id = input("\nWhich course ID do you want to see? ")
        print(f"\n Marks for Course {selected_id} ")
        for student in self.students:
            mark = student.marks.get(selected_id, "No mark entered")
            print(f"{student.name}: {mark}")

    def sort_gpa(self):
        for student in self.students:
            student.calculate_gpa(self.courses)

        self.students.sort(key=lambda student: student.gpa, reverse=True)
        print("\n Students sorted by GPA descending order")
        for student in self.students:
            print(f"ID: {student.id} | Name: {student.name} | GPA: {student.gpa:.2f}")


if __name__ == "__main__":
    school = SchoolManagement()
    school.input_students()
    school.input_courses()
    school.input_marks()
    school.list_courses()
    school.list_students()
    school.sort_gpa()
    school.show_marks()

    