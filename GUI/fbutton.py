from tkinter import *

root = Tk()
def myclick():
    myLabel = Label(root, text = "hey, you clicked")
    myLabel.pack()
myB = Button(root, text = "click me !", command = myclick)
myB.pack()
root.mainloop()