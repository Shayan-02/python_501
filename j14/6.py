# import tkinter as tk
from tkinter import *

root = Tk()
root.config(bg="lightblue")

firstlbl = Label(root, text="firstname").pack()
firstent = Entry(root).pack()
lastlbl = Label(root, text="firstname").pack()
lastent = Entry(root).pack()
root.mainloop()
