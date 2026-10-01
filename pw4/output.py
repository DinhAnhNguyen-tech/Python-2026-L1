import curses

def display_text(stdscr, title, lines):
    stdscr.clear()
    stdscr.addstr(0, 0, f" {title} ", curses.A_BOLD)
    
    row = 2
    for line in lines:
        stdscr.addstr(row, 0, line)
        row += 1
        
    stdscr.addstr(row + 1, 0, "Press any key to continue")
    stdscr.refresh()
    stdscr.getch()

def list_courses(stdscr, courses):
    lines = [f"ID: {c.id} | Name: {c.name} | Credits: {c.credits}" for c in courses]
    display_text(stdscr, "Course List", lines)

def list_students(stdscr, students):
    lines = [f"ID: {s.id} | Name: {s.name} | DoB: {s.dob}" for s in students]
    display_text(stdscr, "Student List", lines)

def show_sorted_gpa(stdscr, students, courses):
    for student in students:
        student.calculate_gpa(courses)
    students.sort(key=lambda s: s.gpa, reverse=True)
    
    lines = [f"ID: {s.id} | Name: {s.name} | GPA: {s.gpa:.2f}" for s in students]
    display_text(stdscr, "Students Sorted by GPA", lines)

def show_marks(stdscr, students, course_id):
    lines = []
    for student in students:
        mark = student.marks.get(course_id, "No mark entered")
        lines.append(f"{student.name}: {mark}")
    display_text(stdscr, f"Marks for Course {course_id}", lines)