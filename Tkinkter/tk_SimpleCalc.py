import tkinter
from tkinter import *
from functools import partial


win = Tk()

def sum(label,x1,x2):
    n1 = (x1.get())
    n2 = (x2.get())
    sum  = int(n1) + int(n2)
    label.config(text = 'sum is : %d' %sum)
    return


l1 = Label(win,text='First Number = ')
l1.grid(row=1,column =0)
l2 = Label(win,text='Second Number = ')
l2.grid(row=2,column =0)

label = Label(win)
label.grid(row = 6 , column = 1)


x1 = StringVar()
x2 = StringVar()
e1 = Entry(win,textvariable = x1)
e1.grid(row =1,column =1)
e2 = Entry(win,textvariable = x2)
e2.grid(row =2,column =1)
sum = partial(sum,label,x1,x2)

b = Button(win,text='Calculate', command = sum)
b.grid(row=3 , column= 0)
win.mainloop()