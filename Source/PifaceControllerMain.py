#########piface controller script

##Required modules
import pifacedigitalio
import imutils
import cv2
import sys
import numpy as np
import os
import tkinter as tk

###my other scripts




LD_PRELOAD="/usr/lib/libv4l/v4l1compat.so"
###GLOBAL VARIABLES HERE

cap = cv2.VideoCapture(0)
pifacedigital = pifacedigitalio.PiFaceDigital()




def switch_pressed(event):
    
    
    ##Declare variables here
    event.chip.output_pins[event.pin_num].turn_on()

    
    #############################ADD SWITCH FUNCTIONS HERE ######################
    
    if event.pin_num == 0 :
    
        takePic()
        print(event.pin_num)
        
        #capture image via button
    elif event.pin_num == 1 :
        
        print(event.pin_num)
    

        
        

    
def switch_unpressed(event):
    event.chip.output_pins[event.pin_num].turn_off()
    
  

    
        
def takePic():
    expImg = 0
    while(True):
        ret,frame = cap.read()
        
        
        if expImg <= 9:
            img_name = "images/exportLib/{}.png".format(expImg)
            cv2.imwrite(img_name, frame)
            expImg += 1
            break
        elif expImg >9:
            expImg = 0
            os.remove("images/exportLib/{}.png".format(expImg))
            img_name = "images/exportLib/{}.png".format(expImg)
            cv2.imwrite(img_name, frame)
            expImg += 1
            break
    print("{} written!".format(expImg))
        

    
class mainView():
    
    
    
    if __name__ == "__main__":
        listener = pifacedigitalio.InputEventListener(chip=pifacedigital)
        for i in range(4):
            listener.register(i, pifacedigitalio.IODIR_ON, switch_pressed)
            listener.register(i, pifacedigitalio.IODIR_OFF, switch_unpressed)
        listener.activate()
        print("running...")
        
    
   
    while(True):
        
        
        ret,frame = cap.read()
        cv2.imshow('My Do-Nothing Application',frame)
        
        if cv2.waitKey(20) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            listener.deactivate()
            break
    
    

        
    
mainView()     
    

cap.release()
cv2.destroyAllWindows()
#listener.deactivate()

