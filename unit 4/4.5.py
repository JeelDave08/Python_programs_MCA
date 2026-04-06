import matplotlib.pyplot as plt

# Step 1: Input data
companies = []
employees = []

print("Enter details of 5 companies:")

for i in range(1, 6):
    name = input(f"Enter company {i} name: ")
    size = int(input(f"Enter number of employees in {name}: "))
    
    companies.append(name)
    employees.append(size)

# Step 2: Create bar graph
plt.bar(companies, employees)

# Step 3: Add labels and title
plt.title("Company Employee Size")
plt.xlabel("Company Names")
plt.ylabel("Number of Employees")

# Step 4: Show graph
plt.show()
