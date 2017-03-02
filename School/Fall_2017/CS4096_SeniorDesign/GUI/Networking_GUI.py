import Tkinter
from Tkinter import *



def fileData(*args):	
	var = entry.get()
	print var

def exit():
	root.quit()

root = Tk()
root.title('File Manager 5000!!!')
Label(text='Enter File Name: ').pack(side=TOP,padx=100,pady=50)

entry = Entry(root, width=20)
entry.pack(side=TOP,padx=30,pady=100)

Button(root, text='OK', command=fileData).pack(side=LEFT)
Button(root, text='CLOSE', command=exit).pack(side= RIGHT)


l = Label(root, textvariable = fileData)
l.pack(side=TOP,padx=100,pady=100)


root.mainloop()
