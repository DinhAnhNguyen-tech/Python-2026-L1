import curses
import input as in_module
import output as out_module
import storage

def main():

    students, courses = [], []
    if storage.decompress_data():
        print("Existing database found. Unpacking students.dat")
        students, courses = storage.load_data()

    if not students or not courses:
        print("No saved data found. Please enter information manually.")
        students = in_module.input_students()
        courses = in_module.input_courses()
        in_module.input_marks(students, courses)

    selected_course_id = input("\nWhich course ID do you want to view marks for? ")

    def run_curses_ui(stdscr):
        out_module.list_courses(stdscr, courses)
        out_module.list_students(stdscr, students)
        out_module.show_sorted_gpa(stdscr, students, courses)
        out_module.show_marks(stdscr, students, selected_course_id)

    print("\nPress Enter.")
    input()
    curses.wrapper(run_curses_ui)
    print("\nCompressing and saving data into students.dat")
    storage.compress_data()
    print("Done.")

if __name__ == "__main__":
    main()