from tkinter import *

def Num(word):
    entry.insert(END,word)
    return

def getvalue():
    try:
        v = eval(entry.get())
        entry.delete(0,END)
        entry.insert(0,"=")
        entry.insert(1,v)
        return
    except:
        entry.delete(0,END)
        entry.insert(0,"ERROR")
        print("enter a valid value to calculate")

def fullclear():
    entry.delete(0,END)

def clear():
    d = len(entry.get())-1
    entry.delete(d)

# creation of window
root = Tk()
root.geometry('400x500')
root.title("calculator")

# label
label=Label(root,text="Calculator")
label.grid(ipadx=100)

# Entry
entry = Entry(root,font=("8"))
entry.grid(ipady=10)

# Number
# Button | 7
value1 = Button(root,text="7",command=lambda:Num("7"))
value1.place(x=6,y=80,width=60,height=60)

# Button | 8
value1 = Button(root,text="8",command=lambda:Num("8"))
value1.place(x=96,y=80,width=60,height=60)

# Button | 9
value1 = Button(root,text="9",command=lambda:Num("9"))
value1.place(x=186,y=80,width=60,height=60)

# Button | 4
value1 = Button(root,text="4",command=lambda:Num("4"))
value1.place(x=6,y=180,width=60,height=60)

# Button | 5
value1 = Button(root,text="5",command=lambda:Num("5"))
value1.place(x=96,y=180,width=60,height=60)

# Button | 6
value1 = Button(root,text="6",command=lambda:Num("6"))
value1.place(x=186,y=180,width=60,height=60)

# Button | 1
value1 = Button(root,text="1",command=lambda:Num("1"))
value1.place(x=6,y=280,width=60,height=60)

# Button | 2
value1 = Button(root,text="2",command=lambda:Num("2"))
value1.place(x=96,y=280,width=60,height=60)

# Button | 3
value1 = Button(root,text="3",command=lambda:Num("3"))
value1.place(x=186,y=280,width=60,height=60)

# Button | 0
value1 = Button(root,text="0",command=lambda:Num("0"))
value1.place(x=6,y=380,width=60,height=60)

# Operator
# division
value1 = Button(root,text="/",command=lambda:Num("/"))
value1.place(x=276,y=80,width=60,height=60)

# Addition
value1 = Button(root,text="+",command=lambda:Num("+"))
value1.place(x=186,y=380,width=60,height=60)

# minus
value1 = Button(root,text="-",command=lambda:Num("-"))
value1.place(x=276,y=280,width=60,height=60)

# clear
value1 = Button(root,text="Del",command=lambda:clear())
value1.place(x=96,y=380,width=60,height=60)

# multiply
value1 = Button(root,text="*",command=lambda:Num("*"))
value1.place(x=276,y=180,width=60,height=60)

# equal
value1 = Button(root,text="=",command=getvalue)
value1.place(x=276,y=380,width=60,height=60)

# normal | num key
root.bind("1",lambda event:Num("1"))
root.bind("2",lambda event:Num("2"))
root.bind("3",lambda event:Num("3"))
root.bind("4",lambda event:Num("4"))
root.bind("5",lambda event:Num("5"))
root.bind("6",lambda event:Num("6"))
root.bind("7",lambda event:Num("7"))
root.bind("8",lambda event:Num("8"))
root.bind("9",lambda event:Num("9"))
root.bind("0",lambda event:Num("0"))

# operator key
root.bind("+",lambda event:Num("+"))
root.bind("-",lambda event:Num("-"))
root.bind("*",lambda event:Num("*"))
root.bind("/",lambda event:Num("/"))
root.bind("=",lambda event:getvalue())

# Enter to return
root.bind("<Return>",lambda event:getvalue())

# x to clear
root.bind("<Escape>",lambda event:fullclear())
root.bind("c",lambda event:fullclear())

# q to quit
root.bind("q",lambda event: root.destroy())

root.mainloop()
