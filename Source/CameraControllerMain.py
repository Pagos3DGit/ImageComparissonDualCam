##delete the useless afterwards
from __future__ import print_function

import threading
import datetime
import imutils
import cv2
import os

import pifacedigitalio

import numpy as np


import tkinter as tk
from tkinter import *


import image_diff 
from image_diff import *


import sched, time




#testing image comparisson b


cap = cv2.VideoCapture(0)
master = Tk()

outpath = "images/exportLib/STD.png"
filename = "STD"



'''

def switch_pressed(event):
    event.chip.output_pins[event.pin_num].turn_on()
    
    #############################ADD SWITCH FUNCTIONS HERE ######################
    
    if event.pin_num == 0 :
        vidstream()
        print(event.pin_num)
    

    
def switch_unpressed(event):
    event.chip.output_pins[event.pin_num].turn_off()

if __name__ == "__main__":
    pifacedigital = pifacedigitalio.PiFaceDigital()

    listener = pifacedigitalio.InputEventListener(chip=pifacedigital)
    for i in range(4):
        listener.register(i, pifacedigitalio.IODIR_ON, switch_pressed)
        listener.register(i, pifacedigitalio.IODIR_OFF, switch_unpressed)
    listener.activate()
        '''
    
def imDiff():
    image_diff.compImg()
    

def vidstream():
    
    img_counter = 0
    while(True):
        # Capture frame-by-frame
        ret,frame = cap.read()
            

        # Our operations on the frame come here
            #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
         # Display the resulting frame
        cv2.imshow('My Do-Nothing Application',frame)
        #cv2.imshow('gray',gray)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
            
        elif cv2.waitKey(20) & 0xFF == ord('s'):
                ####SAVE IMAGE FUNCTION
            img_name = "images/exportLib/{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
           
            img_counter += 1
        elif cv2.waitKey(20) & 0xFF == ord('a'):
                ####SAVE IMAGE  FUNCTION
            img_name = "images/testLib/{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            #imageDiff().imageB = img_name
            img_counter += 1
            
        
    
                
                
            #####SAVE A PICTURE EVERY 2000 MILISECONDS
        #elif cv2.waitKey(2000):                #img_name = "images/exportLib/opencv_frame_{}.png".format(img_counter)
        #cv2.imwrite(img_name, frame)
        # print("{} written!".format(img_name))
        # img_counter += 1
          
    cap.release()
    cv2.destroyAllWindows()

        
    



class App(tk.Frame):
    
   frame = Frame(width=700, height=400, bg="black", colormap="new")
   
   frame.pack()
   
   ret,frame = cap.read()
   
   
   b = Button(master, text="OK", command=vidstream)
   b.pack()
   c = Button(master, text="not so OK", command=imDiff)
   c.pack()
   d = Button(master, text="compare images", command=imDiff)
   d.pack()
   
   #w = Label(frame, text = "test text (to become ssid text)")
   #w.pack()
   
   
  
    
    
   #vidstream().frame.pack()

myapp = App()
myapp.master.title("My Do-Nothing Application")

myapp.mainloop()
myapp.destroy()
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
