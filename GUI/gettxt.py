from tkinter import *


root = Tk()
root.title("window")
root.geometry("400x350")
root.configure(bg = "blue")


e = Entry(root, width=50, bg = "black", fg = "red")
e.pack()
e.insert(0, "enter your name here")

e2 = Entry(root, width=50, bg = "black", fg = "red")
e2.pack()
e2.insert(0, "enter your name here")

def myclick():
    hello = "Hello", e.get()
    myLabel = Label(root, text = hello, fg = "cyan", bg = "green" )
    myLabel.pack()
myB = Button(root, text = "enter your name", command = myclick, fg = "blue", bg= "red")
myB.pack()
root.mainloop()