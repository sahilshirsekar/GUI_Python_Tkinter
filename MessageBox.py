from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title('Hotel Bot')
root.iconbitmap(default='C:/Users/SAHIL/hotelbot.ico')
# showinfo, showerro, showwarning, askquestion, askokcancel, askyesno
def popup():
    response = messagebox.askyesno("This is my Popup!", "Hello World")
    Label(root, text=response).pack()
    if response==1:
        Label(root, text="You clicked Yes!").pack()
    else:
        Label(root, text="No").pack()
Button(root, text="Popup", command=popup).pack()


mainloop()