from tkinter  import *

def say():
    print("button pressed")

def Setit():
    # l.delete(0,END)
    l.insert(END,"+")
    return

def equal():
    l.delete(0,END)
    l.insert(0,"= 3+8")

def one():
    l.insert(END,"1")


but = Tk()
but.geometry('500x600')
but.title("Calculator")

l=Entry(but)
l.grid(row=1)

b=Button(but,text="add",command=Setit)
b.grid(row=2)

b= Button(but,text="=",command=equal)
b.grid(row=3)

value1 = Button(but,text="1",command=one)
value1.grid(row=4)

but.bind("q",lambda x: but.destroy())

but.mainloop()
