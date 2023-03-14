from tkinter import * 
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title("Login here")
root.geometry("1100x500+250+150")
root.configure(bg="#fff")
root.resizable(False, False)

def signin():
    username= user.get()
    password= pwd.get()

    if username == "admin" and password=="Sahil":
        screen = Toplevel(root)
        screen.title("App")
        screen.geometry('925x500+300+200')
        screen.configure(bg="#fff")
        screen.resizable(False, False)

        Label(screen, text="Welcome", bg="#fff", font=("Calbiri(Body)", 50, "bold")).pack(expand=True)

        screen.mainloop()
    
    elif username!= 'admin' and password != 'Sahil':
        messagebox.showerror("Invalid", "Invalid username and password")

    elif password!= "Sahil":
        messagebox.showerror("Invalid", "Invalid password")
    
    elif username!= "admin":
        messagebox.showerror("Invalid", "Invalid username")

img = ImageTk.PhotoImage(Image.open("C:/Users/SAHIL/loginhb.jpg"))
Label(root, image= img, bg= "white").place(x= 75, y= 50)

frame = Frame(root, width= 350, height= 350, bg= "white")
frame.place(x= 700, y =70)

heading = Label(frame, text= "Sign in", fg="#57a1f8", bg= "white", font=("MIcrosoft YaHei UI Light", 23, 'bold'))
heading.place(x= 125, y=5)
# --------------------------
def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name = user.get()
    if name=='':
        user.insert(0, 'Username')

user = Entry(frame, width= 25, fg= 'black', border=0, bg='white',  font=("MIcrosoft YaHei UI Light",11))
user.place(x= 40, y= 80 )
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame, width= 295, height= 2, bg= 'black').place(x= 40, y=107)
# --------------------------
def on_enter1(e):
    pwd.delete(0, 'end')

def on_leave1(e):
    name = pwd.get()
    if name=='':
        pwd.insert(0, 'Password')

pwd = Entry(frame, width= 25, fg= 'black', border=0, bg='white',  font=("MIcrosoft YaHei UI Light",11))
pwd.place(x= 40, y= 150 )
pwd.insert(0, 'Password')
pwd.bind('<FocusIn>', on_enter1)
pwd.bind('<FocusOut>', on_leave1)

Frame(frame, width= 295, height= 2, bg= 'black').place(x= 40, y=177)
# --------------------------
Button(frame, width= 39, pady=7, text= 'Sign in', bg="#57a1f8", fg="white", border= 0, command=signin).place(x= 50, y= 204)
label = Label(frame, text="Don't have an account?", fg="black", bg="white", font=("MIcrosoft YaHei UI Light",9))
label.place(x=90, y= 270)

sign_up = Button(frame, width= 6, text='Sign up', border=0, bg='white', cursor= 'hand2', fg='#57a1f8').place(x= 230, y= 270)

root.mainloop()