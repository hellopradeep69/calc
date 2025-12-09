from tkinter import *

def add():
    try:
        n1 = float(num1.get())
        n2 = float(num2.get())
        print(n1+n2)
    except :
        print("Try valid")

# create window
calc = Tk()
calc.geometry('500x500')
calc.title("Addition")

title = Label(calc,text="Addition",anchor="center",justify="center")
title.grid(row=0,column=10)
title2 = Label(calc,text="+",anchor="center",justify="center")
title2.grid(row=1,column=15)
num1 = Entry(calc)
num1.grid(row=1,column=10)
num2 = Entry(calc)
num2.grid(row=1,column=20)

btn = Button(calc,text="Add",command=add)
btn.grid(row=5)


calc.mainloop()
