from tkinter import *
from tkinter import ttk,messagebox
from PIL import ImageTk,Image
from ttkthemes import ThemedTk as team
import sys
import sqlite3
import login
import dashboard as ds
import json
import dashboard



class View_student():
    

    def __init__(self,root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("800x500+200+100")
        self.root.configure(background="black")
        self.root.resizable(False,False)
        self.firstname = StringVar()
        self.lastname = StringVar()
        self.matric = StringVar()
        self.gender =StringVar()
        self.record = StringVar()
        
        

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
        self.Frame_login = Frame(dashboard_frame,bg="black")
        self.Frame_login.place(x=70,y=150,height=220,width=660)
        title = Label(self.Frame_login,text="Search Student Records",font=("Impact",25,"bold"),fg="white",bg="black").place(x=70,y=30)

        Search_Student = Entry(self.Frame_login,textvariable=self.record,font=("Goudy old style",15,"bold"),fg="black",bd=1,bg="gray").place(x=70,y=140,width=500,height=30)

        self.search =PhotoImage(file="image/search.png")
        Search_btn = Button(self.Frame_login,image=self.search,font=("Goudy old style",15,"bold"),command=self.database).place(x=520,y=140,width=70,height=30)


        self.go_back=PhotoImage(file="image/goto.png")
        Search_btn = Button(self.Frame_login,image=self.go_back,font=("Goudy old style",15,"bold"),command=self.go_to_dashboard,bg="black",bd=0).place(x=560,y=0,width=80,height=50)



    def go_to_dashboard(self):
        dashboard.Dashboard(self.root)


    def database(self):
        global editor
        global fname
        global lname
        global mat
        global update_gender
        
        
        conn = sqlite3.connect('db/student_db.db')
        with conn:
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM Student WHERE matric=?",(self.record.get(),))
            row = cursor.fetchall()
            print(row)

            
            
            editor = team(theme="black")
            editor.title("Update")
            editor.geometry("800x500+200+100")
            
            editor.resizable(False,False)
            editor_frame = ttk.Frame(editor)
            editor_frame.place(x=0,y=0,height=640,width=1000)
        
            #frame
            update_frame = Frame(editor_frame,bg="black")
            update_frame.place(x=150,y=30,height=420,width=460)
            update_title = Label(update_frame,text="Update Records",font=("Impact",29,"bold"),fg="white",bg="black").place(x=70,y=30)

            if row:
        #username 

                Firstname = Label(update_frame,text="Firstname",font=("Goudy old style",15,"bold"),fg="white",bg="black").place(x=60,y=140)

                fname = Entry(update_frame,font=("times new roman",15),bg="lightgray",textvariable=self.firstname)
                fname.place(x=60,y=170,height=35,width=165)

            #password
                Lastname = Label(update_frame,text="Lastname",font=("Goudy old style",15,"bold"),fg="white",bg="black").place(x=240,y=140)

                lname = Entry(update_frame,font=("times new roman",15),bg="lightgray",textvariable=self.lastname)
                lname.place(x=240,y=170,height=35,width=165)

            
                Matric = Label(update_frame,text="Matric No",font=("Goudy old style",15,"bold"),fg="white",bg="black").place(x=55,y=220)

                mat = Entry(update_frame,font=("times new roman",15),bg="lightgray",textvariable=self.matric)
                mat.place(x=60,y=250,height=35,width=345)

            
                Label(update_frame,text="Gender",font=("Goudy old style",15,"bold"),fg="white",bg="black").place(x=60,y=300) 

                update_gender=Entry(update_frame,textvariable=self.gender,font=("times new roman",15),bg="lightgray")
                update_gender.place(x=60,y=330,width=345)
                

                register_btn = Button(editor,command=self.update,text="Update",font=("Goudy old style",20,"bold"),bg="white",fg="black",bd=0).place(x=210,y=430,height=35,width=150)

                cancel_register = Button(editor,text="Cancel",command=self.cancel,font=("Goudy old style",20,"bold"),bg="white",fg="black",bd=0).place(x=410,y=430,height=35,width=150)



                for i in row:
                    fname.insert(0,i[0])
                    lname.insert(0,i[1])
                    mat.insert(0,i[2])
                    update_gender.insert(0,i[3])

            else:
                No_record = Label(update_frame,text="No Record Found",font=("Goudy old style",25,"bold"),fg="white",bg="black").place(x=90,y=200)


    def update(self):
        conn = sqlite3.connect('db/student_db.db')
        with conn:
            cursor=conn.cursor()
            cursor.execute("""UPDATE Student SET
             firstname=:firstname, 
             lastname=:lastname,
             gender=:gender
              WHERE matric=:matric""",
              {
                  'firstname':fname.get(),
                  'lastname':lname.get(),
                  'gender':update_gender.get(),
                  'matric':self.record.get() 
              })
            row = cursor.fetchall()
            print(row)
            conn.commit()
            messagebox.showinfo("Success","Account updated successfully")
            editor.destroy()
            ds.Dashboard(self.root)
            
            
            #conn.close()

                                    
    def cancel(self):
        msg = messagebox.askquestion("Exist Application","Are you sure you want to exist",icon="warning")
        if msg=="yes":
            editor.destroy()              
            ds.Dashboard(self.root)

    def logout_function(self):
        Msg=messagebox.askquestion('Exist Application','Are you sure you want to exist this app',icon="info")
        if Msg == "yes":
            login.Login(self.root)

     

       


if __name__ == "__main__":
   root = team(theme="black")
   obj = View_student(root)
   root.mainloop()
