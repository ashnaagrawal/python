import tkinter
from tkinter import *

win = Tk()

cb = Checkbutton(win, text='Public',offvalue = 0 ,onvalue =1,height = 5, width = 10)
cb.pack()

win.mainloop()