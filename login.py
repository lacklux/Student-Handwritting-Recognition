import sqlite3
import sys
import tkinter as tkinter
from tkinter import *
from tkinter import messagebox, ttk
# from dashboard import *
# import dashboard
import json
import register
from PIL import Image, ImageTk
from ttkthemes import ThemedTk as team


class Login:

    def __init__(self,root):
        self.root = root
        root.title("Login")
        self.root.geometry("800x550+300+50")
        self.root.configure(background="black")
        self.root.resizable(False,False)
        
        #background image
        self.bg =PhotoImage(file="image/bg.png")
        self.bg_image = ttk.Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        self.username = StringVar()
        self.password = StringVar()

        #frame
        Frame_login = Frame(self.root,bg="black")
        Frame_login.place(x=150,y=100,height=340,width=420)

        #Title
        title = Label(Frame_login,text="Login here",font=("Impact",35,"bold"),fg="white",bg="black").place(x=90,y=30)
       
        #username 

        Username = Label(Frame_login,text="Username",font=("Goudy old style",15,"bold"),fg="gray",bg="black").place(x=30,y=140)

        self.txt_user = Entry(Frame_login,font=("times new roman",15),bg="lightgray",textvariable=self.username).place(x=30,y=170,height=35,width=350)

        #password
        password = Label(Frame_login,text="Password",font=("Goudy old style",15,"bold"),fg="gray",bg="black").place(x=30,y=210)

        self.txt_pass = Entry(Frame_login,font=("times new roman",15),show="*+",bg="lightgray",textvariable=self.password).place(x=30,y=240,height=35,width=350)

        create_account = Button(Frame_login,text="Create Account",font=("Goudy old style",12,"bold"),fg="#d77337",bg="black",bd=0,command=self.create_acc).place(x=225,y=280)

        forget_password = Button(Frame_login,text="forgot password?",font=("Goudy old style",12,"bold"),fg="#d77337",bg="black",bd=0,command=self.forget_pass).place(x=30,y=280)


        login_btn = Button(self.root,text="Login",font=("Goudy old style",20,"bold"),bg="white",fg="black",bd=0,command=self.login_function).place(x=180,y=420,height=35,width=150)

        cancel_login = Button(self.root,text="Cancel",font=("Goudy old style",20,"bold"),bg="white",fg="black",bd=0,command=self.cancel).place(x=380,y=420,height=35,width=150)




    def login_function(self):
        if self.username.get() =="" or self.password.get()=="":
            messagebox.showinfo("Error","All field are required")

        else:
            conn = sqlite3.connect('db/lecturer_db.db')
            with conn:
                cursor=conn.cursor()
                find_user = ('SELECT * FROM Lecturer WHERE username =? and password=?')
                cursor.execute(find_user,[(self.username.get()),(self.password.get())])
                row = cursor.fetchall()
                
                if row:
                    print(row)
                    write_username =str( self.username.get())
                    with open('db/lecturer.txt','+w') as textfile:
                        textfile.write( write_username)
                
                    # dashboard.Dashboard(self.root)
                
                else:
                    messagebox.showerror("Error",'Invalid login details',icon="error")


                        
   
    def create_acc(self):
        register.Register(self.root)
   
    def cancel(self):
        sys.exit(0)

    def forget_pass(self):
        global editor
        global email      
        editor = team(theme="black")
        editor.title("Forgot Pass")
        editor.geometry("800x500+200+100")
            
        editor.resizable(False,False)
        editor_frame = ttk.Frame(editor)
        editor_frame.place(x=0,y=0,height=640,width=1000)
        
            #frame
        update_frame = Frame(editor_frame,bg="black")
        update_frame.place(x=150,y=100,height=250,width=460)
        update_title = Label(update_frame,text="Forget Pass",font=("Impact",29,"bold"),fg="white",bg="black").place(x=70,y=30)
        
        #username 

        mail = Label(update_frame,text="Email",font=("Goudy old style",15,"bold"),fg="white",bg="black").place(x=60,y=100)

        email = Entry(update_frame,font=("times new roman",15),bg="lightgray")
        email.place(x=60,y=150,height=35,width=320)

        #password
            
        submit = Button(editor,command=self.GetDetails,text="Submit",font=("Goudy old style",20,"bold"),bg="white",fg="black",bd=0).place(x=250,y=330,height=35,width=250)

        # cancel_submit = Button(editor,text="Cancel",command=self.cancel,font=("Goudy old style",20,"bold"),bg="white",fg="black",bd=0).place(x=380,y=320,height=35,width=150)


    def GetDetails(self):
        conn = sqlite3.connect('db/lecturer_db.db')
        with conn:
            cursor=conn.cursor()
            cursor.execute('SELECT * FROM Lecturer WHERE email=?',(email.get(),))
            row = cursor.fetchall()
            if row:
                username_and_pass = 'Username :{} and Password:{}'.format(row[0][0],row[0][1])
                messagebox.showinfo('Success',username_and_pass,icon="info")
            else:
                no_record = 'No Record found for {}'.format(email.get())
                messagebox.showerror('Error', no_record,icon="error")








if __name__ == "__main__":
   root = team(theme="black")
   obj = Login(root)
   root.mainloop()
