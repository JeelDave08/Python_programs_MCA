# Base Class
class Student:
    def __init__(self, rollno, name, gender, age):
        self.rollno = rollno
        self.name = name
        self.gender = gender
        self.age = age

    def display_student(self):
        print("Student Details:")
        print("Roll No:", self.rollno)
        print("Name:", self.name)
        print("Gender:", self.gender)
        print("Age:", self.age)


# Derived Class
class Course(Student):
    def __init__(self, rollno, name, gender, age, coursename, duration, fee):
        # Calling base class constructor
        super().__init__(rollno, name, gender, age)
        self.coursename = coursename
        self.duration = duration
        self.fee = fee

    def display_course(self):
        print("\nCourse Details:")
        print("Course Name:", self.coursename)
        print("Duration:", self.duration)
        print("Fee:", self.fee)


# Main Program
s1 = Course(101, "Jeel", "Female", 20, "Python", "6 Months", 15000)

s1.display_student()
s1.display_course()
