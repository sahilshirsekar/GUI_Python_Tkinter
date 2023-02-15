from tkinter import * 
from PIL import ImageTk,Image

root = Tk()
root.title('Hotel Bot')
root.iconbitmap(default='C:/Users/SAHIL/hotelbot.ico')


my_img1 = ImageTk.PhotoImage(Image.open("C:/Users/SAHIL/HotelHome.png"))
my_img2 = ImageTk.PhotoImage(Image.open("C:/Users/SAHIL/doorknob.png"))
my_img3 = ImageTk.PhotoImage(Image.open("C:/Users/SAHIL/bed.png"))
my_img4 = ImageTk.PhotoImage(Image.open("C:/Users/SAHIL/breakfast.png"))
my_img5 = ImageTk.PhotoImage(Image.open("C:/Users/SAHIL/umbrella_beach_chair_shade.png"))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

my_Label = Label(image = my_img1)
my_Label.grid(row= 0, column=0, columnspan=3)

def forward(image_number):
    global my_Label
    global button_for
    global button_back

    my_Label.grid_forget()  #forgets/vanishes the last image stored in my_Label i.e my_img1

    my_Label= Label(image = image_list[image_number - 1])
    button_for = Button(root, text=">>",command=lambda: forward(image_number+1) )
    button_back = Button(root , text= "<<", command=lambda: back(image_number-1))

    if image_number==5:
        button_for = Button(root, text =">>",state=DISABLED)

    my_Label.grid(row= 0, column=0, columnspan=3)
    button_for.grid(row=1, column=2)
    button_back.grid(row=1, column=0)

def back(image_number):
    global my_Label
    global button_for
    global button_back


    my_Label.grid_forget() 
    my_Label= Label(image = image_list[image_number - 1])
    button_for = Button(root, text=">>",command=lambda: forward(image_number+1) )
    button_back = Button(root , text= "<<", command=lambda: back(image_number-1))

    if image_number==1:
        button_for = Button(root, text ="<<",state=DISABLED)

    my_Label.grid(row= 0, column=0, columnspan=3)
    button_for.grid(row=1, column=2)
    button_back.grid(row=1, column=0)

button_back = Button(root, text="<<", command=back, state=DISABLED)
button_exit = Button(root, text="Exit", command= root.quit)
button_for = Button(root, text =">>", command=lambda:forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_for.grid(row=1, column=2)

root.mainloop()