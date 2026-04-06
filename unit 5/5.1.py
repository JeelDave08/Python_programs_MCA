import mysql.connector
mydb=mysql.connector.connect(
     host="localhost",
     user="root",
     password="",
     database="python",
     )
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM student")

row = mycursor.fetchone()


while row is not None:
     print(row)
     row = mycursor.fetchone()
mydb.close()
     
