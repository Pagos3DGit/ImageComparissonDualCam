from tkinter import *


import numpy as np 
import cv2
cap = cv2.VideoCapture(0)

window = Tk()
window.title("HaraKiri")

# this is the window width/height
window.geometry('600x350')
cv2.imshow('window ', window(cap.read()) )

lbl = Label(window, text = "HaraKiri")


lbl.grid(column = 0, row =0)
window.mainloop()