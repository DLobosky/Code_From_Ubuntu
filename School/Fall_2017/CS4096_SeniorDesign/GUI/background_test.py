from Tkinter import *
from ScrolledText import *
import ttk
import Tkinter as tk
import tkMessageBox
import tkFont
from PIL import ImageTk,Image

#this outputs the type of image (i.e: RGBA)
#im = Image.open('logo.png')
#print im.mode


t = Tk()
t.title("Transparency")
t.geometry('1700x1000')

frame = Frame(t)
frame.place(x=0, y=0)

xscrollbar = Scrollbar(frame, orient=HORIZONTAL)
xscrollbar.place(x=50, y=50)

yscrollbar = Scrollbar(frame)
yscrollbar.place(x=200, y=50)

canvas = Canvas(frame, bg="black", width=1700, height=1000, xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set)
canvas.pack()

xscrollbar.config(command=canvas.xview)
yscrollbar.config(command=canvas.yview)

photoimage = ImageTk.PhotoImage(file="background6.gif")
canvas.create_image(850, 500, image=photoimage)

photoimage2 = ImageTk.PhotoImage(file="logo.png")
canvas.create_image(850, 500, image=photoimage2)


t.mainloop()