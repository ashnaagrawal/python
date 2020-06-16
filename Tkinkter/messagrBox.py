import tkinter
from tkinter import *
from tkinter import messagebox

win = Tk()

def hello():
    messagebox.showinfo('from computer','hey there')

b = Button(win,text = 'popup',command = hello)
b.pack()

win.mainloop()