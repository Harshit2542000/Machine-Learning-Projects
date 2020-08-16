# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 05:45:50 2020

@author: harshit
"""
import os
import cv2
import numpy as np
from PIL import Image
import pickle
y_label=[]
x_train=[]
#variable to assign id's to each labels
current_id=0
#dictionary for storing the ids with label names with their id's
label_ids={}
#haarcascadeclassifierobject
classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#it will give the Face Reconizer object which helps in recognizing each image face when we will train it
recognizer=cv2.face.LBPHFaceRecognizer_create()
#taking the base directory of our working file
BASE_DIRNAME=os.path.dirname(os.path.abspath(__file__))
#joining the base directory  with the image in order to grab the images folder
img_walk=os.path.join(BASE_DIRNAME,"images")
#traversing through the different folders inside image and in each folder of image taking its total path
for root,dirs,files in os.walk(img_walk):
    for file in files:
        if(file.endswith("jpg") or file.endswith("png")):
            #complete path of the image 
            path=os.path.join(root,file)
            #the folder in which the image of a particular person is inside
            label=os.path.basename(root).replace(" ","-").lower()
            #if the label does not exist in the dictionary then add that new label as a key
            if not label in label_ids:
                label_ids[label]=current_id
                current_id+=1
            #for each image its id to which it belongs
            id_=label_ids[label]
            print(label_ids)
            #opening each image
            img_train=Image.open(path).convert("L") #here "L" means grayscale(black and white image)
            '''size=(550,550)
            resized_img_train=img_train.resize(size,Image.ANTIALIAS)'''
            #converting it into numbers of pixels using numpy array in order to train the machine learning model with images
            training=np.array(img_train,"uint8")
            #getting rectangle coordinate for image
            rect_train=classifier.detectMultiScale(training,scaleFactor=1.5,minNeighbors=5)
            for(x,y,w,h) in rect_train:
                #scrapping region of face from each image
                roi_train=training[y:y+h,x:x+w]
                x_train.append(roi_train)
                print(roi_train)
                #appending the ids for each image to a list
                y_label.append(id_)
#writing the dictionary consisting of label and their ids into the binary pickle file so that it remembers those labels with their ids onto a dictionary
with open("labels.pickle","wb") as f:
    pickle.dump(label_ids,f)
#converting y_label into a numpy array as for learning of machine model should be numpy
#training the recognizer object on each of the image for recognizing the face
recognizer.train(x_train,np.array(y_label))
#saving all the trained data into a y ain't markup language
recognizer.save("labelstrained.yml")