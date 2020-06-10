import tkinter
from tkinter import *

win = Tk()
c1 = IntVar()
c2 =IntVar()
cb = Checkbutton(win, text='Public',offvalue = 0 ,onvalue =1,height = 5, width = 10, variable = c1)
cb.pack()
cb1 = Checkbutton(win, text='Value',offvalue = 0 ,onvalue =1,height = 5, width = 10, variable = c2)
cb1.pack()


var = IntVar()
rb = Radiobutton(win,text = 'option1',variable = var, value=1)
rb.pack()
rb1 = Radiobutton(win,text = 'option2',variable = var, value=2)
rb1.pack()
rb3 = Radiobutton(win,text = 'option3',variable = var, value=3)
rb3.pack()
win.mainloop()