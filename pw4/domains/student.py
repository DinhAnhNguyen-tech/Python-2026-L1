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