import tkinter
from tkinter import *

win = Tk()

l = Label(win,text='username')
l.pack()
e = Entry(win)
e.pack()
t = Text(win)
t.insert(INSERT,'hello')
t.pack()
win.mainloop()