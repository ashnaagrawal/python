import tkinter
from tkinter import *

pw = PanedWindow()
pw.pack(fill=BOTH,expand=1)

left=Entry(pw,bd=5)
pw.add(left)

pw1 = PanedWindow(pw,orient=VERTICAL)
pw.add(pw1)

top = Scale(pw1,orient=HORIZONTAL)
pw1.add(top)
button = Button(pw1,text='OK')
pw1.add(button)


mainloop()