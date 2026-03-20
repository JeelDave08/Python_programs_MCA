class Student:
    
    def __init__(self, rollno, name, age, gender):
        self.rollno = rollno
        self.name = name
        self.age = age
        self.gender = gender
    
    def AddStudent(self, rollno, name, age, gender):
        self.rollno = rollno
        self.name = name
        self.age = age
        self.gender = gender
    
    def DisplayStudent(self):
        print("\nStudent Details:")
        print("Roll No:", self.rollno)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)


# Create object with initial values
s1 = Student(101, "Rahul", 20, "Male")

# Display details
s1.DisplayStudent()

# Update details using method
s1.AddStudent(102, "Priya", 21, "Female")

# Display updated details
s1.DisplayStudent()
