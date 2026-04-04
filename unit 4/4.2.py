import pandas as pd
import os

# Step 1: Check current folder
print("Current Working Directory:", os.getcwd())

# Step 2: File path (same folder as your .py file)
file_path = "student_data.xlsx"

# Step 3: Load Excel file
df = pd.read_excel(file_path)

# Step 4: Display column names and data types
print("\n--- Columns in File ---")
print(df.columns)

print("\n--- Data Types ---")
print(df.dtypes)

# Step 5: List of students from Rajkot City
rajkot_students = df[df['City'] == 'Rajkot']
print("\n--- Students from Rajkot City ---")
print(rajkot_students)

# Step 6: List of Male students
male_students = df[df['Gender'] == 'Male']
print("\n--- Male Students ---")
print(male_students)

# Step 7: List of Male students from Rajkot City
male_rajkot = df[(df['Gender'] == 'Male') & (df['City'] == 'Rajkot')]
print("\n--- Male Students from Rajkot City ---")
print(male_rajkot)

# Step 8: List of students whose age >= 20
age_students = df[df['Age'] >= 20]
print("\n--- Students with Age >= 20 ---")
print(age_students)
