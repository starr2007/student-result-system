from student import Student
from results import get_grade, validate_score
from storage import load_students, save_students

SUBJECTS = ["Maths", "English", "Physics", "Chemistry", "Biology"]


def add_student(students):
    sid = input("Student ID: ").strip()
    if sid in students:
        print("That ID already exists.")
        return
    name = input("Full name: ").strip()
    cls = input("Class/Form: ").strip()
    gender = input("Gender: ").strip()
    dob = input("Date of birth (YYYY-MM-DD): ").strip()
    students[sid] = Student(sid, name, cls, gender, dob)
    save_students(students)
    print("Student added.")


def view_students(students):
    if not students:
        print("No students yet.")
        return
    for s in students.values():
        print(f"{s.student_id} | {s.name} | {s.student_class} | {s.gender} | {s.dob}")


def search_student(students):
    term = input("Enter ID or name: ").strip().lower()
    found = [s for s in students.values()
             if term == s.student_id.lower() or term in s.name.lower()]
    if not found:
        print("No match found.")
    for s in found:
        print(f"{s.student_id} | {s.name} | {s.student_class}")


def update_student(students):
    sid = input("Student ID to update: ").strip()
    s = students.get(sid)
    if not s:
        print("Student not found.")
        return
    print("Press Enter to keep the current value.")
    s.name = input(f"Name [{s.name}]: ").strip() or s.name
    s.student_class = input(f"Class [{s.student_class}]: ").strip() or s.student_class
    s.gender = input(f"Gender [{s.gender}]: ").strip() or s.gender
    s.dob = input(f"DOB [{s.dob}]: ").strip() or s.dob
    save_students(students)
    print("Student updated.")


def delete_student(students):
    sid = input("Student ID to delete: ").strip()
    if sid not in students:
        print("Student not found.")
        return
    if input("Type YES to confirm: ") == "YES":
        del students[sid]
        save_students(students)
        print("Student deleted.")


def record_scores(students):
    sid = input("Student ID: ").strip()
    student = students.get(sid)
    if not student:
        print("Student not found.")
        return
    scores = {}
    for subject in SUBJECTS:
        while True:
            try:
                scores[subject] = validate_score(input(f"{subject} score: "))
            except ValueError:
                print("Enter a number between 0 and 100.")
            else:
                break
    student.set_scores(scores)
    save_students(students)
    print("Scores saved.")


def report_card(students):
    sid = input("Student ID: ").strip()
    s = students.get(sid)
    if not s:
        print("Student not found.")
        return
    if not s.scores:
        print("No scores recorded yet.")
        return
    print("\n--- REPORT CARD ---")
    print(f"Name: {s.name} | ID: {s.student_id} | Class: {s.student_class}")
    for subject, score in s.scores.items():
        print(f"{subject:<12}{score}")
    print(f"Total: {s.total()}  Average: {s.average():.2f}  Grade: {get_grade(s.average())}")
    print(f"Date entered: {s.date_entered}")


def main():
    students = load_students()
    while True:
        print("\n=== STUDENT RESULT SYSTEM ===")
        print("1. Add student")
        print("2. View all students")
        print("3. Search student")
        print("4. Update student info")
        print("5. Delete student")
        print("6. Record/update scores")
        print("7. Report card")
        print("0. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            record_scores(students)
        elif choice == "7":
            report_card(students)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()