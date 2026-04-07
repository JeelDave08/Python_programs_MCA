import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python"
)

mycursor = mydb.cursor()


roll = int(input("Enter Roll Number to search: "))


sql = "SELECT * FROM student WHERE rollno = %s"
val = (roll,)

mycursor.execute(sql, val)

result = mycursor.fetchone()


if result:
    print("Student Found:")
    print("Roll No:", result[0])
    print("Name:", result[1])
    print("Gender:", result[2])
    print("Age:", result[3])
    print("Email:", result[4])
    print("Mobile:", result[5])
    print("City:", result[6])
else:
    print("Student Not Found")

mydb.close()
