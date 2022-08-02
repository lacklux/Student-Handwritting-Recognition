
# coding: utf-8
#import cv2
#import seaborn
#import pillow
import os
from tensorflow import keras
import pickle
import requests
import sqlite3
import matplotlib
import numpy as np
import pandas as pd
import tensorflow as tf
from tkinter import *
from tkinter import ttk,messagebox
from ttkthemes import ThemedTk as team
from tensorflow.keras.models import Sequential
from matplotlib import pyplot as plt
from tensorflow.keras.preprocessing import image
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import Dense,Dropout,Activation,Flatten,Conv2D,MaxPooling2D

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

#global count
class Train_Dataset:
    
    def __init__(self):
        
        train = ImageDataGenerator(rescale=1./255)
        validation = ImageDataGenerator(rescale=1./255)
        train_dataset = train.flow_from_directory("Dataset/",target_size=(200,200),batch_size=15,class_mode='categorical')
        validation_dataset = train.flow_from_directory("validation/",target_size=(200,200),batch_size=15,class_mode='categorical')

        print(train_dataset.class_indices)
        count = []
        count_label = 0
        for i in train_dataset.class_indices:
            count.append(i)
            count_label+=1
        print(count)
        print(train_dataset.class_indices)
        #print(reverse_data[::-1])
        reverse_data = count[::-1]


    
     
    def modelling(self): 
        global train_dataset 
        train = ImageDataGenerator(rescale=1./255)
        validation = ImageDataGenerator(rescale=1./255)
        train_dataset = train.flow_from_directory("Dataset/",target_size=(200,200),batch_size=15,class_mode='categorical')
        validation_dataset = train.flow_from_directory("validation/",target_size=(200,200),batch_size=15,class_mode='categorical')

        print(train_dataset.class_indices,"normal train label")
        
        label =train_dataset.class_indices 
        re_arrange_dict = sorted(label.items(),key=lambda x:x[1])
        print(re_arrange_dict,"re arrange")
        print(dict(re_arrange_dict),"dictionary")
        count_label = 0
        for i in re_arrange_dict:
            count_label+=1
    
        model = Sequential([Conv2D(32,(3,3),activation="relu",padding="same", input_shape=(200,200,3)),
            MaxPooling2D(2,2),
                            
                            #another layer
            Conv2D(32,(3,3),activation="relu",padding="same"),
            MaxPooling2D(2,2),
                            
                            
                            #another layer
            Conv2D(64,(3,3),activation="relu",padding="same"),
            MaxPooling2D(2,2),
                            #another layer
                                        
                            
                #flatten the model
            Flatten(),
            Dense(128,activation="relu"),
            Dropout(0.5),
            Dense(count_label,activation="softmax")
                        
                        ])
        #RMSprop(learning_rate=0.001)
 
        model.compile(loss="categorical_crossentropy",optimizer=RMSprop(learning_rate=0.001),metrics = ["accuracy"])

        # model.summary()
        print(model.summary())

        model_fit = model.fit(train_dataset,steps_per_epoch=10,epochs=30,validation_data=validation_dataset)

        # print(model_fit)

        model.save('model/handwritting.h5')
    
        messagebox.showinfo('info','Handwritting Trained Succesfully',icon='info')



    def check_handwritting(self,filename):
        global actual_handwritting_result
        dir_path = filename
        img = image.load_img(dir_path,target_size=(200, 200))
        plt.imshow(img)
        plt.show()
        img = image.img_to_array(img)
        img = np.expand_dims(img,axis=0)
        img= np.vstack([img])
        model = keras.models.load_model('model/handwritting.h5')
        model.compile(loss="categorical_crossentropy",optimizer='rmsprop',metrics = ["accuracy"])
        result = model.predict(img)
        # classes = model.predict_classes(img,batch_size=10)
        # print("classes",classes)
        print("results",result)
        print("list result",result[0])
        n_result = result[0]
       
        predict_position = [pos for pos,x in enumerate(n_result) if x==1]
        predict_position_list = predict_position[0]
        print('prediction pos',predict_position)
        train = ImageDataGenerator(rescale=1./255)
        train_dataset = train.flow_from_directory("Dataset/",target_size=(200,200),batch_size=20,class_mode='categorical')
        
        label =train_dataset.class_indices
        list_label = list(label)
        print('list label',list_label)
        count = 0
        app_count =[]
        label_count = []
        for i in label:
            count+=1
            if label[i]==predict_position_list:
                app_count.append(count-1)
                label_count.append(i)
                print(count)

        print('real count for dict',app_count)
        print('real count for label',label_count)
        
        actual_handwritting_result = label_count[0]
        print("actual writting",actual_handwritting_result)
        print(type(actual_handwritting_result))


    def database(self):
        global editor
        global fname
        global lname
        global mat
        
        
        conn = sqlite3.connect('db/student_db.db')
        with conn:
            cursor=conn.cursor()
            try:
                cursor.execute("SELECT * FROM Student WHERE matric=?",(actual_handwritting_result,))
                row = cursor.fetchall()
                print(row)

                
                
                editor = team(theme="black")
                editor.title("Update")
                editor.geometry("800x500+200+60")
                
                editor.resizable(False,False)
                editor_frame = ttk.Frame(editor)
                editor_frame.place(x=0,y=0,height=640,width=1000)
            
                #frame
                
            
        
                if row:
                    update_frame = Frame(editor_frame,bg="black")
                    update_frame.place(x=150,y=30,height=420,width=460)
                    update_title = Label(update_frame,text="Result Found",font=("Impact",29,"bold"),fg="white",bg="black").place(x=110,y=60)

                    fname = Entry(update_frame,font=("times new roman",15),bg="lightgray")
                    fname.place(x=60,y=170,height=35,width=165)

                    lname =Entry(update_frame,font=("times new roman",15),bg="lightgray")
                    lname.place(x=240,y=170,height=35,width=165)


                    mat = Entry(update_frame,font=("times new roman",15),bg="lightgray")
                    mat.place(x=60,y=250,height=35,width=345) 

                
                    # cancel_register = Button(editor,text="Cancel",command=self.cancel,font=("Goudy old style",20,"bold"),bg="white",fg="black",bd=0).place(x=270,y=430,height=35,width=220)



                    for i in row:
                        fname.insert(0,i[0])
                        lname.insert(0,i[1])
                        mat.insert(0,i[2])
                        
                
                else:
                    update_frame = Frame(editor_frame,bg="black")
                    update_frame.place(x=150,y=70,height=350,width=460)
                    
                    update_title = Label(update_frame,text="Result Found",font=("Impact",29,"bold"),fg="white",bg="black").place(x=100,y=30)
                    update_title = Label(update_frame,text="No record Found",font=("Impact",20,"bold"),fg="white",bg="black").place(x=120,y=180)
            except Exception as e:
                print('causes of exception',e)
                editor = team(theme="black")
                editor.title("Update")
                editor.geometry("800x500+200+60")
                
                editor.resizable(False,False)
                editor_frame = ttk.Frame(editor)
                editor_frame.place(x=0,y=0,height=640,width=1000)
                update_frame = Frame(editor_frame,bg="black")
                update_frame.place(x=150,y=70,height=350,width=460)
                    
                update_title = Label(update_frame,text="Result Found",font=("Impact",29,"bold"),fg="white",bg="black").place(x=100,y=30)
                update_title = Label(update_frame,text="No record Found",font=("Impact",20,"bold"),fg="white",bg="black").place(x=120,y=180)
            
               
  