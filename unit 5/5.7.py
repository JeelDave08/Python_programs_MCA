import mysql.connector
import re

# Connect database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python"
)

mycursor = mydb.cursor()

# Fetch all records
mycursor.execute("SELECT * FROM student")
rows = mycursor.fetchall()

# Email pattern (regex)
pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

print("Students with Valid Email:\n")

for row in rows:
    email = row[4]   # email column index
    
    if re.match(pattern, email):
        print(row)

mydb.close()
