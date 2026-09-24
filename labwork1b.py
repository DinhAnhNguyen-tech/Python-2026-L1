student_list = []
course_info = []

def class_size():
    return int(input("How many students are in the class? "))

def add_student():
    student_id = input("Student ID: ")
    student_name = input("Student name: ")
    dob = input("DoB (YYYY-MM-DD): ")
    student_dict = {"ID": student_id, "name": student_name, "DoB": dob, "mark": {}}
    student_list.append(student_dict)

def course_size():
    return int(input("How many courses do you study? "))

def add_course():
    course_id = input("Course ID: ")
    course_name = input("Course name: ")
    course_dict = {"courseID": course_id, "courseName": course_name}
    course_info.append(course_dict)

def input_marks():
    selected_course_id = input("Which course ID do you want to enter marks for? ")
    for student in student_list:
        mark = float(input(f"Enter mark for {student['name']} (ID: {student['ID']}): "))
        student["mark"][selected_course_id] = mark

def list_courses():
    for course in course_info:
        print(course)

def list_students():
    for student in student_list:
        print(student)

def show_mark():
    selected_id = input("Which course ID do you want to see? ")
    for student in student_list:
        mark = student["mark"].get(selected_id, "No mark entered")
        print(f"{student['name']}: {mark}")


total_students = class_size()
for _ in range(total_students):
    add_student()

total_courses = course_size()
for _ in range(total_courses):
    add_course()

input_marks()
show_mark()
list_courses()
list_students()