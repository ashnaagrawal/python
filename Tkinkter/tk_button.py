import tkinter
from tkinter import *


win = Tk()
win.geometry('1200x800')
b = Button(win, text = "button")
# b.pack()
b.grid(row=1,column=1)
b1 = Button(win, text = "btn")
# b1.pack()
b1.grid(row=2,column=2)
win.mainloop()

