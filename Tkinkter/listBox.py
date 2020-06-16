import tkinter
from tkinter import *

win = Tk()

lb = Listbox(win)
lb.insert(1,'pyhton')
lb.insert(2,'C')
lb.insert(3,'C++')
lb.insert(4,'JQuery')

lb.pack()

win.mainloop()