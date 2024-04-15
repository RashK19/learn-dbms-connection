import mysql.connector

mydb= mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="1234",
    database="info"
)

mycursor= mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS STUDENT (ID INT AUTO_INCREMENT PRIMARY KEY, NAME VARCHAR (20), AGE INT (3) )")

name= input("enter your name= ")
age= int(input("enter your age= "))

sql= "INSERT INTO STUDENT (NAME,AGE) VALUES (%s,%s)"
val=(name,age)
mycursor.execute(sql,val)

mydb.commit()

mydb.close()
