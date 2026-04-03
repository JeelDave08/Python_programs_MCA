# Base Class 1
class Student:
    def __init__(self, rollno, name):
        self.rollno = rollno
        self.name = name

    def display_student(self):
        print("Student Details:")
        print("Roll No:", self.rollno)
        print("Name:", self.name)


# Base Class 2
class Course:
    def __init__(self, coursename, fee):
        self.coursename = coursename
        self.fee = fee

    def display_course(self):
        print("\nCourse Details:")
        print("Course Name:", self.coursename)
        print("Fee:", self.fee)


# Derived Class (Multiple Inheritance)
class Result(Student, Course):
    def __init__(self, rollno, name, coursename, fee, marks):
        Student.__init__(self, rollno, name)
        Course.__init__(self, coursename, fee)
        self.marks = marks

    def display_result(self):
        print("\nResult Details:")
        print("Marks:", self.marks)


# Main Program
r1 = Result(101, "Jeel", "Python", 15000, 85)

r1.display_student()
r1.display_course()
r1.display_result()

# Display MRO
print("\nMethod Resolution Order (MRO):")
for cls in Result.__mro__:
    print(cls)
