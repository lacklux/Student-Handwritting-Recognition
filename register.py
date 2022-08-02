import sqlite3
import sys

from tkinter import *
from tkinter import messagebox, ttk

import login
from PIL import Image, ImageTk
from ttkthemes import ThemedTk as team


class Register:

    def __init__(self,root):
        self.root = root
        self.root.title("Registration")
        self.root.geometry("800x600+300+40")
        self.root.configure(background="black")
        self.root.resizable(False,False)
        
        
        #background image
        self.bg =PhotoImage(file="image/bg.png")
        self.bg_image = ttk.Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        self.username = StringVar()
        self.url = StringVar()
        # self.confirm_pass = StringVar()
        # self.email = StringVar()

        #frame
        Frame_login = Frame(self.root,bg="gray")
        Frame_login.place(x=150,y=100,height=340,width=500)

        #Title
        title = Label(Frame_login,text="Add New User",font=("Impact",29,"bold"),fg="white",bg="gray").place(x=70,y=30)
        # title = Label(Frame_login,text="Login here",font=("Goudy old style",15,"bold"),fg="#d77337",bg="white").place(x=90,y=100)

        #username 

        Username = Label(Frame_login,text="Username",font=("Goudy old style",15,"bold"),fg="black",bg="gray").place(x=90,y=140)

        self.txt_user = Entry(Frame_login,font=("times new roman",15),bg="lightgray",textvariable=self.username).place(x=90,y=170,height=35,width=350)

        # url
        url = Label(Frame_login,text="Url",font=("Goudy old style",15,"bold"),fg="black",bg="gray").place(x=90,y=210)

        self.txt_url = Entry(Frame_login,font=("times new roman",15),bg="lightgray",textvariable=self.url).place(x=90,y=240,height=35,width=350)

     
        register_btn = Button(self.root,text="Register",font=("Goudy old style",20,"bold"),bg="white",fg="black",bd=0,command=self.database).place(x=240,y=400,height=35,width=150)

        cancel_register = Button(self.root,text="Cancel",font=("Goudy old style",20,"bold"),bg="white",fg="black",bd=0,command=self.cancel_reg).place(x=440,y=400,height=35,width=150)


    

    def cancel_reg(self):     
        self.cancel_register = login.Login(self.root)
       

    def database(self):
        if self.username.get() =="" or self.url.get()=="":
            messagebox.showinfo("Error","All field are required")
        else:
            conn = sqlite3.connect('db/Users.sqlite3')
            with conn:
                cursor=conn.cursor()
                # if self.url.get() != self.confirm_pass.get():
                #     messagebox.showinfo("Error","url not matched")

                # else:
                cursor.execute('CREATE TABLE IF NOT EXISTS Users (username TEXT,urls TEXT)')
                cursor.execute('SELECT * FROM Users')
                row = cursor.fetchall()
                check_user = self.username.get()
                list_row = []
                for i in row:
                    list_row.append(i[0])                  

                if check_user in list_row:
                    messagebox.showwarning("Error","Username Already Exist")
                    pass        
                    
                else:
                    cursor.execute('INSERT INTO Users (username,urls) VALUES(?,?)',(self.username.get(),self.url.get()))
                    conn.commit()
                    messagebox.showinfo("Success","Account Created")
                            
                    self.cancel_reg()
                        
                                
                        
        
        






if __name__ == "__main__":
   root = team(theme="black")
   obj = Register(root)
   root.mainloop()
