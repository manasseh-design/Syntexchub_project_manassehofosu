# Define a class named Student with attributes name, student_id, and grade.
class Student:
    def __init__(self, name, student_id, grade):
        self.name = name
        self.student_id = student_id
        self.grade = grade
import json

#StudentManager class to manage a list of Student objects, with methods to add a student, remove a student by student_id, and display all students.
class StudentManager:
    def __init__(self):
        self.students = {}

    def add_student(self, name, student_id, grade):
        if student_id in self.students:
            print(f"Student with ID {student_id} already exists.")
        else:
            self.students[student_id] = Student(name, student_id, grade)
            print(f"Student {name} added successfully.")

    def update_student(self, student_id, name=None, grade=None):
        if student_id not in self.students:
            print(f"Student with ID {student_id} not found.")
            return
        if name:
            self.students[student_id].name = name
        if grade:
            self.students[student_id].grade = grade
        print(f"Student {student_id} updated successfully.")

    def delete_student(self, student_id):
        if student_id not in self.students:
            print(f"Student with ID {student_id} not found.")
            return
        del self.students[student_id]
        print(f"Student {student_id} deleted successfully.")

    def list_students(self):
        if not self.students:
            print("No students found.")
            return
        for student in self.students.values():
            print(f"ID: {student.student_id} | Name: {student.name} | Grade: {student.grade}")

    def save_to_file(self, filename="students.json"):
        data = {}
        for student_id, student in self.students.items():
            data[student_id] = {
                "name": student.name,
                "grade": student.grade
            }
        with open(filename, "w") as file:
            json.dump(data, file)
            print("Data saved to file successfully.")

    def load_from_file(self, filename="students.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                for student_id, info in data.items():
                    self.students[student_id] = Student(info["name"], student_id, info["grade"])
                print("Data loaded from file successfully.")
        except FileNotFoundError:
            print("NO SAVED DATA FOUND.")
# Example usage
def main():
    manager = StudentManager()
    manager.load_from_file()
    while True:
        print("\nStudent Manager")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. List Students")
        print("5. Save Data & Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter student name: ")
            student_id = input("Enter student ID: ")
            grade = input("Enter student grade: ")
            manager.add_student(name, student_id, grade)
        elif choice == "2":
            student_id = input("Student ID: ")
            name = input("New name(press enter to skip): ")
            grade = input("New grade(press enter to skip): ")
            manager.update_student(student_id, name or None, grade or None)
        elif choice == "3":
            student_id = input("Student ID: ")
            manager.delete_student(student_id)
        elif choice == "4":
            manager.list_students()
        elif choice == "5":
            manager.save_to_file()
            print("Exiting...")
            break
main()
try:
    main()
except Exception as e:
    print(f"An error occurred: {e}")
    input("Press Enter to exit.")
            





