import matplotlib.pyplot as plt

# Step 1: Input ages of 50 students
ages = []

print("Enter age of 50 students:")

for i in range(1, 51):
    age = int(input(f"Enter age of student {i}: "))
    ages.append(age)

# Step 2: Define bins (age groups)
bins = [0, 10, 20, 30, 40, 50, 60, 120]

# Step 3: Create histogram
plt.hist(ages, bins=bins)

# Step 4: Labels and title
plt.title("Age Distribution of Students")
plt.xlabel("Age Groups")
plt.ylabel("Number of Students")

# Step 5: Show graph
plt.show()
