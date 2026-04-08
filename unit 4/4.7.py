import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read Excel file
file_path = "students.xlsx"   # change file name if needed
df = pd.read_excel(file_path)

# Step 2: Count Male and Female
gender_count = df['Gender'].value_counts()

print("Gender Count:")
print(gender_count)

# Step 3: Plot Bar Graph
plt.figure()
plt.bar(gender_count.index, gender_count.values)

plt.title("Male vs Female Students")
plt.xlabel("Gender")
plt.ylabel("Count")

plt.show()
