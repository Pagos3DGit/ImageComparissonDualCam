import tkinter as tk
from tkinter import *

from tkinter import messagebox

messagebox.showinfo("Title", "a Tk MessageBox")

import tkinter
from tkinter import messagebox

# hide main window
root = tkinter.Tk()
root.withdraw()

# message box display
messagebox.showerror("Error", "Error message")
messagebox.showwarning("Warning","Warning message")
messagebox.showinfo("Information","Informative message")