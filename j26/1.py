import sqlite3
from tkinter import *


class Database:

    def __init__(self):
        # init is a constructor
        # when we call this class this function will work automatically
        # but for other functions, It is required to call the function.
        self.conn = sqlite3.connect("books.db")
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, price text, pcs integer, booknumber integer)"
        )
        self.conn.commit()

    def insert(self, title, price, pcs, booknumber):
        self.cur.execute(
            "INSERT INTO book VALUES (NULL,?,?,?,?)", (title, price, pcs, booknumber)
        )
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()

        return rows

    def search(self, title="", price="", pcs="", booknumber=""):
        self.cur.execute(
            "select * from book where  title =? OR price=? OR pcs=? OR booknumber =?",
            (title, price, pcs, booknumber),
        )
        rows = self.cur.fetchall()

        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM book WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id="", title="", price="", pcs="", booknumber=""):
        self.cur.execute(
            "UPDATE book SET title=?, price=?, pcs=?, booknumber=? WHERE id = ?",
            (title, price, pcs, booknumber, id),
        )
        self.conn.commit()

    def __del__(self):
        self.conn.close()


"""
A program that store these book details:
Title, price
pcs, booknumber

user can:
View all records
Search an entry 
Add entry
update entry
delete
close
"""


from tkinter import *


database = Database()


def view_command():
    list1.delete(0, END)
    for row in database.view():
        list1.insert(END, row)


def search_command():
    list1.delete(0, END)
    for row in database.search(
        title_text.get(), price_text.get(), pcs_text.get(), booknumber_text.get()
    ):
        list1.insert(END, row)


def add_command():
    database.insert(
        title_text.get(), price_text.get(), pcs_text.get(), booknumber_text.get()
    )
    list1.delete(0, END)
    list1.insert(
        END, (title_text.get(), price_text.get(), pcs_text.get(), booknumber_text.get())
    )


def get_selected_row(event):
    global selected_tuple
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)
    # return(selected_tuple)
    e1.delete(0, END)
    e1.insert(END, selected_tuple[1])
    e2.delete(0, END)
    e2.insert(END, selected_tuple[2])
    e3.delete(0, END)
    e3.insert(END, selected_tuple[3])
    e4.delete(0, END)
    e4.insert(END, selected_tuple[4])


def delete_command():
    database.delete(selected_tuple[0])
    view_command()


def update_command():
    database.update(
        selected_tuple[0],
        title_text.get(),
        price_text.get(),
        pcs_text.get(),
        booknumber_text.get(),
    )
    view_command()


window = Tk()


l1 = Label(window, text="نام")
l1.grid(row=0, column=0)

l2 = Label(window, text="قیمت")
l2.grid(row=0, column=2)

l3 = Label(window, text="تعداد")
l3.grid(row=1, column=0)

l4 = Label(window, text="شماره کتاب")
l4.grid(row=1, column=2)


title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

price_text = StringVar()
e2 = Entry(window, textvariable=price_text)
e2.grid(row=0, column=3)

pcs_text = StringVar()
e3 = Entry(window, textvariable=pcs_text)
e3.grid(row=1, column=1)

booknumber_text = StringVar()
e4 = Entry(window, textvariable=booknumber_text)
e4.grid(row=1, column=3)


list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=3, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind("<<ListboxSelect>>", get_selected_row)

b1 = Button(window, text="نمایش همه", width=12, command=view_command)
b1.grid(row=2, column=3)

b2 = Button(window, text="جستجو", width=12, command=search_command)
b2.grid(row=3, column=3)

b3 = Button(window, text="اضافه کردن", width=12, command=add_command)
b3.grid(row=4, column=3)

b4 = Button(window, text="بروزرسانی", width=12, command=update_command)
b4.grid(row=5, column=3)

b5 = Button(window, text="پاکسازی", width=12, command=delete_command)
b5.grid(row=6, column=3)

b6 = Button(window, text="بستن", width=12, command=window.destroy)
b6.grid(row=7, column=3)

view_command()  # This will initially show books list in the column
window.wm_title("فروشگاه کتاب")  # title of the  window

window.mainloop()
