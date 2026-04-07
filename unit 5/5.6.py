import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python"
)

mycursor = mydb.cursor()

roll = int(input("Enter Roll No to delete: "))

sql = "DELETE FROM student WHERE rollno = %s"
val = (roll,)

mycursor.execute(sql, val)
mydb.commit()

if mycursor.rowcount > 0:
    print("Record Deleted Successfully")
else:
    print("Student Not Found")

mydb.close()
