# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 03:41:24 2020

@author: harshit
"""
'''print(help('cv2'))'''

import cv2
import pickle
#harecascadeclassifieralgorithm
classifier=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_classifier=cv2.CascadeClassifier('haarcascade_eye.xml')
'''smile_classifier=cv2.CascadeClassifier('haarcascade_smile.xml')'''
#creating a recognizer object and reading the trained data of the images and putting it into my recognizer object in this python file
recognizer=cv2.face.LBPHFaceRecognizer_create()
recognizer.read("labelstrained.yml")
og_label={}
rev_label={}
#loading the dictionary of labels from the file and then reversing its key value pair because we want id as a key and label name as its value
with open("labels.pickle","rb") as f:
    og_label=pickle.load(f)
    rev_label={v:k for k,v in og_label.items()}
#capturing the live video with webcam
cap=cv2.VideoCapture(0)
while(True):
    #taking each frame
    ret,frame=cap.read()
    #converting the image to greyscale(black and white)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=classifier.detectMultiScale(gray,scaleFactor=1.5,minNeighbors=5)
    for (x,y,w,h) in faces:
        #region of interest of frames
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=frame[y:y+h,x:x+w]
        duplicate="myimage.png"
        cv2.imwrite(duplicate,roi_gray)
        #capturing face in a rectangle 
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        #predicting based on my frame in my region of the interest and returning the id label for trained image and the confidence level
        #as the confidence level inreases the less the image is recognized and less confidence level means that more the image is recognized
        id_,conf=recognizer.predict(roi_gray)
        if (conf>=45 and conf<=85):
            #displaying the predicted id and the label name of the person
            font=cv2.FONT_HERSHEY_SIMPLEX
            name=rev_label[id_]
            color=(255,255,255)
            stroke=2
            cv2.putText(frame,name,(x,y),font,1,color,stroke,cv2.LINE_AA)
    eyes=eye_classifier.detectMultiScale(gray)
    for(ex,ey,ew,eh) in eyes:
        roi_eyes=frame[ey:ey+eh,ex:ex+ew]
        cv2.rectangle(frame,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    '''smiles=smile_classifier.detectMultiScale(gray)
    for(sx,sy,sw,sh) in smiles:
        roi_smile=frame[sy:sy+sh,sx:sx+sw]
        cv2.rectangle(frame,(sx,sy),(sx+sw,sy+sh),(0,0,255),2)'''
    #displaying the frames
    cv2.imshow("frame",frame)
    if((cv2.waitKey(250) & 0xFF)==ord('q')):
        break
cap.release()
cv2.destroyAllWindows()
