from tkinter import *
from tkinter import ttk,messagebox
from PIL import ImageTk,Image
from ttkthemes import ThemedTk as team
import sys
import sqlite3
import login
import dashboard
import json




class Add_student():

    def __init__(self,root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("800x600+300+60")
        self.root.configure(background="black")
        self.root.resizable(False,False)
        self.firstname = StringVar()
        self.lastname = StringVar()
        self.matric = StringVar()
        self.gender =StringVar()
        
        

        #frame
        dashboard_frame = ttk.Frame(self.root)
        dashboard_frame.place(x=0,y=0,height=640,width=1000)
        data = open('db/lecturer.txt','r')
        for i in data:
            User_label = Label(dashboard_frame,text=i,font=("Goudy old style",15,"bold")).place(x=0,y=0,width=800)
        #logout
        self.logout =PhotoImage(file="image/logout.png")

        logout =Button(User_label,image=self.logout,text="Add Student",command=self.logout_function,bd=0).place(x=730,y=0,height=30,width=60)

        
        
        #frame
        Frame_login = Frame(dashboard_frame,bg="black")
        Frame_login.place(x=150,y=80,height=420,width=460)
        title = Label(Frame_login,text="Register Student",font=("Impact",29,"bold"),fg="white",bg="black").place(x=70,y=30)
      
        #username 

        Firstname = Label(Frame_login,text="Firstname",font=("Goudy old style",15,"bold"),fg="white",bg="black").place(x=60,y=140)

        self.txt_firstname = Entry(Frame_login,font=("times new roman",15),bg="lightgray",textvariable=self.firstname).place(x=60,y=170,height=35,width=165)

        #password
        Lastname = Label(Frame_login,text="Lastname",font=("Goudy old style",15,"bold"),fg="white",bg="black").place(x=240,y=140)

        self.txt_lastname = Entry(Frame_login,font=("times new roman",15),bg="lightgray",textvariable=self.lastname).place(x=240,y=170,height=35,width=165)

        #comfirm password
        Matric = Label(Frame_login,text="Matric No",font=("Goudy old style",15,"bold"),fg="white",bg="black").place(x=55,y=220)

        self.txt_matric = Entry(Frame_login,font=("times new roman",15),bg="lightgray",textvariable=self.matric).place(x=60,y=250,height=35,width=345)

        
        Label(Frame_login,text="Gender",font=("Goudy old style",15,"bold"),fg="white",bg="black").place(x=60,y=300) 
        Radiobutton(Frame_login, text="Male",padx = 5, variable=self.gender, value=1).place(x=60,y=330,width=160)
        Radiobutton(Frame_login, text="Female",padx = 20, variable=self.gender, value=2).place(x=245,y=330,width=160)


        register_btn = Button(self.root,command=self.student_database,text="Register",font=("Goudy old style",20,"bold"),bg="white",fg="black",bd=0).place(x=210,y=480,height=35,width=150)

        cancel_register = Button(self.root,text="Cancel",command=self.cancel,font=("Goudy old style",20,"bold"),bg="white",fg="black",bd=0).place(x=410,y=480,height=35,width=150)


    def student_database(self):            
        if self.firstname.get() =="" or self.lastname.get()=="" or self.matric.get()=="" or self.gender.get()=="":
            messagebox.showinfo("Error","All field are required")
        else:
            conn = sqlite3.connect('db/student_db.db')
            with conn:
                cursor=conn.cursor()
                    
                cursor.execute('CREATE TABLE IF NOT EXISTS Student (firstname TEXT,lastname TEXT,matric TEXT,gender TEXT)')
                cursor.execute('SELECT * FROM Student')
                row = cursor.fetchall()
                check_user = self.matric.get()
                list_row = []
                for i in row:
                    list_row.append(i[2])                  
                
                if check_user in list_row:
                    messagebox.showwarning("Error","Username with that matric number Already Exist")
                    pass        
                       
                else:
                    cursor.execute('INSERT INTO Student (firstname,lastname,matric,gender) VALUES(?,?,?,?)',(self.firstname.get(),self.lastname.get(),self.matric.get(),self.gender.get()))
                    conn.commit()
                    messagebox.showinfo("Success","Account Created")
                                        
                    dashboard.Dashboard(self.root)
                    pass
                    #pass
                                    
    def cancel(self):
        dashboard.Dashboard(self.root)

    def logout_function(self):
        Msg=messagebox.askquestion('Exist Application','Are you sure you want to exist this app',icon="info")
        if Msg == "yes":
            login.Login(self.root)

     

       


if __name__ == "__main__":
   root = team(theme="black")
   obj = Add_student(root)
   root.mainloop()
