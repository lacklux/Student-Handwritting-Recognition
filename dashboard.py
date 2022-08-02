import ast
import json
import os
import re
import random
import sys
import time
import sqlite3
from datetime import date
from turtle import bgcolor, width
import requests
from tkinter import ttk
from tkinter import messagebox, ttk
import tkinter as tk
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait
# import undetected_chromedriver.v2 as uc
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class Bot:
    def __init__(self):
        self.option = Options()
        self.option.add_argument("--incognito")
        # self.option.add_argument('--headless')
        self.option.add_argument("--no-sandbox")
        self.option.add_argument("--disable-dev-shm-usage")
        self.option.add_argument("--disable-notifications")
        self.option.add_argument('--disable-blink-features=AutomationControlled')
        self.option.add_argument("--window-size=1280,800")
        self.option.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")
        self.visual()

    def visual(self):
        global user
        window = tk.Tk()
        window.geometry("800x650+300+50")
        window.resizable(False,False)
        window.configure(background="black")
        
        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 13),background="black",foreground="white",padding=10) # Modify the font of the body
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 13,'bold')) # Modify the font of the headings
        # style.map('mystyle.Treeview', background="white")
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders
        self.tv = ttk.Treeview(window,selectmode ='extended',height=20,style="mystyle.Treeview")
        self.tv['columns']=('SN','Users','url', 'start', 'stop')
        self.tv.column('#0', width=0, stretch="NO")
        self.tv.column('SN', anchor="center", width=50)
        self.tv.column('Users', anchor="center", width=140)
        self.tv.column('url', anchor="center", width=400)
        self.tv.column('start', anchor="center", width=100)
        self.tv.column('stop', anchor="center", width=100)


        self.tv.heading('#0', text='', anchor="center")
        self.tv.heading('SN', text='sn', anchor="center")
        self.tv.heading('Users', text='Users', anchor="center")
        self.tv.heading('url', text='url', anchor="center")
        self.tv.heading('start', text='start', anchor="center")
        self.tv.heading('stop', text='stop', anchor="center")
        # self.tv.heading('stop', text='Share', anchor="center")
        scroll = tk.Scrollbar(window,orient=tk.VERTICAL,bg="black")
        scroll.pack(side=tk.RIGHT,fill=tk.Y)
        self.tv.config(yscrollcommand=scroll.set)
        scroll.config(command=self.tv.yview)
        # datas = self.search_videos
        # print(self.search_videos)
        # print(datas)
        self.tv.place(x=0,y=1)    
        data = self.database()
        count = 0
        y_axis = 30 
        for row in data:         
            row = list(row) 
            
            self.tv.insert(parent='', index=count, iid=count, text='', values=(f'{count}',f'{row[0]}',f'{row[1]}',
            f'{tk.Button(window,text=">",font=("Goudy old style",12,"bold"),fg="white",bg="black",bd=0,command="",width=4,height=1).place(x=550,y=y_axis)}',
            f'{tk.Button(window,text="x",font=("Goudy old style",12,"bold"),fg="white",bg="black",bd=0,command="").place(x=630,y=y_axis)}'))
            count+=1
            y_axis+=30
        window.mainloop()
        
        
    def database(self):
        conn = sqlite3.connect('db/Users.sqlite3')
        with conn:
            cursor=conn.cursor()
            # if self.url.get() != self.confirm_pass.get():
            #     messagebox.showinfo("Error","url not matched")

            # else:
            cursor.execute('CREATE TABLE IF NOT EXISTS Users (username TEXT,urls TEXT)')
            cursor.execute('SELECT * FROM Users')
            row = cursor.fetchall()
            # check_user = self.username.get()
            list_row = []
            for i in row:
                list_row.append(i) 
            return list_row
    
if __name__ =="__main__":
    Bot()
    
