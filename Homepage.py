# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 15:34:17 2021

@author: Az Developer
"""

from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk,messagebox
from ttkthemes import ThemedTk as team
import sys
from login import Login



class HomePage:
    def __init__(self,root):
        self.root = root
        self.root.title("Homepage")
        self.root.geometry("850x500+300+50")
        self.root.configure(background="black")
        self.root.resizable(False,False)
        
        #background image
        self.bg =PhotoImage(file="image/bg.png")
        self.bg_image = ttk.Label(self.root,image=self.bg).place(x=0,y=0)

        self.start =PhotoImage(file="image/start.png")
        start_label = Label(self.root,text="Handwritting Recognition Software",font=("Goudy old style",25,"bold")).place(x=10,y=350,width=500,height=50)

        start_btn = Button(self.root,image=self.start,command=self.login_function,bg="gray",bd=0).place(x=20,y=410,width=140) 


    def login_function(self):
        Login(self.root)
        

if __name__ == "__main__":
   root = team(theme="black")
   obj = HomePage(root)
   root.mainloop()


