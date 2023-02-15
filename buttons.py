from tkinter import * 

root = Tk()

def myClick() :
    myLabel = Label(root, text = "I clicked the button!")
    myLabel.pack()

myButton = Button(root , text = "Click me!", padx= 50, pady= 50,
                  command = myClick, fg ="blue" , bg ="cyan")
myButton.pack()

root.mainloop()