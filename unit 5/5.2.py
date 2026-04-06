import mysql.connector
mydb=mysql.connector.connect(
     host="localhost",
     user="root",
     password="",
     database="python",
     )
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM student")

row = mycursor.fetchall()



for row in row:
    print(row)
mydb.close()

    
