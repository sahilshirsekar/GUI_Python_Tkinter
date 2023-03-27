from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learning to code')
root.iconbitmap('C:/Users/SAHIL/hotelbot.ico')

def open():
    global my_img
    top = Toplevel()
    top.title('My Second Window')
    top.iconbitmap('C:/Users/SAHIL/hotelbot.ico')
    my_img = ImageTk.PhotoImage(Image.open('C:/Users/SAHIL/hotelbot.ico'))
    my_label = Label(top, image=my_img).pack()
    btn2 = Button(top, text= "Close Window", command= top.destroy).pack()
    

btn = Button(root, text = "Open Second Window", command= open).pack()


mainloop()