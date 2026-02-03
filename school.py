students = {}
teachers = {}


def add_student():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = input("Enter student grade: ")

    student = {
        'id': student_id,
        'name': name,
        'age': age,
        'grade': grade
    }

    students[student_id] = student
    print("Student added successfully.")

def view_students():
    if not students:
        print("No students found.")
    else:
        print("List of students:")
        for student_id, student_info in students.items():
            print("ID: {}, Name: {}, Age: {}, Grade: {}".format(student_id, student_info['name'], student_info['age'], student_info['grade']))


def search_student():
    student_id = input("Enter student ID to search: ")
    if student_id in students:
        student_info = students[student_id]
        print(f"Student found - ID: {student_info['id']}, Name: {student_info['name']}, Age: {student_info['age']}, Grade: {student_info['grade']}")
    else:
        print("Student not found.")

def update_student():
    student_id = input("Enter student ID to update: ")
    if student_id in students:
        name = input("Enter updated name: ")
        age = int(input("Enter updated age: "))
        grade = input("Enter updated grade: ")

        students[student_id]['name'] = name
        students[student_id]['age'] = age
        students[student_id]['grade'] = grade

        print("Student updated successfully.")
    else:
        print("Student not found.")

def delete_student():
    student_id = input("Enter student ID to delete: ")
    if student_id in students:
        del students[student_id]
        print("Student deleted successfully.")
    else:
        print("Student not found.")



def add_teacher():
    teacher_id = input("Enter teacher ID: ")
    name = input("Enter teacher name: ")
    subject = input("Enter subject: ")

    teacher = {
        'id': teacher_id,
        'name': name,
        'subject': subject
    }

    teachers[teacher_id] = teacher
    print("Teacher added successfully.")

def view_teachers():
    if not teachers:
        print("No teachers found.")
    else:
        print("List of teachers:")
        for teacher_id, teacher_info in teachers.items():
            print(f"ID: {teacher_id}, Name: {teacher_info['name']}, Subject: {teacher_info['subject']}")

def search_teacher():
    teacher_id = input("Enter teacher ID to search: ")
    if teacher_id in teachers:
        teacher_info = teachers[teacher_id]
        print(f"Teacher found - ID: {teacher_info['id']}, Name: {teacher_info['name']}, Subject: {teacher_info['subject']}")
    else:
        print("Teacher not found.")

def update_teacher():
    teacher_id = input("Enter teacher ID to update: ")
    if teacher_id in teachers:
        name = input("Enter updated name: ")
        subject = input("Enter updated subject: ")

        teachers[teacher_id]['name'] = name
        teachers[teacher_id]['subject'] = subject

        print("Teacher updated successfully.")
    else:
        print("Teacher not found.")

def delete_teacher():
    teacher_id = input("Enter teacher ID to delete: ")
    if teacher_id in teachers:
        del teachers[teacher_id]
        print("Teacher deleted successfully.")
    else:
        print("Teacher not found.")





def handle_choice(choice):
    if choice == 1:
        add_student()
    elif choice == 2:
        view_students()
    elif choice == 3:
        search_student()
    elif choice == 4:
        update_student()
    elif choice == 5:
        delete_student()
    elif choice == 6:
        add_teacher()
    elif choice == 7:
        view_teachers()
    elif choice == 8:
        search_teacher()
    elif choice == 9:
        update_teacher()
    elif choice == 10:
        delete_teacher()
    
def main_menu():
    while True:
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Add Teacher")
        print("7. View Teachers")
        print("8. Search Teacher")
        print("9. Update Teacher")
        print("10. Delete Teacher")
        print("11. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 16:
            break
        else:
            handle_choice(choice)

main_menu()
