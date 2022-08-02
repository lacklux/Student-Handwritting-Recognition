from tkinter import *
from tkinter import ttk,messagebox,filedialog
from distutils.dir_util import copy_tree
from PIL import ImageTk,Image
from ttkthemes import ThemedTk as team
import sys
import sqlite3
import login
import dashboard as ds
import json
import os
import shutil
from shutil import copyfile,copy2,copy,move
from handwritting import Train_Dataset
import dashboard



class Check_writting():

    def __init__(self,root):
        self.root = root
        self.root.title("Check writting")
        self.root.geometry("800x500+300+45")
        self.root.configure(background="black")
        self.root.resizable(False,False)
        
        self.matric_num = StringVar()
        global train_dataset
        
        

        #frame
        dashboard_frame = ttk.Frame(self.root)
        dashboard_frame.place(x=0,y=0,height=660,width=1000)
        data = open('db/lecturer.txt','r')
        for i in data:
            User_label = Label(dashboard_frame,text=i,font=("Goudy old style",15,"bold")).place(x=0,y=0,width=800)
        #logout
        self.logout =PhotoImage(file="image/logout.png")

        logout =Button(User_label,image=self.logout,command=self.logout_function,bd=0).place(x=730,y=0,height=30,width=60)

        
        
        #frame
        Frame_login = Frame(dashboard_frame,bg="black")
        Frame_login.place(x=150,y=50,height=400,width=460)
        title = Label(Frame_login,text="Add Writting",font=("Impact",20,"bold"),fg="white",bg="black").place(x=170,y=10)
      
       

        self.matric =Button(Frame_login,font=("times new roman",15),bg="lightgray",textvariable=self.matric_num)
        self.matric.place(x=140,y=60,height=200,width=200)

        new_folder = Button(Frame_login,text="Add file",font=("Goudy old style",15,"bold"),fg="white",bg="black",command=self.Add_folder).place(x=110,y=270,width=250)

        Check_writting_btn = Button(Frame_login,text="Check writting",font=("Goudy old style",15,"bold"),fg="white",bg="black",command=self.check_handwritting_function).place(x=110,y=315,width=250)



        cancel_testeditor = Button(self.root,text="Exit",command=self.cancel,font=("Goudy old style",20,"bold"),bg="white",fg="black",bd=0).place(x=260,y=420,height=35,width=250)




    def Add_folder(self):
        global photo
        global filename
        filename = filedialog.askopenfilename()
        load_image = Image.open(filename)
        load_image.save('image/check_writting.png')
        photo=PhotoImage(file="image/check_writting.png")

        self.matric.configure(image=photo)
    
    def check_handwritting_function(self):
        Train_Dataset.check_handwritting(self,filename)
        Train_Dataset.database(self)
         
    def cancel(self):
        dashboard.Dashboard(self.root)

    def logout_function(self):
        Msg=messagebox.askquestion('Exist Application','Are you sure you want to exist this app',icon="info")
        if Msg == "yes":
            login.Login(self.root)

    

     
       


if __name__ == "__main__":
   root = team(theme="black")
   obj = Check_writting(root)
   root.mainloop()
