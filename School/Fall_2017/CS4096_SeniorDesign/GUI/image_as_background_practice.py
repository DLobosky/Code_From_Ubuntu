from Tkinter import *
import tkMessageBox
import tkFont
from PIL import ImageTk,Image
import ttk
import Tkinter as tk

app = Tk()
app.title("Welcome")



#image2 =Image.open('/home/GUI/background.gif')

image1=tk.PhotoImage(file='/home/GUI/background6.gif')
background_label = tk.Label(app, image=image1)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

#image1 = ImageTk.PhotoImage(image2)
w = image1.width()
h = image1.height()





app.geometry('1700x1000')
#app.geometry('%dx%d+0+0' % (w,h))

app.mainloop()
