class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Grade: {self.grade}"


class StudentDatabase:
    def __init__(self):
        self.students = {}

    def add_student(self):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        grade = input("Enter student grade: ")

        student = Student(student_id, name, age, grade)
        self.students[student_id] = student
        print("Student added successfully.")

    def view_students(self):
        if not self.students:
            print("No students found.")
        else:
            print("List of students:")
            for student_id, student_info in self.students.items():
                print(student_info)

    def search_student(self):
        student_id = input("Enter student ID to search: ")
        if student_id in self.students:
            print("Student found:", self.students[student_id])
        else:
            print("Student not found.")

    def update_student(self):
        student_id = input("Enter student ID to update: ")
        if student_id in self.students:
            name = input("Enter updated name: ")
            age = int(input("Enter updated age: "))
            grade = input("Enter updated grade: ")

            self.students[student_id].name = name
            self.students[student_id].age = age
            self.students[student_id].grade = grade

            print("Student updated successfully.")
        else:
            print("Student not found.")

    def delete_student(self):
        student_id = input("Enter student ID to delete: ")
        if student_id in self.students:
            del self.students[student_id]
            print("Student deleted successfully.")
        else:
            print("Student not found.")

    def handle_choice(self, choice):
        if choice == 1:
            self.add_student()
        elif choice == 2:
            self.view_students()
        elif choice == 3:
            self.search_student()
        elif choice == 4:
            self.update_student()
        elif choice == 5:
            self.delete_student()


def main_menu():
    student_db = StudentDatabase()
    while True:
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("16. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 16:
            break
        else:
            student_db.handle_choice(choice)


main_menu()
