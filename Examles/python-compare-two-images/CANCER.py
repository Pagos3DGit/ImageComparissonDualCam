#import tkMessageBox


from tkinter import *
import tkinter as tk
from tkinter import messagebox
#--------------------------------WE IMPORT EVERYTHING--------------------------------------------------------------------


#ANTIKATASTASH TOU TKINTER ME MESSAGEBOX---------------------------------------------
#from tkniter import messagebox

#--------------------------we import an empty function----------------------------------------
window = tk()

#-------------------------vazoume to popup sto kentro----------------------------------
window.eval('tk::PlaceWindow %s center' % windo.winfo_toplevel())

#--------------------------to kanei diafano------------------------------------------
window.withdraw()

#tkMessageBox.showinfo("Title", "a Tk MessageBox")
##---------------------showerror/showwarning---------------------------------------
messagebox.showinfo('Question', 'you are dickhead?')
window.deiconify()
window.destroy()
window.quit()
