from tkinter import *

root = Tk() #mandatory to every gui using tkinter

#creating  a label widget
myLabel1 = Label(root , text = "Hello World!")
myLabel2 = Label(root , text = "My name is Sahil")

 
#Shoving it onto the screen
myLabel1.grid(row = 0 , column = 0)
myLabel2.grid(row = 1 , column = 5)

root = mainloop()