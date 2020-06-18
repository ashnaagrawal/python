import tkinter
from tkinter import *


win = Tk()

l1=Label(win,text='Maths')
l1.place(x=10,y=10)
e1=Entry(win,bd=5)
e1.place(x=80,y=10)

l2=Label(win,text='English')
l2.place(x=10,y=50)
e2=Entry(win,bd=5)
e2.place(x=80,y=50)

b=Button(win,text='Submit')
b.place(x=100,y=100)
win.mainloop()