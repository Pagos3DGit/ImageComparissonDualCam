import numpy as np 
import cv2

import tkinter as tk
from tkinter import *


#testing image comparisson bs
import ImgComp

sh = ImgComp.testShow

cap = cv2.VideoCapture(0)
master = Tk()
#capture = cv.CaptureFromCAM(0)

#image_path = r'C:\Users\gkami\Documents\GitHub\ImageComparissonDualCam\test_files\Mocking-Spongebob.jpg'


def vidstream():

    while(True):
        # Capture frame-by-frame
        ret,frame = cap.read()
        

        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
        # Display the resulting frame
        cv2.imshow('My Do-Nothing Application',frame)
        #img = cv2.imshow('My Do-Nothing Application',frame)
        
        #cv2.imshow('gray',gray)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            #scrCapt()
            cv2.destroyWindow()
            break
            
        
    



class App(tk.Frame):
   frame = Frame(width=768, height=576, bg="", colormap="new")
   
   frame.pack()
   b = Button(master, text="OK", command=vidstream)
   b.pack()
   c = Button(master, text="OK", command=sh)
   c.pack()
  
    
    
   #vidstream().frame.pack()

myapp = App()
myapp.master.title("My Do-Nothing Application")

myapp.mainloop()
# When everything done, release the capture
cap.release()
cv2.destroyWindow()
