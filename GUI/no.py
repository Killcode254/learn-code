from tkinter import *


root = Tk()
root.title("calculator1.0")
root.geometry("400x350")
root.configure(bg = "blue")


e = Entry(root, width=50, bg = "black", fg = "red")
e.pack()

e2 = Entry(root, width=50, bg = "black", fg = "red")
e2.pack()
fu = Entry(root, width=50, bg = "black", fg = "red")
fu.pack()

def myclick():
    f = float(e.get())
    s = float(e2.get())
    func = fu.get
    if func == "-":
        ans = f-s
    elif func == "+" :
        ans = "f+s"
    elif func == "/":
        ans = "f/s"
        myLabel = Label(root, text = ans, fg = "cyan", bg = "green" )
        myLabel.pack()
    elif func == "*":
        ans = "f*s"
        myLabel = Label(root, text = ans, fg = "cyan", bg = "green" )
        myLabel.pack()

myB = Button(root, text = "calculate", command = myclick, fg = "blue", bg= "red")
myB.pack()
root.mainloop()