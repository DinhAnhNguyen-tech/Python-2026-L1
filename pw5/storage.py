import os
import zipfile
import tarfile
from domains import Student, Course

DATA_FILE = "students.dat"
TXT_FILES = ["students.txt", "courses.txt", "marks.txt"]

def decompress_data():
    if not os.path.exists(DATA_FILE):
        return False

    if zipfile.is_zipfile(DATA_FILE):
        with zipfile.ZipFile(DATA_FILE, 'r') as zip_ref:
            zip_ref.extractall()
        return True
    return False

def load_data():
    students = []
    courses = []

    if os.path.exists("courses.txt"):
        with open("courses.txt", "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    c_id, name, credits = line.split(",")
                    courses.append(Course(c_id, name, int(credits)))

    if os.path.exists("students.txt"):
        with open("students.txt", "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    s_id, name, dob = line.split(",")
                    students.append(Student(s_id, name, dob))

    if os.path.exists("marks.txt") and students:
        student_dict = {s.id: s for s in students}
        with open("marks.txt", "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    c_id, s_id, mark = line.split(",")
                    if s_id in student_dict:
                        student_dict[s_id].marks[c_id] = float(mark)

    return students, courses


def compress_data():
    files_to_compress = [f for f in TXT_FILES if os.path.exists(f)]
    if not files_to_compress:
        return

    with zipfile.ZipFile(DATA_FILE, 'w', compression=zipfile.ZIP_DEFLATED) as zip_file:
        for file in files_to_compress:
            zip_file.write(file)
            
    for file in files_to_compress:
        os.remove(file)