# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 00:28:42 2020

@author: harshit
"""

'''mport cv2
cap=cv2.VideoCapture(0)#capturing my video from a source  that is webcam here
while cap.isOpened:
    ret,frame=cap.read()#reading the frames from the webcam
    if ret:
        cv2.imshow("frames",frame)#showing the frames
        #waits for 10 milliseconds to capture a frame and in between capturing a frame if a key q is pressed it will exit from the loop
        if (cv2.waitKey(10) & 0xFF)==ord('q'):
            image="capturebackgound.jpg"
            cv2.imwrite(image,frame)#saving the background image to the image variable
            break
cap.release()
cv2.destroyAllWindows()'''
import cv2
cap=cv2.VideoCapture(0)#capturing my video from a source  that is webcam here
while cap.isOpened():
    ret,frame=cap.read()#reading the frames from the webcam
    if ret:
        cv2.imshow("frames",frame)#showing the frames
        #waits for 10 milliseconds to capture a frame and in between capturing a frame if a key q is pressed it will exit from the loop
        if (cv2.waitKey(10) & 0xFF)==ord('q'):
            image="capturebackground.png"
            cv2.imwrite(image,frame)#saving the background image to the image variable
            break
cap.release()#release all the frames and making webcam off
cv2.destroyAllWindows()#closes all frame windows