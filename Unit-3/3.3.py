#Write a program to make use of class method and instance method.

class Student:
    
    school_name = "ABC School"   # Class variable
    
    def __init__(self, name, marks):
        self.name = name        # Instance variable
        self.marks = marks
    
    # Instance method
    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("School:", Student.school_name)
    
    # Class method
    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name


# Create objects
s1 = Student("Rahul", 85)
s2 = Student("Priya", 90)

# Call instance method
s1.display()
print()

# Change class variable using class method
Student.change_school("XYZ School")

# Call again to see change
s2.display()
