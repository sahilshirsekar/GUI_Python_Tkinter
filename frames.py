from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learning to code')
root.iconbitmap('C:/Users/SAHIL/hotelbot.ico')

frame = LabelFrame(root, padx = 50, pady = 50) #create the widget 
frame.pack(padx = 100, pady =100)# put on the screen

b = Button(frame, text = "Don't CLick here!")
b2 = Button(frame , text = ".....or here", )
b.grid(row = 0, column=0)
b2.grid(row =1 , column = 1)
root.mainloop()