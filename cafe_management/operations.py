def view_students(students):
    if not students:
        return "No students found."
    return "Students:", [student for student in students]