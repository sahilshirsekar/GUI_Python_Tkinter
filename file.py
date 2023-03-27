from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Tkinter")

def open():
    global my_img
    root.filename = filedialog.askopenfilename(initialdir="SAHIL/hotelbot.ico", title="Select a file", 
                                           filetypes=(("png files", "*.png"),("all files", "*.*")))
    my_label = Label(root, text=root.filename).pack()
    my_img = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image = my_img).pack()


my_btn = Button(root, text = "Open file", command=open).pack()

mainloop()