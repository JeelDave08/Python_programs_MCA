import matplotlib.pyplot as plt

# Step 1: Input profit for 5 years
years = []
profits = []

print("Enter profit for 5 years:")

for i in range(1, 6):
    year = input(f"Enter year {i}: ")
    profit = float(input(f"Enter profit for {year}: "))
    
    years.append(year)
    profits.append(profit)

# Step 2: Plot line graph
plt.plot(years, profits, marker='o')

# Step 3: Add labels and title
plt.title("Profit of 5 Years")
plt.xlabel("Year")
plt.ylabel("Profit")

# Step 4: Show grid
plt.grid()

# Step 5: Display graph
plt.show()
