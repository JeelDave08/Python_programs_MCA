import pandas as pd

# Load Excel file
file_path = "student_data.xlsx"
df = pd.read_excel(file_path)

# Display original data
print("\n--- Original Data ---")
print(df)

# -------------------------------
# 1) Using dropna()
# -------------------------------
# Remove rows with any missing values
dropna_df = df.dropna()

print("\n--- Data after dropna() ---")
print(dropna_df)

# -------------------------------
# 2) Using fillna()
# -------------------------------
# Fill missing values with default values
fillna_df = df.fillna({
    'Name': 'Unknown',
    'Gender': 'Not Specified',
    'E-Mail': 'noemail@gmail.com',
    'Mobile': 0,
    'Age': 0,
    'City': 'Unknown'
})

print("\n--- Data after fillna() ---")
print(fillna_df)
