''' 2.9 Write a program to do student operations using menu as follows
a) Add Student
b) Search Student
c) List All Students
d) Update Student
e) Delete Student
f) Exit '''

students = {}

while True:
    print("\n----- Student Menu -----")
    print("a) Add Student")
    print("b) Search Student")
    print("c) List All Students")
    print("d) Update Student")
    print("e) Delete Student")
    print("f) Exit")

    choice = input("Enter your choice: ")

    if choice == 'a':
        sid = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        students[sid] = name
        print("Student added successfully.")

    elif choice == 'b':
        sid = input("Enter Student ID to search: ")
        if sid in students:
            print("Student Name:", students[sid])
        else:
            print("Student not found.")

    elif choice == 'c':
        print("\nList of Students:")
        for sid, name in students.items():
            print(sid, ":", name)

    elif choice == 'd':
        sid = input("Enter Student ID to update: ")
        if sid in students:
            name = input("Enter new name: ")
            students[sid] = name
            print("Student updated.")
        else:
            print("Student not found.")

    elif choice == 'e':
        sid = input("Enter Student ID to delete: ")
        if sid in students:
            del students[sid]
            print("Student deleted.")
        else:
            print("Student not found.")

    elif choice == 'f':
        print("Exiting program...")
        break

    else:
        print("Invalid choice.")
