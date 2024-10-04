# WLCOME TO THIS APP. THIS APP CAN meter to kilometer and vs AND ALSO OTHER CONVERTS OTHER CONVERSIONS.
# AT FIRST I IMPORTED ALL FROM THE TKINTER
from tkinter import ttk
from tkinter import *

root = Tk()
root.title("Unit conversion")
root.geometry("400x400")
root.config(bg="#E0FFFF")
# root.resizable(False,False)
combos1 = ""
combos2 = ""
# combos3=""
# combos4=""
entrys1 = ""


# entrys2=""
def checkValue(val):
    # THIS FUNCTION CHECKS IF THE VALUE OF THE ENTRY IS FLOAT OR NOT
    try:
        float(val)
        return True
    except ValueError:
        return False


def tabdil():
    # THIS FUNCTION CALCULATES AND EXCHANGE METER TO KILOMETER and vs AND DOES OTHER CONVERSIONS.
    global combos
    global combos2
    global combos1
    global entrys1
    global texts
    texts = ""
    entrys1 = entry1.get()

    if entrys1 == "":
        return

    if checkValue(entrys1) == False:
        lbl.config(text="Not a number!")
        return

    if combos1 == "METER" and combos2 == "KILOMETER":
        texts = float(entrys1) / 1000
    elif combos1 == "KILOMETER" and combos2 == "METER":
        texts = float(entrys1) * 1000
    elif combos1 == "CENTIMETER" and combos2 == "METER":
        texts = float(entrys1) / 100
    elif combos1 == "METER" and combos2 == "CENTIMETER":
        texts = float(entrys1) * 100
    elif combos1 == "KILOMETER" and combos2 == "CENTIMETER":
        texts = float(entrys1) * 100000
    elif combos1 == "CENTIMETER" and combos2 == "KILOMETER":
        texts = float(entrys1) / 100000
    elif combos1 == "MILIMETER" and combos2 == "METER":
        texts = float(entrys1) / 1000
    elif combos1 == "METER" and combos2 == "MILIMETER":
        texts = float(entrys1) * 1000
    elif combos1 == "MILIMETER" and combos2 == "KILOMETER":
        texts = float(entrys1) / 1000000
    elif combos1 == "KILOMETER" and combos2 == "MILIMETER":
        texts = float(entrys1) * 1000000
    elif combos1 == "MILIMETER" and combos2 == "CENTIMETER":
        texts = float(entrys1) / 10
    elif combos1 == "CENTIMETER" and combos2 == "MILIMETER":
        texts = float(entrys1) * 10
    elif combos1 == combos2:
        texts = entrys1
    # texts=f'{texts:.5f}'
    lbl.config(text=texts)
    # if entrys2=='':
    #     return
    # combos3==""


def get(event):
    # THIS FUNCTION GETS THE USER'S ENTRY(COMBOBOX)
    global combos1
    global combos2
    # global #combos4
    # global #combos3
    combos1 = combo1.get()
    combos2 = combo2.get()
    # tabdil()
    # combos3=combo3.get()
    # combos4=combo4.get()


lbl1 = Label(root, text="FROM", bg="#E0FFFF")
lbl1.pack()
combo1 = ttk.Combobox(root, state="readonly")
combo1["values"] = ("METER", "KILOMETER", "CENTIMETER", "MILIMETER")
combo1.current()
combo1.bind("<<ComboboxSelected>>", get)
combo1.pack()
lbl2 = Label(root, text="To", bg="#E0FFFF")
lbl2.pack()
combo2 = ttk.Combobox(root, state="readonly")
combo2["values"] = ("METER", "KILOMETER", "CENTIMETER", "MILIMETER")
combo2.current()
combo2.bind("<<ComboboxSelected>>", get)
combo2.pack()
entry1 = Entry(root)
entry1.pack()
btn = Button(root, command=tabdil, text="CONVERT", height=2, width=12, bg="#FFC0CB")
btn.pack()
lbl = Label(root, bg="#E0FFFF", font="bold")
lbl.pack()

root.mainloop()
