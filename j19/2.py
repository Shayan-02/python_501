from tkinter import *


def show_fullname():
    fn = fnametxt.get()
    ln = lnametxt.get()
    fullnamelbl.config(text=fn + " " + ln, foreground="green", bg="gray")


root = Tk()
root.title("fullname app")
root.geometry("350x350")


fnamelbl = Label(root, text="first name", font=("arial", 15, "bold"), fg="blue")
fnamelbl.place(x=10, y=10)
fnametxt = Entry(root, width=20, font=('arial', 15, 'bold'))
fnametxt.place(x=120, y=12)

lnamelbl = Label(root, text="last name", font=("arial", 15, "bold"), fg="blue")
lnamelbl.place(x=10, y=60)
lnametxt = Entry(root, width=20, font=("arial", 15, "bold"))
lnametxt.place(x=120, y=62)

fullnamebtn = Button(root, text="show fullname", font=("arial", 15, "bold"), fg="blue", command=lambda:show_fullname())
fullnamebtn.place(x=120, y=120)

fullnamelbl = Label(root, text="", font=("arial", 20, "bold"))
fullnamelbl.place(x=120, y=180)

root.mainloop()
