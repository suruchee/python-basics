import tk as tk
from tkinter import *
root = tk()
label1 = Label(root, text="Hello World")
label1.pack()
root.mainloop()


#frame
from tkinter import *
root = tk()
newframe = Frame(root)
newframe.pack()
otherframe = Frame(root)
otherframe.pack(slide=BOTTOM)
button1 = Button(newframe, text = "Click Here",fg="Red")
button2 = Button(otherframe, text = "Click Here", fg = "Blue")

button1.pack()
button2.pack()
root.mainloop()

#grid
from tkinter import *

root = tk()

label1 = Label(root, text="Firstname")
label2 = Label(root, text="Lastname")

entry1 = Entry(root)
entry2 = Entry(root)

label1.grid(row= 0, column=0)
label2.grid(row= 1, column=0)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

label1.pack()
root.mainloop()


#adjisting widget
from tkinter import *

root = tk()

label1 = Label(root, text="Firstname", bg="Red", fg="White")
label1.pack(fill = X)

label2 = Label(root, text="Lastname", bg="Blue", fg="Green")
label2.pack(side=LEFT, fill=Y)

root.mainloop()


#button action
from tkinter import *

root = tk()
def dosometing():
	print("You have clicked the button")

button1 = Button(root, test"Click Me", command= dosometing)
button1.pack()

root.mainloop()

#class
from tkinter import *
class MyButtons:
    def __init__(self, rootone):
        frame = Frame(rootone)
        frame.pack()

        self.printbutton = Button(frame, text="Click Here", command = self.printmessage)
        self.printbutton.pack()

        self.quitbutton = Button(frame, text="Exit", command= frame.quit)
        self.quitbutton.pack(side=LEFT)
def printmessage(self):
    print("Button clicked")
root = tk()
b= MyButtons(root)
root.mainloop()


#drop down tootlbar statusbar
from tkinter import *
def function1():
    print("Menu item clicked")

root = tk()
mymenu = Menu(root)
root.config(menu=mymenu)

submenu = Menu(mymenu)
mymenu.add_cascade(label="File", menu=submenu)

submenu.add_command(label="Project", command=function1)
submenu.add_command(label="save",command=function1)

submenu.add_separator()
submenu.add_command(label="exit",command=function1)

###########################
newmenu = Menu(mymenu)
mymenu.add_cascade(label="Edit", menu=newmenu)

newmenu.add_command(label="Undo", command=function1)
newmenu.add_command(label="save",command=function1)

newmenu.add_separator()
newmenu.add_command(label="exit",command=function1)

toolbar = Frame(root, bg="Pink")
insertbutton = Button(toolbar, text = "Insert files", command=function1)
insertbutton.pack(side=LEFT, padx=2, pady=3)

printbutton = Button(toolbar, text="print", command=function1)
printbutton.pack(side=LEFT, padx=2, pady=3)

toolbar.pack(side=TOP, fill=X)

status = Label(root, text="This is the status", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BUTTOM, fill=X)


root.mainloop()


#Message box
from tkinter import *
import tkinter.messagebox
root=tk()
tkinter.messagebox.showinfo("Title","This is awesome")
response = tkinter.messagebox.askquestion("Question 1","Do you like coffee")
if response=='yes':
    print("Here is coffee for you")
root.mainloop()

#Drawing

from tkinter import *

root=tk()
canvas = Canvas(root, width=200, height=100)
canvas.pack()

newline = canvas.create_line(0,0,50,100)
otherline = canvas.create-line(10,10,100,100, fill="green")
root.mainloop()

