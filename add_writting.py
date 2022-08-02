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



class Add_writting():

    def __init__(self,root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("800x600+300+60")
        self.root.configure(background="black")
        self.root.resizable(False,False)
        self.folderPath = StringVar()
        self.matric_num = StringVar()
        global train_dataset
        

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
        Frame_login.place(x=150,y=80,height=400,width=460)
        title = Label(Frame_login,text="Add Writting",font=("Impact",29,"bold"),fg="white",bg="black").place(x=130,y=30)
      
        #username 
        #folder_selected = filedialog.askdirectory()

        matric_label = Label(Frame_login,text="Matric",font=("Goudy old style",15,"bold"),fg="white",bg="black").place(x=60,y=130)


        self.matric = Entry(Frame_login,font=("times new roman",15),bg="lightgray",textvariable=self.matric_num)
        self.matric.place(x=60,y=160,height=35,width=340)

        new_folder = Button(Frame_login,text="Add folder",font=("Goudy old style",15,"bold"),fg="white",bg="black",command=self.Add_folder).place(x=100,y=230,width=250)

        train_dataset = Button(Frame_login,text="Train Dataset",font=("Goudy old style",15,"bold"),fg="white",bg="black",command=self.train_dataset_model).place(x=100,y=280,width=250)


        # register_btn = Button(self.root,command="",text="Register",font=("Goudy old style",20,"bold"),bg="white",fg="black",bd=0).place(x=210,y=480,height=35,width=150)

        cancel_register = Button(self.root,text="Exit",command=self.cancel,font=("Goudy old style",20,"bold"),bg="white",fg="black",bd=0).place(x=250,y=460,height=35,width=250)




    def Add_folder(self):
        folder_selected = filedialog.askdirectory()
        self.folderPath.set(folder_selected)
        src_folder = self.folderPath.get()
        print("Doing stuff with folder", src_folder)
        destination_folder =os.path.join("Dataset/",self.matric.get())
        val_destination_folder = os.path.join("validation/",self.matric.get())
        if not os.path.exists(destination_folder) and not os.path.exists(val_destination_folder):
            os.mkdir(destination_folder) 
            os.mkdir(val_destination_folder)     

            for i in os.listdir(src_folder):
                if i.endswith(('.jpg','png','jpeg')):
                    copy((src_folder+"/"+i),destination_folder)
                    copy((src_folder+"/"+i),val_destination_folder)
                    print(i)
                #move((src_folder+"/"+i),destination_folder,copy_function=copy2)
            

    def train_dataset_model(self):
        Train_Dataset.modelling(self)

    def cancel(self):
        dashboard.Dashboard(self.root)

    def logout_function(self):
        Msg=messagebox.askquestion('Exist Application','Are you sure you want to exist this app',icon="info")
        if Msg == "yes":
            login.Login(self.root)

     
       


if __name__ == "__main__":
   root = team(theme="black")
   obj = Add_writting(root)
   root.mainloop()
