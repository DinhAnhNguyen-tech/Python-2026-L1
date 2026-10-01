import curses
import input as in_mod
import output as out

def main():

    students = in_mod.input_students()
    courses = in_mod.input_courses()
    in_mod.input_marks(students)
    
    selected_course_id = input("\nWhich course ID do you want to see marks for? ")

    def run_curses_ui(stdscr):
        out.list_courses(stdscr, courses)
        out.list_students(stdscr, students)
        out.show_sorted_gpa(stdscr, students, courses)
        out.show_marks(stdscr, students, selected_course_id)

    print("\nPress Enter.")
    input()
    curses.wrapper(run_curses_ui)

if __name__ == "__main__":
    main()