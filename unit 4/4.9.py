import re
import pandas as pd

# Read file (change file name as needed)
df = pd.read_csv("students.csv")

# Email regex pattern
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

print("Records with valid emails:\n")

# Filter and display
for index, row in df.iterrows():
    email = str(row['Email'])
    if re.match(email_pattern, email):
        print(row)
