# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 02:06:49 2020

@author: harshit
"""
'''import cv2
import numpy as np
cap=cv2.VideoCapture(0)
read_img=cv2.imread("capturebackground.png")
while cap.isOpened():
    ret,frame=cap.read()
    if ret:
        hsv_img=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        #cv2.imshow("hsvimage",hsv_img)
        red=np.uint8([[[0,0,255]]])
        hsv_red=cv2.cvtColor(red,cv2.COLOR_BGR2HSV)
        l_red=np.array([0,100,100])
        u_red=np.array([10,255,255])
        mask=cv2.inRange(hsv_img,l_red,u_red)
        cv2.imshow("mask",mask)
        if (cv2.waitKey(10) & 0xFF) == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()'''
import cv2
import numpy as np
import time
time.sleep(3)
cap=cv2.VideoCapture(0)
for i in range(30):
    #capturing the background over the 30 iterations so that the webcam can adjust itself with the environmet and can capture a smooth image of the background
    ret,read_img=cap.read() 
while cap.isOpened():
    ret,frame=cap.read()
    if ret:
        '''converting frame to hue saturated value which is used in image cropping
        here hue means colour,saturation means how much the color is mixed with white colour,
        value means how much the image is mixed with black colour.the hsv is more readable to
        the human eyes as rgb consists of a combination of colours but hsv consisits of the
        combination of colours along with this it also takes into account the intensity of the
        light.it considers luminoscity in the image which means the intensity of light how 
        much is falling into an object.so we will use the hsv value and convert bgr to hsv'''
        #converting to the hsv
        hsv_img=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        #displaying the hsv image
        #cv2.imshow("hsv",hsv_img)
        if (cv2.waitKey(250) & 0xFF)==ord('q'):
            break
        #taking the hsv value of the pixels corresponding to only the read colour
        red=np.uint8([[[0,0,255]]])
        red_hsv=cv2.cvtColor(red,cv2.COLOR_BGR2HSV)
        #threshold for the hsv in lower is [h-10,100,100] and in higher is [h+10,255,255]
        l_red=np.array([0,120,70]) #defining the lower threshold for red colour because using the red cloak
        u_red=np.array([10,255,255]) #defining the upper threshold for red colour because using the red cloak
        #taking all colors which falls only in this threshold and ignoring all the other pixels of colours which are not in this threshold
        mask=cv2.inRange(hsv_img,l_red,u_red)
        #displays only red part of the image and highlights only that part of the frame
        #cv2.imshow("mask",mask)
        #performing bitwise and so that the red portion which is hiding background selected by mask gets replaced by the previously saved captured image
        mask=cv2.morphologyEx(mask,cv2.MORPH_OPEN,np.ones((3,3),np.uint8),iterations=2)
        mask=cv2.morphologyEx(mask,cv2.MORPH_DILATE,np.ones((3,3),np.uint8),iterations=1)
        #capturing everything except red
        mask1=cv2.bitwise_not(mask)
        res1=cv2.bitwise_and(read_img,read_img,mask=mask)
        res2=cv2.bitwise_and(frame,frame,mask=mask1)
        finres=cv2.addWeighted(res1,1,res2,1,0)
        cv2.imshow("invisible cloak",finres)
        #replacing everything except the red with the real time frame i am capturing
        #combining the part1 and part2 to display the feature of the real-time frame capturing and replacing the red part with my captured background image
        
   
cap.release()
cv2.destroyAllWindows()

        