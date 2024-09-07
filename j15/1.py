from tkinter import *
# import tkinter
from tkinter import messagebox


def show_fullName():
    firstName = first_ent.get()
    lastName = last_ent.get()
    fullname = firstName + " " + lastName
    messagebox.showinfo("fullname", fullname)


window = Tk()
window.title("class")
window.geometry("500x500")
window.resizable(1, 1)
window.config(bg="lightblue")

first_name = Label(window, text="first name", bg="lightblue", font=("Arial", 14, "bold"))
first_name.pack()
first_ent = Entry(window, font=("Arial", 14, "bold"))
first_ent.pack()
last_name = Label(window, text="last name", bg="lightblue", font=("Arial", 14, "bold"))
last_name.pack()
last_ent = Entry(window, font=("Arial", 14, "bold"))
last_ent.pack()
submit_btn = Button(window, text="submit", bg="lightblue", font=("Arial", 14, "bold"), command= lambda: show_fullName())
submit_btn.pack()

window.mainloop()