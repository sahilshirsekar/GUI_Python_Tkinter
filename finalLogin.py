from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
class Login_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Bot")
        self.root.geometry("1550x800+0+0")
        self.root.config(bg="#fff")
        self.phone_image = ImageTk.PhotoImage(file= "C:/Tkinter/IM1.jpeg")
        self.lbl_Phone_image = Label(self.root, image=self.phone_image, bd=0).place(x=200, y=200)
        # ====Login Frame====
        login_frame= Frame(self.root , bd=2, relief=RIDGE, bg="#fff")
        login_frame.place(x=900, y=150, width= 350, height= 460)

        title = Label(login_frame, text= "Login", font=("Microsoft", 30, "bold"), bg="#fff").place(x=0, y=30,relwidth=1)
        lbl_user = Label(login_frame, text="Username", font=("Andalus", 15), bg="#fff", fg="#767171").place(x=50, y=100)
        self.username = StringVar()
        self.password = StringVar()
        text_username = Entry(login_frame,textvariable=self.username,  font=("times new roman", 15), bg="#ECECEC").place(x=50, y=140, width=250)
       
        lbl_pass = Label(login_frame, text="Password", font=("Andalus", 15), bg="#fff", fg="#767171").place(x=50, y=200)
        text_pass = Entry(login_frame, textvariable=self.password,show="*", font=("times new roman", 15), bg="#ECECEC").place(x=50, y=240, width=250)

        btn_login = Button(login_frame,command=self.login, text="Log In", font=("Arial Rounded MT Bold", 15), bg= "#00B0F0", activebackground="#00B0F0",fg= "#fff", activeforeground="#fff", cursor="hand2").place(x=50, y=300, width=250, height= 35)

        # #=========
        # self.im1 = ImageTk.PhotoImage(file=)
        # self.im1 = ImageTk.PhotoImage(file=)
        # self.im1 = ImageTk.PhotoImage(file=)

        # self.lbl_change_image = Label(self.root, bg="#fff")
        # self.lbl_change_image.place(x=400,  y=150, width=360, height=428)

        # self.animate()

    def animate(self):
        self.im= self.im1
        self.im1 = self.im2
        self.im2= self.im3 
        self.im3 = self.im
        self.lbl_change_image.config(image=self.im)
        self.lbl_change_image.after(2000, self.animate)      
    def login(self):
        if self.username.get()== "" or self.password.get()=="":
            messagebox.showerror("Error", "All Fields are required")
        elif self.username.get()!= "Sahil" or self.password.get()!="123456":
            messagebox.showerror("Error", "Invalid Username or Password\nTry again with correct credentials")
        else:
            messagebox.showinfo("Information", f"Welcome: {self.username.get()}\nYour Password: {self.password.get()}")

    

root = Tk()
obj = Login_System(root)
root.mainloop()
