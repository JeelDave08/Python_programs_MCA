import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python"
)

mycursor = mydb.cursor()

roll = int(input("Enter Roll No to update: "))
new_city = input("Enter new city: ")

sql = "UPDATE student SET city = %s WHERE rollno = %s"
val = (new_city, roll)

mycursor.execute(sql, val)
mydb.commit()

if mycursor.rowcount > 0:
    print("Record Updated Successfully")
else:
    print("Student Not Found")

mydb.close()
