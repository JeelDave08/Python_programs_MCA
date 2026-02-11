#Write a program to enter marks of 4 subjects and display result (result shall include total, percentage and grade)


m1 = float(input("Enter marks of subject 1: "))
m2 = float(input("Enter marks of subject 2: "))
m3 = float(input("Enter marks of subject 3: "))
m4 = float(input("Enter marks of subject 4: "))

total = m1 + m2 + m3 + m4
percentage = (total / 400) * 100

print("Total Marks =", total)
print("Percentage =", percentage)

if percentage >= 75:
    print("Grade: A")
elif percentage >= 60:
    print("Grade: B")
elif percentage >= 45:
    print("Grade: C")
else:
    print("Grade: Fail")
