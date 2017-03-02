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

frame = Frame(t)
frame.pack()

canvas = Canvas(frame, bg="black", width=500, height=500)
canvas.pack()

photoimage = ImageTk.PhotoImage(file="logo.png")
canvas.create_image(150, 150, image=photoimage)

t.mainloop()