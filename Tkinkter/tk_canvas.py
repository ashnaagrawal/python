import tkinter
from tkinter import *


win = Tk()
c = Canvas(win, height = 250, width = 300, bg = 'blue')
cords = 10,50,240,213
arc = c.create_arc(cords,start =0 , extent = 180, fill='red')
line = c.create_line(10,10,400,400)

c.pack()
win.mainloop()