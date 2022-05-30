from tkinter import *
root = Tk()
root.title("window")
my_label_1 = Label(root, text = "hello world")
my_label_2 = Label(root, text = "hello world")
my_label_1.grid(row = 0, column = 2)
my_label_2.grid(row = 1, column = 0)
root.mainloop()