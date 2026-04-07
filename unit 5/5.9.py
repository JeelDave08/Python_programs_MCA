# Program to create a list with name, data type and size
# and generate SQL CREATE TABLE statement

# Step 1: Create list to store column details
columns = []

# Step 2: Take input from user
n = int(input("Enter number of columns: "))

for i in range(n):
    print(f"\nEnter details for column {i+1}:")
    name = input("Column Name: ")
    datatype = input("Data Type (varchar/int/etc): ")
    size = input("Size: ")
    
    # Store as tuple (name, datatype, size)
    columns.append((name, datatype, size))

# Step 3: Display stored list
print("\nStored Column Information:")
for col in columns:
    print(col)

# Step 4: Generate SQL CREATE TABLE statement
table_name = input("\nEnter table name: ")

query = f"CREATE TABLE {table_name} (\n"

for i, col in enumerate(columns):
    name, datatype, size = col
    
    # Format for SQL
    if datatype.lower() == "int":
        query += f"  {name} {datatype}({size})"
    else:
        query += f"  {name} {datatype}({size})"
    
    # Add comma except last column
    if i != len(columns) - 1:
        query += ",\n"
    else:
        query += "\n"

query += ");"

# Step 5: Display final query
print("\nGenerated SQL Table:")
print(query)
