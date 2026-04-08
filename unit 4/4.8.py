import matplotlib.pyplot as plt

# Input number of courses
n = int(input("Enter number of courses: "))

courses = []
students = []

# Input course names and student counts
for i in range(n):
    name = input(f"Enter name of course {i+1}: ")
    count = int(input(f"Enter number of students in {name}: "))
    courses.append(name)
    students.append(count)

# Find index of course with maximum students
max_index = students.index(max(students))

# Create explode list (separate max slice)
explode = [0] * n
explode[max_index] = 0.2   # Highlight the max slice

# Plot pie chart
plt.figure()
plt.pie(students, labels=courses, autopct='%1.1f%%',
        explode=explode, shadow=True, startangle=90)

plt.title("Course-wise Student Distribution")
plt.show()
