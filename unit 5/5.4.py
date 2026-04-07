import mysql.connector

# Connect to database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python"
)

mycursor = mydb.cursor()

# User se input lo
roll = int(input("Enter Roll No: "))
name = input("Enter Name: ")
gender = input("Enter Gender: ")
age = int(input("Enter Age: "))
email = input("Enter Email: ")
mobile = input("Enter Mobile: ")
city = input("Enter City: ")

# Insert query
sql = "INSERT INTO student (rollno, name, gender, age, email, mobile, city) VALUES (%s,%s,%s,%s,%s,%s,%s)"
val = (roll, name, gender, age, email, mobile, city)

mycursor.execute(sql, val)
mydb.commit()

print("Record Inserted Successfully")

mydb.close()
