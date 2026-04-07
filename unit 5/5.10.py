# Menu-based Student Management System

students = []   # list to store student records (as dictionaries)

def insert_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")
    
    student = {"roll": roll, "name": name, "marks": marks}
    students.append(student)
    print("Student inserted successfully!\n")


def update_student():
    roll = input("Enter Roll No to update: ")
    for s in students:
        if s["roll"] == roll:
            s["name"] = input("Enter new Name: ")
            s["marks"] = input("Enter new Marks: ")
            print("Student updated successfully!\n")
            return
    print("Student not found!\n")


def search_student():
    roll = input("Enter Roll No to search: ")
    for s in students:
        if s["roll"] == roll:
            print("Student Found:")
            print(s)
            return
    print("Student not found!\n")


def delete_student():
    roll = input("Enter Roll No to delete: ")
    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            print("Student deleted successfully!\n")
            return
    print("Student not found!\n")


def list_students():
    if not students:
        print("No records found!\n")
    else:
        print("\nStudent List:")
        for s in students:
            print(s)
        print()


# Main Menu
while True:
    print("----- MENU -----")
    print("1. Insert Student")
    print("2. Update Student")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. List Students")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        insert_student()
    elif choice == '2':
        update_student()
    elif choice == '3':
        search_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        list_students()
    elif choice == '6':
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.\n")
