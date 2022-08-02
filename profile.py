from tkinter import *
from tkinter import ttk,messagebox
from PIL import ImageTk,Image
from ttkthemes import ThemedTk as team
import sys
import sqlite3
import login
import dashboard as ds
import json




class Profile():
    

    def __init__(self,root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("800x500+200+100")
        self.root.configure(background="black")
        self.root.resizable(False,False)
        self.username = StringVar()
        self.password = StringVar()
        self.confirm_pass = StringVar()
        self.email =StringVar()
        self.record = StringVar()
        global editor
        global username_btn
        global password_btn
        global confirm_pass_btn
        global email_btn 

        
        editor_frame = ttk.Frame(self.root)
        editor_frame.place(x=0,y=0,height=680,width=1000)
        
            #frame
        update_frame = Frame(editor_frame,bg="black")
        update_frame.place(x=150,y=50,height=420,width=460)
        update_title = Label(update_frame,text="Update Records",font=("Impact",29,"bold"),fg="white",bg="black").place(x=70,y=30)
        
        
        #frame
        data = open('db/lecturer.txt','r')
        for update_username in data:
            User_label = Label(update_frame,text=update_username,font=("Goudy old style",15,"bold")).place(x=0,y=0,width=800)

        #logout
            self.logout =PhotoImage(file="image/logout.png")

            logout =Button(User_label,image=self.logout,text="Add Student",command=self.logout_function,bd=0).place(x=730,y=0,height=30,width=60)
            
            conn = sqlite3.connect('db/lecturer_db.db')
            with conn:
                cursor=conn.cursor()
                cursor.execute('SELECT * FROM Lecturer WHERE username=?',(update_username,))
                row = cursor.fetchall()
                print(row)

                
                #username 

                username_label = Label(update_frame,text="Username",font=("Goudy old style",15,"bold"),fg="white",bg="black").place(x=60,y=140)

                username_btn = Entry(update_frame,font=("times new roman",15),bg="lightgray",textvariable=self.username)
                username_btn.place(x=60,y=170,height=35,width=165)

            #password
                password_label= Label(update_frame,text="password",font=("Goudy old style",15,"bold"),fg="white",bg="black").place(x=240,y=140)

                password_btn = Entry(update_frame,font=("times new roman",15),bg="lightgray",textvariable=self.password)
                password_btn.place(x=240,y=170,height=35,width=165)

            
                confirm_pass_label = Label(update_frame,text="Confirm password",font=("Goudy old style",15,"bold"),fg="white",bg="black").place(x=55,y=220)

                confirm_pass_btn = Entry(update_frame,font=("times new roman",15),bg="lightgray",textvariable=self.confirm_pass)
                confirm_pass_btn.place(x=60,y=250,height=35,width=345)

            
                email_label =Label(update_frame,text="Email",font=("Goudy old style",15,"bold"),fg="white",bg="black").place(x=60,y=300) 

                email_btn=Entry(update_frame,textvariable=self.email,font=("times new roman",15),bg="lightgray")
                email_btn.place(x=60,y=330,width=345)
                

                register_btn = Button(self.root,command=self.update,text="Update",font=("Goudy old style",20,"bold"),bg="white",fg="black",bd=0).place(x=210,y=430,height=35,width=150)

                cancel_register = Button(self.root,text="Cancel",command=self.cancel,font=("Goudy old style",20,"bold"),bg="white",fg="black",bd=0).place(x=410,y=430,height=35,width=150)



                for i in row:
                    username_btn.insert(0,i[0])
                    password_btn.insert(0,i[1])
                    confirm_pass_btn.insert(0,i[2])
                    email_btn.insert(0,i[3])

        
    def update(self): 
        conn = sqlite3.connect('db/lecturer_db.db')
        with conn:
            cursor=conn.cursor()
            cursor.execute("""UPDATE Lecturer SET
            password=:password, 
            confirm_pass=:confirm_pass,
            email=:email
            WHERE username=:username""",
              {
                  'username':username_btn.get(),
                  'password':password_btn.get(),
                  'confirm_pass':confirm_pass_btn.get(),
                  'email':email_btn.get() 
              })
            row = cursor.fetchall()
            print(row)
            conn.commit()
            messagebox.showinfo("Success","Account updated successfully")
            ds.Dashboard(self.root)
            
            
            #conn.close()


    
                                    
    def cancel(self):
        msg = messagebox.askquestion("Exist Application","Are you sure you want to exist",icon="warning")
        if msg=="yes":        
            ds.Dashboard(self.root)

    def logout_function(self):
        Msg=messagebox.askquestion('Exist Application','Are you sure you want to exist this application',icon="info")
        if Msg == "yes":
            login.Login(self.root)

     

       


if __name__ == "__main__":
   root = team(theme="black")
   obj = Profile(root)
   root.mainloop()

#root.eval('tk::PlaceWindow . center')
