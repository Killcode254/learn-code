from tkinter import *

root = Tk()
root.title("window")

def myclick():
    myLabel = Label(root, text = "hey, you clicked me", fg = "cyan" )
    myLabel.pack()
myB = Button(root, text = "click me !", command = myclick, fg = "blue", bg= "red")
myB.pack()
root.mainloop()