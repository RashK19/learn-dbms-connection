import tkinter as tk
import mysql.connector

mydb=mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="1234",
        database="info"
    )

mycursor=mydb.cursor()

def check_user():
    # print(name.get())
    # print(age.get())
    sql="SELECT *FROM STUDENT WHERE NAME= %s AND AGE= %s"
    val=(name.get(),age.get())
    mycursor.execute(sql,val)
    result=mycursor.fetchone()

    if result:
        welcome_label.config(text="Welcome, " + name.get())
    else:
        welcome_label.config(text="Wrong credentials")


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

login_button = tk.Button(root, text="Login", command=check_user)
login_button.place(x=250,y=300)

# Label to display login result
welcome_label = tk.Label(root, text="")
welcome_label.place(x=250,y=400)

root.mainloop()