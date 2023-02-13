from tkinter import *

root = Tk() #mandatory to every gui using tkinter

#creating  a label widget
myLabel = Label(root ,text = "Hello World!")
 
#Shoving it onto the screen
myLabel.pack()

root = mainloop()