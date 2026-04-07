import mysql.connector

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

print("Students whose name starts with 'N' and length is 5:\n")

for row in rows:
    name = row[1]   # name column
    
    if name.startswith('N') and len(name) == 5:
        print(row)

mydb.close()
