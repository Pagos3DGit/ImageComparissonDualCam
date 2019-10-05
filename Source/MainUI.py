import tkinter as tk
from tkinter import *


master = Tk()

def callback():
    print ("click!")
    
    

class App(tk.Frame):
   frame = Frame(width=768, height=576, bg="", colormap="new")
   frame.pack()
   b = Button(master, text="OK", command=callback)
   b.pack()

   

# create the application
myapp = App()

#
# here are method calls to the window manager class
#

myapp.master.title("My Do-Nothing Application")
#myapp.master.size(1000, 400)

# start the program
myapp.mainloop()