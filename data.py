import tkinter as tk
import mysql.connector

mydb=mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="1234",
        database="info"
    )

mycursor=mydb.cursor()

def submit():
    # print(name.get())
    # print(age.get())
    sql="INSERT INTO STUDENT (NAME,AGE) VALUES(%s,%s)"
    val=(name.get(),age.get())
    mycursor.execute(sql,val)
    mydb.commit()
    mydb.close()
    name.set(" ")
    age.set(" ")

root=tk.Tk()
root.geometry("500x500")
root.resizable(width=False, height=False)

l1=tk.Label(text="Name",font="14").place(x=100,y=100)
l2=tk.Label(text="Age",font="14").place(x=100,y=200)

name=tk.Variable();
age=tk.IntVar();

e_name=tk.Entry(root,textvariable=name).place(x=300,y=100)
e_age=tk.Entry(root,textvariable=age).place(x=300,y=200)

submit=tk.Button(root,text="Submit",command=submit).place(x=250,y=300)

root.mainloop()